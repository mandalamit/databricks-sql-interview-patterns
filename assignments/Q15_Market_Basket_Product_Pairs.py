# Databricks notebook source
# MAGIC %md
# MAGIC # Q15: Market Basket Analysis (Products Bought Together)
# MAGIC
# MAGIC - **Pattern:** Pattern 5: Joins, Anti-Joins & Market Basket
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Find pairs of distinct products bought by the **same customer on the same day** in `orders_raw` (completed), along with how many times each pair occurred. Avoid mirror duplicates like `(Laptop, Mouse)` and `(Mouse, Laptop)`.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT customer_id, order_date, product_name FROM orders_raw WHERE status='COMPLETED' ORDER BY customer_id, order_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q15_Market_Basket_Product_Pairs_Solution.py`.
