# Databricks notebook source
# MAGIC %md
# MAGIC # Q26 Solution: Employee-Manager Org Chart & Reporting Path (WITH RECURSIVE)
# MAGIC
# MAGIC - **Pattern:** Pattern 10: Hierarchical & Graph Queries
# MAGIC - **Difficulty:** Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Using `employees`, write a **recursive CTE** to generate the full org hierarchy starting from the CEO (`manager_id IS NULL`), showing `level` and full `reporting_path` (e.g., `Aarav -> Meera -> Priya`).

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC WITH RECURSIVE org_tree AS (
# MAGIC   SELECT emp_id, emp_name, manager_id, 1 AS level, emp_name AS reporting_path
# MAGIC   FROM employees
# MAGIC   WHERE manager_id IS NULL
# MAGIC 
# MAGIC   UNION ALL
# MAGIC 
# MAGIC   SELECT e.emp_id, e.emp_name, e.manager_id,
# MAGIC          t.level + 1 AS level,
# MAGIC          CONCAT(t.reporting_path, ' -> ', e.emp_name) AS reporting_path
# MAGIC   FROM employees e
# MAGIC   JOIN org_tree t ON e.manager_id = t.emp_id
# MAGIC )
# MAGIC SELECT emp_id, emp_name, level, reporting_path
# MAGIC FROM org_tree
# MAGIC ORDER BY level, reporting_path;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Always mention cycle prevention (e.g., `NOT ARRAY_CONTAINS(visited, e.emp_id)` or max depth guard) when discussing recursive CTEs in interviews.
