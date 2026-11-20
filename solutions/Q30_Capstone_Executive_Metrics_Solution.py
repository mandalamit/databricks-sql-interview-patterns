# Databricks notebook source
# MAGIC %md
# MAGIC # Q30 Solution: Capstone: End-to-End Executive Metrics Query
# MAGIC
# MAGIC - **Pattern:** Pattern 12: Databricks DE Case Study
# MAGIC - **Difficulty:** Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Combine multiple patterns in one clean, modular multi-CTE Databricks SQL query:
# MAGIC 1. Deduplicate `orders_raw` (completed, non-null, excluding outliers > 10,000)
# MAGIC 2. Compute each region's monthly revenue & MoM growth %
# MAGIC 3. Rank regions per month and return the **#1 top-performing region each month**.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC WITH clean_orders AS (
# MAGIC   SELECT order_id, region, order_date, amount
# MAGIC   FROM orders_raw
# MAGIC   WHERE status = 'COMPLETED' AND amount IS NOT NULL AND amount <= 10000
# MAGIC   QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1
# MAGIC ),
# MAGIC regional_monthly AS (
# MAGIC   SELECT DATE_TRUNC('MONTH', order_date) AS order_month,
# MAGIC          region,
# MAGIC          COUNT(order_id) AS order_count,
# MAGIC          ROUND(SUM(amount), 2) AS revenue
# MAGIC   FROM clean_orders
# MAGIC   GROUP BY 1, 2
# MAGIC ),
# MAGIC with_growth AS (
# MAGIC   SELECT order_month,
# MAGIC          region,
# MAGIC          order_count,
# MAGIC          revenue,
# MAGIC          ROUND(
# MAGIC            (revenue - LAG(revenue) OVER (PARTITION BY region ORDER BY order_month)) * 100.0
# MAGIC            / NULLIF(LAG(revenue) OVER (PARTITION BY region ORDER BY order_month), 0), 2
# MAGIC          ) AS mom_growth_pct
# MAGIC   FROM regional_monthly
# MAGIC )
# MAGIC SELECT DATE_FORMAT(order_month, 'yyyy-MM') AS month,
# MAGIC        region AS top_region,
# MAGIC        order_count,
# MAGIC        revenue,
# MAGIC        mom_growth_pct
# MAGIC FROM with_growth
# MAGIC QUALIFY RANK() OVER (PARTITION BY order_month ORDER BY revenue DESC) = 1
# MAGIC ORDER BY month;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC In senior interviews, structure matters as much as correctness: readable CTEs (`clean_orders` -> `regional_monthly` -> `with_growth`), early filtering, `NULLIF` guards, and `QUALIFY`.
