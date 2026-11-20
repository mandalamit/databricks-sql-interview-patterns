# Databricks notebook source
# MAGIC %md
# MAGIC # Q03: Deduplicate CDC Records Keeping Latest Event
# MAGIC
# MAGIC - **Pattern:** Pattern 1: Ranking & Top-N
# MAGIC - **Difficulty:** Easy-Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC The `orders_raw` table contains duplicate `order_id` records from an upstream CDC stream. Return a deduplicated dataset keeping only the **most recent record** per `order_id` based on `updated_at`.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT order_id, COUNT(*) AS cnt FROM orders_raw GROUP BY order_id HAVING COUNT(*) > 1;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q03_Deduplicate_CDC_Records_Solution.py`.
