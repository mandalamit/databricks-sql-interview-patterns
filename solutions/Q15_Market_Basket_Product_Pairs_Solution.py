# Databricks notebook source
# MAGIC %md
# MAGIC # Q15 Solution: Market Basket Analysis (Products Bought Together)
# MAGIC
# MAGIC - **Pattern:** Pattern 5: Joins, Anti-Joins & Market Basket
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Find pairs of distinct products bought by the **same customer on the same day** in `orders_raw` (completed), along with how many times each pair occurred. Avoid mirror duplicates like `(Laptop, Mouse)` and `(Mouse, Laptop)`.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC WITH basket AS (
# MAGIC   SELECT DISTINCT customer_id, order_date, product_name
# MAGIC   FROM orders_raw
# MAGIC   WHERE status = 'COMPLETED'
# MAGIC )
# MAGIC SELECT a.product_name AS product_1,
# MAGIC        b.product_name AS product_2,
# MAGIC        COUNT(*) AS co_occurrence_count
# MAGIC FROM basket a
# MAGIC JOIN basket b
# MAGIC   ON a.customer_id = b.customer_id
# MAGIC  AND a.order_date = b.order_date
# MAGIC  AND a.product_name < b.product_name
# MAGIC GROUP BY a.product_name, b.product_name
# MAGIC ORDER BY co_occurrence_count DESC, product_1, product_2;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC The `a.product_name < b.product_name` join condition eliminates both self-pairs `(A, A)` and mirror duplicates `(B, A)`.
