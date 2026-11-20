# Databricks notebook source
# MAGIC %md
# MAGIC # Q28: Median & P95 Order Value per Region
# MAGIC
# MAGIC - **Pattern:** Pattern 11: Analytical & Statistical SQL
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Calculate the **average**, **exact median (P50)**, and **95th percentile (P95)** of completed order amounts per region in `orders_raw` (deduplicated).
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT region, amount FROM orders_raw WHERE status='COMPLETED' AND amount IS NOT NULL;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q28_Median_and_P95_Percentiles_Solution.py`.
