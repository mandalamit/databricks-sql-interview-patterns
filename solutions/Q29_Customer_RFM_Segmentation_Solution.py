# Databricks notebook source
# MAGIC %md
# MAGIC # Q29 Solution: Customer RFM Segmentation (NTILE)
# MAGIC
# MAGIC - **Pattern:** Pattern 11: Analytical & Statistical SQL
# MAGIC - **Difficulty:** Medium-Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Build a **Recency, Frequency, Monetary (RFM)** table for all completed customers in `orders_raw` (using `'2026-04-15'` as the reference date). Assign 1–4 quartile scores using `NTILE(4)`.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC
# MAGIC WITH dedup AS (
# MAGIC   SELECT customer_id, order_id, order_date, amount
# MAGIC   FROM orders_raw
# MAGIC   WHERE status = 'COMPLETED' AND amount IS NOT NULL
# MAGIC   QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1
# MAGIC ),
# MAGIC rfm_raw AS (
# MAGIC   SELECT customer_id,
# MAGIC          DATEDIFF(DATE '2026-04-15', MAX(order_date)) AS recency_days,
# MAGIC          COUNT(order_id) AS frequency,
# MAGIC          ROUND(SUM(amount), 2) AS monetary
# MAGIC   FROM dedup
# MAGIC   GROUP BY customer_id
# MAGIC )
# MAGIC SELECT customer_id, recency_days, frequency, monetary,
# MAGIC        NTILE(4) OVER (ORDER BY recency_days DESC) AS r_score,
# MAGIC        NTILE(4) OVER (ORDER BY frequency ASC) AS f_score,
# MAGIC        NTILE(4) OVER (ORDER BY monetary ASC) AS m_score
# MAGIC FROM rfm_raw
# MAGIC ORDER BY monetary DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Notice `recency_days DESC` for `r_score`: fewer days since last order = higher recency score (4 is best).
