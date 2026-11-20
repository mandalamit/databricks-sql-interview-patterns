# Databricks notebook source
# MAGIC %md
# MAGIC # Q06: Pareto Analysis (80/20 Rule) by Product
# MAGIC
# MAGIC - **Pattern:** Pattern 2: Running Totals & Window Frames
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Identify the **top products** in `orders_raw` (completed, deduplicated) whose cumulative revenue accounts for the **first 80% of total revenue**.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT product_name, SUM(amount) AS rev FROM orders_raw WHERE status='COMPLETED' GROUP BY product_name;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q06_Pareto_80_20_Analysis_Solution.py`.
