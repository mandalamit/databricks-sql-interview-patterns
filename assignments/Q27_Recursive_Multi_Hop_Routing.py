# Databricks notebook source
# MAGIC %md
# MAGIC # Q27: Multi-Hop Warehouse Logistics Routing
# MAGIC
# MAGIC - **Pattern:** Pattern 10: Hierarchical & Graph Queries
# MAGIC - **Difficulty:** Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Using `warehouse_routes`, find all possible routes (1-hop or multi-hop) from `'BLR'` to `'CCU'`, returning the `route_path`, `hops`, `total_distance_km`, and `total_cost`, ordered by cheapest route first.
# MAGIC
# MAGIC > **Prerequisite:** Run `Day00_Setup.py` once to create the `sql_interview_prep` database and tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC -- Preview input data
# MAGIC SELECT * FROM warehouse_routes;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Your SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO: Write your Databricks SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ### Interview Tip / Edge Case to Consider
# MAGIC Think about NULLs, duplicate rows, ties, and partition/shuffle performance before checking `solutions/Q27_Recursive_Multi_Hop_Routing_Solution.py`.
