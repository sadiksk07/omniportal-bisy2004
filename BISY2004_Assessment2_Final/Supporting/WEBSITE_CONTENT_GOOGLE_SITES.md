# PROJECT OMNIPORTAL — GOOGLE SITES TEXT & LAYOUT BLUEPRINT
**Course:** BISY2004 Project Management | Assessment 2  
**Institution:** Australian Institute of Higher Education  
**Group Members:**
- Tanvir Ahmed (Student ID: 238983) — Project Lead & Systems Architect
- Momen Ahmed (Student ID: 242048) — Risk, Finance & Governance Lead
- MD Rejvi Jaman Mafti (Student ID: 241964) — Quality, Delivery & Tracking Lead

---

## Google Sites Navigation Setup
When setting up Google Sites, create a **Top Navigation Menu** with the following 6 main pages (or one scrolling homepage with section anchors):
1. **1. Scope & WBS** (Lead: Tanvir Ahmed)
2. **2. Schedule & Cost** (Lead: Tanvir Ahmed & Momen Ahmed)
3. **3. Risk & Stakeholders** (Lead: Momen Ahmed)
4. **4. Quality & Change** (Lead: MD Rejvi Jaman Mafti)
5. **5. Dashboard & EVM** (Lead: MD Rejvi Jaman Mafti)
6. **6. Final Recommendation** (Collaborative Synthesis)

---

## PAGE 1: PROJECT OVERVIEW, CHARTER & SCOPE
*(Assigned Lead: Tanvir Ahmed — 238983)*

### Business Problem & Need
Apex Metropolitan University (28,000 students, 3,200 staff) currently operates four fragmented, legacy student-facing platforms: Blackboard (LMS), Ellucian Banner (SIS for enrolment and records), TouchNet (tuition fee billing), and Zendesk (support queries). This fragmentation forces students to navigate disparate logins and interfaces, resulting in 4,200 repetitive helpdesk tickets per semester, an 18% record desynchronization rate, and $185,000 in annual recurring multi-vendor maintenance overheads.

### Project Purpose & SMART Objectives
Project OmniPortal will consolidate all student administrative, academic, and financial workflows into a unified, cloud-native, responsive web platform. The project is governed by four SMART objectives:
1. **Schedule:** Complete production cutover within 24 calendar weeks (120 working days) prior to Semester 1 enrolment.
2. **Cost:** Restrict total capital and operational expenditure to the approved $450,000 AUD budget cap.
3. **Scope & Quality:** Achieve 100% data fidelity migrating 28,000 student academic profiles with zero record loss.
4. **Performance:** Deliver 99.95% system uptime and sub-1.80 second page response under 12,000 concurrent sessions.

### Project Life Cycle Approach
A **Hybrid Agile-Waterfall** lifecycle is deployed:
- **Predictive Waterfall:** Governs Project Initiation, Enterprise Architecture, Data Privacy Compliance (APP/GDPR), Infrastructure Provisioning, and Final Blue-Green Production Cutover.
- **Adaptive Agile (Scrum):** Executes two-week development sprints for UI/UX wireframing, feature microservice coding, and automated ETL data migration scripts.

### Scope Boundaries & Exclusions
- **In-Scope Deliverables:** Centralized Single Sign-On (SSO) with Multi-Factor Authentication (MFA); Course enrolment and cart checkout; Interactive timetable scheduler; Tuition fee payment integration; Automated ETL migration of 28,000 historical records; WCAG 2.1 AA responsive web interface.
- **Explicit Project Exclusions:** Migration of legacy human resource and employee payroll systems; Native compiled binary mobile app store packages (iOS/Android native apps); Replacement of physical student smartcard campus turnstiles; Ongoing operational tier-1 helpdesk staffing beyond the 30-day hypercare period.

### Work Breakdown Structure (WBS)
*(Insert WBS Diagram Export from diagrams.net here: `A2_Group_WBS_Diagram.png`)*
The project is decomposed into six level-1 work packages:
- **1.0 Project Initiation & Governance** (15 days, $16,500)
- **2.0 Requirements & Architecture** (20 days, $31,200)
- **3.0 Data Migration & Security Setup** (25 days, $39,500)
- **4.0 Core Portal Development** (35 days, $68,000)
- **5.0 Testing, Quality Assurance & Pilot** (20 days, $34,800)
- **6.0 Training, Deployment & Closure** (15 days, $24,200)

### Section 1 Artefact Interpretation & Management Decision
- **What it Shows:** A 100% rule-compliant hierarchical breakdown defining 6 core deliverables, 28 discrete work packages, and 6 milestone quality gates.
- **Why it is Important:** Establishes unambiguous ownership, separates in-scope deliverables from excluded payroll systems, and provides the baseline structure for the ProjectLibre schedule.
- **Management Decision:** Enforced a strict scope baseline freeze following Milestone 2 architectural sign-off. Any non-mandatory feature requests must submit formal Change Requests to prevent scope creep.

---

## PAGE 2: SCHEDULE, COST & RESOURCES
*(Assigned Leads: Tanvir Ahmed — 238983 & Momen Ahmed — 242048)*

### ProjectLibre Schedule & Critical Path Analysis
*(Insert ProjectLibre Gantt Chart Screenshot here: Showing Critical Path in Red)*
The ProjectLibre schedule models 120 working days (02 February 2026 to 17 July 2026). The Critical Path is 86 working days and spans:
**1.1 → 1.2 → 1.3 → 2.1 → 2.3 → 2.4 → 3.1 → 3.2 → 3.3 → 4.1 → 4.2 → 4.3 → 4.4 → 5.1 → 5.2 → 5.3 → 5.4 → 6.3 → 6.4**.

#### Six Formal Milestone Quality Gates:
| Milestone | Deliverable Name | Scheduled Date | Total Float | Gate Approver |
| :--- | :--- | :---: | :---: | :--- |
| **M1** | Project Charter & Governance Framework Signed Off | 20-Feb-2026 | 0 Days | CIO / Project Sponsor |
| **M2** | Technical Architecture & API Specifications Approved | 20-Mar-2026 | 0 Days | Lead Solutions Architect |
| **M3** | Data Cleansing & Automated ETL Scripts Validated | 24-Apr-2026 | 0 Days | Database & Migration Lead |
| **M4** | Core Portal Development Feature Complete | 12-Jun-2026 | 0 Days | Lead Developer & PM |
| **M5** | UAT & Independent Security Penetration Sign-Off | 10-Jul-2026 | 0 Days | University Registrar & CIO |
| **M6** | Production Cutover & Operational Handover | 17-Jul-2026 | 0 Days | Steering Committee |

### Cost Model & Resource Budget Breakdown
*(Insert Cost Breakdown Table from Excel: `A2_Group_University_Portal_Data.xlsx`)*
- **Direct Labour Expenditure:** $219,600 (305 resource days across Project Manager at $95/hr, Solutions Architect at $115/hr, Full-Stack Devs at $85/hr, Database Specialist at $95/hr, QA/Security at $80/hr, and Change Lead at $75/hr).
- **Capital & Non-Labour Expenditure (Capex):** $90,500 (AWS multi-AZ hosting $28,500; Okta SSO licences $24,000; CREST penetration testing $16,500; video training media $9,500; UI/UX testing lab $6,200; payment gateway escrow $5,800).
- **Subtotal Cost Baseline (BAC):** **$385,000 AUD**.
- **Contingency Reserve (10% of BAC):** $38,500 AUD (allocated for technical migration risks and interface rework).
- **Total Cost Baseline:** **$423,500 AUD**.
- **Management Reserve (5% of BAC):** $19,250 AUD (reserved for unforeseen institutional scope changes).
- **Total Approved Project Budget:** **$442,750 AUD** (Leaves $7,250 headroom below the $450,000 institutional ceiling).

### Section 2 Artefact Interpretation & Management Decision
- **What it Shows:** The ProjectLibre schedule proves that database migration (WBS 3.2) and payment integration (WBS 4.4) possess zero total float and dictate the project completion date.
- **Why it is Important:** Non-critical tasks (such as training guide production with 8 days float) can absorb minor delays, whereas any delay on ETL scripts directly threatens the Semester 1 cutover.
- **Management Decision:** Ring-fenced the Senior Database Specialist's time and pre-authorized an immediate drawdown of up to $7,000 from contingency reserves if ETL data reconciliation falls behind by more than 3 days.

---

## PAGE 3: RISK, STAKEHOLDERS & COMMUNICATION
*(Assigned Lead: Momen Ahmed — 242048)*

### 5×5 Risk Assessment & Top Risk Priorities
*(Insert 5×5 Risk Heat Map Screenshot from Excel)*
Risks are evaluated using a 5×5 scoring model ($Likelihood \times Impact$, range 1–25). Ten active risks are monitored:
1. **R01 — Legacy DB Schema Mismatch & Data Corruption ($L=4, I=5 \rightarrow \mathbf{20}$, Extreme):** Automated ETL script failure. *Mitigation:* Staged ETL sandbox runs with 10% data sampling; automated schema validation scripts with instant rollback checkpoints.
2. **R02 — Infrastructure Outage During Enrolment Surge ($L=3, I=5 \rightarrow \mathbf{15}$, Extreme):** Server crash during peak traffic (>10,000 concurrent). *Mitigation:* AWS Auto-Scaling, Redis caching; automated stress testing at 250% capacity (15,000 sessions).
3. **R03 — User Adoption Resistance from Academic Staff ($L=4, I=3 \rightarrow \mathbf{12}$, High):** Faculty pushback against new grading UI. *Mitigation:* Appoint 12 departmental 'Change Champions'; deliver 30-min drop-in clinics and video micro-guides.
4. **R04 — Student PII Data Breach ($L=2, I=5 \rightarrow \mathbf{10}$, High):** Violation of Australian Privacy Principles. *Mitigation:* AES-256 at-rest and TLS 1.3 in-transit encryption; independent CREST penetration testing.
5. **R05 — Scope Creep from Inter-Faculty Demands ($L=4, I=3 \rightarrow \mathbf{12}$, High):** Conflicting customization requests. *Mitigation:* Strict Change Control Board (CCB) review; freeze non-mandatory features for Phase 2.

### Stakeholder Analysis & Power-Interest Classification
*(Insert Stakeholder Power-Interest Matrix from diagrams.net: `A2_Group_Stakeholder_Matrix.png`)*
- **Manage Closely (High Power, High Interest):** CIO / Project Sponsor (SH01), University Registrar (SH02), Central IT Security (SH05). Handled via weekly 1-on-1 briefings and fortnightly Steering Committee meetings.
- **Keep Satisfied (High Power, Low Interest):** Academic Senate (SH03), TEQSA Regulators (SH08), Finance Office (SH06). Handled via monthly progress digests and formal compliance audits.
- **Keep Informed (Low Power, High Interest):** Student Representative Council & Student Body (SH04), Helpdesk Staff (SH07). Handled via bi-weekly email bulletins, student focus groups, and live training workshops.

### Section 3 Artefact Interpretation & Management Decision
- **What it Shows:** The 5×5 heat map clusters technical migration (R01) and peak infrastructure scalability (R02) in the critical red zone.
- **Why it is Important:** Proves that project viability hinges on technical data architecture and privacy compliance rather than cosmetic visual design.
- **Management Decision:** Reallocated $16,500 of the Capex budget to commission an external CREST-certified penetration testing firm and mandated stress testing at 2.5× peak historical traffic.

---

## PAGE 4: QUALITY, CHANGE & TEAM STRUCTURE
*(Assigned Lead: MD Rejvi Jaman Mafti — 241964)*

### Measurable Quality Requirements & Verification Standards
Quality is controlled through six binding, quantifiable acceptance metrics:
1. **System Availability:** $\ge 99.95\%$ uptime during semester terms (verified by AWS CloudWatch Synthetics 24/7).
2. **Peak Concurrency Response:** $< 1.80$ seconds page load at 12,000 concurrent sessions (verified via JMeter automated load tests).
3. **Migration Fidelity:** $100.0\%$ checksum hash match across 28,000 student academic records (zero data loss).
4. **Software Defect Density:** Exactly zero Severity-1 (Critical) or Severity-2 (High) defects at UAT sign-off.
5. **Student Usability:** $\ge 80/100$ System Usability Scale (SUS) score across a 50-student beta cohort.
6. **Cybersecurity Assurance:** Zero High or Critical CVE vulnerabilities confirmed by independent CREST penetration testing.

### Formal Change Management: Change Request CR-01
- **Title:** Mandatory Multi-Factor Authentication (MFA) & Mobile Push SSO Integration.
- **Origin & Justification:** Mandated on 14-Apr-2026 by University Cybersecurity Advisory Board to comply with Australian Cyber Security Centre (ACSC) Essential Eight directives.
- **Scope Impact:** Integration of Twilio SMS microservice, Authenticator app TOTP hooks, and 'Remember Device for 30 Days' secure cookie logic.
- **Schedule Impact:** $+8$ working days in authentication development, absorbed by fast-tracking UI testing in parallel with Sprint 2 (zero net change to go-live date).
- **Cost Impact:** $+\$14,500$ AUD, funded entirely from the approved $\$38,500$ Contingency Reserve (Baseline budget unaffected).
- **CCB Decision:** **APPROVED** by Project Sponsor (CIO) on 18-Apr-2026.

### RACI Governance Structure
The RACI matrix guarantees single-point accountability:
- **1.0 Initiation:** Accountable = Sponsor; Responsible = PM.
- **2.0 Requirements & Architecture:** Accountable = PM; Responsible = Solutions Architect.
- **3.0 Data Migration:** Accountable = PM; Responsible = Database Lead.
- **4.0 Core Development:** Accountable = PM; Responsible = Lead Dev Team.
- **5.0 Testing & UAT:** Accountable = PM; Responsible = QA & Security Lead.
- **6.0 Deployment & Closure:** Accountable = Sponsor; Responsible = PM & Change Lead.

### Section 4 Artefact Interpretation & Management Decision
- **What it Shows:** The RACI matrix and Change Log demonstrate that changes are evaluated against scope, schedule, cost, and risk before authorization.
- **Why it is Important:** Confirms that CR-01 was absorbed methodically without schedule delay, utilizing pre-planned contingency reserves.
- **Management Decision:** Approved drawing $14,500 from the Contingency Reserve to fund CR-01 while enforcing an immediate freeze on all further enhancement requests.

---

## PAGE 5: TRACKING & PROJECT DASHBOARD
*(Assigned Lead: MD Rejvi Jaman Mafti — 241964)*

### Trello Sprint Workflow & Task Linkage
The Trello board translates WBS work packages into active sprint task cards across five standard columns: *Backlog*, *Sprint Backlog / To Do*, *In Progress*, *Review & QA*, and *Done*. Every Trello card links explicitly to its corresponding WBS task ID and ProjectLibre activity.

### Mid-Project Status Review (Week 14 EVM Snapshot)
*(Insert EVM KPI Dashboard Graphic from Excel)*
- **Planned Value (PV):** $\$225,000$ AUD
- **Earned Value (EV):** $\$198,000$ AUD
- **Actual Cost (AC):** $\$210,000$ AUD
- **Schedule Variance (SV):** $EV - PV = -\$27,000$ AUD *(Unfavourable — Behind Schedule)*
- **Cost Variance (CV):** $EV - AC = -\$12,000$ AUD *(Unfavourable — Over Budget)*
- **Schedule Performance Index (SPI):** $\frac{EV}{PV} = \mathbf{0.880}$ *(10 working days behind plan)*
- **Cost Performance Index (CPI):** $\frac{EV}{AC} = \mathbf{0.943}$
- **Estimate at Completion (EAC):** $\frac{BAC}{CPI} = \frac{\$385,000}{0.943} = \mathbf{\$408,271}$ AUD (Fully covered by contingency).

### Variance Root Cause & Corrective Management Action
- **Identified Variance:** At Week 14, earned progress is 51.4% against a planned 58.4% (SPI = 0.880, 10 working days delayed on Critical Path task 3.2: Automated ETL Scripts).
- **Root Cause Analysis:** The legacy Ellucian Banner database contained 14 unindexed tables and corrupted student address strings, causing migration scripts to crash during initial test runs.
- **Corrective Management Action:**
  1. *Schedule Crashing:* Allocated $\$6,800$ from the Contingency Reserve to onboard an external Senior ETL Engineer for 10 days to run data cleansing concurrently with API stub development.
  2. *Fast-Tracking:* Re-sequenced Sprint 3 course enrolment frontend development using simulated mock data rather than waiting for 100% database population.
  3. *Outcome:* Recovered 7 of the 10 lost days by Week 16; SPI rebounded to 0.96; final go-live milestone protected.

### Section 5 Artefact Interpretation & Management Decision
- **What it Shows:** Objective EVM metrics caught an isolated 10-day delay in database migration at Week 14.
- **Why it is Important:** Allowed management to intervene before the delay could cascade into UAT and threaten the Semester 1 cutover.
- **Management Decision:** Approved a targeted crashing intervention ($6,800 contingency spend) and frontend fast-tracking, pulling the project back onto its critical path schedule.

---

## PAGE 6: INTEGRATION & FINAL MANAGEMENT RECOMMENDATION
*(Group Collaborative Synthesis)*

### Cross-Domain Artefact Integration
Project OmniPortal exhibits end-to-end integration across all project management domains:
- **Scope to Schedule:** The 28 WBS work packages map 1:1 into the ProjectLibre schedule and Trello sprint cards.
- **Schedule to Cost:** Activity durations and assigned labour rates directly establish the $\$385,000$ BAC baseline.
- **Risk to Cost:** The 5×5 Risk Register justified the $\$38,500$ Contingency Reserve, which subsequently absorbed Change Request CR-01 ($\$14,500$) and the Week 14 ETL crashing action ($\$6,800$).
- **Variance to Control:** Mid-project EVM tracking diagnosed an SPI slip to 0.880, triggering the corrective crashing and fast-tracking actions that protected the critical path.

### Final Management Recommendation
The Project Management Team formally recommends that the Project Sponsor and University Steering Committee **AUTHORIZE PROCEEDING TO FINAL PRODUCTION CUTOVER (GO-LIVE)** on 17 July 2026.

**Justification:**
1. **Schedule Readiness:** All six milestone quality gates (M1 to M6) have been completed; critical path float is restored to zero.
2. **Budget Health:** The final projected cost at completion (EAC) is $\$406,300$ AUD, leaving $\$43,700$ headroom below the $\$450,000$ institutional ceiling.
3. **Quality & Compliance Verification:** Achieved 100.0% data fidelity migrating 28,000 records; zero open P1/P2 defects; independent CREST penetration testing cleared with zero critical CVEs.
4. **Benefits Realization:** Upon cutover, legacy platform decommissioning will begin immediately, realizing $\$120,000$ in annual recurring licensing savings and reducing helpdesk volume by an estimated 50%.
