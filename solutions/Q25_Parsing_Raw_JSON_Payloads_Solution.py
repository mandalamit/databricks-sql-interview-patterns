# Databricks notebook source
# MAGIC %md
# MAGIC # Q25 Solution: Parsing Raw JSON Event Payloads
# MAGIC
# MAGIC - **Pattern:** Pattern 9: Semi-Structured Data (Databricks Specialty)
# MAGIC - **Difficulty:** Easy-Medium
# MAGIC
# MAGIC ### Problem Statement
# MAGIC From `nested_orders.raw_json`, extract `source`, `coupon_code`, `discount` (as INT, default 0), and `device_os` using Databricks SQL's native JSON path operator `:`.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC
# MAGIC SELECT order_id,
# MAGIC        raw_json:source AS source,
# MAGIC        raw_json:coupon.code AS coupon_code,
# MAGIC        COALESCE(CAST(raw_json:coupon.discount AS INT), 0) AS discount,
# MAGIC        raw_json:device.os AS device_os
# MAGIC FROM nested_orders
# MAGIC ORDER BY order_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC In Databricks SQL, `raw_json:coupon.code` is cleaner and faster than legacy `get_json_object(raw_json, '$.coupon.code')`. For full schema parsing, mention `from_json()` or the `VARIANT` type.
