# Databricks notebook source
# MAGIC %md
# MAGIC # Q21: Forward-Fill Missing Daily Product Prices
# MAGIC
# MAGIC - **Pattern:** Pattern 8: Data Cleaning & Quality Audits
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC In `product_prices`, some dates have `NULL` prices. Fill each `NULL` with the **most recent non-null price** for that product.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT * FROM product_prices ORDER BY product_id, price_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q21_Forward_Fill_Missing_Prices_Solution.py`.
