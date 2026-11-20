<!-- Excerpt of the BRD (docs/Motor Insurance Policy Admin and Claims System Prototype Brief and BRD.docx). Copied as-is, not summarised. Source lines: 176,191 226,297. -->
## 6. Vehicle classes in scope

Five vehicle classes cover every type of motor vehicle, and all five are built in the 6-week project on the same schema-driven engine.

| Vehicle class                 | Sub-classes                                                                                                   | What makes it different                                                             | Main rating drivers                                                          |
|-------------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| 1\. Two-wheeler               | Scooter, motorcycle, moped, electric two-wheeler                                                              | High volume, theft, rider and pillion injury, low repair cost                       | Engine size, age, IDV, zone                                                  |
| 2\. Private car               | Hatchback, sedan, SUV, multi-purpose vehicle, electric car                                                    | The base case: own damage plus third-party, many add-ons, claim-free discount       | IDV, age, engine size or power, fuel, zone, claim-free years                 |
| 3\. Goods-carrying            | Light, medium and heavy trucks, tipper, tanker, trailer, goods three-wheeler                                  | Business use, permit and route, heavy third-party exposure, hazardous loads, fleets | Gross vehicle weight, age, IDV, permit area, type of goods, fleet experience |
| 4\. Passenger-carrying        | Taxi or cab, bus, school bus, minibus or van, passenger three-wheeler                                         | Liability to passengers, seats, permit and route, contract or school use            | Vehicle category, seats, age, IDV, permit area                               |
| 5\. Miscellaneous and special | Agricultural tractor and trailer, construction equipment (crane, excavator), ambulance, other special-purpose | Mixed on-road and site use, equipment values, low road exposure                     | Type, age, IDV, on-road or site-only use                                     |

**Fleet policies** (many vehicles on one policy) apply to every class and are most common for goods-carrying and passenger-carrying vehicles. **Electric vehicles** are a fuel type within each class, with extra fields for battery and charger.

> **Own damage (OD)** = cover for loss of or damage to the insured's own vehicle. **Third-party (TP)** = cover for the owner's legal liability to others for injury, death or property damage caused by the vehicle. **No-claim bonus (NCB)** = a discount at renewal for a claim-free year. **GVW (gross vehicle weight)** = the maximum loaded weight of a vehicle, which sets the size class of trucks. **Permit** = official permission to use a commercial vehicle for goods or passengers in a given area. **Fitness certificate** = proof that a commercial vehicle passed its roadworthiness check. **Tipper** = a truck whose load bed tilts to unload. **Tanker** = a truck that carries liquid or gas in a tank. **Trailer** = an unpowered unit towed by another vehicle. **Fleet** = a group of vehicles insured together on one policy. **Cashless repair** = the insurer pays the garage directly, so the owner does not pay upfront.


## 8. Vehicle field specifications

These are the fields each vehicle-class schema must capture. Each becomes a field in the schema format of Section 5; groups map to form sections. Mandatory flags, option lists and validations are set per product in the configurator.

**Build note.** Build the schema for private car first, with validation and rating inputs, then copy it for the other four classes and change the class-specific groups. If time runs short, trim each schema to its 20 most important fields and keep the group structure.

### 8.1 Common policy header (all classes)

| Group                        | Fields                                                                                                                                                                                     |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Policy identity              | Product code, vehicle class, policy type (new, renewal, rollover, fleet), cover type (comprehensive, own damage only, liability only), branch, region, channel, intermediary code and type |
| Period and money             | Start and end date and time, total IDV, currency, premium, tax, total, payment mode and status                                                                                             |
| Parties                      | Insured, registered owner if different, financier or lender, nominee                                                                                                                       |
| Terms                        | Compulsory and voluntary deductibles, geographical area, limitations as to use, warranties, exclusions, special conditions, free-text remarks                                              |
| Co-insurance and reinsurance | Co-insurer names and shares, lead flag                                                                                                                                                     |

### 8.2 Vehicle identity and specification (all classes)

| Group            | Fields                                                                                                                                                                                   |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Identity         | Registration number (or "applied for"), registration authority code, registration date, make, model, variant, year of manufacture, chassis number, engine number, colour                 |
| Specification    | Vehicle class and sub-class, body type, fuel type, engine capacity (cc) or power (kW), seating capacity including driver, number of wheels, new or used, odometer reading, imported flag |
| Purchase         | Purchase date, invoice price, dealer, manufacturer's listed price                                                                                                                        |
| Electric vehicle | Battery capacity (kWh), battery serial number, charger type, home charger value                                                                                                          |
| Location         | City where garaged, parking type                                                                                                                                                         |

### 8.3 Class-specific fields

| Class                     | Fields                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Two-wheeler               | Type (scooter, motorcycle, moped), engine capacity, number of pillion seats, anti-theft device fitted, electric or fuel                                                                                                                                                                                                                                                                                                            |
| Private car               | Body type (hatchback, sedan, SUV, multi-purpose), accessories fitted, anti-theft device, airbags, use (private or business)                                                                                                                                                                                                                                                                                                        |
| Goods-carrying            | GVW (kg), unladen weight, carrying capacity (tonnes), body type (open, closed, tipper, tanker, container, flatbed), number of axles, type of goods (general, perishable, hazardous, high value), permit type, number and validity (local, state, national), route or area, radius of operation, fitness certificate number and validity, trailer details (number, chassis, value), number of paid drivers and cleaners, fleet code |
| Passenger-carrying        | Category (taxi or cab, bus, school bus, minibus or van, passenger three-wheeler), seats excluding driver, standing capacity, permit type, number and validity, route or area, fitness certificate and validity, contract or school use flag, number of conductors and cleaners                                                                                                                                                     |
| Miscellaneous and special | Type (tractor, trailer, crane, excavator, forklift, ambulance, other), use (agricultural, construction, other), power (kW), operating weight, value of attached equipment, place of use (public road or private site only), trailer details, registered or unregistered                                                                                                                                                            |

### 8.4 Valuation and accessories

| Group             | Fields                                                                                                                                                                        |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IDV and valuation | Manufacturer's listed price, age at inception, depreciation percentage, calculated IDV, agreed override with reason, market value for older vehicles                          |
| Accessories       | Non-electrical accessories and value, electrical and electronic accessories and value, CNG or LPG kit and value, body or chassis value for commercial vehicles, trailer value |
| Financier         | Lender name, loan reference                                                                                                                                                   |

### 8.5 Owner, driver and fleet

| Group             | Fields                                                                                                                                                                  |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Owner             | Owner type (individual, company, partnership, government), name, address, contact, KYC documents, tax number                                                            |
| Driver            | Name, licence number and class, issue date and validity, date of birth, years of experience, driver type (owner, named, paid employee), age and experience restrictions |
| Personal accident | Owner-driver cover (compulsory), nominee, unnamed passenger cover, cover for paid driver and cleaner                                                                    |
| Fleet             | Fleet owner, fleet size, vehicle list (repeating group), claims in the last 3 years, fleet loss ratio, annual distance, fleet discount                                  |

### 8.6 Cover and add-ons

| Group                           | Fields                                                                                                                                                                                     |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cover                           | Comprehensive, own damage only or liability only; compulsory and voluntary deductible; geographical extension                                                                              |
| Add-ons for all classes         | Zero depreciation, engine protect, return to invoice, roadside assistance, consumables, key and lock replacement, tyre protect, claim-free discount protect, daily allowance during repair |
| Add-ons for electric vehicles   | Battery protect, charger cover                                                                                                                                                             |
| Add-ons for commercial vehicles | Legal liability to paid driver and cleaner, trailer cover, loading and unloading risk, passenger liability extension                                                                       |

### 8.7 Previous insurance and inspection

| Group           | Fields                                                                                                                     |
|-----------------|----------------------------------------------------------------------------------------------------------------------------|
| Previous policy | Insurer, number, expiry, cover type, claim-free percentage, claims in the last year (count and amount), policy lapsed flag |
| Break-in        | Days since expiry, inspection required flag                                                                                |
| Inspection      | Mode (self-inspection photos or surveyor), requested and completed dates, photos, existing damage found, result            |

> **Zero depreciation** = an add-on where the insurer pays the full cost of replaced parts without deducting wear and tear. **Engine protect** = cover for engine damage caused by water entering the engine or by oil leakage, which a basic policy usually excludes. **Return to invoice** = on total loss or theft the insurer pays the original invoice price, not the lower IDV. **Consumables** = small items used in a repair, such as nuts, bolts and oil. **Claim-free discount protect** = an add-on that keeps the discount after one claim. **Limitations as to use** = a policy condition that the vehicle is used only for the declared purpose, for example private use.


