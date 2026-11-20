# Databricks notebook source
# MAGIC %md
# MAGIC # Q24: Higher-Order Functions Without Exploding (TRANSFORM & FILTER)
# MAGIC
# MAGIC - **Pattern:** Pattern 9: Semi-Structured Data (Databricks Specialty)
# MAGIC - **Difficulty:** Medium-Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Using `nested_orders` **without using `EXPLODE`**, compute:
# MAGIC 1. `order_total` using `AGGREGATE()`
# MAGIC 2. `high_value_skus` (items with `unit_price >= 100`) using `FILTER()` and `TRANSFORM()`.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT order_id, items FROM nested_orders;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q24_Higher_Order_Array_Functions_Solution.py`.
