<!-- Excerpt of the BRD (docs/Motor Insurance Policy Admin and Claims System Prototype Brief and BRD.docx). Copied as-is, not summarised. Source lines: 699,715. -->
### A.5 Passenger-carrying vehicles

**passenger_od_base.csv**: own-damage base rate as a percentage of IDV

| Category                | Age 0 to 5 | Age 6 to 10 | Over 10 |
|-------------------------|------------|-------------|---------|
| Taxi or cab             | 3.30%      | 3.60%       | 4.00%   |
| Passenger three-wheeler | 2.60%      | 2.90%       | 3.20%   |
| Minibus or van          | 3.10%      | 3.40%       | 3.80%   |
| Bus                     | 3.00%      | 3.30%       | 3.70%   |

Other rules: permit area factor as in A.4; school or contract use factor 1.15 on own damage; fleet discount and experience adjustment as in A.4; third-party base premium for taxi, three-wheeler, minibus, bus is 9,000, 5,500, 16,000, 28,000, plus 150 for each passenger seat (driver excluded); legal liability to paid driver or conductor 80 each; owner-driver personal accident 300.

**Test case PC1:** taxi; IDV 700,000; age 4; 4 passenger seats; local permit; Zone A; no claim-free years; one paid driver; Region B. Own damage = 700,000 × 3.30% × 0.90 × 1.10 = 22,869; third-party 9,000 + 4 × 150 = 9,600; staff liability 80; total before tax 32,549; tax at 8% is 2,603.92; **total 35,152.92**.

**Test case PC2:** school bus; IDV 3,500,000; age 7; 30 passenger seats; state permit; Zone B; driver and conductor; Region A. Own damage = 3,500,000 × 3.30% × 1.15 = 132,825; third-party 28,000 + 30 × 150 = 32,500; staff liability 160; total before tax 165,485; tax at 10% is 16,548.50; **total 182,033.50**; referred by rule R7.


