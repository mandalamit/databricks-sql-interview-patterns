# Databricks notebook source
# MAGIC %md
# MAGIC # Q13 Solution: Customers Who Bought Laptop & Mouse, Never Headphones
# MAGIC
# MAGIC - **Pattern:** Pattern 5: Joins, Anti-Joins & Market Basket
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC From `orders_raw` (completed), find all `customer_id`s who purchased **both `'Laptop'` and `'Mouse'`**, but **never purchased `'Headphones'`**.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC SELECT customer_id
# MAGIC FROM orders_raw
# MAGIC WHERE status = 'COMPLETED'
# MAGIC GROUP BY customer_id
# MAGIC HAVING COUNT(DISTINCT CASE WHEN product_name = 'Laptop' THEN 1 END) = 1
# MAGIC    AND COUNT(DISTINCT CASE WHEN product_name = 'Mouse' THEN 1 END) = 1
# MAGIC    AND COUNT(DISTINCT CASE WHEN product_name = 'Headphones' THEN 1 END) = 0
# MAGIC ORDER BY customer_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Single-pass `GROUP BY` + `HAVING` avoids 3 separate table scans/self-joins and runs in one shuffle stage in Spark.
