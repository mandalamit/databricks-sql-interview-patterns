# Databricks notebook source
# MAGIC %md
# MAGIC # Q11 Solution: Time Between 1st and 2nd Purchase per Customer
# MAGIC
# MAGIC - **Pattern:** Pattern 4: Sessionization & Event Sequencing
# MAGIC - **Difficulty:** Easy-Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC For every customer in `orders_raw` (completed, deduplicated) who has at least 2 orders, compute the **number of days between their 1st and 2nd order**.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC
# MAGIC WITH ranked_orders AS (
# MAGIC   SELECT customer_id, order_date,
# MAGIC          ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date, order_id) AS order_num
# MAGIC   FROM (
# MAGIC     SELECT * FROM orders_raw
# MAGIC     WHERE status = 'COMPLETED'
# MAGIC     QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1
# MAGIC   )
# MAGIC )
# MAGIC SELECT customer_id,
# MAGIC        MAX(CASE WHEN order_num = 1 THEN order_date END) AS first_order_date,
# MAGIC        MAX(CASE WHEN order_num = 2 THEN order_date END) AS second_order_date,
# MAGIC        DATEDIFF(
# MAGIC          MAX(CASE WHEN order_num = 2 THEN order_date END),
# MAGIC          MAX(CASE WHEN order_num = 1 THEN order_date END)
# MAGIC        ) AS days_to_second_order
# MAGIC FROM ranked_orders
# MAGIC WHERE order_num <= 2
# MAGIC GROUP BY customer_id
# MAGIC HAVING COUNT(*) = 2
# MAGIC ORDER BY customer_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Filtering `WHERE order_num <= 2` before grouping minimizes shuffle volume.
