# Databricks notebook source
# MAGIC %md
# MAGIC # Q12 Solution: Detect Sudden Product Price Drops (>20%)
# MAGIC
# MAGIC - **Pattern:** Pattern 4: Sessionization & Event Sequencing
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Using `product_prices`, flag any date where a product's non-null price dropped by **more than 20%** compared to its most recent previous non-null price.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC WITH non_null AS (
# MAGIC   SELECT product_id, price_date, price,
# MAGIC          LAG(price) OVER (PARTITION BY product_id ORDER BY price_date) AS prev_price
# MAGIC   FROM product_prices
# MAGIC   WHERE price IS NOT NULL
# MAGIC )
# MAGIC SELECT product_id, price_date, prev_price, price AS current_price,
# MAGIC        ROUND((price - prev_price) * 100.0 / prev_price, 2) AS pct_change
# MAGIC FROM non_null
# MAGIC WHERE prev_price IS NOT NULL AND (price - prev_price) / prev_price < -0.20
# MAGIC ORDER BY product_id, price_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Filtering `WHERE price IS NOT NULL` first ensures `LAG` compares against the last *known* price rather than an intermediate `NULL`.
