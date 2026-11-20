# Databricks notebook source
# MAGIC %md
# MAGIC # Q09: Find Missing Order IDs (Sequence Gaps)
# MAGIC
# MAGIC - **Pattern:** Pattern 3: Gaps & Islands
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Find all **missing `order_id` values** between the minimum and maximum `order_id` in `orders_raw`.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT DISTINCT order_id FROM orders_raw ORDER BY order_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q09_Missing_Sequence_IDs_Solution.py`.
