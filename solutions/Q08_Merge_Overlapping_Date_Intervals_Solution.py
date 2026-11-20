# Databricks notebook source
# MAGIC %md
# MAGIC # Q08 Solution: Merge Overlapping Subscription Intervals
# MAGIC
# MAGIC - **Pattern:** Pattern 3: Gaps & Islands
# MAGIC - **Difficulty:** Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC In `subscriptions`, a user may have overlapping or adjacent (`end_date + 1 = next start_date`) subscription records. Merge them into continuous active periods per `user_id`.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC WITH prev_max AS (
# MAGIC   SELECT user_id, start_date, end_date,
# MAGIC          MAX(end_date) OVER (
# MAGIC            PARTITION BY user_id ORDER BY start_date, end_date
# MAGIC            ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
# MAGIC          ) AS max_prev_end
# MAGIC   FROM subscriptions
# MAGIC ),
# MAGIC flags AS (
# MAGIC   SELECT *,
# MAGIC          CASE WHEN max_prev_end IS NULL OR start_date > DATE_ADD(max_prev_end, 1) THEN 1 ELSE 0 END AS is_new_island
# MAGIC   FROM prev_max
# MAGIC ),
# MAGIC grouped AS (
# MAGIC   SELECT *, SUM(is_new_island) OVER (PARTITION BY user_id ORDER BY start_date, end_date) AS island_id
# MAGIC   FROM flags
# MAGIC )
# MAGIC SELECT user_id, MIN(start_date) AS active_start, MAX(end_date) AS active_end
# MAGIC FROM grouped
# MAGIC GROUP BY user_id, island_id
# MAGIC ORDER BY user_id, active_start;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Why `MAX(end_date) OVER (... UNBOUNDED PRECEDING AND 1 PRECEDING)` instead of `LAG(end_date)`? Because of fully contained intervals (like user 2: Jan 8-12 inside Jan 5-20). `LAG` fails on contained intervals!
