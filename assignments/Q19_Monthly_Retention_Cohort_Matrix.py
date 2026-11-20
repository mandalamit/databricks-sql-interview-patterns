# Databricks notebook source
# MAGIC %md
# MAGIC # Q19: Monthly Customer Retention Cohort Matrix
# MAGIC
# MAGIC - **Pattern:** Pattern 7: Cohort Analysis, Retention & Churn
# MAGIC - **Difficulty:** Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Assign each customer in `orders_raw` (completed) to their **acquisition cohort month** (month of first order). Calculate how many customers returned in Month 0, Month 1, Month 2, and Month 3.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT customer_id, order_date FROM orders_raw WHERE status='COMPLETED' ORDER BY customer_id, order_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q19_Monthly_Retention_Cohort_Matrix_Solution.py`.
