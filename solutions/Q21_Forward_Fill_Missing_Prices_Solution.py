# Databricks notebook source
# MAGIC %md
# MAGIC # Q21 Solution: Forward-Fill Missing Daily Product Prices
# MAGIC
# MAGIC - **Pattern:** Pattern 8: Data Cleaning & Quality Audits
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC In `product_prices`, some dates have `NULL` prices. Fill each `NULL` with the **most recent non-null price** for that product.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC
# MAGIC SELECT product_id,
# MAGIC        price_date,
# MAGIC        price AS raw_price,
# MAGIC        LAST_VALUE(price, TRUE) OVER (
# MAGIC          PARTITION BY product_id
# MAGIC          ORDER BY price_date
# MAGIC          ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
# MAGIC        ) AS filled_price
# MAGIC FROM product_prices
# MAGIC ORDER BY product_id, price_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Databricks SQL supports `LAST_VALUE(col, TRUE)` (where `TRUE` means `IGNORE NULLS`), making forward-fill a one-liner!
