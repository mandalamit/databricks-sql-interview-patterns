# Databricks notebook source
# MAGIC %md
# MAGIC # Q30: Capstone: End-to-End Executive Metrics Query
# MAGIC
# MAGIC - **Pattern:** Pattern 12: Databricks DE Case Study
# MAGIC - **Difficulty:** Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Combine multiple patterns in one clean, modular multi-CTE Databricks SQL query:
# MAGIC 1. Deduplicate `orders_raw` (completed, non-null, excluding outliers > 10,000)
# MAGIC 2. Compute each region's monthly revenue & MoM growth %
# MAGIC 3. Rank regions per month and return the **#1 top-performing region each month**.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT * FROM orders_raw LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q30_Capstone_Executive_Metrics_Solution.py`.
