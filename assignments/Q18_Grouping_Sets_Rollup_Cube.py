# Databricks notebook source
# MAGIC %md
# MAGIC # Q18: Multi-Dimensional Sales Subtotals (ROLLUP / GROUPING SETS)
# MAGIC
# MAGIC - **Pattern:** Pattern 6: Pivoting, Funnels & Cubes
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Produce a single query over `orders_raw` (completed, deduplicated) returning revenue by `(region, product_name)`, regional subtotals, and the grand total, labeling subtotal rows as `'ALL'`.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT region, product_name, amount FROM orders_raw LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q18_Grouping_Sets_Rollup_Cube_Solution.py`.
