# Databricks notebook source
# MAGIC %md
# MAGIC # Q06 Solution: Pareto Analysis (80/20 Rule) by Product
# MAGIC
# MAGIC - **Pattern:** Pattern 2: Running Totals & Window Frames
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Identify the **top products** in `orders_raw` (completed, deduplicated) whose cumulative revenue accounts for the **first 80% of total revenue**.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC WITH prod_rev AS (
# MAGIC   SELECT product_name, ROUND(SUM(amount), 2) AS product_rev
# MAGIC   FROM (
# MAGIC     SELECT * FROM orders_raw
# MAGIC     WHERE status = 'COMPLETED' AND amount IS NOT NULL
# MAGIC     QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1
# MAGIC   )
# MAGIC   GROUP BY product_name
# MAGIC ),
# MAGIC running AS (
# MAGIC   SELECT product_name,
# MAGIC          product_rev,
# MAGIC          SUM(product_rev) OVER (ORDER BY product_rev DESC) AS cum_rev,
# MAGIC          SUM(product_rev) OVER () AS total_rev
# MAGIC   FROM prod_rev
# MAGIC )
# MAGIC SELECT product_name,
# MAGIC        product_rev,
# MAGIC        ROUND(cum_rev * 100.0 / total_rev, 2) AS cum_pct
# MAGIC FROM running
# MAGIC WHERE (cum_rev - product_rev) / total_rev < 0.80
# MAGIC ORDER BY product_rev DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Notice `(cum_rev - product_rev) / total_rev < 0.80`: this includes the boundary product that pushes the cumulative share *over* 80%.
