# ProjectLibre Step-by-Step Execution & Submission Guide
**Author / Responsible Lead:** Tanvir Ahmed (Student ID: 238983)  
**File Created:** `A2_Group_ProjectLibre_import.xml`  
**Target Output File:** `A2_GroupXX_ProjectLibre.pod`  

---

## 1. Overview of the ProjectLibre Deliverable
ProjectLibre Desktop is the mandatory scheduling and Gantt chart tool for BISY2004 Assessment 2.
Your submission requires the native ProjectLibre source file named:
`A2_GroupXX_ProjectLibre.pod` (replace `XX` with your assigned group number, e.g., `A2_Group03_ProjectLibre.pod`).

We have already pre-generated the complete, error-free Microsoft Project XML import file:
`C:\Users\USER\Desktop\web\A2_Group_ProjectLibre_import.xml`.

This file contains all **36 tasks, outline levels (WBS 1.0 to 6.5), durations, dependencies (Finish-to-Start), milestones (0-day duration), and resource assignments**.

---

## 2. Step-by-Step Instructions to Create the .pod File

### Step 1: Open ProjectLibre Desktop
- Launch ProjectLibre Desktop on your computer.
- When the welcome screen appears, click **Open** (or go to `File` > `Open`).

### Step 2: Import the XML File
- In the file browser dialog, change the file type filter in the bottom right corner from `ProjectLibre (*.pod)` to **`Microsoft Project XML (*.xml)`** (or `All Files (*.*)`).
- Navigate to your project folder:
  `C:\Users\USER\Desktop\web\A2_Group_ProjectLibre_import.xml`
- Select the file and click **Open**.
- ProjectLibre will instantly parse the XML and construct the entire 24-week schedule, Gantt bars, dependencies, and WBS outline!

### Step 3: Verify Schedule Parameters
Confirm the following key data points in ProjectLibre:
1. **Start Date:** `02/02/2026` (Monday)
2. **Finish Date:** `17/07/2026` (Friday) — Total Duration: **120 Working Days (24 Weeks)**
3. **Milestones:** Verify that the 6 milestones appear with a `0` duration and display as black diamond symbols on the Gantt chart:
   - `1.4 MILESTONE 1: Project Charter Signed Off`
   - `2.5 MILESTONE 2: Architecture & Specs Approved`
   - `3.5 MILESTONE 3: Migration Scripts & Security Ready`
   - `4.6 MILESTONE 4: Core Development Feature Complete`
   - `5.5 MILESTONE 5: UAT & Security Sign-Off`
   - `6.5 MILESTONE 6: Final Project Closure & Decommissioning`

### Step 4: Display the Critical Path
- Click on the **View** or **Gantt** ribbon tab.
- Look for the **Critical** or **Filter** dropdown:
  - In ProjectLibre, critical activities (tasks with zero total float) are highlighted with **Red Gantt bars**, while non-critical tasks have **Blue Gantt bars**.
- Confirm that the critical path passes through:
  `1.1 -> 1.2 -> 1.3 -> 2.1 -> 2.3 -> 2.4 -> 3.1 -> 3.2 -> 3.3 -> 4.1 -> 4.2 -> 4.3 -> 4.4 -> 5.1 -> 5.2 -> 5.3 -> 5.4 -> 6.3 -> 6.4`
- Note that non-critical tasks (e.g., `2.2 Data Privacy Review`, `3.4 RBAC Setup`, `4.5 Mobile UI Polish`, `6.1 User Guides`, `6.2 Staff Clinics`) show slack / float and appear blue.

### Step 5: Save as Native .pod File
- Go to `File` > `Save As...`.
- Ensure the format is **ProjectLibre (*.pod)**.
- Name the file according to your group number:
  **`A2_GroupXX_ProjectLibre.pod`** (e.g., `A2_Group03_ProjectLibre.pod`).
- Save it into this directory.

---

## 3. Capturing Required Screenshots for the Website and Evidence Pack
You must take 3 to 4 clear, high-resolution screenshots for the website and PDF evidence pack:

1. **Full Gantt Chart Overview:**
   - Zoom out so the full 24-week timeline is visible.
   - Ensure task names, durations, and Gantt bars are clearly legible.
2. **Critical Path View:**
   - Show the Red Gantt bars showing the path through WBS 3.2 (Automated ETL) and WBS 4.4 (Payment Gateway).
3. **Milestones View:**
   - Filter or scroll to capture the diamond milestone markers with their dates.
4. **Resource Usage View:**
   - Go to `View` > `Resources` or `Resource Usage` to show the assigned team roles and rates.

---

## 4. Key Talking Points for Tanvir Ahmed (Viva Defense)
When the lecturer asks you to explain the ProjectLibre schedule during the viva:
- **Q: What is the Critical Path and what does it mean in your project?**
  - *Answer:* "Our critical path is 86 working days within the 120-day project timeline. It connects tasks that have zero total float. If any critical path task—such as WBS 3.2 (Automated ETL Scripts)—is delayed by even 1 day, the entire project completion date slips beyond our 17 July deadline, threatening the Semester 1 student enrolment period."
- **Q: How does this schedule connect to your WBS?**
  - *Answer:* "Every single task in our ProjectLibre schedule shares the exact WBS identifier (from 1.1 to 6.5) established in our diagrams.net WBS. There are no orphan tasks. The 6 summary rows in ProjectLibre match the 6 level-1 WBS deliverables."
- **Q: What float exists in the project?**
  - *Answer:* "Tasks like 6.1 (User Guides) and 6.2 (Staff Onboarding Clinics) have 8 days of total float. This gave us flexibility during the Week 14 ETL bottleneck to reallocate attention to the critical path without delaying the final delivery."
