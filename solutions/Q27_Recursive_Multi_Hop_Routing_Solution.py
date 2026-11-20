# Databricks notebook source
# MAGIC %md
# MAGIC # Q27 Solution: Multi-Hop Warehouse Logistics Routing
# MAGIC
# MAGIC - **Pattern:** Pattern 10: Hierarchical & Graph Queries
# MAGIC - **Difficulty:** Hard
# MAGIC
# MAGIC ### Problem Statement
# MAGIC Using `warehouse_routes`, find all possible routes (1-hop or multi-hop) from `'BLR'` to `'CCU'`, returning the `route_path`, `hops`, `total_distance_km`, and `total_cost`, ordered by cheapest route first.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE sql_interview_prep;
# MAGIC
# MAGIC WITH RECURSIVE routes AS (
# MAGIC   SELECT src_hub, dst_hub,
# MAGIC          CONCAT(src_hub, ' -> ', dst_hub) AS route_path,
# MAGIC          1 AS hops,
# MAGIC          distance_km AS total_distance_km,
# MAGIC          cost AS total_cost,
# MAGIC          ARRAY(src_hub, dst_hub) AS visited
# MAGIC   FROM warehouse_routes
# MAGIC   WHERE src_hub = 'BLR'
# MAGIC 
# MAGIC   UNION ALL
# MAGIC 
# MAGIC   SELECT r.src_hub, w.dst_hub,
# MAGIC          CONCAT(r.route_path, ' -> ', w.dst_hub),
# MAGIC          r.hops + 1,
# MAGIC          r.total_distance_km + w.distance_km,
# MAGIC          r.total_cost + w.cost,
# MAGIC          CONCAT(r.visited, ARRAY(w.dst_hub))
# MAGIC   FROM routes r
# MAGIC   JOIN warehouse_routes w ON r.dst_hub = w.src_hub
# MAGIC   WHERE NOT ARRAY_CONTAINS(r.visited, w.dst_hub) AND r.hops < 5
# MAGIC )
# MAGIC SELECT route_path, hops, total_distance_km, total_cost
# MAGIC FROM routes
# MAGIC WHERE dst_hub = 'CCU'
# MAGIC ORDER BY total_cost ASC;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key Interview Talking Points
# MAGIC Tracking `visited` as an `ARRAY` and checking `NOT ARRAY_CONTAINS` prevents infinite loops in cyclic graphs.
