# Databricks notebook source
# MAGIC %md
# MAGIC # Q23: Exploding Nested Arrays & Structs (EXPLODE_OUTER)
# MAGIC
# MAGIC - **Pattern:** Pattern 9: Semi-Structured Data (Databricks Specialty)
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC From `nested_orders`, flatten the `items` array so each SKU is on its own row and compute `line_total = qty * unit_price`. Make sure orders with empty arrays (`order_id = 3`) are **still preserved**.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT * FROM nested_orders;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q23_Explode_Nested_Arrays_and_Structs_Solution.py`.
