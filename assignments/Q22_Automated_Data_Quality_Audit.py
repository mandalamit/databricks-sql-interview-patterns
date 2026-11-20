# Databricks notebook source
# MAGIC %md
# MAGIC # Q22: Data Quality Audit (Duplicates, Nulls & Outliers)
# MAGIC
# MAGIC - **Pattern:** Pattern 8: Data Cleaning & Quality Audits
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Write a single SQL query against `orders_raw` that flags rows with any of the following issues: `DUPLICATE_ORDER_ID`, `NULL_AMOUNT`, or `AMOUNT_OUTLIER` (amount > mean + 2 * stddev).
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT * FROM orders_raw ORDER BY order_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q22_Automated_Data_Quality_Audit_Solution.py`.
