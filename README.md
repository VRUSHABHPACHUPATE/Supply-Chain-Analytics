# DataCo Supply Chain & Profitability Analytics

## Project Overview
This project transforms a complex, 180,000-row real-world logistics dataset into a dual-view Business Intelligence solution. Designed for enterprise agility, the workflow leverages Python for rapid data engineering, SQL for foundational metric validation, and Tableau for executive-level visual reporting. 

Rather than building a single, cluttered dashboard, this project demonstrates stakeholder awareness by separating insights into two targeted tools: a **Logistics & Fulfillment Dashboard** for supply chain managers and a **Sales & Profitability Dashboard** for finance executives.

## Executive Dashboards

### 1. Logistics & Fulfillment
<img width="1705" height="888" alt="Screenshot 2026-10-27 172029" src="https://github.com/user-attachments/assets/3bbcd0c5-b764-44b1-96d6-d0944f1e71cc" />


### 2. Sales & Profitability 
<img width="1708" height="896" alt="Screenshot 2026-10-27 171949" src="https://github.com/user-attachments/assets/e65bfe48-9e77-406d-a236-a186d53c3b8c" />


## Tech Stack
* **Data Engineering & Cleaning:** Python (Pandas)
* **Metric Validation & Querying:** SQL 
* **Data Visualization & BI:** Tableau

## Core Business Questions Answered
**1. Logistics & Fulfillment**
* *Where are our global logistics networks failing?* (Geospatial mapping of high-volume delay regions).
* *Which shipping modes are driving our highest penalty rates?* (Isolating Standard Class bottlenecks).
* *Are shipping delays impacting our highest-grossing product categories?* (Cross-referencing logistics failure rates against category revenue).

**2. Sales & Profitability**
* *Are excessive discounts cannibalizing our profit margins?* (Scatter plot correlation of average discount rates vs. top-line sales).
* *How is revenue distributed across our core B2B and B2C segments?* (Demographic breakdown of Corporate, Consumer, and Home Office clients).
* *How much potential revenue is lost to canceled or fraudulent orders?* (Pipeline analysis of order status vs. gross sales).

## Workflow & Methodology
1. **Data Preparation (Python):** Ingested the raw Kaggle DataCo dataset, stripped out 35+ irrelevant columns, engineered custom metrics (`is_delayed`, `late_delivery_risk`), and exported a clean CSV.
2. **KPI Validation (SQL):** Authored aggregate queries to validate the integrity of total sales, delivery rates, and high-risk regions.
3. **Dashboard Design (Tableau):** Engineered custom expressions and interactive global filters to create two distinct, responsive executive dashboards.
