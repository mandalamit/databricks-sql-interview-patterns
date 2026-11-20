# Databricks notebook source
# MAGIC %md
# MAGIC # Q05: 7-Day Rolling Average of Daily Revenue
# MAGIC
# MAGIC - **Pattern:** Pattern 2: Running Totals & Window Frames
# MAGIC - **Difficulty:** Medium-Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Calculate the **7-day rolling average** of daily completed revenue from `orders_raw`. Handle missing calendar dates properly using `RANGE BETWEEN` (not just `ROWS BETWEEN 6 PRECEDING`).
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT order_date, SUM(amount) AS daily_rev FROM orders_raw WHERE status='COMPLETED' GROUP BY order_date ORDER BY order_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q05_Rolling_7_Day_Average_Solution.py`.
