# Databricks notebook source
# MAGIC %md
# MAGIC # Q09 Solution: Find Missing Order IDs (Sequence Gaps)
# MAGIC
# MAGIC - **Pattern:** Pattern 3: Gaps & Islands
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Find all **missing `order_id` values** between the minimum and maximum `order_id` in `orders_raw`.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC
# MAGIC WITH bounds AS (
# MAGIC   SELECT MIN(order_id) AS min_id, MAX(order_id) AS max_id FROM orders_raw
# MAGIC ),
# MAGIC all_ids AS (
# MAGIC   SELECT EXPLODE(SEQUENCE(min_id, max_id)) AS expected_id FROM bounds
# MAGIC )
# MAGIC SELECT a.expected_id AS missing_order_id
# MAGIC FROM all_ids a
# MAGIC LEFT ANTI JOIN orders_raw o ON a.expected_id = o.order_id
# MAGIC ORDER BY missing_order_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Databricks SQL's `SEQUENCE(min_id, max_id)` + `EXPLODE` + `LEFT ANTI JOIN` is much cleaner and faster than recursive number generators.
