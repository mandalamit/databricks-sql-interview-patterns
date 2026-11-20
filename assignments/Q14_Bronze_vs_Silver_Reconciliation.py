# Databricks notebook source
# MAGIC %md
# MAGIC # Q14: Bronze vs. Silver Data Reconciliation
# MAGIC
# MAGIC - **Pattern:** Pattern 5: Joins, Anti-Joins & Market Basket
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Compare deduplicated `orders_raw` (Bronze) against `orders_silver` and classify every discrepancy as `'MISSING_IN_SILVER'`, `'ORPHAN_IN_SILVER'`, or `'AMOUNT_MISMATCH'`.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT COUNT(*) AS bronze_cnt FROM orders_raw; SELECT COUNT(*) AS silver_cnt FROM orders_silver;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q14_Bronze_vs_Silver_Reconciliation_Solution.py`.
