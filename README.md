# Databricks Data Engineer: SQL Interview Patterns (30 Hands-On Notebooks)

A complete, pattern-based SQL interview preparation repository built specifically for **Databricks Data Engineer** interviews. Every question is a standalone Databricks notebook using **Databricks SQL / Spark SQL**, backed by a single setup notebook that generates all required tables automatically.

## Repository Structure

```text
databricks-sql-interview-patterns/
├── README.md                                   # Complete pattern guide & roadmap
├── Day00_Setup.py                              # Run this FIRST to create all interview tables
├── assignments/                                # 30 ready-to-solve problem notebooks
│   ├── README.md
│   ├── Q01_Top_N_Per_Group_QUALIFY.py
│   ├── ...
│   └── Q30_Capstone_Executive_Metrics.py
└── solutions/                                  # 30 complete SQL solution notebooks with explanations
    ├── README.md
    ├── Q01_Top_N_Per_Group_QUALIFY_Solution.py
    ├── ...
    └── Q30_Capstone_Executive_Metrics_Solution.py
```

## Quick Start (Databricks Community Edition & Enterprise)

1. **Import into Databricks:**
   - **Enterprise / Databricks Repos:** Clone this GitHub repo via **Workspace > Repos > Add Repo**.
   - **Databricks Community Edition:** Download the repo as ZIP, unzip it, and import `Day00_Setup.py` and the `assignments/` notebooks via **Workspace > Import**.
2. **Run `Day00_Setup.py` Once:**
   - Attach to a cluster and click **Run All**.
   - Creates the `sql_interview_prep` database and 9 realistic Delta tables (employees, orders_raw, orders_silver, user_logins, subscriptions, clickstream_events, product_prices, nested_orders, warehouse_routes).
3. **Solve by Pattern:**
   - Open `assignments/QXX_*.py`, read the problem statement, schema, and expected output, and write your SQL in the `# TODO` cell.
   - Compare your approach and edge-case handling against `solutions/QXX_*_Solution.py`.

---

## All 12 Interview Patterns & 30 Questions

### Pattern 1: Ranking, Top-N & Deduplication
- **Q01:** Top 3 Highest-Paid Employees per Department (`DENSE_RANK` + `QUALIFY`)
- **Q02:** Second Highest Salary per Department (Handling Ties & Missing 2nd Rank)
- **Q03:** Deduplicate CDC Records Keeping Latest Event (`ROW_NUMBER` + `QUALIFY`)

### Pattern 2: Running Totals, Moving Averages & Window Frames
- **Q04:** Cumulative Revenue & Month-over-Month (MoM) Growth % (`LAG` + `SUM OVER`)
- **Q05:** 7-Day Rolling Average of Daily Revenue (`RANGE BETWEEN` vs `ROWS BETWEEN`)
- **Q06:** Pareto Analysis (80/20 Rule) — Products Contributing to 80% of Revenue

### Pattern 3: Gaps & Islands (Consecutive Streaks & Ranges)
- **Q07:** Consecutive Login Streaks (Users Active 3+ Consecutive Days)
- **Q08:** Merge Overlapping Subscription Date Intervals
- **Q09:** Detect Missing Order IDs / Sequence Gaps (`SEQUENCE` / `LEAD`)

### Pattern 4: Sessionization & Event Sequencing
- **Q10:** Clickstream Sessionization (30-Minute Inactivity Timeout)
- **Q11:** Days Between First and Second Purchase per Customer
- **Q12:** Price Drop & Anomaly Detection (Compare Current vs. Previous & Next Row)

### Pattern 5: Joins, Anti-Joins & Market Basket
- **Q13:** Customers Who Bought Product A and B, Never C (`HAVING` + Conditional Count)
- **Q14:** Bronze vs. Silver Data Reconciliation (`FULL OUTER JOIN` & `LEFT ANTI JOIN`)
- **Q15:** Market Basket Analysis — Product Pairs Frequently Bought Together (Self-Join)

### Pattern 6: Pivoting, Funnels & Multi-Dimensional Aggregation
- **Q16:** Monthly Revenue Pivot by Region (`PIVOT` & Conditional Aggregation)
- **Q17:** E-Commerce Conversion Funnel & Step-to-Step Drop-off Rates
- **Q18:** Multi-Dimensional Sales Subtotals (`GROUPING SETS`, `ROLLUP`, `CUBE`)

### Pattern 7: Cohort Analysis, Retention & Churn
- **Q19:** Monthly Customer Retention Cohort Matrix (Month 0, 1, 2 %)
- **Q20:** Monthly Active User (MAU) Lifecycle Classification (New, Retained, Resurrected, Churned)

### Pattern 8: Data Cleaning, Null Handling & Quality Audits
- **Q21:** Forward-Fill Missing Daily Product Prices (`LAST_VALUE(..., TRUE)`)
- **Q22:** Automated Data Quality Audit (Duplicates, Nulls, and Z-Score Outliers)

### Pattern 9: Semi-Structured Data (Databricks / Spark SQL Specialty)
- **Q23:** Exploding Nested Arrays & Structs (`EXPLODE_OUTER`, `LATERAL VIEW`)
- **Q24:** Higher-Order Array Functions Without Exploding (`TRANSFORM`, `FILTER`, `AGGREGATE`)
- **Q25:** Parsing Raw JSON Payloads (`:`, `from_json`, `get_json_object`)

### Pattern 10: Hierarchical & Graph Queries (Recursive CTEs)
- **Q26:** Employee-Manager Org Chart & Reporting Path (`WITH RECURSIVE`)
- **Q27:** Multi-Hop Warehouse Logistics Routing & Total Cost (`WITH RECURSIVE`)

### Pattern 11: Analytical & Statistical SQL
- **Q28:** Median & P95 Order Amount per Region (`PERCENTILE_CONT`, `PERCENTILE_APPROX`)
- **Q29:** Customer RFM Segmentation (`NTILE(4)`)

### Pattern 12: End-to-End Databricks DE Case Study
- **Q30:** Executive E-Commerce Metrics Pipeline (Dedup + Sessionization + MoM Growth + Top-N)
