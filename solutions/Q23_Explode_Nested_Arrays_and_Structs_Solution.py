# Databricks notebook source
# MAGIC %md
# MAGIC # Q23 Solution: Exploding Nested Arrays & Structs (EXPLODE_OUTER)
# MAGIC
# MAGIC - **Pattern:** Pattern 9: Semi-Structured Data (Databricks Specialty)
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC From `nested_orders`, flatten the `items` array so each SKU is on its own row and compute `line_total = qty * unit_price`. Make sure orders with empty arrays (`order_id = 3`) are **still preserved**.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC
# MAGIC SELECT order_id,
# MAGIC        customer_id,
# MAGIC        item.sku,
# MAGIC        item.qty,
# MAGIC        item.unit_price,
# MAGIC        COALESCE(item.qty * item.unit_price, 0.0) AS line_total
# MAGIC FROM nested_orders
# MAGIC LATERAL VIEW EXPLODE_OUTER(items) AS item
# MAGIC ORDER BY order_id, item.sku;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Interview trap: `EXPLODE()` drops rows with empty or NULL arrays (`order_id = 3`). Always use `EXPLODE_OUTER()` when you must preserve parent rows.
