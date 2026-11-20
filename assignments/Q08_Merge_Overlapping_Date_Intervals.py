# Databricks notebook source
# MAGIC %md
# MAGIC # Q08: Merge Overlapping Subscription Intervals
# MAGIC
# MAGIC - **Pattern:** Pattern 3: Gaps & Islands
# MAGIC - **Difficulty:** Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC In `subscriptions`, a user may have overlapping or adjacent (`end_date + 1 = next start_date`) subscription records. Merge them into continuous active periods per `user_id`.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT * FROM subscriptions ORDER BY user_id, start_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q08_Merge_Overlapping_Date_Intervals_Solution.py`.
