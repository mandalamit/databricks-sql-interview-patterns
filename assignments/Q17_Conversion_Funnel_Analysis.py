# Databricks notebook source
# MAGIC %md
# MAGIC # Q17: E-Commerce Conversion Funnel & Drop-off Rates
# MAGIC
# MAGIC - **Pattern:** Pattern 6: Pivoting, Funnels & Cubes
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Using `clickstream_events`, compute unique users at each funnel stage (`visit` -> `add_to_cart` -> `checkout` -> `purchase`) and calculate the conversion rate from `visit`.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT * FROM clickstream_events ORDER BY user_id, event_ts;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q17_Conversion_Funnel_Analysis_Solution.py`.
