# Databricks notebook source
# MAGIC %md
# MAGIC # Q12: Detect Sudden Product Price Drops (>20%)
# MAGIC
# MAGIC - **Pattern:** Pattern 4: Sessionization & Event Sequencing
# MAGIC - **Difficulty:** Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Using `product_prices`, flag any date where a product's non-null price dropped by **more than 20%** compared to its most recent previous non-null price.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT * FROM product_prices ORDER BY product_id, price_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q12_Price_Drop_Anomaly_Detection_Solution.py`.
