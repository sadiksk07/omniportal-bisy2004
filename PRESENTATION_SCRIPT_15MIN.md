# BISY2004 Assessment 2: Live In-Class Presentation Script (12–15 Minutes)
**Project Title:** Project OmniPortal — University Student Portal Consolidation  
**Target Duration:** 12 to 14 minutes (+ 2 min questions)  
**Total Marks:** 10 Marks (Individual Assessment)  

---

## Group Speaker Breakdown & Timing

| Speaker | Assigned Role | Section Covered | Time Allocated | Primary Artefact Interpreted |
| :--- | :--- | :--- | :---: | :--- |
| **Tanvir Ahmed (238983)** | Project Lead | **Section 1 & Section 2** (Scope, WBS, Schedule, Critical Path, Cost) | 0:00 – 4:30 (4.5 min) | **WBS (draw.io) & ProjectLibre Gantt Chart** |
| **Momen Ahmed (242048)** | Risk & Governance Lead | **Section 3 & Section 2 (Cost Model)** (Risk Register, 5×5 Heat Map, Stakeholder Matrix, Budget) | 4:30 – 9:00 (4.5 min) | **5×5 Risk Heat Map & Stakeholder Matrix** |
| **MD Rejvi Jaman Mafti (241964)** | Quality & Delivery Lead | **Section 4, Section 5 & Section 6** (Quality Gates, CR-01, RACI, Trello, EVM Dashboard, Recommendation) | 9:00 – 13:30 (4.5 min) | **EVM Status Dashboard & Trello Kanban Linkage** |
| **All Members** | Collaborative | **Q&A & Viva Transition** | 13:30 – 15:00 (1.5 min) | **Cross-domain synthesis** |

---

## SPEAKER 1: Tanvir Ahmed (Student ID: 238983)
**Duration:** 0:00 – 4:30  
**Screens to Display:** Live Website Homepage -> Section 1 (Overview, Scope & WBS) -> Section 2 (ProjectLibre Gantt & Critical Path)

### Verbatim Presentation Script:
> "Good morning, respected lecturer and fellow students. Today, our team—Momen, Rejvi, and myself, Tanvir—is proud to present **Project OmniPortal**, our integrated project management framework for consolidating university student portals at Apex Metropolitan University.
>
> *(Navigate to Section 1: Overview & Scope)*
>
> Let us begin with the core business problem. Currently, our university operates four separate legacy portals: Blackboard LMS, Ellucian Banner SIS for enrolment, TouchNet for tuition payments, and Zendesk for student support. This fragmentation causes severe operational friction: students endure conflicting logins, staff face an 18% record desynchronization rate, and during semester enrolment periods, our student central helpdesk is overwhelmed with over 4,200 repetitive support tickets. Furthermore, maintaining four separate vendor contracts costs the university $185,000 annually.
>
> To resolve this, Project OmniPortal will deliver a consolidated, cloud-native platform providing centralized Single Sign-On, real-time enrolment, an interactive timetable builder, and automated fee processing. We are operating under four strict constraints: a fixed 24-week delivery window (120 working days) prior to Semester 1 enrolment, a hard budget cap of $450,000 AUD, 100% data fidelity migrating 28,000 student academic profiles, and a 99.95% system uptime standard.
>
> To govern this complex transformation, we adopted a **Hybrid Agile-Waterfall** lifecycle. We utilize predictive Waterfall governance for enterprise architecture, data privacy regulations, and deployment cutover, while deploying two-week Agile sprints for UI/UX design, microservice feature coding, and automated ETL scripts.
>
> *(Scroll to WBS Diagram)*
>
> Here you see our **Work Breakdown Structure**, constructed in diagrams.net. Decomposed strictly using the 100% rule, our project is partitioned into six level-1 deliverables, 28 discrete work packages, and six formal milestone quality gates. Notice how we established clear boundaries: in-scope features encompass core academic workflows and MFA authentication, while legacy HR payroll systems and native compiled app-store binary applications are explicitly excluded to protect our project baseline.
>
> *(Navigate to Section 2: Schedule & ProjectLibre Gantt)*
>
> Turning to our project schedule in **ProjectLibre**, our 120-day timeline spans from 2 February to 17 July 2026. Rather than simply displaying the Gantt chart, let me interpret its critical path implications.
>
> In ProjectLibre, the red Gantt bars trace our **86-working-day Critical Path**. It connects Tasks 1.1 through 2.4, passes directly into **WBS 3.2: Automated ETL Script Development**, moves through core sprint features, and terminates at **WBS 5.3: User Acceptance Testing** and **6.3: Production Cutover**. 
>
> The key management deduction from this evidence is that activities along this path have **zero total float**. If our database migration scripts slip by even a single business day, our Semester 1 go-live deadline is breached. Conversely, non-critical tasks—such as producing student video walkthroughs in WBS 6.1—possess 8 days of float. This vital insight allowed management to ring-fence our senior database engineers and protect the zero-float path.
>
> I will now hand over to Momen Ahmed to interpret our cost model, risk analysis, and stakeholder governance."

---

## SPEAKER 2: Momen Ahmed (Student ID: 242048)
**Duration:** 4:30 – 9:00  
**Screens to Display:** Live Website Section 2 (Cost Model Table) -> Section 3 (Risk Register, 5×5 Heat Map & Stakeholder Matrix)

### Verbatim Presentation Script:
> "Thank you, Tanvir. Good morning everyone. I will now explain our cost engineering, risk architecture, and stakeholder engagement strategy.
>
> *(Scroll to Cost & Budget Breakdown Table in Section 2)*
>
> Our financial model in Excel is structured across two expenditure pillars: Direct Labour and Capital Non-Labour expenditure. Direct project labour totals $219,600 across 305 resource days, pricing specialist roles from our Project Manager at $95/hr down to technical trainers at $75/hr. Capital expenditure totals $90,500, funding AWS multi-AZ cloud infrastructure, Okta enterprise SSO licensing, and independent security audits.
>
> This establishes our **Budget at Completion (BAC)** at **$385,000 AUD**. To safeguard against technical uncertainties, we calculated an explicit 10% **Contingency Reserve** of $38,500, establishing our baseline cost at $423,500. A 5% **Management Reserve** of $19,250 covers unforeseen strategic scope additions, bringing our total approved project budget to **$442,750 AUD**—safely maintaining $7,250 in reserve headroom below the university's $450,000 cap.
>
> *(Navigate to Section 3: Risk Register & 5×5 Heat Map)*
>
> Now, let us examine our **5×5 Risk Heat Map** created in Excel. We evaluated project threats using a formal scoring formula: Likelihood (1 to 5) multiplied by Impact (1 to 5), categorizing risks into Low, Medium, High, and Extreme.
>
> Looking at the heat map, our top vulnerability is **Risk R01: Legacy database schema mismatch and data corruption during automated ETL execution**. Because corrupting student academic records carries severe regulatory penalties and operational catastrophe, we assigned an Impact of 5 and a Likelihood of 4, yielding an **Extreme risk score of 20**.
>
> Our second major threat is **Risk R02: Cloud infrastructure outage during peak enrolment surge**, with a score of 15.
>
> Let me interpret what management decision follows from this data: rather than treating risk as a passive log, our score of 20 directly dictated our resource allocations. We pre-approved automated checksum hash scripts, established sandbox ETL dry-runs with 10% data sampling, and configured AWS auto-scaling with Redis caching capable of handling 15,000 concurrent sessions—250% of historical peak load.
>
> *(Scroll to Stakeholder Power-Interest Matrix in Section 3)*
>
> Turning to our **Stakeholder Power-Interest Matrix**, we mapped key university groups into four operational quadrants. 
> - In **Manage Closely (High Power, High Interest)**, we positioned our CIO Sponsor, University Registrar, and Central IT Security. They have operational veto authority over production cutover; thus, they receive weekly 1-on-1 executive status briefings and fortnightly steering governance.
> - In **Keep Satisfied (High Power, Low Interest)**, we placed the Academic Senate and Faculty Deans. While they do not manage daily IT work, faculty resistance could derail adoption. We provide them monthly executive digests and early interface demonstrations.
> - In **Keep Informed (Low Power, High Interest)**, we placed our 28,000 students and helpdesk staff, who receive bi-weekly updates and beta-testing clinics.
>
> Notice how our stakeholder matrix connects directly to our communication plan: power and interest dictate information frequency and channel.
>
> I now invite Rejvi Jaman to present our quality metrics, change control, project tracking, and final integrated recommendation."

---

## SPEAKER 3: MD Rejvi Jaman Mafti (Student ID: 241964)
**Duration:** 9:00 – 13:30  
**Screens to Display:** Live Website Section 4 (Quality & Change CR-01) -> Section 5 (Trello & EVM Dashboard) -> Section 6 (Integration & Recommendation)

### Verbatim Presentation Script:
> "Thank you, Momen. Respected lecturer, I will now demonstrate our quality assurance frameworks, change control evidence, Trello sprint tracking, EVM dashboard, and our final management recommendation.
>
> *(Navigate to Section 4: Quality & Change Control)*
>
> In Section 4, project quality is governed by empirical, measurable criteria rather than vague aspirations. We established six binding metrics: 99.95% system uptime monitored 24/7 by AWS Synthetics; page response times under 1.8 seconds at 12,000 concurrent users; 100% data fidelity migrating 28,000 student records verified by automated SHA-256 hash checks; and zero open Severity-1 or Severity-2 defects at UAT sign-off.
>
> We also maintained strict governance through our **Change Control Log**. On 14 April, the University Cybersecurity Board submitted **Change Request CR-01: Mandatory Multi-Factor Authentication (MFA) Integration** to comply with updated Australian Cyber Security Centre guidelines. 
>
> As documented in our change analysis, CR-01 added 8 days of development effort and $14,500 AUD in costs. However, because our Project Manager fast-tracked UI testing in parallel with Sprint 2, the schedule delay was completely absorbed, protecting our 17 July go-live date. Furthermore, the $14,500 was funded entirely from our pre-planned $38,500 Contingency Reserve. The Change Control Board formally approved CR-01, demonstrating that controlled flexibility does not compromise project baselines.
>
> *(Navigate to Section 5: Tracking & EVM Dashboard)*
>
> Now, let us inspect our operational tracking in **Trello** and **Excel**.
>
> In Trello, our Kanban board mirrors our WBS. Cards move systematically across five columns: Backlog, Sprint To-Do, In Progress, Review/QA, and Done. Every single card carries its corresponding WBS code and checklist.
>
> *(Focus on EVM Dashboard KPI cards in Section 5)*
>
> To quantify project health, we conducted a rigorous **Earned Value Management (EVM)** review at Week 14. Here is our performance evidence:
> - Our **Planned Value (PV)** was $225,000.
> - Our **Earned Value (EV)** achieved was $198,000.
> - Our **Actual Cost (AC)** incurred was $210,000.
>
> Let me interpret these critical metrics:
> Our **Schedule Performance Index (SPI)** was **0.880**, and our **Cost Performance Index (CPI)** was **0.943**. This revealed that at Week 14, our project was running **10 working days behind schedule** with an unfavourable schedule variance of -$27,000. 
>
> What was the root cause? The legacy Ellucian Banner database contained unindexed tables and corrupt address strings that crashed our automated ETL migration scripts on Critical Path task 3.2.
>
> What management decision followed from this evidence? Rather than hoping the project would magically recover, we took immediate decisive action:
> 1. We executed **Schedule Crashing** by drawing $6,800 from our Contingency Reserve to contract an external Senior ETL Data Engineer for two weeks.
> 2. We executed **Fast-Tracking** by decoupling Sprint 3 course enrolment frontend development, building UI screens against simulated mock data while the backend ETL scripts were resolved.
>
> This data-driven intervention recovered 7 of the 10 lost days by Week 16, restoring our SPI to 0.96 and keeping our critical path protected.
>
> *(Navigate to Section 6: Integration & Final Recommendation)*
>
> Finally, in Section 6, our artefacts demonstrate complete end-to-end integration: the business problem defined the charter scope; the WBS structured the schedule and cost baseline; the risk register justified our contingency reserve; and EVM tracking triggered the exact corrective interventions needed to safeguard delivery.
>
> With all six milestone quality gates signed off, 100% data integrity verified, and zero open critical defects, our team's final management recommendation to the University Steering Committee is to **AUTHORIZE FINAL PRODUCTION CUTOVER (GO-LIVE)** for Semester 1.
>
> Thank you for your time. Tanvir, Momen, and I are now ready to answer your questions and proceed to the individual viva."
