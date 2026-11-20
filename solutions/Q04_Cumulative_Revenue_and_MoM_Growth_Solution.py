# Databricks notebook source
# MAGIC %md
# MAGIC # Q04 Solution: Cumulative Revenue & Month-over-Month (MoM) Growth %
# MAGIC
# MAGIC - **Pattern:** Pattern 2: Running Totals & Window Frames
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Using `orders_raw` (deduplicated, `status = 'COMPLETED'`, non-null amounts), compute **monthly total revenue**, **running cumulative revenue**, and **MoM percentage growth**.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC WITH dedup AS (
# MAGIC   SELECT * FROM orders_raw
# MAGIC   WHERE status = 'COMPLETED' AND amount IS NOT NULL
# MAGIC   QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1
# MAGIC ),
# MAGIC monthly AS (
# MAGIC   SELECT DATE_TRUNC('MONTH', order_date) AS order_month,
# MAGIC          ROUND(SUM(amount), 2) AS monthly_rev
# MAGIC   FROM dedup
# MAGIC   GROUP BY 1
# MAGIC )
# MAGIC SELECT order_month,
# MAGIC        monthly_rev,
# MAGIC        ROUND(SUM(monthly_rev) OVER (ORDER BY order_month), 2) AS cumulative_rev,
# MAGIC        LAG(monthly_rev) OVER (ORDER BY order_month) AS prev_month_rev,
# MAGIC        ROUND(
# MAGIC          (monthly_rev - LAG(monthly_rev) OVER (ORDER BY order_month)) * 100.0
# MAGIC          / NULLIF(LAG(monthly_rev) OVER (ORDER BY order_month), 0), 2
# MAGIC        ) AS mom_growth_pct
# MAGIC FROM monthly
# MAGIC ORDER BY order_month;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Always wrap the denominator in `NULLIF(..., 0)` to prevent division-by-zero errors in production SQL.
