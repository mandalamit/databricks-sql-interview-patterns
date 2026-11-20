# Databricks notebook source
# MAGIC %md
# MAGIC # Q14 Solution: Bronze vs. Silver Data Reconciliation
# MAGIC
# MAGIC - **Pattern:** Pattern 5: Joins, Anti-Joins & Market Basket
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Compare deduplicated `orders_raw` (Bronze) against `orders_silver` and classify every discrepancy as `'MISSING_IN_SILVER'`, `'ORPHAN_IN_SILVER'`, or `'AMOUNT_MISMATCH'`.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC
# MAGIC WITH bronze AS (
# MAGIC   SELECT order_id, amount
# MAGIC   FROM orders_raw
# MAGIC   QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1
# MAGIC )
# MAGIC SELECT COALESCE(b.order_id, s.order_id) AS order_id,
# MAGIC        b.amount AS bronze_amount,
# MAGIC        s.amount AS silver_amount,
# MAGIC        CASE
# MAGIC          WHEN s.order_id IS NULL THEN 'MISSING_IN_SILVER'
# MAGIC          WHEN b.order_id IS NULL THEN 'ORPHAN_IN_SILVER'
# MAGIC          WHEN NOT (b.amount <=> s.amount) THEN 'AMOUNT_MISMATCH'
# MAGIC        END AS issue_type
# MAGIC FROM bronze b
# MAGIC FULL OUTER JOIN orders_silver s ON b.order_id = s.order_id
# MAGIC WHERE s.order_id IS NULL OR b.order_id IS NULL OR NOT (b.amount <=> s.amount)
# MAGIC ORDER BY order_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Note the NULL-safe equality operator `<=>` in Databricks SQL! Standard `!=` fails silently when one side is `NULL`.
