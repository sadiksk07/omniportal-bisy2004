# BISY2004 Assessment 2: Individual Viva Mastery & Defense Pack
**Weighting:** 10 Marks (Individual Assessment)  
**Rubric Focus:**
- *Individual Ownership & Tool Knowledge (4 Marks):* Proves genuine authorship, hands-on tool navigation, and deep comprehension of outputs.
- *Application & Reasoning (4 Marks):* Explains trade-offs, dependencies, risk dynamics, and why decisions were made using empirical evidence.
- *Accuracy & Professional Judgement (2 Marks):* Delivers concise, professional, mathematically sound explanations.

---

## 1. The Universal Viva Answer Structure: "A-E-R-D"
Whenever the lecturer asks a question, structure your answer using the 4-step **AERD Framework**:
1. **A — Answer directly:** Give a concise 1-sentence conclusion immediately.
2. **E — Evidence & Number:** Cite the specific artefact, task code, dollar value, or metric (e.g., "In our ProjectLibre schedule, WBS 3.2...", "In our Excel Risk Register, Risk R01...").
3. **R — Reasoning / Cause:** Explain the underlying project logic (e.g., "Because legacy schemas had unindexed keys...", "Because students have zero contractual power but high operational stake...").
4. **D — Decision / Implication:** State what management action followed (e.g., "Therefore, we crashed the schedule with $6,800 contingency...", "Therefore, we placed them in Keep Informed with bi-weekly updates...").

---

## 2. Tanvir Ahmed (Student ID: 238983) — Viva Question Bank & Model Answers
*Focus Areas: Charter, Scope, WBS, ProjectLibre Schedule, Critical Path, Float, Baseline*

### Q1: "Show me the Critical Path in your ProjectLibre schedule. What happens if an activity on the critical path is delayed by 3 days?"
- **Model Answer:**
  > "In our ProjectLibre schedule, the Critical Path is displayed with **red Gantt bars** across an 86-working-day sequence from Task 1.1 down through Task 6.4. By definition, every task on the critical path has **zero total float** ($Total\ Float = Late\ Finish - Early\ Finish = 0$). 
  > If a critical activity—such as **WBS 3.2: Automated ETL Script Development**—is delayed by 3 days, that delay propagates directly to all successor tasks (Sprint 1, UAT, and Cutover) with zero absorption. As a result, our final project delivery date would slip from **17 July to 22 July 2026**. This would violate our primary charter constraint by colliding with the start of Semester 1 student enrolments, leading to reputational damage and enrolment failure."

### Q2: "What is the difference between Critical Path tasks and tasks with Float in your schedule? Give an example of a non-critical task."
- **Model Answer:**
  > "A critical task has zero float and directly dictates the project completion date. A non-critical task has slack or float, meaning its start can be delayed without affecting the project finish date.
  > In our ProjectLibre schedule, an example of a non-critical task is **WBS 6.1: End-User Guides & Video Walkthroughs**, which has **8 days of Total Float**. Its earliest start is 10 July, but its latest start is 22 July. This float provided crucial flexibility: when our database migration encountered delays in Week 14, we did not have to divert resources from user documentation because we knew that activity had sufficient slack."

### Q3: "How does your diagrams.net WBS connect to your ProjectLibre schedule?"
- **Model Answer:**
  > "Our WBS is the architectural parent of our schedule. We adhered strictly to the **100% Rule**: all 6 level-1 deliverables (1.0 Initiation to 6.0 Closure) and their 28 level-2 work packages in our diagrams.net diagram were transcribed directly into ProjectLibre using the exact same WBS coding hierarchy. 
  > There are no tasks in ProjectLibre that do not originate from the WBS, and no WBS work package is left out of the schedule. The WBS defines *what* deliverables are required; ProjectLibre sequences *when* and *by whom* they are executed."

### Q4: "If the University Sponsor demanded that the project finish 3 weeks earlier, what project artefacts would you modify and what trade-offs would you make?"
- **Model Answer:**
  > "First, I would open the **Scope Statement** and **WBS** to identify scope that could be deferred to a post-launch Phase 2, such as non-essential timetable export widgets. 
  > Second, in **ProjectLibre**, I would analyze **Schedule Crashing** and **Fast-Tracking** options along the Critical Path—specifically running Sprint 3 (Course Enrolment) and Sprint 4 (Payments) in parallel. 
  > Third, I would update the **Cost Baseline in Excel**, because crashing would increase direct developer overtime costs. 
  > Finally, in the **Risk Register**, I would escalate Risk R02 (concurrency bugs) and R08 (testing defects), because compressing the schedule reduces testing duration, requiring additional contingency reserves."

---

## 3. Momen Ahmed (Student ID: 242048) — Viva Question Bank & Model Answers
*Focus Areas: Risk Register, 5×5 Scoring, Heat Map, Stakeholder Matrix, Cost Model, Contingency Reserves*

### Q1: "Explain the reasoning behind the scoring and response strategy for your highest-priority risk."
- **Model Answer:**
  > "Our highest-priority risk is **Risk R01: Legacy database schema mismatch and data corruption during automated ETL execution**. 
  > In our 5×5 scoring model in Excel, we assigned a **Likelihood of 4 (Likely)** and an **Impact of 5 (Severe / Catastrophic)**, yielding an **Extreme Risk Score of 20** ($4 \times 5 = 20$). 
  > The Likelihood is 4 because our legacy Banner SIS contains 15 years of legacy schema modifications and inconsistent data formats. The Impact is 5 because corrupting 28,000 student academic profiles or tuition billing ledgers would breach the Australian Privacy Principles, trigger TEQSA regulatory fines, and halt university operations.
  > Our response strategy is **Mitigation**: we built automated checksum validation algorithms, staged ETL dry-runs in an isolated AWS sandbox using 10% sampling, and established instantaneous database rollback checkpoints."

### Q2: "How did you arrive at your $385,000 Cost Baseline (BAC), and why did you separate Contingency Reserve from Management Reserve?"
- **Model Answer:**
  > "Our Cost Baseline is built from bottom-up resource cost engineering in Excel:
  > - **Direct Labour:** 305 total resource days across our 6 core roles (Project Manager at $95/hr, Architect at $115/hr, Developers at $85/hr, DB Specialist at $95/hr, QA at $80/hr, and Change Lead at $75/hr), totaling **$219,600 AUD**.
  > - **Capital Expenditure (Capex):** Fixed quotes totaling **$90,500 AUD**, including AWS multi-AZ cloud hosting ($28,500), Okta SSO licences ($24,000), and an independent CREST security audit ($16,500).
  > - Adding these gives a **Budget at Completion (BAC) of $385,000 AUD**.
  > We separated reserves based on PMBOK standards:
  > - The **10% Contingency Reserve ($38,500)** is managed directly by the Project Manager to handle *known-unknowns* (e.g., technical ETL errors or interface rework).
  > - The **5% Management Reserve ($19,250)** is held by the Project Sponsor/CIO to handle *unknown-unknowns* or unforeseen strategic shifts. This brought our total budget to $442,750, leaving $7,250 headroom below the $450,000 ceiling."

### Q3: "Why was the University Registrar classified as 'High Power, High Interest' while the Student Body was classified as 'Low Power, High Interest'?"
- **Model Answer:**
  > "In our Stakeholder Matrix:
  > - The **University Registrar (SH02)** is classified as **High Power, High Interest (Manage Closely)** because the Registrar has formal institutional authority and operational veto power over student admissions and academic grading. If student record fidelity is not 100% verified, the Registrar can legitimately refuse to sign off on production cutover.
  > - The **Student Body and SRC (SH04)** are classified as **Low Power, High Interest (Keep Informed)**. As individual end-users, students have extremely high interest—the portal directly dictates their daily course enrolment and grades. However, they lack contractual governance power over technical architecture or project budgets. Therefore, their strategy is 'Keep Informed' through bi-weekly bulletins, FAQs, and a 50-student beta focus group."

### Q4: "How does your Risk Register connect to your Cost Model and Schedule?"
- **Model Answer:**
  > "The Risk Register is directly linked to both:
  > - **Link to Cost:** Risk R01 (data corruption) and Risk R04 (security breach) directly justified our $38,500 Contingency Reserve and our $16,500 investment in third-party penetration testing. When Risk R01 materialized at Week 14, we drew $6,800 from this contingency reserve to hire a senior ETL contractor.
  > - **Link to Schedule:** Risks R01 and R02 are located directly on the Critical Path (Tasks 3.2 and 5.1). Identifying them in the Risk Register led us to insert formal buffer days and schedule load testing at 250% capacity before UAT sign-off."

---

## 4. MD Rejvi Jaman Mafti (Student ID: 241964) — Viva Question Bank & Model Answers
*Focus Areas: Quality Requirements, Change Control CR-01, RACI Matrix, Trello Kanban Linkage, EVM Dashboard, Status Variance*

### Q1: "Walk me through your Week 14 EVM status. What do SPI = 0.880 and CPI = 0.943 tell management, and what was your corrective action?"
- **Model Answer:**
  > "At our Week 14 mid-project checkpoint in Excel:
  > - **Planned Value (PV)** was $225,000.
  > - **Earned Value (EV)** was $198,000.
  > - **Actual Cost (AC)** was $210,000.
  > This generated a **Schedule Variance (SV) of -$27,000** and an **SPI of 0.880** ($198k / 225k$). An SPI of 0.880 indicates that we were progressing at only 88% of our planned rate—translating to **10 working days behind schedule** on critical path task 3.2 (Automated ETL Scripts). Our **CPI of 0.943** indicated an unfavourable cost variance of -$12,000 due to unplanned engineering hours.
  > **Root Cause:** Legacy Banner database tables had 14 unindexed foreign keys causing migration timeouts.
  > **Corrective Management Action:**
  > 1. We executed **Schedule Crashing** by releasing $6,800 from our Contingency Reserve to contract an external Senior ETL Engineer for 2 weeks to optimize the SQL queries.
  > 2. We executed **Fast-Tracking** by decoupling Sprint 3 course enrolment frontend development, building UI screens against simulated mock data in parallel with backend ETL fixes.
  > 3. By Week 16, we recovered 7 of the 10 lost days, bringing our SPI back to 0.96 and securing the critical path."

### Q2: "Show how a specific card on your Trello board connects to your WBS and ProjectLibre schedule."
- **Model Answer:**
  > "Every card on our Trello board carries a direct 1:1 tag matching its WBS code.
  > For example, in our 'In Progress' column, we have the card: **`[WBS 3.2] Data Mapping & Automated ETL Scripts Dev`**.
  > - In our **WBS (draw.io)**, WBS 3.2 is the core technical deliverable under Phase 3.0.
  > - In our **ProjectLibre schedule**, Task ID 14 is WBS 3.2, scheduled for 10 working days on the Critical Path with zero float.
  > - On our **Trello board**, that exact card contains the checklist for schema mappings, assigned to Momen Ahmed and our external contractor, with the orange label flagging the Week 14 delay.
  > This provides complete traceability: the WBS defines the work package, ProjectLibre calculates the timeline dependencies, and Trello manages daily sprint execution."

### Q3: "Explain how you evaluated Change Request CR-01 (MFA Integration). Why was it approved and how did it affect project constraints?"
- **Model Answer:**
  > "On 14 April 2026, the University Cybersecurity Advisory Board submitted **Change Request CR-01: Mandatory MFA and Mobile Push SSO Integration** to comply with updated Australian Cyber Security Centre (ACSC) Essential Eight mandates.
  > Through our formal Change Control Board (CCB), we conducted a four-dimensional impact assessment:
  > 1. **Scope:** Added Twilio SMS microservices, Authenticator app TOTP hooks, and 'Remember Device for 30 Days' cookie logic.
  > 2. **Schedule:** Added +8 working days of development effort. We absorbed this delay without extending the project end date by fast-tracking UI testing in parallel with Sprint 2.
  > 3. **Cost:** Incurred +$14,500 AUD for SMS infrastructure and security specialist effort. This was funded 100% from our pre-existing $38,500 Contingency Reserve, leaving the $385,000 BAC baseline untouched.
  > 4. **Risk:** Drastically reduced our high-priority PII data breach risk (R04) from High to Low.
  > Because it fulfilled federal compliance without slipping the 17 July go-live date or breaching the budget cap, the CCB **APPROVED** CR-01."

### Q4: "How does your RACI Matrix prevent communication breakdowns or conflict during project execution?"
- **Model Answer:**
  > "Our RACI Matrix adheres strictly to the rule of **Single-Point Accountability**. For every one of our 6 main phases, there is exactly **one 'A' (Accountable)**. 
  > For instance, in Phase 4.0 (Core Portal Development), the Project Manager is Accountable (A) for project delivery within time and cost constraints, while the Lead Development Team is Responsible (R) for coding the software. The Solutions Architect is Consulted (C) on architectural integrity, and the Project Sponsor is Informed (I). 
  > This eliminates role confusion: developers know who makes the final architectural call, and management knows exactly who is responsible for daily execution."

---

## 5. Cross-Cutting Viva Questions (Any Student)

### Q: "Why did your group select a Hybrid Agile-Waterfall lifecycle rather than Pure Waterfall or Pure Agile?"
- **Model Answer:**
  > "Pure Waterfall would be too rigid for designing student-facing interfaces, as requirements evolve through user feedback. However, Pure Agile would be inappropriate because our university environment has fixed contractual dates (Semester 1 enrolment cannot move) and strict regulatory compliance requirements (TEQSA and privacy laws). 
  > Therefore, a **Hybrid approach** gave us the best of both worlds: Waterfall provided predictive governance, fixed milestone quality gates, and security compliance, while Agile Scrum allowed two-week iterative sprints for responsive UI wireframing and feature delivery."

### Q: "What evidence proves that your project is ready for final Go-Live?"
- **Model Answer:**
  > "Our recommendation to Go-Live is grounded in empirical evidence across four artefacts:
  > 1. **Quality Sign-off:** Exactly zero open Severity-1 or Severity-2 defects at the conclusion of UAT, with an 84/100 System Usability Scale rating from 50 pilot students.
  > 2. **Security & Compliance:** Independent CREST-certified penetration testing confirmed zero High or Critical vulnerabilities.
  > 3. **Data Integrity:** 100% checksum match across all 28,000 migrated student records with zero data corruption.
  > 4. **Budget & Contingency:** Final projected cost at completion (EAC) is $406,300 AUD, safely below our $450,000 cap with $17,200 in unspent contingency reserves returned to the university."
