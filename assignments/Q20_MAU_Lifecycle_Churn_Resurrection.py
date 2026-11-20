# Databricks notebook source
# MAGIC %md
# MAGIC # Q20: MAU Lifecycle Classification (New, Retained, Resurrected)
# MAGIC
# MAGIC - **Pattern:** Pattern 7: Cohort Analysis, Retention & Churn
# MAGIC - **Difficulty:** Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC For each customer's active month in `orders_raw` (completed), classify them as:
# MAGIC - `'NEW'` (first ever month)
# MAGIC - `'RETAINED'` (active in the immediately preceding month)
# MAGIC - `'RESURRECTED'` (previously active, skipped >=1 month, then returned).
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT DISTINCT customer_id, DATE_TRUNC('MONTH', order_date) AS m FROM orders_raw WHERE status='COMPLETED' ORDER BY 1, 2;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q20_MAU_Lifecycle_Churn_Resurrection_Solution.py`.
