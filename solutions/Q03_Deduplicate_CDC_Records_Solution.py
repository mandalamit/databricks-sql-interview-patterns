# Databricks notebook source
# MAGIC %md
# MAGIC # Q03 Solution: Deduplicate CDC Records Keeping Latest Event
# MAGIC
# MAGIC - **Pattern:** Pattern 1: Ranking & Top-N
# MAGIC - **Difficulty:** Easy-Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC The `orders_raw` table contains duplicate `order_id` records from an upstream CDC stream. Return a deduplicated dataset keeping only the **most recent record** per `order_id` based on `updated_at`.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC SELECT order_id, customer_id, region, product_name, status, amount, order_date, updated_at
# MAGIC FROM orders_raw
# MAGIC QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1
# MAGIC ORDER BY order_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC In Databricks, `ROW_NUMBER() ... QUALIFY` is the standard Bronze-to-Silver deduplication pattern. Always ask the interviewer what tie-breaker column to use if two rows share the exact same `updated_at`.
