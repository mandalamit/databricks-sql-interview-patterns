# Databricks notebook source
# MAGIC %md
# MAGIC # Q17 Solution: E-Commerce Conversion Funnel & Drop-off Rates
# MAGIC
# MAGIC - **Pattern:** Pattern 6: Pivoting, Funnels & Cubes
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Using `clickstream_events`, compute unique users at each funnel stage (`visit` -> `add_to_cart` -> `checkout` -> `purchase`) and calculate the conversion rate from `visit`.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC WITH stage_counts AS (
# MAGIC   SELECT COUNT(DISTINCT CASE WHEN event_type = 'visit' THEN user_id END) AS visitors,
# MAGIC          COUNT(DISTINCT CASE WHEN event_type = 'add_to_cart' THEN user_id END) AS cart_users,
# MAGIC          COUNT(DISTINCT CASE WHEN event_type = 'checkout' THEN user_id END) AS checkout_users,
# MAGIC          COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) AS purchasers
# MAGIC   FROM clickstream_events
# MAGIC )
# MAGIC SELECT visitors,
# MAGIC        cart_users,
# MAGIC        ROUND(cart_users * 100.0 / NULLIF(visitors, 0), 2) AS visit_to_cart_pct,
# MAGIC        checkout_users,
# MAGIC        ROUND(checkout_users * 100.0 / NULLIF(cart_users, 0), 2) AS cart_to_checkout_pct,
# MAGIC        purchasers,
# MAGIC        ROUND(purchasers * 100.0 / NULLIF(visitors, 0), 2) AS overall_conversion_pct
# MAGIC FROM stage_counts;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC In stricter funnel interviews, you also enforce timestamp ordering (`visit_ts < cart_ts < checkout_ts < purchase_ts`) per user.
