# Databricks notebook source
# MAGIC %md
# MAGIC # Q19 Solution: Monthly Customer Retention Cohort Matrix
# MAGIC
# MAGIC - **Pattern:** Pattern 7: Cohort Analysis, Retention & Churn
# MAGIC - **Difficulty:** Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Assign each customer in `orders_raw` (completed) to their **acquisition cohort month** (month of first order). Calculate how many customers returned in Month 0, Month 1, Month 2, and Month 3.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC
# MAGIC WITH cust_months AS (
# MAGIC   SELECT DISTINCT customer_id,
# MAGIC          DATE_TRUNC('MONTH', order_date) AS activity_month
# MAGIC   FROM orders_raw
# MAGIC   WHERE status = 'COMPLETED'
# MAGIC ),
# MAGIC cohorts AS (
# MAGIC   SELECT customer_id,
# MAGIC          MIN(activity_month) OVER (PARTITION BY customer_id) AS cohort_month,
# MAGIC          activity_month
# MAGIC   FROM cust_months
# MAGIC ),
# MAGIC indexed AS (
# MAGIC   SELECT cohort_month,
# MAGIC          CAST(MONTHS_BETWEEN(activity_month, cohort_month) AS INT) AS month_number,
# MAGIC          COUNT(DISTINCT customer_id) AS active_users
# MAGIC   FROM cohorts
# MAGIC   GROUP BY 1, 2
# MAGIC )
# MAGIC SELECT DATE_FORMAT(cohort_month, 'yyyy-MM') AS cohort,
# MAGIC        month_number,
# MAGIC        active_users,
# MAGIC        ROUND(active_users * 100.0 / FIRST_VALUE(active_users) OVER (PARTITION BY cohort_month ORDER BY month_number), 2) AS retention_pct
# MAGIC FROM indexed
# MAGIC ORDER BY cohort, month_number;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Cohort retention is a staple for Senior Data Engineer and Analytics Engineer rounds. `MONTHS_BETWEEN` + `FIRST_VALUE` computes retention % cleanly.
