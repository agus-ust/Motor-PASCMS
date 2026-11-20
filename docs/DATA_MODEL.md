# Data model (lean version). SQLModel classes are the truth; this file is the plan.

This is the lean model that matches the sponsor's feedback: separate make-model-variant masters, a separate customer (party) table, configurable add-ons through covers, an append-only claim transaction log, and policy-level price adjustment. Claude reads this instead of the whole BRD.

## Conventions
- Every table has id (int PK), created_at, updated_at. Masters also have code (unique), name, sort_order, is_active.
- Never hard-delete. Retire with is_active = 0 or a status.
- Config rows carry effective_from / effective_to. A change adds a new dated row or a new version.
- JSON columns hold class-specific data. Fields used for search or rating are also real columns.
- Dropdown values live in mst_lookup_value, grouped by lookup type. Lookup types: ROLE, PARTY_ROLE, GENDER, ID_TYPE, KYC_STATUS, FUEL_TYPE, BODY_TYPE, SEGMENT, RATING_ZONE, POLICY_TYPE, POLICY_STATUS, SALES_CHANNEL, ENDORSEMENT_TYPE, UW_OUTCOME, REASON, CLAIM_TYPE, PERIL, CLAIM_STATUS, CLAIMANT_TYPE, CASE_STAGE, TXN_TYPE, PAYMENT_MODE, DOCUMENT_TYPE.
- "x_id -> table" means a foreign key to table.id. "(L:TYPE)" means a foreign key to mst_lookup_value of that lookup type.

## Masters
- mst_lookup_type: code, name, is_system
- mst_lookup_value: lookup_type_id -> mst_lookup_type, code, name, parent_value_id -> self, attributes json. Unique (lookup_type_id, code)
- mst_state: code, name, gst_state_code
- mst_city: state_id -> mst_state, rating_zone_id (L:RATING_ZONE)
- mst_rto: state_id -> mst_state, city_id -> mst_city, rating_zone_id (L:RATING_ZONE)
- mst_vehicle_class: code, name, parent_id -> self, is_commercial
- mst_vehicle_make: code, name
- mst_vehicle_model: make_id -> mst_vehicle_make, vehicle_class_id -> mst_vehicle_class, segment_id (L:SEGMENT), launch_year, discontinued_year
- mst_vehicle_variant: model_id -> mst_vehicle_model, fuel_type_id (L:FUEL_TYPE), body_type_id (L:BODY_TYPE), engine_cc, seating_capacity, gvw_kg, power_kw, ex_showroom_price, attributes json

## Organisation and users
- org_unit: code, name, parent_id -> self, state_id -> mst_state, city_id -> mst_city, is_active
- sec_user: username (unique), password_hash, display_name, email, role_id (L:ROLE), party_id -> pty_party (set for intermediaries), org_unit_id -> org_unit, last_login_at, is_active

## Product configuration (a new product = new rows or files here)
- cfg_product: code, name, vehicle_class_id -> mst_vehicle_class, is_active
- cfg_product_version: product_id -> cfg_product, version_no, status (DRAFT, PUBLISHED, RETIRED), effective_from, effective_to, term_months, policy_schema json, risk_schema json, claim_schema json, cloned_from_version_id -> self. Unique (product_id, version_no)
- cfg_coverage: code, name, coverage_kind (OD, TP, PA, ADDON), vehicle_class_id -> mst_vehicle_class
- cfg_product_coverage: product_version_id -> cfg_product_version, coverage_id -> cfg_coverage, is_mandatory, is_default, calc_method, rate_table_id -> cfg_rate_table, sort_order
- cfg_rate_table: code, name, dimensions json, value_type, vehicle_class_id -> mst_vehicle_class
- cfg_rate_table_row: rate_table_id -> cfg_rate_table, row_key json, range_from, range_to, rate_value, effective_from, effective_to
- cfg_rating_step: product_version_id -> cfg_product_version, step_no, code, name, step_type, rate_table_id -> cfg_rate_table, coverage_id -> cfg_coverage, expression, decimals, show_in_breakup. Unique (product_version_id, step_no)
- cfg_uw_rule: code (R1..R9), name, product_id -> cfg_product, vehicle_class_id -> mst_vehicle_class, outcome_id (L:UW_OUTCOME), condition_json, message, priority, effective_from, effective_to, is_active
- cfg_parameter: param_key, param_value, value_type, product_id -> cfg_product, vehicle_class_id -> mst_vehicle_class, effective_from, effective_to
- cfg_document_template: code, name, document_type_id (L:DOCUMENT_TYPE), version_no, body_html, is_active

## People and vehicles
- pty_party: party_no (unique), party_kind (INDIVIDUAL, ORGANISATION), display_name, first_name, last_name, date_of_birth, gender_id (L:GENDER), mobile, email, address_line, city_id -> mst_city, state_id -> mst_state, pincode, kyc_status_id (L:KYC_STATUS)
- pty_party_role: party_id -> pty_party, role_id (L:PARTY_ROLE: INSURED, DRIVER, CLAIMANT, GARAGE, SURVEYOR, INTERMEDIARY, FINANCIER, PREVIOUS_INSURER), attributes json
- pty_party_identifier: party_id -> pty_party, id_type_id (L:ID_TYPE), id_number, expiry_date
- veh_vehicle: vehicle_class_id -> mst_vehicle_class, make_id, model_id, variant_id (-> the three vehicle masters), manual_make_model (when not in masters), fuel_type_id (L:FUEL_TYPE), chassis_no (unique), engine_no, manufacture_year, colour, engine_cc, seating_capacity, gvw_kg, owner_party_id -> pty_party, vehicle_data json
- veh_registration: vehicle_id -> veh_vehicle, registration_no, rto_id -> mst_rto, registered_on, is_current. Unique (vehicle_id, registration_no)

## Policy
- pol_policy: policy_no (unique), quote_no (unique), product_version_id -> cfg_product_version, policy_type_id (L:POLICY_TYPE), status_id (L:POLICY_STATUS), sales_channel_id (L:SALES_CHANNEL), insured_party_id -> pty_party, intermediary_party_id -> pty_party, org_unit_id -> org_unit, previous_policy_id -> self, previous_ncb_pct, is_fleet, inception_at, expiry_at, total_idv, net_premium, tax_amount, total_premium, issued_at, policy_data json
- pol_risk_item: policy_id -> pol_policy, vehicle_id -> veh_vehicle, risk_no, idv, ncb_pct, net_premium, tax_amount, total_premium, status, risk_data json. Unique (policy_id, risk_no)
- pol_risk_coverage: risk_item_id -> pol_risk_item, coverage_id -> cfg_coverage, is_selected, sum_insured, deductible, premium. Unique (risk_item_id, coverage_id)
- pol_endorsement: policy_id -> pol_policy, endorsement_no (unique), endorsement_type_id (L:ENDORSEMENT_TYPE), status_id, reason_id (L:REASON), effective_from, premium_delta, tax_delta, total_delta, change_data json (before and after)
- pol_premium_breakup: policy_id -> pol_policy, risk_item_id, endorsement_id, rating_step_id -> cfg_rating_step, step_no, component_code, component_name, base_amount, rate_applied, amount
- pol_price_adjustment (underwriter, policy-level): policy_id -> pol_policy, risk_item_id, adjustment_pct, adjustment_amount, reason_id (L:REASON), applied_by_user_id -> sec_user, approved_by_user_id -> sec_user
- pol_uw_result: policy_id -> pol_policy, risk_item_id, rule_id -> cfg_uw_rule, outcome_id (L:UW_OUTCOME), message, evaluated_at
- pol_inspection (cut-list item): policy_id, risk_item_id, claim_id, status_id, inspection_at, findings, result

## Claims
- clm_claim: claim_no (unique), policy_id -> pol_policy, risk_item_id -> pol_risk_item, claim_type_id (L:CLAIM_TYPE), peril_id (L:PERIL), status_id (L:CLAIM_STATUS), org_unit_id, garage_party_id, surveyor_party_id (-> pty_party), reported_at, loss_at, loss_location, loss_city_id, loss_state_id, description, police_report_no, is_drivable, claim_data json, closed_at
- clm_claimant: claim_id -> clm_claim, party_id -> pty_party, claimant_type_id (L:CLAIMANT_TYPE), injury_description, claimed_amount, assessed_amount, status, case_data json
- clm_assessment: claim_id -> clm_claim, version_no, idv_at_loss, gross_estimate, parts_depreciation, compulsory_deductible, voluntary_deductible, salvage_value, net_payable, is_total_loss, is_current, assessed_at, calc_data json. Unique (claim_id, version_no)
- clm_assessment_line: assessment_id -> clm_assessment, line_no, line_type (PART, LABOUR, PAINT), description, quantity, estimate_amount, depreciation_pct, assessed_amount
- clm_transaction (the claim transaction log, append only; balances are computed from here): claim_id -> clm_claim, txn_type_id (L:TXN_TYPE), coverage_id, claimant_id, party_id, payment_id -> fin_payment, reason_id (L:REASON), amount, txn_date, remarks

## Workflow, money, documents, platform
- wf_approval: entity_type, entity_id, approval_type, amount, requested_by_user_id, approver_role_id (L:ROLE), approver_user_id, status (PENDING, APPROVED, DECLINED), reason_id (L:REASON), comments, decided_at
- fin_payment: payment_no (unique), direction (IN, OUT), purpose_id, policy_id, endorsement_id, claim_id, party_id, payment_mode_id (L:PAYMENT_MODE), amount, status, reference_no, paid_at
- doc_document: document_type_id (L:DOCUMENT_TYPE), entity_type, entity_id, template_id, file_name, storage_path, mime_type, version_no
- sys_audit_log (no updated_at): audit_at, user_id, entity_type, entity_id, action_code, before_json, after_json
- sys_number_sequence: sequence_code, org_unit_id, fiscal_year, prefix, padding, last_number. Unique (sequence_code, org_unit_id, fiscal_year)
- sys_integration_log: adapter_code, entity_type, entity_id, request_key, request_payload, response_payload, status_code, called_at
