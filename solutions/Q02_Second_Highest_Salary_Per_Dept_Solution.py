# Databricks notebook source
# MAGIC %md
# MAGIC # Q02 Solution: Second Highest Salary per Department (Edge Cases)
# MAGIC
# MAGIC - **Pattern:** Pattern 1: Ranking & Top-N
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Return every department from `employees` along with its **2nd highest distinct salary**. If a department has only one distinct salary (like `Legal`), return `NULL` instead of dropping the department.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC
# MAGIC WITH ranked AS (
# MAGIC   SELECT dept_name, salary,
# MAGIC          DENSE_RANK() OVER (PARTITION BY dept_name ORDER BY salary DESC) AS rnk
# MAGIC   FROM employees
# MAGIC )
# MAGIC SELECT d.dept_name,
# MAGIC        MAX(CASE WHEN r.rnk = 2 THEN r.salary END) AS second_highest_salary
# MAGIC FROM (SELECT DISTINCT dept_name FROM employees) d
# MAGIC LEFT JOIN ranked r ON d.dept_name = r.dept_name
# MAGIC GROUP BY d.dept_name
# MAGIC ORDER BY d.dept_name;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Interviewers love testing the single-row department edge case (`Legal`). Using `LEFT JOIN` or conditional `MAX(CASE WHEN rnk = 2 THEN salary END)` ensures no department is lost.
