# Databricks notebook source
# MAGIC %md
# MAGIC # Q10 Solution: Clickstream Sessionization (30-Minute Timeout)
# MAGIC
# MAGIC - **Pattern:** Pattern 4: Sessionization & Event Sequencing
# MAGIC - **Difficulty:** Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Assign a unique `session_id` to each event in `clickstream_events`. A new session starts for a user whenever more than **30 minutes** pass since their previous event.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC
# MAGIC WITH gaps AS (
# MAGIC   SELECT event_id, user_id, event_type, event_ts,
# MAGIC          LAG(event_ts) OVER (PARTITION BY user_id ORDER BY event_ts) AS prev_ts
# MAGIC   FROM clickstream_events
# MAGIC ),
# MAGIC flags AS (
# MAGIC   SELECT *,
# MAGIC          CASE
# MAGIC            WHEN prev_ts IS NULL OR (UNIX_TIMESTAMP(event_ts) - UNIX_TIMESTAMP(prev_ts)) > 1800 THEN 1
# MAGIC            ELSE 0
# MAGIC          END AS new_session_flag
# MAGIC   FROM gaps
# MAGIC )
# MAGIC SELECT event_id, user_id, event_type, event_ts,
# MAGIC        CONCAT(user_id, '_', SUM(new_session_flag) OVER (PARTITION BY user_id ORDER BY event_ts)) AS session_id
# MAGIC FROM flags
# MAGIC ORDER BY user_id, event_ts;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Sessionization is one of the top 5 Data Engineering SQL interview questions. The 3-step blueprint is always: `LAG()` -> flag timeout -> cumulative `SUM(flag)`.
