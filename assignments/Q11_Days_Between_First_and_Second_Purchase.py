# Databricks notebook source
# MAGIC %md
# MAGIC # Q11: Time Between 1st and 2nd Purchase per Customer
# MAGIC
# MAGIC - **Pattern:** Pattern 4: Sessionization & Event Sequencing
# MAGIC - **Difficulty:** Easy-Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC For every customer in `orders_raw` (completed, deduplicated) who has at least 2 orders, compute the **number of days between their 1st and 2nd order**.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT customer_id, order_id, order_date FROM orders_raw WHERE status='COMPLETED' ORDER BY customer_id, order_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q11_Days_Between_First_and_Second_Purchase_Solution.py`.
