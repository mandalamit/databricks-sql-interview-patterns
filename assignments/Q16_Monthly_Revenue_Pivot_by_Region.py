# Databricks notebook source
# MAGIC %md
# MAGIC # Q16: Monthly Revenue Pivot Table by Region
# MAGIC
# MAGIC - **Pattern:** Pattern 6: Pivoting, Funnels & Cubes
# MAGIC - **Difficulty:** Easy-Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Build a pivoted report from `orders_raw` (completed, deduplicated) with one row per `order_month` and separate columns for `APAC`, `EMEA`, and `NA` revenue.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT region, SUM(amount) FROM orders_raw WHERE status='COMPLETED' GROUP BY region;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q16_Monthly_Revenue_Pivot_by_Region_Solution.py`.
