# NASA interplanetary mission (NIM) dataset

Dataset DOI: [10.5061/dryad.fj6q5745z](10.5061/dryad.fj6q5745z)

## Description of the data and file structure

The database consists of a survey of NASA Interplanetary Missions (NIMs) launched between May 1989 and October 2023. Mission data includes system-level attributes in support of advanced system-level modeling. The attributes include elements of the program, schedule, cost, and technical design. Cost silos include three inflation formats: Then$ representing realized expenses in the Year of recording, NASA’s New Start Inflation Index (NSII) adjusted expenses, and Personal Consumption Expenditures Price Index (PCEPI) adjusted expenses. Inflated values are adjusted to fiscal Year 2022 equivalent dollars with an index of 1.00 applied forward to adjust to 2023 and 2024 equivalent expenditures. The NIM database serves as a reference for future research and cost analytics in NASA's system-level analysis of the Interplanetary Mission.

### Files and variables

#### File: NIM\_Database.xlsx

**Description:** The NIM database is organized by data segment, consisting of programmatic, schedule, cost, and technical data silos. Cost is provided in three data formats: Then $ is represented as the sum of incurred costs valued at the year of inception, NSII adjusted $ is defined as the sum of adjusted incurred costs inflated from the value of the year of inception to 2022 $ using the appropriate index multiplier, and PCEPI adjusted $ represented as the sum of adjusted incurred costs inflated from the value of the year of inception to 2022 $ using the appropriate index multiplier.

Unpopulated cells are designated with “na”. Cells containing a zero value represent a quantity of zero or a value of 0 and do not designate a blank entry.

##### Variables

***Mission Definition***

The mission definition provides the programmatic attributes of the mission elements. These variables are string-formatted data. This includes:

* *Mission* – Given the identification name of the NASA interplanetary mission/program
* *COSPAR* – International identifier assigned to artificial objects in space by the Committee on Space Research (COSPAR)
* *Initiative* – NASA program name or program directive of a class of missions
* *Destination* –  Planet or celestial body identified as the primary science objective of the mission: lunar, LaGrange 1, Mercury, Venus, Mars, Saturn, Jupiter, comet, asteroid, asteroid belt.
* *Success* – The operational status of the mission: Success, Failure, or Operational. Failure is defined as the inability to achieve the primary science objective.
* *Type* – Primary science function class of the mission: flyby, impact, lander, orbiter, rendezvous, rover, or sample return
* *Launch Vehicle* – Expendable or reusable launch platform used to achieve Earth-based transfer orbit status

 ***Schedule***

The schedule definition provides the initial budget schedule attributes of the mission elements. Month and year time durations are real-number data. Dates are presented in the format mm/dd/yyyy. This includes:

* *Proposed Design Schedule (PDS)* – Initial schedule budget for development activities defined as initiation (contract award or funding announcement) to launch. (months)
* Proposed Mission Schedule (PMS) – Proposed or initial schedule budget for the operations life defined as launch to end of mission disposal (years)
* Realized Design Schedule (RDS) – The reported development schedule is stated as the period between initiation (contract award or funding announcement) and launch. (months)
* Calculated Design Schedule (CDS) – Calculated as the [number of days/30] from the funding announcement to the manifest launch date, actual time realized. (months)
* Realized Mission Schedule (RMS) –  The reported primary operations schedule stated as launch to current status. The current status is either the end of the mission (for both successful and failed missions) or March 17, 2024 (the date establishing Version 1.0). This data should be updated for consistency as operational missions transition to extended missions or reach the end of mission status. (years)
* Calculated Mission Schedule (CMS) – Calculated as the [number of days/365] from the operational schedule reported from the launch date to the end of the mission date, actual time realized. (years)
* Feasibility – The document's feasibility date indicates when the proposed mission was considered viable for concept development, feasibility analysis, or consideration. (date)
* Funding – The document date for the selection or award indicates the initiation of the mission, which is typically identified by the award date, funding date, and budget request initiation date, as acknowledged in a NASA announcement. (date)
* PDR – The document/report date for the completion of the mission, Preliminary Design Review (PDR) associated with the spacecraft bus PDR. Instrument and Launch Vehicle PDRs are completed before the spacecraft bus/mission PDR. (date)
* CDR – The documented/report date for the completion of the mission Critical Design Review (CDR) associated with the spacecraft bus CDR. Instrument and Launch Vehicle CDRs are completed before the spacecraft bus/mission CDR. (date)
* Launch – The document/manifest date recording the mission launch. (date)
* *On-station* – The document date recording the arrival of the mission at the primary destination is described as the initiation of orbit acquisition, spacecraft initiation, or initial instrument operation/ check-out. (date)
* Science – The document/announcement date signifying the initiation of primary science operations. (date)
* Mission Extension (Extend) – The document/announcement date signifying the end of primary operations, initiation of extended mission operation scope, or extension of operation funding. (date)
* End of Mission (EoM) – The document/announcement date indicates the end of the mission, either as loss of communication, loss of science function, loss of tracking contact, or disposal. (date)           
* StartY – The Year the mission was identified as a line item in the NASA budget requests. (yyyy format)
* LaunchY – The Year the mission was reported launched in the NASA budget requests. (yyyy format)

***Cost***

The cost attributes are organized into four parts: cost and schedule planning and performance, cost accounting in Then Year $, cost accounting adjusted for inflation using the NSII index, and cost accounting adjusted for inflation using the PCEPI index. Headings use a WXYZ format for identification:

* W represents the cost context: P – proposed, F – final, and T – total reported
* X represents the program phase: M – mission (full program duration), D – development, L – launch, O – primary operations, E – extended operations
* Y represents the system component: C – cost
* Z represents the accounting format: T – Then-Year (reported) dollars, N – NSII adjusted dollars, P – PCEPI adjusted dollars. All dollars are reported in millions ($M)

The Part 1 cost attributes (PMCT, CMCT) provide the initial budget cost and schedule attributes of the original mission planning.

The Part 2 cost attributes (T*CT) provide the cost summation by mission cost attributes (development, launch, primary operations, and extended operations) for the mission. Lumped costs are distributed over a time duration consistent with other detailed cost profiles. This was common with launch vehicle cost accounting, which was reported as a single cost budget item.  When required, the launch cost was distributed over a 2 or 3-year period of performance, including the launch year and preceding years.

The Part 3 cost attributes (T*CN) provide the cost summation by mission cost attribute (development, launch, primary operations, and extended operations) for the mission adjusted for inflation using the NSII index. The NSII index adjusts cost elements to 2022 $ based on the NSII index multiplier and the year of cost incurred. Cost attributes represent the accumulation of expenses over successive years, with each year assigned an independent multiplier based on the NSII index. Expenses incurred in 2023 and 2024 were assigned a multiplier of 1.00.

The Part 4 cost attributes (T*CP) provide the cost summation by mission cost attribute (development, launch, primary operations, and extended operations) for the mission adjusted for inflation using the PCEPI index. The PCEPI index adjusts cost elements to 2022 $ based on the PCEPI index multiplier and the year of cost incurred. Cost attributes are the accumulation of expenses over successive years, with each year assigned an independent multiplier based on the PCEPI index. Expenses incurred in 2023 and 2024 were assigned a multiplier of 1.00.

Cost values are listed in millions of dollars ($M). This includes:

* PMCT – Proposed Mission Cost Total represents the total mission cost proposed in the initial NASA budget request or amount allocated by NASA before the mission award.
* CMCT – Calculated Mission Cost Total represents the current/final realized mission cost reported in the NASA budget requests.
* TMCT – Total Mission Cost in Then-$ represents the total mission cost summed for all years of program reporting, as actual costs reported in the NASA budget requests. These values are not adjusted.
* TDCT – Total Development Cost in Then-$ represents the total development cost summed for all years of program reporting as actual cost reported in the NASA budget requests. These values are not adjusted.
* TLCT – Total Launch Cost in Then-$ represents the total launch cost summed for all years of program reporting as actual cost reported in the NASA budget requests. These values are not adjusted.
* TOCT –  Total Operations Cost in Then-$ represents the total planned operations cost summed for all years of program reporting as actual cost reported in the NASA budget requests. These values are not adjusted.
* TECT – Total Extension Cost in Then-$ represents the total extended operations cost summed for all years of program reporting as actual cost reported in the NASA budget requests. These values are not adjusted.
* TMCN –  Total Mission Cost in NSII-$ represents the total mission cost summed for all years of the program reported as actual cost in the NASA budget requests and adjusted to Year 2022-$ using the NSII index.
* TDCN – Total Development Cost in NSII-$ represents the total development cost summed for all years of program reporting as actual cost in the NASA budget requests and adjusted to Year 2022-$ using the NSII index.
* TLCN – Total Launch Cost in NSII-$ represents the total launch cost summed for all years of program reporting as actual cost in the NASA budget requests and adjusted to Year 2022-$ using the NSII index.
* TOCN – Total Operations Cost in NSII-$ represents the total planned operations cost summed for all years of program reporting as actual cost reported in the NASA budget requests and adjusted to Year 2022-$ using the NSII index.
* TECN – Total Extension Cost in NSII-$ represents the total extended operations cost summed for all years of program reporting as actual cost reported in the NASA budget requests and adjusted to Year 2022-$ using the NSII index.
* TMCP – Total Mission Cost in PCEPI-$ represents the total mission cost summed for all years of the program reported as actual cost in the NASA budget requests and adjusted to Year 2022-$ using the PCEPI index.
* TDCP – Total Development Cost in PCEPI-$ represents the total development cost summed for all years of program reporting as actual cost in the NASA budget requests and adjusted to Year 2022-$ using the PCEPI index.
* TLCP – Total Development Cost in PCEPI-$ represents the total development cost summed for all years of program reporting as actual cost in the NASA budget requests and adjusted to Year 2022-$ using the PCEPI index.
* TOCP – Total Operations Cost in PCEPI-$ represents the total planned operations cost summed for all years of program reporting as actual cost reported in the NASA budget requests and adjusted to Year 2022-$ using the PCEPI index.
* TECP – Total Extension Cost in PCEPI-$ represents the total extended operations cost summed for all years of program reporting as actual cost reported in the NASA budget requests and adjusted to Year 2022-$ using the PCEPI index.

***Technical***

The technical definition provides the design attributes of the mission elements. This includes:

* Launch mass (LM) – The manifested launch mass of the spacecraft. (kgs)
* *Fuel –*  The spacecraft fuel load. In most cases, the fuel load is the difference between the launch mass and the spacecraft's dry mass. Where documented, this is confirmed by fuel budgets. Fuel includes propellant and oxidizer. (kgs)
* *AKM –*  AKM is the mass of the apogee kick motor (AKM) used for orbit circularization or transfer boost integrated within the spacecraft. (kgs)
* *Ballast and Adapter (Ball) –* The ballast and adapter account for any non-space vehicle accommodations, including the launch vehicle adapter and/or ballast that is not included in the SCdry mass but contributes to the total launch mass of the spacecraft, independent of fuel. (kgs)
* *SCdry  –*  SCdry is the total spacecraft dry mass ready for launch before launch site fueling. (kgs)
* *SVbus  –* SVbus is the space vehicle bus mass, less payload and fuel integration. (kgs)
* *SVpayload-(SVpay) –* SVpayload is the total, or calculated from the instruments, space vehicle payload mass ready for integration with the space vehicle bus. (kgs)
* *Probe  –* The probe mass accounts for secondary payload elements that are deployed from the primary spacecraft, such as probes, and are not integral to the spacecraft science operations. (kgs)
* *Cruise –* The Cruise mass is associated with cruise phase elements of the space vehicle. In the case of a cruise phase, the spacecraft consists of the science payload-carrying vehicle, and the Cruise segment transfers the spacecraft from an Earth orbit to a destination, either with or without orbit capture. (kgs)
* *Lander –* The lander mass is associated with the landing and deployment phase elements of the space vehicle. In the case of a landing phase, the lander includes both the science payload and a carrying and support landing vehicle. (kgs)
* Aeroshield (Aero) – The aeroshield mass is associated with re-entry shield elements of the space vehicle. In the case of a re-entry phase, the spacecraft consists of a science payload-carrying and support vehicle. (kgs)
* Obj – The number of objectives quantifies the published scientific objectives of the mission. A standard for space mission objectives does not exist. The values reported represent an estimate of the scientific and functional objectives of the mission. Delivery of secondary payloads and continuation of service as a communication relay are examples of additional objectives attributed to the mission objective quantity. (quantity)
* Ins – The number of science instruments manifested with the mission, including radio science (+1). Instruments are defined as science-gathering devices and exclude power and data electronics that directly support one or more instruments. In their presence, the mass and power associated with support electronics are included in the individual instrument properties. In the case of multiple or redundant units, the science is counted as a particular quantity. For example, a mission may include multiple magnetometer units that are considered a single magnetometer experiment due to redundancy or cross-correlation. (quantity)
* *InsMass –*  The reported mass of all payload instruments is recorded as the sum of the payload components or a combination of components, including power and data units that directly support individual or multiple payload instruments. (kgs)
* *InsPwr –* The reported instrument power orbit average power of the payload components as determined by allocation, the sum of payload instruments, or a combination that includes the power associated with power and data units that directly support individual or multiple payload instruments. (Watts)
* *Deployments (Deploy) –* The number of unique mission deployments, excluding separation from the launch vehicle adapter. Solar array deployment constitutes a single deployment independent of the number of wings or staged to deploy the solar array(s) fully. The number of deployments is a measure of the complexity and risk associated with spacecraft and operations. (quantity)
* *Bus Volume (BV) –* Where documented or calculated from spacecraft dimensions, the value represents the volume of the spacecraft core structure in launch configuration. (meters3)
* *SA – * Indicates the primary source of spacecraft power, including solar arrays (SA) or Radioactive Thermal Generator (RTG). (RTG or SA)
* *BoLP –*  The reported solar array power capability at 1 AU beginning of life (BoL) for a fully deployed solar array complement. (Watts)
* *BoMPwr–* The reported solar array power capability at destination orbit at perihelion as determined at the beginning of the mission (BoM). (Watts)
* *BoSPwr–* The reported solar array power capability at destination orbit at perihelion as determined at the beginning of science (BoS), where there is an extended non-science operation phase of the mission. (Watts)
* *Solar Array Area (SAA) –* The documented or calculated from spacecraft geometry, the total area of the spacecraft's solar array(s). When calculated, a packing factor of 0.90 or 0.95 is used. (meters2)
* *Solar Array Type (SAT) –* The type of solar array included in the spacecraft design, including mount and articulation employed. (2-axis gimbal, roll out, body mount, wing, articulated, fixed)

## Code/software

Excel csv

## Access information

Other publicly accessible locations of the data:

* Zenodo document link (see Supplemental Information Related Works)

Data was derived from the following sources:

* ***General Data References***

  \[1] Hunt, Charles. (2022) NASA New Start Inflation Index. NASA HQ. [https://www.nasa.gov/wp-content/uploads/2024/09/nnsi-2022-faqs.pdf?emrc=67f4e781a1917](https://www.nasa.gov/wp-content/uploads/2024/09/nnsi-2022-faqs.pdf?emrc=67f4e781a1917) .

  \[2] U.S. Bureau of Economic Analysis, Personal Consumption Expenditures: Chain-type Price Index [PCEPI], retrieved from FRED, Federal Reserve Bank of St. Louis; [https://fred.stlouisfed.org/series/PCEPI](https://fred.stlouisfed.org/series/PCEPI) , September 17, 2024.

  \[3] Bond, Peter R. (2011) ***Jane’s Space Systems and Industry 2011-2012, 27th ed***. Jane’s Information Group, Alexandria, Va.

  \[4] The Planet Society. Every NASA Budget Request, from 1961 to Now. [https://www.planetary.org/space-policy/every-nasa-budget-request](https://www.planetary.org/space-policy/every-nasa-budget-request) .
* ***2001 Mars Odyssey References***

  Krebs, Gunter D. ***2001 Mars Odyssey (MGM)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/mars_odyssey_2001.htm](https://space.skyrocket.de/doc_sdat/mars_odyssey_2001.htm) .

  NASA. ***2001 Mars Odyssey***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2001-013A](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2001-013A) , downloaded Mar 3, 2024. 

  JPL. Science Team and Instruments Selected for Mars Surveyor 2001. Nov 6, 1997. [https://www.jpl.nasa.gov/news/science-team-and-instruments-selected-for-mars-surveyor-2001](https://www.jpl.nasa.gov/news/science-team-and-instruments-selected-for-mars-surveyor-2001) , viewed Mar 18, 2024.
* ***Cassini References***

  Krebs, Gunter D. ***Cassini / Huygens***. Gunter's Space Page. Retrieved Mar 3, 2024, from [https://space.skyrocket.de/doc_sdat/cassini.htm](https://space.skyrocket.de/doc_sdat/cassini.htm) .

  NASA. ***Magellan***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/ display.action?id=1997-061A](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/%20display.action?id=1997-061A) , downloaded Mar 3, 2024.

  NASA. ***Huygens***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/ display.action?id=1997-061C](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/%20display.action?id=1997-061C) , downloaded Mar 3, 2024.

  Matson, D.L., Spilker, L.J. & Lebreton, JP. ***The Cassini/Huygens Mission to the Saturnian System***. Space Science Reviews 104, 1–58 (2002). [https://doi.org/10.1023/A:1023609211620](https://doi.org/10.1023/A:1023609211620)

  Gibbs, R., 1996, ***Cassini Spacecraft Design***, [https://hdl.handle.net/2014/26154](https://hdl.handle.net/2014/26154) , Denver, Colorado, USA, JPL Open Repository.
* ***Contour References***

  Krebs, Gunter D. ***CONTOUR (Discovery 6)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/contour.htm](https://space.skyrocket.de/doc_sdat/contour.htm) .

  NASA. ***CONTOUR***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc](https://nssdc.gsfc). nasa.gov/nmc/spacecraft/display.action?id=2002-034A , downloaded Mar 3, 2024.

  M.C. Chiu, J. Veverka, E.L. Reynolds (2003) ***The CONTOUR mission—status of implementation***. Acta Astronautica, Volume 52, Issues 2–6, 2003, Pages 99-103, ISSN 0094-5765,

  [https://doi.org/10.1016/S0094-5765(02)00143-1](https://doi.org/10.1016/S0094-5765\(02\)00143-1).

  E. Reynolds, M. Chiu, R. Farquhar and D. Dunham, ***The CONTOUR Discovery Mission***, 1999 IEEE Aerospace Conference. Proceedings (Cat. No.99TH8403), Snowmass, CO, USA, 1999, pp. 11-18 vol.2, doi: 10.1109/AERO.1999.793137.

  NASA. ***Contour***. [https://science.nasa.gov/mission/contour](https://science.nasa.gov/mission/contour), viewed Mar 12, 2024.

  P. E. Panneton, D. S. Mehoke and G. Dakermanji, ***The CONTOUR Spacecraft Power Subsystem***, IECEC '02. 2002 37th Intersociety Energy Conversion Engineering Conference, 2002., Washington, DC, USA, 2002, pp. 75-80, doi: 10.1109/IECEC.2002.1391982.
* ***Double Asteroid Redirection Test (Dart) References***

  Krebs, Gunter D. ***DART***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/dart_apl.htm](https://space.skyrocket.de/doc_sdat/dart_apl.htm) .

  NASA. ***Double Asteroid Redirection Test***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2021-110A](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2021-110A) , downloaded Mar 3, 2024.

  NASA. ***LICIACube***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/display.action?id=2021-110C](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/display.action?id=2021-110C) , downloaded Mar 5, 2024.

  NASA. NASA Awards Launch Services Contract for Asteroid Redirect Test Mission. Apr 11, 2019. [https://www.nasa.gov/news-release/nasa-awards-launch-services-contract-for-asteroid-redirect-test-mission/](https://www.nasa.gov/news-release/nasa-awards-launch-services-contract-for-asteroid-redirect-test-mission/) , viewed Mar 22, 2024.

  Adams, Elena et. al. ***Double Asteroid Redirection Test (DART) Mission***. Oct 1, 2023. APL_COMM-23-04772. NTRS Document ID 20230015804. [https://ntrs.nasa.gov/api/citations/20230015804/downloads/ DART%20Final%20Technical%20Report.pdf](https://ntrs.nasa.gov/api/citations/20230015804/downloads/%20DART%20Final%20Technical%20Report.pdf) , downloaded Mar 22, 2024.
* ***Dawn References***

  Krebs, Gunter D. ***Dawn (Discovery 9)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/dawn.htm](https://space.skyrocket.de/doc_sdat/dawn.htm) .

  NASA. ***Dawn***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/ spacecraft/display.action?id=2007-043A](https://nssdc.gsfc.nasa.gov/nmc/%20spacecraft/display.action?id=2007-043A) , downloaded Mar 3, 2024.

  Spaceflight101.com. ***Dawn Spacecraft & Mission Overview***. [https://spaceflight101.com/ spacecraft/ dawn-spacecraft-mission-overview/](https://spaceflight101.com/%20spacecraft/%20dawn-spacecraft-mission-overview/)  , viewed Mar 6, 2024.

  Thomas, V.C., Makowski, J.M., Brown, G.M. et al. **The Dawn Spacecraft**. Space Sci Rev 163, 175–249 (2011). [https://doi.org/10.1007/s11214-011-9852-2](https://doi.org/10.1007/s11214-011-9852-2) , downloaded Mar 6, 2024.

  NASA. ***Dawn Spacecraft Launch – Press Kit.*** Sep 2006. [https://science.nasa.gov/resource/dawn-launch-press-kit/](https://science.nasa.gov/resource/dawn-launch-press-kit/) , downloaded Mar 22, 2024.

  NASA. ***Dawn at Vesta – Press Kit***. Jul 2011. [https://science.nasa.gov/resource/dawn-at-vesta-press-kit/](https://science.nasa.gov/resource/dawn-at-vesta-press-kit/) , downloaded Mar 22, 2024.
* ***Deep Impact References***

  Krebs, Gunter D. ***Deep Impact / EPOXI (Discovery 7)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/deep_impact.htm](https://space.skyrocket.de/doc_sdat/deep_impact.htm) .

  NASA. ***Deep Impact/EPOXI***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/ display.action?id=2005-001A](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/%20display.action?id=2005-001A) , downloaded Mar 3, 2024.

  University of Maryland. ***Deep Impact – Mission Timeline***. Last updated Nov 14, 2017. [https://deepimpact.astro.umd.edu/mission /timeline.html](https://deepimpact.astro.umd.edu/mission%20/timeline.html) , viewed Mar 6, 2024.

  NASA. (2005) ***Deep Impact Comet Encounter – Press Kit***. Jun 2005. [https://deepimpact.astro](https://deepimpact.astro). umd.edu/gallery/pdf/deep-impact-encounter.pdf , viewed Mar 6, 2024.

  NASA. (2010) ***Epoxi Comet Encounter Fact Sheet***. Nov 2, 2010. [https://epoxi.astro.umd.edu/7press/ kits.shtml](https://epoxi.astro.umd.edu/7press/%20kits.shtml) , downloaded Mar 23, 2024.

  NASA. (2007). ***NASA Sends Spacecraft on Mission to Comet Hartley 2 – Press Release***. Dec 13, 2007. [https://epoxi.astro.umd.edu/7press/news/20071213.shtml](https://epoxi.astro.umd.edu/7press/news/20071213.shtml) , viewed Mar 23, 2024.

  NASA. (2005) ***Deep Impact/EPOXI***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc](https://nssdc.gsfc). nasa.gov/nmc/spacecraft/ display.action?id=2005-001A, NSSDCA/COSPAR ID: 2005-001A, viewed Mar 23, 2024.

  Mr. Monte Henderson, Mr. William Blume, ***Deep Impact – A Review of the World's Pioneering Hypervelocity Impact Mission***, Procedia Engineering, Volume 103, 2015, Pages 165-172, ISSN 1877-7058, [https://doi.org/10.1016/j.proeng.2015.04.023](https://doi.org/10.1016/j.proeng.2015.04.023).

  University of Maryland. ***Deep Impact – Technology – Flyby Spacecraft***. [https://deepimpact.astro.umd](https://deepimpact.astro.umd). edu/tech/flyby.html , viewed Mar 24, 2024.
* ***Deep Space 1 (DS 1) References***

  Krebs, Gunter D. ***DS1 (Deep Space 1)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/ds-1.htm](https://space.skyrocket.de/doc_sdat/ds-1.htm) .

  NASA. ***Deep Space 1***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa](https://nssdc.gsfc.nasa). gov/nmc/spacecraft/display.action?id=1998-061A  , downloaded Mar 3, 2024.

  NASA. (1999) **Deep Space 1 Asteroid Flyby – Press Kit**. Jul 1999. [https://www.jpl.nasa.gov/news/ press_kits/ds1asteroid.pdf](https://www.jpl.nasa.gov/news/%20press_kits/ds1asteroid.pdf) , downloaded Mar 11, 2024.
* ***Galileo References***

  Krebs, Gunter D. ***Galileo***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/galileo.htm](https://space.skyrocket.de/doc_sdat/galileo.htm) .

  NASA. ***Galileo Orbiter***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display. action?id =1989-084B](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.%20action?id%20=1989-084B) , downloaded Mar 3, 2024.

  Wikipedia. (2024). ***Galileo (spacecraft)***. [https://en.wikipedia.org/ wiki/Galileo_(spacecraft)](https://en.wikipedia.org/%20wiki/Galileo_\(spacecraft\)) , last updated Feb 1, 2024, viewed Mar 4, 2024.

  NASA. (1995). ***Galileo Jupiter Arrival (PDF) (Press Kit)***. NASA/ Jet Propulsion Laboratory. December 1995. [https://www.jpl.nasa](https://www.jpl.nasa). gov/news/press_kits/gllarpk.pdf  , downloaded Mar 4, 2024.

  NASA Science. ***Galileo***. [https://science.nasa.gov/mission/galileo/](https://science.nasa.gov/mission/galileo/), last updated Oct 2023, viewed Mar 4, 2024.

  Wikipedia. (2024). ***Galileo project***. [https://en.wikipedia.org/ wiki/Galileo_project](https://en.wikipedia.org/%20wiki/Galileo_project) , last updated Mar 2, 2024, viewed Mar 4, 2024.

  GAO Fact Sheet. **Space Exploration - Cost, Schedule, and Performance of NASA’s Galileo Mission to Jupiter**. May 1988. [https://www.gao.gov/assets/nsiad-88-138fs.pdf](https://www.gao.gov/assets/nsiad-88-138fs.pdf) , downloaded 3/26/2024.
* ***Genesis References***

  Krebs, Gunter D. ***Genesis (Discovery 5)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/genesis.htm](https://space.skyrocket.de/doc_sdat/genesis.htm).

  NASA. ***Genesis***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/display.action?id=2001-034A](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/display.action?id=2001-034A) , downloaded Mar 3, 2024.

  Burnett, D., Barraclough, B., Bennett, R. et al. ***The Genesis Discovery Mission: Return of Solar Matter to Earth***. Space Science Reviews 105, 509–534 (2003). [https://doi.org/10.1023/A:1024425810605](https://doi.org/10.1023/A:1024425810605).
* ***Grail References***

  Krebs, Gunter D. ***GRAIL A, B (Discovery 11, Ebb, Flow)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/grail.htm](https://space.skyrocket.de/doc_sdat/grail.htm) .

  NASA. ***Gravity Recovery and Interior Laboratory-A (GRAIL)***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2011-046A](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2011-046A) , downloaded Mar 3, 2024.

  NASA. ***Gravity Recovery and Interior Laboratory-B (GRAIL)***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2011-046B](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2011-046B) , downloaded Mar 3, 2024.

  eoPortal. (2012). ***GRAIL (Gravity Recovery and Interior Laboratory)***. May 30, 2012. [https://www.eoportal.org/satellite-missions/grail](https://www.eoportal.org/satellite-missions/grail), viewed Mar 14, 2024.

  Spath, Stuart. ***Small Spacecraft Design for the GRAIL Mission***. Aug 13, 2012, Small Satellite Conference. [https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=1027&context= smallsat&httpsredir=1](https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=1027&context=%20smallsat&httpsredir=1) , downloaded Mar 14, 2024.

  Edwards-Stewart, Christine. ***NASA’s Frail Spacecraft Formation Flight, End Mission Results, and Small-Satellite Applications***. Lockheed Martin Space Systems Company, Denver, CO. SSC13-X-2. 27th Annual AIAA/USU Conference on Small Satellites. [https://digitalcommons.usu.edu/cgi/viewcontent.cgi ?article=2979&context=smallsat](https://digitalcommons.usu.edu/cgi/viewcontent.cgi%20?article=2979&context=smallsat) , downloaded Mar 14, 2024.

  Zuber, Mark, and Christopher Russell eds. **GRAIL: Mapping the Moon's Interior**. Illustrated Edition, Springer, New York, NY, 2016.
* ***InSight References***

  Krebs, Gunter D. ***InSight (Discovery 12)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/insight.htm](https://space.skyrocket.de/doc_sdat/insight.htm) .

  NASA. ***InSight***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2018- 042A](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2018-%20042A) , downloaded Mar 3, 2024.

  NASA JPL. ***InSight Launch Press Kit***. Quick Facts – Launch Facts. [https://www.jpl.nasa.gov/ news/presskits/ insight/launch/facts/](https://www.jpl.nasa.gov/%20news/presskits/%20insight/launch/facts/) , downloaded Mar 5, 2024.

  NASA JPL. ***Mars InSight Landing Press Kit***. [https://www.jpl.nasa.gov/news/press_kits/ insight/landing/download/mars_insight_landing_presskit.pdf](https://www.jpl.nasa.gov/news/press_kits/%20insight/landing/download/mars_insight_landing_presskit.pdf) , downloaded Mar 31, 2024.

  Spaceflight101. ***InSight Instrument Overview***. NASA Insight Mission. [https://spaceflight101.com/ insight/insight-instruments/](https://spaceflight101.com/%20insight/insight-instruments/) , downloaded Mar 5, 2024.
* ***Juno References***

  Krebs, Gunter D. ***Juno (New Frontiers 2)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/ doc_sdat/juno.htm](https://space.skyrocket.de/%20doc_sdat/juno.htm) .

  NASA. ***Juno***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/display.action?id= 2011-040A](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/display.action?id=%202011-040A) , downloaded Mar 3, 2024.

  NASA JPL. ***Jupiter Orbit Insertion - Press Kit***. Not dated. [https://www.jpl.nasa.gov/news/ press_kits/juno/pdf/juno-hires.pdf](https://www.jpl.nasa.gov/news/%20press_kits/juno/pdf/juno-hires.pdf) , downloaded Mar 5, 2024.

  Bolton, S.J., Lunine, J., Stevenson, D. et al. ***The Juno Mission***. Space Sci Rev 213, 5–37 (2017). [https://doi.org/10.1007/s11214-017-0429-6](https://doi.org/10.1007/s11214-017-0429-6) .

  Dodge, Randy; Boyles, Mark A., 2007, ***Key and driving requirements for the Juno Payload of instruments***, [https://hdl.handle.net/2014/40566](https://hdl.handle.net/2014/40566) , AIAA Space Conference & Exposition, Long Beach, California, September 18-20, 2007., JPL Open Repository.
* ***Ladee References***

  Krebs, Gunter D. ***LADEE***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/ladee.htm](https://space.skyrocket.de/doc_sdat/ladee.htm) .

  NASA. ***Lunar Atmosphere and Dust Environment Explorer (LADEE)***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2013-047A](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2013-047A) , downloaded Mar 3, 2024.

  NASA. (2013). ***Lunar Atmosphere and Dust Environment Explorer (LADEE) Launch (Press Kit)***. NASA / Jet Propulsion Laboratory. August 2012. [https://www.jpl.nasa.gov/news/press_kits/ gllarpk.pdf](https://www.jpl.nasa.gov/news/press_kits/%20gllarpk.pdf) , downloaded Mar 5, 2024.

  Spaceflight101.com. (2018). ***Lunar Laser Communication Demonstration***. [https://spaceflight101.com/ladee/lunar-laser-com munication-demonstration/](https://spaceflight101.com/ladee/lunar-laser-com%20munication-demonstration/) , viewed Mar 5, 2024.

  Spaceflight101.com. (2018). ***Science Instruments***. [https://spaceflight101.com/ladee/science-instruments/](https://spaceflight101.com/ladee/science-instruments/)  , viewed Mar 5, 2024.

  Elphic, R.C., Delory, G.T., Hine, B.P. et al. ***The Lunar Atmosphere and Dust Environment Explorer Mission***. Space Sci Rev 185, 3–25 (2014). [https://doi.org/10.1007/s11214-014-0113-z](https://doi.org/10.1007/s11214-014-0113-z) , downloaded Apr 1, 2024.
* ***Lucy References***

  Krebs, Gunter D. ***Lucy (Discovery 13)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket. de/doc_sdat/lucy.htm](https://space.skyrocket.de/doc_sdat/lucy.htm) .

  NASA. ***Lucy***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/display.action?id= 2021-093A](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/display.action?id=%202021-093A) , downloaded Mar 3, 2024.

  SWRI. ***LUCY: Twelve Years, Eleven Asteroids, One Spacecraft***. updated Oct 17, 2020. Mission: Spacecraft. [https://lucy.swri](https://lucy.swri). edu/mission/Spacecraft.html , downloaded Mar 4, 2024.

  Catherine B. Olkin et al. (2021). ***Lucy Mission to the Trojan Asteroids: Instrumentation and Encounter Concept of Operations***. Planet. Sci. J. 2 172. Oct 2021. DOI 10.3847/PSJ/abf83f, [https://iopscience.iop.org/article/10.3847/ PSJ/abf83f/pdf](https://iopscience.iop.org/article/10.3847/%20PSJ/abf83f/pdf), downloaded Mar 4, 2024.

  Wikipedia. (2024). ***Lucy (spacecraft)***. [https://en.wikipedia.org](https://en.wikipedia.org) /wiki/Lucy_(spacecraft), last updated Feb 24, 2024, viewed Mar 4, 2024.

  Dunbar, Brian ed. **FY 2018 Budget Estimates**. NASA prepared for Office of the President. Last updated: Jul 26, 2023, [https://www.nasa.gov/wp-content/uploads/2018/02/fy_2018\_ budget\_ estimates.pdf?emrc=1b1694](https://www.nasa.gov/wp-content/uploads/2018/02/fy_2018_%20budget_%20estimates.pdf?emrc=1b1694) , downloaded Dec 16, 2022, pages PS21 – PS-24.
* ***Lunar Prospector References***

  Krebs, Gunter D. ***Lunar Prospector (Discovery 3)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/lunar_prospector.htm](https://space.skyrocket.de/doc_sdat/lunar_prospector.htm) .

  NASA. ***Lunar Prospector***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc](https://nssdc.gsfc). nasa.gov/nmc/spacecraft/display. action?id=1998-001A , downloaded Mar 3, 2024.

  Hubbard, G. S., A. B. Binder and W. Feldman, ***The Lunar Prospector Discovery Mission: Mission and Measurement Description***, 1997 IEEE Nuclear Science Symposium Conference Record, Albuquerque, NM, USA, 1997, pp. 22-26 vol.1, doi: 10.1109/NSSMIC.1997.672491, downloaded Mar 12, 2024.

  Andolz, Francisco J. **Lunar Prospector Mission Handbook**. April 10, 1998. Lockheed Martin Missiles & Space, Sunnyvale CA. [https://pds-geosciences.wustl.edu/missions/lunarp/schandbk.pdf](https://pds-geosciences.wustl.edu/missions/lunarp/schandbk.pdf) , downloaded Mar 12, 2024.

  Hubbard, G.S., Alan B. Binder, Thomas A. Dougherty, Sylvia A. Cox, ***The Lunar Prospector Discovery Mission: A new Approach to Planetary Science***, Acta Astronautica, Volume 41, Issues 4–10, 1997, Pages 585-597, ISSN 0094-5765, [https://doi.org/10.1016/S0094-5765(98)00070-8](https://doi.org/10.1016/S0094-5765\(98\)00070-8) .
* ***Mars 2020 (Mars Perseverance) References***

  Krebs, Gunter D. ***Mars 2020 (Perseverance).*** Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/ doc_sdat/mars-2020.htm](https://space.skyrocket.de/%20doc_sdat/mars-2020.htm) .

  NASA. ***Mars 2020***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/display. action?id=2020-052A](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/display.%20action?id=2020-052A) , downloaded Mar 3, 2024.
* ***Magellan References***

  Krebs, Gunter D. ***Magellan***. Gunter's Space Page. Retrieved Mar 3, 2024, from [https://space.skyrocket](https://space.skyrocket). de/doc_sdat/magellan.htm .

  NASA. ***Magellan***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/display. action?id=1989-033B](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/display.%20action?id=1989-033B) , downloaded Mar 3, 2024.

  NASA. ***Synthetic Aperture Radar (SAR)***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/experiment/display.action?id=1989-033B-01](https://nssdc.gsfc.nasa.gov/nmc/experiment/display.action?id=1989-033B-01) , downloaded Mar 7, 2024.

  NASA. ***Magellan Mission at a Glance.*** Solar System Exploration – Magellan Mission to Venus. [https://solarsystem.nasa.gov/ magellan/fact.html](https://solarsystem.nasa.gov/%20magellan/fact.html) , viewed Apr 1, 2024.

  GAO. ***Space Exploration – Cost, Schedule, and Performance of NASA’s Magellan Mission to Venus***. GAO Home - Reports & Testimonies. May 27, 1988, NSIAD-88-130FS, [https://www.gao.gov/products/ nsiad-88-130fs](https://www.gao.gov/products/%20nsiad-88-130fs) , downloaded Mar 3, 2024.
* ***Mars Climate Orbiter References***

  Krebs, Gunter D. ***Mars Climate Orbiter (MCO)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/mars_climate_orbiter.htm](https://space.skyrocket.de/doc_sdat/mars_climate_orbiter.htm) .

  NASA. ***Mars Climate Orbiter***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft/ display.action?id=1998-073A](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/%20display.action?id=1998-073A) , downloaded Mar 3, 2024.

  NASA. (1999) **Mars Climate Orbiter Arrival – Press Kit**. Sep 1999. [https://mars.nasa.gov/ internal_resources/812/](https://mars.nasa.gov/%20internal_resources/812/), downloaded Mar 12, 2024.
* ***MER A (MER 2) Spirit Rover References***

  Krebs, Gunter D. ***Mars Exploration Rover A, B (MER A, B / Spirit / Opportunity)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/mars_exploration \_rover.htm](https://space.skyrocket.de/doc_sdat/mars_exploration%20_rover.htm)

  NASA. ***Spirit***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/display.action?id= 2003-027A](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/display.action?id=%202003-027A) , downloaded Mar 3, 2024.

  NASA. (2003) ***Mars Exploration Rover Launches***. Jun 2003. [https://mars.nasa.gov/ internal_resources/827/](https://mars.nasa.gov/%20internal_resources/827/) , viewed Mar 14, 2024.

  Cook, Richard A., 2004, ***The Mars Exploration Rover Project***, [https://hdl.handle.net/2014/40202](https://hdl.handle.net/2014/40202), International Astronautical Congress, Vacouver, Bristish Columbia, Canada, October 02, 2004., JPL Open Repository.

  Stella, Paul & Ewell, R.C. & Hoskin, J.J. (2005). ***Design and Performance of the MER (Mars Exploration Rovers) Solar Arrays***. 626 - 630. 10.1109/PVSC.2005.1488209.

  MSNBC. ***NASA extends Mars rovers mission***. Associated Press. Oct. 16, 2007. [https://web.archive.org/ web/20071019042407/ http://www.msnbc.msn.com/id/21327647/](https://web.archive.org/%20web/20071019042407/%20http:/www.msnbc.msn.com/id/21327647/) , viewed Apr 24, 2024.
* ***MER B (Mer 1) Opportunity Rover References***

  Krebs, Gunter D. ***Mars Exploration Rover A, B (MER A, B / Spirit / Opportunity)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/mars_exploration \_rover.htm](https://space.skyrocket.de/doc_sdat/mars_exploration%20_rover.htm) .

  NASA. ***Opportunity***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/display. action?id=2003-032A](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/display.%20action?id=2003-032A) , downloaded Mar 3, 2024.
* ***Mars Global Surveyor References***

  Krebs, Gunter D. ***Mars Global Surveyor (MGS).*** Gunter's Space Page. Retrieved Mar 3, 2024, from [https://space.skyrocket](https://space.skyrocket) .de/doc_sdat/mars_global_surveyor.htm .

  NASA. ***Mars Global Surveyor***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft/ display.action?id=1996-062A](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/%20display.action?id=1996-062A) , downloaded Mar 3, 2024.

  Glenn E. Cunningham, ***Mars Global Surveyor Mission***, Acta Astronautica, Volume 38, Issues 4–8, 1996, Pages 367-375, ISSN 0094-5765, [https://doi.org/10.1016/0094-5765(96)00035-5](https://doi.org/10.1016/0094-5765\(96\)00035-5) .

  Albee, A. L., R. E. Arvidson, F. Palluconi, and T. Thorpe (2001), ***Overview of the Mars Global Surveyor Mission***, J. Geophys. Res., 106(E10), 23291–23316, doi:10.1029/2000JE001306.

  JPL. ***Mars Global Surveyor – Press Releases***. Apr 13, 2007. [https://mars.nasa.gov/mgs/newsroom/ 20070413a.html](https://mars.nasa.gov/mgs/newsroom/%2020070413a.html) , viewed Mar 17, 2024.
* ***Mars Observer References***

  Krebs, Gunter D. ***Mars Observer (MO).*** Gunter’s Space Page. Retrieved Mar 3, 2024, from [https://space.skyrocket.de/doc_sdat/mars_observer.htm](https://space.skyrocket.de/doc_sdat/mars_observer.htm) .

  Albee, A L, R. E. Arvidson and F D Palluconi. (1992) ***Mars Observer Mission***. Journal of Geophysical Research, Vol. 97, No. E5, May 25, 1992, pp. 7665-7680.

  Planetary Society. (2024) ***The Planetary Exploration Budget Dataset***. Database downloaded from [https://www.planetary.org/space-policy/planetary-exploration-budget-dataset](https://www.planetary.org/space-policy/planetary-exploration-budget-dataset) , downloaded Feb 2, 2024.

  NASA. ***Mars Observer***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa](https://nssdc.gsfc.nasa). gov/nmc/spacecraft/display.action?id=1992-063A , downloaded Mar 3, 2024.

  Malin, Michael C. et al. ***An overview of the 1985-2006 Mars Orbiter Camera science investigation***. The Mars Journal 4 (2010), pages 1-60.
* ***Mars Pathfinder References***

  Krebs, Gunter D. Mars Pathfinder (MPF, Discovery 1). Gunter's Space Page. Retrieved Mar 3, 2024, from [https://space.skyrocket.de/doc_sdat/mars_pathfinder.htm](https://space.skyrocket.de/doc_sdat/mars_pathfinder.htm) .

  NASA. ***Mars Pathfinder***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa](https://nssdc.gsfc.nasa). gov/nmc/spacecraft/display. action?id=1996-068A, downloaded Mar 3, 2024.

  NASA. ***Mars Pathfinder Rover***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft/ display.action?id=MESURPR](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/%20display.action?id=MESURPR) , downloaded Mar 3, 2024.

  Anbari, F. T., Critten, D., Deneny, T., Goculdas, K., Pottruff, & Ruiz, J. (2006). ***The Mars Pathfinder Project***. Case Studies in Project Management. [https://www.pmi.org/learning/library/mars-pathfinder-case-study-13318](https://www.pmi.org/learning/library/mars-pathfinder-case-study-13318) , viewed Mar 8, 2024.

  Spear, Anthony J., 1994, ***Low Cost Approach to Mars Pathfinder and Small Landers***, [https://hdl.handle.net/2014/33871](https://hdl.handle.net/2014/33871) , Laurel, Maryland, USA, JPL Open Repository.

  Cook, Richard A., 2004, ***The Mars Exploration Rover Project***, [https://hdl.handle.net/2014/40202](https://hdl.handle.net/2014/40202)  , International Astronautical Congress, Vacouver, Bristish Columbia, Canada, October 02, 2004., JPL Open Repository.

  Sturms, Francis M, William C Dias, Albert Y Nakata, Wallace D Tai.  ***Mars Pathfinder Mission Operations Concepts***. Jet Propulsion Laboratory. Document id 19950010814. Nov 1, 1994. [https://archive.org/details/nasa_techdoc_19950010814](https://archive.org/details/nasa_techdoc_19950010814)  , downloaded April 11, 2024.

  Kallemeyn, Pieter, Richard Cook, Anthony Spear, Matthew Golombek. ***The Mars Pathfinder Mission***. Presented at the 7th International Space Conference of Pacific Basin Societies (ISCOPS), Nagasaki, Japan, July 14-18, 1997, JPL Open Repository,  [https://dataverse.jpl.nasa.gov/dataset.xhtml? persistentId=hdl:2014/22399](https://dataverse.jpl.nasa.gov/dataset.xhtml?%20persistentId=hdl:2014/22399) , downloaded Apr 11, 2024.
* ***Mars Polar Lander References***

  Krebs, Gunter D. ***Mars Polar Lander (MPL)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/ doc_sdat/mars_polar_lander.htm](https://space.skyrocket.de/%20doc_sdat/mars_polar_lander.htm) .

  NASA. ***Mars Polar Lander***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft/ display.action?id=1999-001A](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/%20display.action?id=1999-001A) , downloaded Mar 3, 2024.

  IKI RAS (JPL mirror site). ***Mars Polar Lander Timeline***. [http://www.iki.rssi.ru/mpfmirror/msp98/lander/timeline.html](http://www.iki.rssi.ru/mpfmirror/msp98/lander/timeline.html), viewed Mar 13, 2024.
* ***Mars Reconnaissance Orbiter (MRO) References***

  Krebs, Gunter D. ***Mars Reconnaissance Orbiter (MRO)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space](https://space). skyrocket.de/doc_sdat/mro.htm .

  NASA. ***Mars Reconnaissance Orbiter***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft /display.action?id=2005-029A](https://nssdc.gsfc.nasa.gov/nmc/spacecraft%20/display.action?id=2005-029A) , downloaded Mar 3, 2024.

  Zurek, R. W., and S. E. Smrekar (2007). ***An overview of the Mars Reconnaissance Orbiter (MRO) science mission***. J. Geophys. Res., 112, E05S01, doi:10.1029/2006JE002701.

  Zurek, R.; Graf, J. (2001) ***Mars Reconnaissance Orbiter Mission***, [https://hdl.handle.net/2014/ 36860](https://hdl.handle.net/2014/%2036860) , ['IAF Congress', 'Toulouse, France'], JPL Open Repository.
* ***Mars Science Laboratory (MSL, Curiosity) References***

  Krebs, Gunter D. ***Mars Science Laboratory (MSL, Curiosity)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/msl.htm](https://space.skyrocket.de/doc_sdat/msl.htm) .

  NASA. ***Mars Science Laboratory (MSL)***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/ spacecraft/display.action?id=2011-070A](https://nssdc.gsfc.nasa.gov/nmc/%20spacecraft/display.action?id=2011-070A) , downloaded Mar 3, 2024.

  Martin, Paul K. (2011) **NASA’s Management of the Mars Science Laboratory Project**. Office of the Inspector General – Audit Report. Jun 8, 2011. Report No. IG-11-019 (Assignment Number A-10-007-00). [https://oig.nasa.gov/docs/IG-11-019.pdf](https://oig.nasa.gov/docs/IG-11-019.pdf) , downloaded 3/6/2024.

  Fields, Keith, 2012, ***Mass Property Measurements of the Mars Science Laboratory Rover***, [https://hdl.handle.net/2014/42953](https://hdl.handle.net/2014/42953) , 27th Space Simulation Conference, Annapolis, Maryland, November 5-8, 2012, JPL Open Repository.
* ***Maven References***

  Krebs, Gunter D. ***MAVEN (Mars Scout 2)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/ doc_sdat/maven.htm](https://space.skyrocket.de/%20doc_sdat/maven.htm) .

  NASA. ***Mars Atmosphere and Volatile EvolutioN (MAVEN)***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2013-063A](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2013-063A) , downloaded Mar 3, 2024.

  University of Colorado. ***MAVEN Spacecraft***. [https://lasp.colorado](https://lasp.colorado) .edu/maven/about/spacecraft/, viewed Mar 5, 2024.

  NASA. ***MAVEN – Press Kit***. Nov 2013. [https://mars.nasa.gov/files/resources/MAVEN_PressKit\_ Final.pdf](https://mars.nasa.gov/files/resources/MAVEN_PressKit_%20Final.pdf) , downloaded Mar 5, 2024.

  Anderson, Larry et al. ***The Langmuir Probe and Waves (LPW) Instrument for MAVEN***. Space Sci Rev (2015) 195:173–198, DOI 10.1007/s11214-015-0194-3,  [https://link.springer.com/article /10.1007/s11214-015-0194-3](https://link.springer.com/article%20/10.1007/s11214-015-0194-3), downloaded Mar 5, 2024.

  Jakosky, B.M. et al. ***The Mars Atmosphere and Volatile Evolution (MAVEN) Mission***. Space Sci Rev (2015) 195:3–48, DOI 10.1007/s11214-015-0139-x, [https://link.springer.com/article/ 10.1007/](https://link.springer.com/article/%2010.1007/) s11214-015-0139-x, downloaded Mar 5, 2024.
* ***Messenger References***

  Krebs, Gunter D. ***MESSENGER (Discovery 8)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/messenger.htm](https://space.skyrocket.de/doc_sdat/messenger.htm) .

  NASA. ***MESSENGER***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/display. action?id=2004-030A](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/display.%20action?id=2004-030A)  , downloaded Mar 3, 2024.

  NASA. (2014) ***Messenger – NASA’s Mission to Mercury – Launch Press Kit***. Aug 2004. [https://web.archive.org/ web/20070824103010/http://www.nasa.gov/pdf/168019main_MESSENGER_71504_PressKit.pdf](https://web.archive.org/%20web/20070824103010/http:/www.nasa.gov/pdf/168019main_MESSENGER_71504_PressKit.pdf) , downloaded Mar 6, 2024.

  Solomon, S.C., McNutt, R.L., Gold, R.E. et al. (2007) ***MESSENGER Mission Overview***. Space Sci Rev 131, 3–39 Oct 5, 2007. [https://doi.org/10.1007/s11214-007-9247-6](https://doi.org/10.1007/s11214-007-9247-6) , downloaded Mar 6, 2024.

  Ralph L. McNutt, Sean C. Solomon, Robert E. Gold, James C. Leary. (2006) ***The MESSENGER mission to Mercury: Development history and early mission status***. Advances in Space Research, Volume 38, Issue 4, 2006, Pages 564-571, ISSN 0273-1177, [https://doi.org/10.1016/j.asr.2005 .05.044](https://doi.org/10.1016/j.asr.2005%20.05.044) , downloaded Mar 6, 2024.

  Santo, Andrew G, et al. ***The MESSENGER mission to Mercury: spacecraft and mission design***. Planetary and Space Science, Volume 49, Issues 14–15, 2001, Pages 1481-1500, ISSN 0032-0633, [https://doi.org/10.1016/S0032-0633(01)00087-3](https://doi.org/10.1016/S0032-0633\(01\)00087-3), downloaded Apr 19, 2024.

  Solomon, Sean C, et al. The MESSENGER mission to Mercury: scientific objectives and implementation. ***Planetary and Space Science,*** ***Volume 49, Issues 14–15,*** ***2001,*** ***Pages 1445-1465,*** ***ISSN 0032-0633,*** [https://doi.org/10.1016/S0032-0633(01)00085-X](https://doi.org/10.1016/S0032-0633\(01\)00085-X), downloaded Apr 19, 2024.
* ***NEAR (Near Earth Asteroid Rendezvous) References***

  Krebs, Gunter D. ***NEAR (Discovery 2, Shoemaker)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space](https://space). skyrocket.de/doc_sdat/near.htm .

  NASA. ***NEAR Shoemaker***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft /display.action?id=1996-008A](https://nssdc.gsfc.nasa.gov/nmc/spacecraft%20/display.action?id=1996-008A) , downloaded Mar 3, 2024.
* ***New Horizons References***

  Krebs, Gunter D. ***New Horizons (New Frontiers 1)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/ doc_sdat/new-horizons.htm](https://space.skyrocket.de/%20doc_sdat/new-horizons.htm) .

  NASA. ***New Horizons Pluto Kuiper Belt Flyby***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/display.action?id=2006-001A](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/display.action?id=2006-001A) , downloaded Mar 3, 2024.
* ***Osiris-Rex References***

  Krebs, Gunter D. ***OSIRIS-REx → OSIRIS-APEX (New Frontiers 3)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc_sdat/osiris-rex.htm](https://space.skyrocket.de/doc_sdat/osiris-rex.htm) .

  NASA. ***OSIRIS-Rex***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/display. action?id=2016-055A](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/display.%20action?id=2016-055A) , downloaded Mar 3, 2024.

  Spaceflight101. (2024). ***OSIRIS-REx Mission & Trajectory Design***. [https://spaceflight101.com/osiris-rex/osiris-rex-mission-profile/](https://spaceflight101.com/osiris-rex/osiris-rex-mission-profile/) . viewed Mar 14. 2024.

  Spaceflight101. (2024). ***OSIRIS-REx Spacecraft***. [https://spaceflight101.com/osiris-rex/osiris-rex-spacecraft-overview/](https://spaceflight101.com/osiris-rex/osiris-rex-spacecraft-overview/) . viewed Mar 14. 2024.
* ***Phoenix References***

  Krebs, Gunter D. ***Phoenix (Mars Scout 1)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de](https://space.skyrocket.de) /doc_sdat/phoenix.htm.

  NASA. ***Phoenix Mars Lander***. NASA Space Science Data Coordinated Achieve. [https://nssdc](https://nssdc). gsfc.nasa.gov/nmc/spacecraft /display.action?id=2007-034A , downloaded Mar 3, 2024.

  NASA. ***Phoenix Launch - Mission to the Martian Polar North – Press Kit***. Aug 2007. [https://www.jpl.nasa.gov/news/press\_ kits/phoenix-launch-presskit.pdf](https://www.jpl.nasa.gov/news/press_%20kits/phoenix-launch-presskit.pdf) , downloaded Mar 5, 2024.

  NASA. ***Phoenix Mars Mission – Mission Fact Sheet***. Nov 2005. [https://mars.nasa.gov/ internal_resources/817/](https://mars.nasa.gov/%20internal_resources/817/) , viewed Mar 5, 2024.

  NASA (2007). Phoenix Launch - Mission to the Martian Polar North – Press Kit. Aug 2007. [https://www.nasa.gov/wp-content/uploads/2015/03/181835main_phoenix-launch-presskit.pdf](https://www.nasa.gov/wp-content/uploads/2015/03/181835main_phoenix-launch-presskit.pdf) , downloaded Mar 6, 2024.

  Goldstein, Barry, and Robert Shotwell (2008) ***Phoenix – the first Mars scout mission***, [https://hdl.handle.net/2014/45413](https://hdl.handle.net/2014/45413) , 59th International Astronautical Congress, Glasgow, Scotland, September 29 - October 3, 2008, JPL Open Repository.

  Smith, P. H., et al. (2008), ***Introduction to special section on the Phoenix Mission: Landing Site Characterization Experiments, Mission Overviews, and Expected Science***, J. Geophys. Res., 113, E00A18, [https://doi.org/10.1029/2008JE003083](https://doi.org/10.1029/2008JE003083) , downloaded Apr 23, 2024.

  Carolyn R. Mercer, **Photovoltaics for Space.** Elsevier, 2023, Pages 349-378, ISBN 9780128233009, [https://doi.org/10.1016/B978-0-12-823300-9.00006-6](https://doi.org/10.1016/B978-0-12-823300-9.00006-6).
* ***Psyche References***

  Krebs, Gunter D. ***Psyche (Discovery 14)***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket.de/doc\_ sdat/psyche.htm](https://space.skyrocket.de/doc_%20sdat/psyche.htm) .

  NASA. ***Psyche***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/display.action?id= 2023-157A](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/display.action?id=%202023-157A) , downloaded Mar 3, 2024.

  Dunbar, Brian ed. **FY 2018 Budget Estimates**. NASA prepared for Office of the President. Last updated: Jul 26, 2023, [https://www.nasa.gov/wp-content/uploads/2018/02/fy_2018 \_budget\_ estimates.pdf?emrc=1b1694](https://www.nasa.gov/wp-content/uploads/2018/02/fy_2018%20_budget_%20estimates.pdf?emrc=1b1694) , downloaded Dec 16, 2022, pages PS25 – PS-29.

  Solish, Benjamin; Drain, Tracy; Hart, Shirley; Hart, William; Geiser, Joshua; Lum, Karen; Oh, David, 2019, ***Psyche Early Project Verification & Validation Planning Development***, [https://hdl.handle.net/2014/52301](https://hdl.handle.net/2014/52301) , IEEE Aerospace Conference 2019, Big Sky, Montana, March 2-9, 2019, JPL Open Repository.

  Hart, William; Brown, G. Mark; Collins, Steven M.; De Soria-Satacruz, Maria; Fiesler, Paul; Goebel, Dan; Marsh, Danielle; Oh, David Y.; Snyder, Steve; Warner, Noah; Whiffen, Gregory; Elkins-Tanton, Linda T.; Bell III, James F.; Lawrence, David J.; Lord, Peter; Prikl, Zachary, 2018, ***Overview of the Spacecraft Design for the Psyche Mission Concept***, [https://hdl.handle.net/2014/47495](https://hdl.handle.net/2014/47495), 2018 IEEE Aerospace Conference, Big Sky, Montana, March 3-10, 2018, JPL Open Repository.

  Wikipedia. (2024). ***Psyche (spacecraft)***. [https://en.wikipedia.org/ wiki/Psyche_(spacecraft)](https://en.wikipedia.org/%20wiki/Psyche_\(spacecraft\)), last updated Feb 10, 2024, viewed Mar 4, 2024.
* ***Stardust References***

  Krebs, Gunter D. ***Stardust (Discovery 4) / NExT***. Gunter's Space Page. Retrieved March 03, 2024, from [https://space.skyrocket](https://space.skyrocket) .de/doc_sdat/stardust.htm .

  NASA. ***Stardust/NExT***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display. action?id=1999-003A](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.%20action?id=1999-003A) , downloaded Mar 3, 2024.

  NASA. ***Stardust Sample Return Capsule***. NASA Space Science Data Coordinated Achieve. [https://nssdc.gsfc.nasa.gov/ nmc/spacecraft/display.action?id=1999-003D](https://nssdc.gsfc.nasa.gov/%20nmc/spacecraft/display.action?id=1999-003D) , downloaded Mar 3, 2024.

