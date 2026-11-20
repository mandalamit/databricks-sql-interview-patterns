# Databricks notebook source
# MAGIC %md
# MAGIC # Q16 Solution: Monthly Revenue Pivot Table by Region
# MAGIC
# MAGIC - **Pattern:** Pattern 6: Pivoting, Funnels & Cubes
# MAGIC - **Difficulty:** Easy-Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Build a pivoted report from `orders_raw` (completed, deduplicated) with one row per `order_month` and separate columns for `APAC`, `EMEA`, and `NA` revenue.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC WITH dedup AS (
# MAGIC   SELECT DATE_FORMAT(order_date, 'yyyy-MM') AS order_month, region, amount
# MAGIC   FROM orders_raw
# MAGIC   WHERE status = 'COMPLETED' AND amount IS NOT NULL
# MAGIC   QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1
# MAGIC )
# MAGIC SELECT *
# MAGIC FROM dedup
# MAGIC PIVOT (
# MAGIC   ROUND(SUM(amount), 2)
# MAGIC   FOR region IN ('APAC', 'EMEA', 'NA')
# MAGIC )
# MAGIC ORDER BY order_month;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Also know the ANSI portable equivalent: `SUM(CASE WHEN region = 'APAC' THEN amount ELSE 0 END) AS APAC` or `SUM(amount) FILTER (WHERE region = 'APAC')`.
