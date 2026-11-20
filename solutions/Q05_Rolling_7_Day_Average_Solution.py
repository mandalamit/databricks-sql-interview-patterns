# Databricks notebook source
# MAGIC %md
# MAGIC # Q05 Solution: 7-Day Rolling Average of Daily Revenue
# MAGIC
# MAGIC - **Pattern:** Pattern 2: Running Totals & Window Frames
# MAGIC - **Difficulty:** Medium-Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Calculate the **7-day rolling average** of daily completed revenue from `orders_raw`. Handle missing calendar dates properly using `RANGE BETWEEN` (not just `ROWS BETWEEN 6 PRECEDING`).

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC
# MAGIC WITH daily AS (
# MAGIC   SELECT order_date,
# MAGIC          SUM(amount) AS daily_rev
# MAGIC   FROM (
# MAGIC     SELECT * FROM orders_raw
# MAGIC     WHERE status = 'COMPLETED' AND amount IS NOT NULL
# MAGIC     QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1
# MAGIC   )
# MAGIC   GROUP BY order_date
# MAGIC )
# MAGIC SELECT order_date,
# MAGIC        ROUND(daily_rev, 2) AS daily_rev,
# MAGIC        ROUND(
# MAGIC          AVG(daily_rev) OVER (
# MAGIC            ORDER BY CAST(order_date AS TIMESTAMP)
# MAGIC            RANGE BETWEEN INTERVAL 6 DAYS PRECEDING AND CURRENT ROW
# MAGIC          ), 2
# MAGIC        ) AS rolling_7d_avg
# MAGIC FROM daily
# MAGIC ORDER BY order_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Crucial interview distinction: `ROWS BETWEEN 6 PRECEDING` averages the last 7 *rows* (wrong if dates are missing). `RANGE BETWEEN INTERVAL 6 DAYS PRECEDING` averages the true 7-day *calendar window*.
