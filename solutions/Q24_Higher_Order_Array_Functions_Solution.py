# Databricks notebook source
# MAGIC %md
# MAGIC # Q24 Solution: Higher-Order Functions Without Exploding (TRANSFORM & FILTER)
# MAGIC
# MAGIC - **Pattern:** Pattern 9: Semi-Structured Data (Databricks Specialty)
# MAGIC - **Difficulty:** Medium-Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Using `nested_orders` **without using `EXPLODE`**, compute:
# MAGIC 1. `order_total` using `AGGREGATE()`
# MAGIC 2. `high_value_skus` (items with `unit_price >= 100`) using `FILTER()` and `TRANSFORM()`.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC SELECT order_id,
# MAGIC        AGGREGATE(items, CAST(0.0 AS DOUBLE), (acc, x) -> acc + (x.qty * x.unit_price)) AS order_total,
# MAGIC        TRANSFORM(
# MAGIC          FILTER(items, x -> x.unit_price >= 100),
# MAGIC          x -> x.sku
# MAGIC        ) AS high_value_skus
# MAGIC FROM nested_orders
# MAGIC ORDER BY order_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Higher-order functions (`TRANSFORM`, `FILTER`, `AGGREGATE`) are a huge Databricks performance win because they avoid row explosion and expensive re-aggregation shuffles.
