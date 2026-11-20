# Databricks notebook source
# MAGIC %md
# MAGIC # Q02: Second Highest Salary per Department (Edge Cases)
# MAGIC
# MAGIC - **Pattern:** Pattern 1: Ranking & Top-N
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Return every department from `employees` along with its **2nd highest distinct salary**. If a department has only one distinct salary (like `Legal`), return `NULL` instead of dropping the department.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT * FROM employees ORDER BY dept_name, salary DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q02_Second_Highest_Salary_Per_Dept_Solution.py`.
