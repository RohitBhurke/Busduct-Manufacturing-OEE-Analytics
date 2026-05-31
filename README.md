# Busduct-Manufacturing-OEE-Analytics
An interactive Power BI MIS dashboard optimizing Overall Equipment Effectiveness (OEE) and root-cause downtime analysis for an electrical busduct plant
<video src="dashboard_vedio.mp4" width="100%" controls></video>

## 📌 Project Overview
This project delivers an interactive management information system (MIS) dashboard tailored for an electrical busduct manufacturing plant. Utilizing **Power BI**, **Python**, and **DAX**, this analytics tool tracks 90 days of factory floor operations to analyze **Overall Equipment Effectiveness (OEE)** and pinpoint structural bottlenecks across the plant's production lines.

---

## 🛠️ The Tech Stack & Architecture
1. **Data Engineering (Python):** Developed a custom discrete-event simulation script utilizing `Pandas` to programmatically generate 1,000+ rows of transactional manufacturing records containing hidden baseline variances.
2. **Data Modeling (Power Query/M Code):** Implemented an automated local folder pipeline streaming multi-sheet data. Engineered a Many-to-Many composite routing bridge (`Date_Shift_Key`) using **Both** cross-filtering direction rules.
3. **Analytical Calculations (DAX):** Formulated enterprise-grade global operational KPIs for *Availability*, *Performance*, and *Quality First-Pass Yield*.
4. **UI/UX Optimization:** Constructed a high-contrast dark-themed visual framework integrated with **Field Value Conditional Formatting Alerts** to dynamically highlight compliance failure zones.

---

## 💡 Key Business Insights (The Root Cause)
By leveraging diagnostic cross-filtering and analytical deep-dives across the data model, the following core plant floor constraints were uncovered:
* **The Shift B Breakdown:** While Shift A and Shift C maintained stable OEE scores averaging above **80%**, **Shift B experienced a critical drop down to ~60%**, severely bottlenecking total factory throughput.
* **The Core Bottleneck:** Cross-filtering Shift B revealed that **Insulation Thickness Defects** on the **Insulation Coating Line** accounted for the vast majority of total unplanned stoppage minutes.
* **Product Line Vulnerability:** The operational failure is heavily concentrated in the fabrication of **Feeder Busducts**, driving up scrap rates significantly beyond the safe factory threshold of 5%.

---

## 🚀 Actionable Engineering Recommendations
Based on the visual diagnostic findings, the following mitigation strategy was submitted to plant management:
1. **Align Maintenance Windows:** Re-schedule preventive tooling calibrations to occur right during the Shift B changeover buffer window to minimize active run-time disruption.
2. **Targeted Operator Training:** Deploy technical training resources explicitly to the Shift B evening crew handling insulation coatings to reduce material structural defects.
