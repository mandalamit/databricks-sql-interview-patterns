# Databricks notebook source
# MAGIC %md
# MAGIC # Q22 Solution: Data Quality Audit (Duplicates, Nulls & Outliers)
# MAGIC
# MAGIC - **Pattern:** Pattern 8: Data Cleaning & Quality Audits
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Write a single SQL query against `orders_raw` that flags rows with any of the following issues: `DUPLICATE_ORDER_ID`, `NULL_AMOUNT`, or `AMOUNT_OUTLIER` (amount > mean + 2 * stddev).

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC
# MAGIC WITH stats AS (
# MAGIC   SELECT *,
# MAGIC          COUNT(*) OVER (PARTITION BY order_id) AS id_cnt,
# MAGIC          AVG(amount) OVER () AS mean_amt,
# MAGIC          STDDEV(amount) OVER () AS std_amt
# MAGIC   FROM orders_raw
# MAGIC )
# MAGIC SELECT order_id, customer_id, amount,
# MAGIC        CASE WHEN id_cnt > 1 THEN TRUE ELSE FALSE END AS is_duplicate,
# MAGIC        CASE WHEN amount IS NULL THEN TRUE ELSE FALSE END AS is_null_amount,
# MAGIC        CASE WHEN amount > mean_amt + 2 * std_amt THEN TRUE ELSE FALSE END AS is_outlier
# MAGIC FROM stats
# MAGIC WHERE id_cnt > 1 OR amount IS NULL OR amount > mean_amt + 2 * std_amt
# MAGIC ORDER BY order_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Window functions let you compute global statistics (`AVG() OVER ()`, `STDDEV() OVER ()`) alongside row-level checks in a single scan.
