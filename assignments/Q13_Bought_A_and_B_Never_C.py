# Databricks notebook source
# MAGIC %md
# MAGIC # Q13: Customers Who Bought Laptop & Mouse, Never Headphones
# MAGIC
# MAGIC - **Pattern:** Pattern 5: Joins, Anti-Joins & Market Basket
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC From `orders_raw` (completed), find all `customer_id`s who purchased **both `'Laptop'` and `'Mouse'`**, but **never purchased `'Headphones'`**.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT DISTINCT customer_id, product_name FROM orders_raw WHERE status='COMPLETED' ORDER BY customer_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q13_Bought_A_and_B_Never_C_Solution.py`.
