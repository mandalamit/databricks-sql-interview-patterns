# Databricks notebook source
# MAGIC %md
# MAGIC # Q04: Cumulative Revenue & Month-over-Month (MoM) Growth %
# MAGIC
# MAGIC - **Pattern:** Pattern 2: Running Totals & Window Frames
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Using `orders_raw` (deduplicated, `status = 'COMPLETED'`, non-null amounts), compute **monthly total revenue**, **running cumulative revenue**, and **MoM percentage growth**.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT * FROM orders_raw LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q04_Cumulative_Revenue_and_MoM_Growth_Solution.py`.
