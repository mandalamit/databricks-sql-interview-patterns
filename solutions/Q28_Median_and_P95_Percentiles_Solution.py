# Databricks notebook source
# MAGIC %md
# MAGIC # Q28 Solution: Median & P95 Order Value per Region
# MAGIC
# MAGIC - **Pattern:** Pattern 11: Analytical & Statistical SQL
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Calculate the **average**, **exact median (P50)**, and **95th percentile (P95)** of completed order amounts per region in `orders_raw` (deduplicated).

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC WITH dedup AS (
# MAGIC   SELECT region, amount
# MAGIC   FROM orders_raw
# MAGIC   WHERE status = 'COMPLETED' AND amount IS NOT NULL
# MAGIC   QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1
# MAGIC )
# MAGIC SELECT region,
# MAGIC        ROUND(AVG(amount), 2) AS avg_amount,
# MAGIC        ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY amount), 2) AS median_p50,
# MAGIC        ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY amount), 2) AS p95_amount
# MAGIC FROM dedup
# MAGIC GROUP BY region
# MAGIC ORDER BY region;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC For billion-row tables in Databricks, mention `PERCENTILE_APPROX(amount, 0.95)` — it uses a memory-bounded digest and avoids full sorting.
