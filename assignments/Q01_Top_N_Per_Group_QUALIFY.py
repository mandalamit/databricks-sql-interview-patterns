# Databricks notebook source
# MAGIC %md
# MAGIC # Q01: Top 3 Highest-Paid Employees per Department
# MAGIC
# MAGIC - **Pattern:** Pattern 1: Ranking & Top-N
# MAGIC - **Difficulty:** Easy-Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Find the **top 3 highest salaries** in each department from `employees`. If two employees tie for the same salary, include both (do not skip ranks).
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT * FROM employees LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q01_Top_N_Per_Group_QUALIFY_Solution.py`.
