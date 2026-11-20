# Databricks notebook source
# MAGIC %md
# MAGIC # Q26: Employee-Manager Org Chart & Reporting Path (WITH RECURSIVE)
# MAGIC
# MAGIC - **Pattern:** Pattern 10: Hierarchical & Graph Queries
# MAGIC - **Difficulty:** Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Using `employees`, write a **recursive CTE** to generate the full org hierarchy starting from the CEO (`manager_id IS NULL`), showing `level` and full `reporting_path` (e.g., `Aarav -> Meera -> Priya`).
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT emp_id, emp_name, manager_id FROM employees;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q26_Recursive_Org_Hierarchy_Solution.py`.
