# Databricks notebook source
# MAGIC %md
# MAGIC # Q07 Solution: Consecutive Login Streaks (Gaps & Islands)
# MAGIC
# MAGIC - **Pattern:** Pattern 3: Gaps & Islands
# MAGIC - **Difficulty:** Medium-Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC From `user_logins`, find all users who logged in for **3 or more consecutive days**, along with the streak's `start_date`, `end_date`, and `streak_length`. Handle duplicate logins on the same day.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC WITH distinct_logins AS (
# MAGIC   SELECT DISTINCT user_id, login_date FROM user_logins
# MAGIC ),
# MAGIC islands AS (
# MAGIC   SELECT user_id,
# MAGIC          login_date,
# MAGIC          DATE_SUB(login_date, CAST(ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) AS INT)) AS grp
# MAGIC   FROM distinct_logins
# MAGIC )
# MAGIC SELECT user_id,
# MAGIC        MIN(login_date) AS streak_start,
# MAGIC        MAX(login_date) AS streak_end,
# MAGIC        COUNT(*) AS streak_days
# MAGIC FROM islands
# MAGIC GROUP BY user_id, grp
# MAGIC HAVING COUNT(*) >= 3
# MAGIC ORDER BY user_id, streak_start;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC The classic Gaps & Islands trick: subtracting `ROW_NUMBER()` days from consecutive dates yields a constant anchor date (`grp`). Always deduplicate `(user_id, login_date)` first!
