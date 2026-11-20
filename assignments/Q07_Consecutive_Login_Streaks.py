# Databricks notebook source
# MAGIC %md
# MAGIC # Q07: Consecutive Login Streaks (Gaps & Islands)
# MAGIC
# MAGIC - **Pattern:** Pattern 3: Gaps & Islands
# MAGIC - **Difficulty:** Medium-Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC From `user_logins`, find all users who logged in for **3 or more consecutive days**, along with the streak's `start_date`, `end_date`, and `streak_length`. Handle duplicate logins on the same day.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT * FROM user_logins ORDER BY user_id, login_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q07_Consecutive_Login_Streaks_Solution.py`.
