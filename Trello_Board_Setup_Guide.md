# Trello Board Setup & WBS-to-Kanban Linkage Guide
**Author / Responsible Lead:** MD Rejvi Jaman Mafti (Student ID: 241964)  
**Tool Required:** Trello (Free Tier — https://trello.com)  
**Deliverable:** Public Viewable Board Link + Labelled Screenshots for PDF Evidence Pack  

---

## 1. Board Configuration Overview
To demonstrate genuine Agile-Kanban workflow tracking, your Trello board must reflect your active sprint execution (specifically capturing the mid-project Week 14 status).

- **Board Name:** `BISY2004 — OmniPortal Consolidation Project (Group XX)`
- **Board Visibility:** Change from *Private* to **Public** (or *Workspace with shareable link*) so your lecturer can view it without requiring login permissions.

### Standard 5 Columns (Workflow Stages):
1. 📥 **Project Backlog (Upcoming WBS Tasks)**
2. 📋 **Sprint Backlog / To Do (Current Sprint 3 & 4)**
3. ⚙️ **In Progress (Active Work)**
4. 🔍 **Review & QA / Testing**
5. ✅ **Done (Completed WBS Deliverables)**

---

## 2. Card Breakdown & Exact WBS Linkage
Create cards using the exact task names and WBS IDs from your WBS and ProjectLibre schedule:

### Column 1: ✅ Done (Completed WBS Deliverables)
1. **[WBS 1.1] Project Charter & Stakeholder Approval**
   - *Member:* Tanvir Ahmed
   - *Due Date:* 06-Feb-2026
   - *Checklist:* [x] Executive sponsor sign-off, [x] Governance committee review
   - *Label:* Green (Completed)
2. **[WBS 1.2] Project Management Plan & Risk Framework**
   - *Member:* Momen Ahmed
   - *Due Date:* 13-Feb-2026
   - *Checklist:* [x] Baseline PMP created, [x] 5x5 scoring matrix approved
   - *Label:* Green (Completed)
3. **[WBS 1.4] MILESTONE 1: Project Charter Signed Off**
   - *Member:* Tanvir Ahmed, Sponsor
   - *Due Date:* 20-Feb-2026
   - *Label:* Purple (Milestone Gate)
4. **[WBS 2.1] Stakeholder Requirements Gathering**
   - *Member:* Tanvir Ahmed
   - *Due Date:* 04-Mar-2026
   - *Checklist:* [x] Student focus groups, [x] Registrar interviews, [x] User stories
   - *Label:* Green (Completed)
5. **[WBS 2.3] Technical Architecture & AWS Cloud Spec**
   - *Member:* Tanvir Ahmed
   - *Due Date:* 18-Mar-2026
   - *Checklist:* [x] AWS multi-AZ diagram, [x] Microservice boundaries
   - *Label:* Green (Completed)
6. **[WBS 2.5] MILESTONE 2: Architecture & Specs Approved**
   - *Member:* Solutions Architect, PM
   - *Due Date:* 20-Mar-2026
   - *Label:* Purple (Milestone Gate)
7. **[WBS 3.1] Legacy Data Profiling & Cleansing**
   - *Member:* Momen Ahmed
   - *Due Date:* 08-Apr-2026
   - *Checklist:* [x] 28,000 student records sampled, [x] Address anomalies flagged
   - *Label:* Green (Completed)
8. **[WBS 4.1] Sprint 1: SSO & Unified Authentication**
   - *Member:* Tanvir Ahmed, Lead Dev
   - *Due Date:* 22-Apr-2026
   - *Checklist:* [x] Okta SAML hook, [x] Azure AD sync
   - *Label:* Green (Completed)

### Column 2: ⚙️ In Progress (Active at Week 14 Review)
9. **[WBS 3.2] Data Mapping & Automated ETL Scripts Dev** *(Critical Path)*
   - *Member:* Momen Ahmed, External ETL Contractor
   - *Due Date:* 08-May-2026 (Extended by 3 days)
   - *Checklist:* [x] Course enrolment schema map, [ ] Historical marks transform, [ ] Checksum validation
   - *Label:* Red (Critical Path) + Orange (Delayed - Fast Tracking)
   - *Card Description:* "Variance flagged: 14 unindexed tables in Banner causing timeout. External contractor onboarded to crash schedule."
10. **[WBS 4.3] Sprint 3: Course Enrolment & Cart Flow**
   - *Member:* MD Rejvi Jaman Mafti, Senior Dev
   - *Due Date:* 15-May-2026
   - *Checklist:* [x] Frontend UI mockups complete, [x] Cart state management, [ ] API endpoint binding
   - *Label:* Blue (Development)

### Column 3: 🔍 Review & QA / Testing
11. **[CR-01] MFA Microservice & Push Notification Hook**
   - *Member:* MD Rejvi Jaman Mafti, Security Officer
   - *Due Date:* 01-May-2026
   - *Checklist:* [x] Twilio API hooked, [x] Authenticator TOTP tested, [ ] Security code review sign-off
   - *Label:* Yellow (Under Review) + Orange (Change Request CR-01)
12. **[WBS 4.2] Sprint 2: Academic Records & Timetable Hub**
   - *Member:* MD Rejvi Jaman Mafti
   - *Due Date:* 29-Apr-2026
   - *Checklist:* [x] Timetable visual grid, [x] PDF export generator, [ ] Cross-browser check
   - *Label:* Yellow (Under Review)

### Column 4: 📋 Sprint Backlog / To Do (Upcoming Sprint 4 & 5)
13. **[WBS 4.4] Sprint 4: Financial Payment Gateway Integration** *(Critical Path)*
   - *Member:* Momen Ahmed, Fintech Specialist
   - *Due Date:* 29-May-2026
   - *Checklist:* [ ] Stripe/NAB sandbox escrow, [ ] Webhook retry queue, [ ] PCI-DSS tokenization
   - *Label:* Red (Critical Path)
14. **[WBS 4.5] Sprint 5: Mobile UI Optimization & Accessibility**
   - *Member:* MD Rejvi Jaman Mafti
   - *Due Date:* 05-Jun-2026
   - *Checklist:* [ ] WCAG 2.1 AA screen reader audit, [ ] Mobile viewport CSS
   - *Label:* Blue (Development)

### Column 5: 📥 Project Backlog (Testing, Deployment & Closure)
15. **[WBS 5.1] Functional, Performance & Load Testing**
16. **[WBS 5.2] Independent Penetration Testing (CREST)**
17. **[WBS 5.3] User Acceptance Testing (UAT) with 50 Pilot Students**
18. **[WBS 6.1] Student Video Guides & Helpdesk Knowledgebase**
19. **[WBS 6.3] Blue-Green Production Cutover & DNS Switch**
20. **[WBS 6.5] MILESTONE 6: Final Project Closure**

---

## 3. How to Export Trello Evidence for the PDF Evidence Pack
1. In Trello, navigate to your board.
2. Click **Show Menu** (top right) > **More** > **Print and Export** > **Export as JSON** (preserves raw data).
3. Take 2 to 3 full-screen screenshots:
   - Full Board View showing all 5 columns and card distributions.
   - Detailed Card View of **[WBS 3.2]** showing the checklist, labels, and description detailing the Week 14 variance and contractor onboarding.
   - Detailed Card View of **[CR-01]** showing the Change Request tag and QA checklist.

---

## 4. Key Talking Points for MD Rejvi Jaman Mafti (Viva Defense)
- **Q: How does this Trello board relate to your WBS and ProjectLibre schedule?**
  - *Answer:* "Every single card on our Trello board carries the exact WBS number (e.g., [WBS 3.2] or [WBS 4.3]) from our WBS and schedule. While ProjectLibre manages the macro-level predictive critical path, timeline, and dependencies, Trello acts as our micro-level Agile execution engine. We track daily task progression from Backlog to In Progress to Review/QA to Done."
- **Q: How did Trello help you identify or manage the Week 14 variance?**
  - *Answer:* "During our daily stand-up, card [WBS 3.2] stalled in the 'In Progress' column for over 8 days due to foreign-key schema errors in the legacy database. Because we monitor WIP (Work in Progress) limits, the blockage was immediately transparent. We updated the card description, escalated to the Project Manager, and attached the external contractor to the card to crash the activity and pull it into QA."
