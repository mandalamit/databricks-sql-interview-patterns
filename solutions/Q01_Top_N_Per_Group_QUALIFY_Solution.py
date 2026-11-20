# Databricks notebook source
# MAGIC %md
# MAGIC # Q01 Solution: Top 3 Highest-Paid Employees per Department
# MAGIC
# MAGIC - **Pattern:** Pattern 1: Ranking & Top-N
# MAGIC - **Difficulty:** Easy-Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Find the **top 3 highest salaries** in each department from `employees`. If two employees tie for the same salary, include both (do not skip ranks).

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC SELECT dept_name, emp_name, salary,
# MAGIC        DENSE_RANK() OVER (PARTITION BY dept_name ORDER BY salary DESC) AS salary_rank
# MAGIC FROM employees
# MAGIC QUALIFY DENSE_RANK() OVER (PARTITION BY dept_name ORDER BY salary DESC) <= 3
# MAGIC ORDER BY dept_name, salary DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Explain the difference between `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`. Highlight Databricks SQL's `QUALIFY` clause, which avoids wrapping window functions in a subquery/CTE.
