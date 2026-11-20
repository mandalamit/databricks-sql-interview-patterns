# Databricks notebook source
# MAGIC %md
# MAGIC # Q25: Parsing Raw JSON Event Payloads
# MAGIC
# MAGIC - **Pattern:** Pattern 9: Semi-Structured Data (Databricks Specialty)
# MAGIC - **Difficulty:** Easy-Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC From `nested_orders.raw_json`, extract `source`, `coupon_code`, `discount` (as INT, default 0), and `device_os` using Databricks SQL's native JSON path operator `:`.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT order_id, raw_json FROM nested_orders;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q25_Parsing_Raw_JSON_Payloads_Solution.py`.
