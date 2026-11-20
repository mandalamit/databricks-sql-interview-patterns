# Databricks notebook source
# MAGIC %md
# MAGIC # Q29: Customer RFM Segmentation (NTILE)
# MAGIC
# MAGIC - **Pattern:** Pattern 11: Analytical & Statistical SQL
# MAGIC - **Difficulty:** Medium-Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Build a **Recency, Frequency, Monetary (RFM)** table for all completed customers in `orders_raw` (using `'2026-04-15'` as the reference date). Assign 1–4 quartile scores using `NTILE(4)`.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT customer_id, COUNT(*) AS orders, SUM(amount) AS spend FROM orders_raw WHERE status='COMPLETED' GROUP BY customer_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q29_Customer_RFM_Segmentation_Solution.py`.
