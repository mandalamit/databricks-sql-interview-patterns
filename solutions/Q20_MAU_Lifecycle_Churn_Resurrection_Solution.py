# Databricks notebook source
# MAGIC %md
# MAGIC # Q20 Solution: MAU Lifecycle Classification (New, Retained, Resurrected)
# MAGIC
# MAGIC - **Pattern:** Pattern 7: Cohort Analysis, Retention & Churn
# MAGIC - **Difficulty:** Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC For each customer's active month in `orders_raw` (completed), classify them as:
# MAGIC - `'NEW'` (first ever month)
# MAGIC - `'RETAINED'` (active in the immediately preceding month)
# MAGIC - `'RESURRECTED'` (previously active, skipped >=1 month, then returned).

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC
# MAGIC WITH monthly_active AS (
# MAGIC   SELECT DISTINCT customer_id,
# MAGIC          DATE_TRUNC('MONTH', order_date) AS active_month
# MAGIC   FROM orders_raw
# MAGIC   WHERE status = 'COMPLETED'
# MAGIC ),
# MAGIC with_prev AS (
# MAGIC   SELECT customer_id, active_month,
# MAGIC          LAG(active_month) OVER (PARTITION BY customer_id ORDER BY active_month) AS prev_active_month
# MAGIC   FROM monthly_active
# MAGIC )
# MAGIC SELECT DATE_FORMAT(active_month, 'yyyy-MM') AS month,
# MAGIC        customer_id,
# MAGIC        CASE
# MAGIC          WHEN prev_active_month IS NULL THEN 'NEW'
# MAGIC          WHEN MONTHS_BETWEEN(active_month, prev_active_month) = 1 THEN 'RETAINED'
# MAGIC          ELSE 'RESURRECTED'
# MAGIC        END AS user_state
# MAGIC FROM with_prev
# MAGIC ORDER BY month, customer_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Follow-up question: How would you also count `'CHURNED'` users for month M? Left anti-join month M-1 active users against month M active users.
