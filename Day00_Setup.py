# Databricks notebook source
# MAGIC %md
# MAGIC # Day 00: SQL Interview Dataset Setup
# MAGIC
# MAGIC Run this notebook **once** before solving any question (`Q01` through `Q30`).
# MAGIC
# MAGIC ### Tables Created in `sql_interview_prep`:
# MAGIC 1. `employees` — Org hierarchy & salaries (ties, single-person dept, manager_id)
# MAGIC 2. `orders_raw` — E-commerce orders with intentional duplicates, sequence gaps, nulls & outliers
# MAGIC 3. `orders_silver` — Curated orders table with slight mismatches for reconciliation
# MAGIC 4. `user_logins` — Daily login logs with 3+ day consecutive streaks and gaps
# MAGIC 5. `subscriptions` — Overlapping and adjacent subscription date intervals
# MAGIC 6. `clickstream_events` — Timestamped user events for sessionization & conversion funnel
# MAGIC 7. `product_prices` — Daily prices with NULL gaps and sudden price drops
# MAGIC 8. `nested_orders` — Complex ARRAY<STRUCT>, ARRAY<STRING>, and raw JSON strings
# MAGIC 9. `warehouse_routes` — Directed graph of logistics hubs for recursive routing

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS sql_interview_prep;
# MAGIC USE SCHEMA sql_interview_prep;
# MAGIC SELECT current_catalog() AS active_catalog, current_schema() AS active_schema;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 1. employees (Q01, Q02, Q26)
# MAGIC CREATE OR REPLACE TABLE employees (
# MAGIC   emp_id INT, emp_name STRING, dept_name STRING, manager_id INT, salary INT, hire_date DATE
# MAGIC ) USING DELTA;
# MAGIC
# MAGIC INSERT INTO employees VALUES
# MAGIC   (1,  'Aarav',   'Engineering', NULL, 220000, '2021-01-10'),
# MAGIC   (2,  'Meera',   'Engineering', 1,    180000, '2021-06-15'),
# MAGIC   (3,  'Rohan',   'Engineering', 1,    180000, '2022-02-01'),
# MAGIC   (4,  'Priya',   'Engineering', 2,    150000, '2022-08-20'),
# MAGIC   (5,  'Kabir',   'Engineering', 2,    130000, '2023-03-11'),
# MAGIC   (6,  'Sneha',   'Sales',       1,    160000, '2021-04-05'),
# MAGIC   (7,  'Vikram',  'Sales',       6,    140000, '2022-01-19'),
# MAGIC   (8,  'Ananya',  'Sales',       6,    140000, '2022-07-23'),
# MAGIC   (9,  'Dev',     'Sales',       7,    110000, '2023-09-01'),
# MAGIC   (10, 'Riya',    'HR',          1,    125000, '2022-05-14'),
# MAGIC   (11, 'Karan',   'HR',          10,   95000,  '2023-11-01'),
# MAGIC   (12, 'Zoya',    'Legal',       1,    175000, '2023-01-01');

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 2. orders_raw (Q03, Q04, Q05, Q06, Q09, Q11, Q13, Q14, Q15, Q16, Q18, Q19, Q20, Q22, Q28, Q29, Q30)
# MAGIC CREATE OR REPLACE TABLE orders_raw (
# MAGIC   order_id INT, customer_id INT, region STRING, product_name STRING,
# MAGIC   status STRING, amount DOUBLE, order_date DATE, updated_at TIMESTAMP
# MAGIC ) USING DELTA;
# MAGIC
# MAGIC INSERT INTO orders_raw VALUES
# MAGIC   -- Normal orders across months & regions
# MAGIC   (1001, 1, 'APAC',  'Laptop',     'COMPLETED', 1200.0, '2026-01-05', '2026-01-05 10:00:00'),
# MAGIC   (1001, 1, 'APAC',  'Laptop',     'COMPLETED', 1250.0, '2026-01-05', '2026-01-05 12:30:00'), -- duplicate (latest)
# MAGIC   (1002, 1, 'APAC',  'Mouse',      'COMPLETED', 40.0,   '2026-01-05', '2026-01-05 10:05:00'),
# MAGIC   (1003, 2, 'EMEA',  'Laptop',     'COMPLETED', 1150.0, '2026-01-10', '2026-01-10 09:00:00'),
# MAGIC   (1004, 2, 'EMEA',  'Keyboard',   'COMPLETED', 90.0,   '2026-01-15', '2026-01-15 11:00:00'),
# MAGIC   (1005, 3, 'NA',    'Monitor',    'COMPLETED', 400.0,  '2026-01-20', '2026-01-20 14:00:00'),
# MAGIC   -- Note: order_id 1006 is intentionally missing (sequence gap for Q09)
# MAGIC   (1007, 1, 'APAC',  'Keyboard',   'COMPLETED', 85.0,   '2026-02-02', '2026-02-02 08:30:00'),
# MAGIC   (1008, 2, 'EMEA',  'Mouse',      'COMPLETED', 45.0,   '2026-02-05', '2026-02-05 16:00:00'),
# MAGIC   (1009, 4, 'APAC',  'Laptop',     'COMPLETED', 1300.0, '2026-02-10', '2026-02-10 10:15:00'),
# MAGIC   (1010, 4, 'APAC',  'Mouse',      'COMPLETED', 35.0,   '2026-02-10', '2026-02-10 10:20:00'),
# MAGIC   (1011, 4, 'APAC',  'Headphones', 'COMPLETED', 150.0,  '2026-02-18', '2026-02-18 13:00:00'),
# MAGIC   (1012, 5, 'NA',    'Laptop',     'CANCELLED', 1100.0, '2026-02-22', '2026-02-22 15:00:00'),
# MAGIC   (1013, 5, 'NA',    'Monitor',    'COMPLETED', 420.0,  '2026-02-25', '2026-02-25 17:00:00'),
# MAGIC   -- Note: order_id 1014 is intentionally missing
# MAGIC   (1015, 1, 'APAC',  'Monitor',    'COMPLETED', 380.0,  '2026-03-01', '2026-03-01 09:00:00'),
# MAGIC   (1016, 3, 'NA',    'Laptop',     'COMPLETED', 1220.0, '2026-03-04', '2026-03-04 11:30:00'),
# MAGIC   (1017, 3, 'NA',    'Mouse',      'COMPLETED', 50.0,   '2026-03-04', '2026-03-04 11:35:00'),
# MAGIC   (1018, 6, 'EMEA',  'Headphones', 'COMPLETED', 180.0,  '2026-03-08', '2026-03-08 14:45:00'),
# MAGIC   (1019, 6, 'EMEA',  'Keyboard',   'COMPLETED', 95.0,   '2026-03-10', '2026-03-10 10:00:00'),
# MAGIC   (1020, 7, 'APAC',  'Laptop',     'COMPLETED', 1280.0, '2026-03-12', '2026-03-12 12:00:00'),
# MAGIC   (1021, 7, 'APAC',  'Mouse',      'COMPLETED', NULL,   '2026-03-13', '2026-03-13 12:00:00'), -- NULL amount for Q22
# MAGIC   (1022, 8, 'NA',    'ServerRack', 'COMPLETED', 15000.0,'2026-03-15', '2026-03-15 18:00:00'), -- Outlier for Q22
# MAGIC   (1023, 2, 'EMEA',  'Monitor',    'COMPLETED', 410.0,  '2026-03-20', '2026-03-20 09:30:00'),
# MAGIC   (1024, 1, 'APAC',  'Headphones', 'COMPLETED', 160.0,  '2026-04-02', '2026-04-02 10:00:00'),
# MAGIC   (1025, 3, 'NA',    'Keyboard',   'COMPLETED', 100.0,  '2026-04-05', '2026-04-05 11:00:00'),
# MAGIC   (1026, 9, 'EMEA',  'Laptop',     'COMPLETED', 1190.0, '2026-04-07', '2026-04-07 15:00:00');
# MAGIC
# MAGIC -- 3. orders_silver (for Q14 Reconciliation)
# MAGIC CREATE OR REPLACE TABLE orders_silver AS
# MAGIC SELECT order_id, customer_id, region, product_name, status, amount, order_date
# MAGIC FROM (
# MAGIC   SELECT *, ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) AS rn
# MAGIC   FROM orders_raw
# MAGIC ) WHERE rn = 1 AND order_id NOT IN (1025, 1026);
# MAGIC
# MAGIC -- Inject one mismatched amount and one extra orphan record in silver
# MAGIC UPDATE orders_silver SET amount = 999.0 WHERE order_id = 1003;
# MAGIC INSERT INTO orders_silver VALUES (9999, 99, 'APAC', 'LegacyItem', 'COMPLETED', 50.0, '2025-12-31');

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 4. user_logins (Q07 Gaps & Islands)
# MAGIC CREATE OR REPLACE TABLE user_logins (user_id INT, login_date DATE) USING DELTA;
# MAGIC INSERT INTO user_logins VALUES
# MAGIC   (101, '2026-03-01'), (101, '2026-03-02'), (101, '2026-03-03'), (101, '2026-03-04'), -- 4-day streak
# MAGIC   (101, '2026-03-04'), -- duplicate login same day
# MAGIC   (101, '2026-03-07'), (101, '2026-03-08'), -- 2-day streak
# MAGIC   (102, '2026-03-01'), (102, '2026-03-03'), (102, '2026-03-04'), (102, '2026-03-05'), -- 3-day streak
# MAGIC   (103, '2026-03-01'), (103, '2026-03-02'), (103, '2026-03-05'); -- max 2-day streak
# MAGIC
# MAGIC -- 5. subscriptions (Q08 Merge Overlapping Intervals)
# MAGIC CREATE OR REPLACE TABLE subscriptions (user_id INT, start_date DATE, end_date DATE) USING DELTA;
# MAGIC INSERT INTO subscriptions VALUES
# MAGIC   (1, '2026-01-01', '2026-01-15'),
# MAGIC   (1, '2026-01-10', '2026-01-25'), -- overlaps
# MAGIC   (1, '2026-01-26', '2026-02-05'), -- adjacent
# MAGIC   (1, '2026-02-20', '2026-03-01'), -- separate island
# MAGIC   (2, '2026-01-05', '2026-01-20'),
# MAGIC   (2, '2026-01-08', '2026-01-12'); -- fully contained

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 6. clickstream_events (Q10 Sessionization, Q17 Funnel, Q30 Capstone)
# MAGIC CREATE OR REPLACE TABLE clickstream_events (
# MAGIC   event_id INT, user_id INT, event_type STRING, event_ts TIMESTAMP
# MAGIC ) USING DELTA;
# MAGIC
# MAGIC INSERT INTO clickstream_events VALUES
# MAGIC   (1,  1, 'visit',       '2026-03-01 10:00:00'),
# MAGIC   (2,  1, 'add_to_cart', '2026-03-01 10:10:00'),
# MAGIC   (3,  1, 'checkout',    '2026-03-01 10:25:00'),
# MAGIC   (4,  1, 'purchase',    '2026-03-01 10:28:00'),
# MAGIC   (5,  1, 'visit',       '2026-03-01 11:30:00'), -- >30 min gap -> new session
# MAGIC   (6,  2, 'visit',       '2026-03-01 09:00:00'),
# MAGIC   (7,  2, 'add_to_cart', '2026-03-01 09:15:00'),
# MAGIC   (8,  2, 'checkout',    '2026-03-01 09:50:00'), -- >30 min gap -> new session
# MAGIC   (9,  3, 'visit',       '2026-03-01 14:00:00'),
# MAGIC   (10, 3, 'add_to_cart', '2026-03-01 14:05:00'),
# MAGIC   (11, 4, 'visit',       '2026-03-01 15:00:00');
# MAGIC
# MAGIC -- 7. product_prices (Q12 Anomaly, Q21 Forward Fill)
# MAGIC CREATE OR REPLACE TABLE product_prices (
# MAGIC   product_id INT, price_date DATE, price DOUBLE
# MAGIC ) USING DELTA;
# MAGIC
# MAGIC INSERT INTO product_prices VALUES
# MAGIC   (10, '2026-03-01', 100.0),
# MAGIC   (10, '2026-03-02', NULL),
# MAGIC   (10, '2026-03-03', NULL),
# MAGIC   (10, '2026-03-04', 75.0),  -- 25% drop
# MAGIC   (10, '2026-03-05', 80.0),
# MAGIC   (20, '2026-03-01', 200.0),
# MAGIC   (20, '2026-03-02', 195.0),
# MAGIC   (20, '2026-03-03', NULL),
# MAGIC   (20, '2026-03-04', 150.0); -- >20% drop

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 8. nested_orders (Q23 Explode, Q24 Higher-Order Functions, Q25 JSON Parsing)
# MAGIC CREATE OR REPLACE TABLE nested_orders AS
# MAGIC SELECT
# MAGIC   1 AS order_id,
# MAGIC   101 AS customer_id,
# MAGIC   ARRAY(
# MAGIC     NAMED_STRUCT('sku', 'LAP-01', 'qty', 1, 'unit_price', 1200.0),
# MAGIC     NAMED_STRUCT('sku', 'MOU-02', 'qty', 2, 'unit_price', 25.0)
# MAGIC   ) AS items,
# MAGIC   ARRAY('electronics', 'priority', 'online') AS tags,
# MAGIC   '{"source":"mobile_app","coupon":{"code":"SAVE10","discount":10},"device":{"os":"iOS"}}' AS raw_json
# MAGIC UNION ALL
# MAGIC SELECT
# MAGIC   2,
# MAGIC   102,
# MAGIC   ARRAY(
# MAGIC     NAMED_STRUCT('sku', 'MON-03', 'qty', 2, 'unit_price', 300.0)
# MAGIC   ),
# MAGIC   ARRAY('electronics', 'b2b'),
# MAGIC   '{"source":"web","coupon":null,"device":{"os":"Windows"}}'
# MAGIC UNION ALL
# MAGIC SELECT
# MAGIC   3,
# MAGIC   103,
# MAGIC   CAST(ARRAY() AS ARRAY<STRUCT<sku:STRING, qty:INT, unit_price:DOUBLE>>),
# MAGIC   ARRAY('empty_cart'),
# MAGIC   '{"source":"mobile_app","coupon":{"code":"NEW5","discount":5},"device":{"os":"Android"}}';
# MAGIC
# MAGIC -- 9. warehouse_routes (Q27 Recursive Graph Routing)
# MAGIC CREATE OR REPLACE TABLE warehouse_routes (
# MAGIC   src_hub STRING, dst_hub STRING, distance_km INT, cost DOUBLE
# MAGIC ) USING DELTA;
# MAGIC
# MAGIC INSERT INTO warehouse_routes VALUES
# MAGIC   ('BLR', 'HYD', 570,  400.0),
# MAGIC   ('BLR', 'MUM', 980,  700.0),
# MAGIC   ('HYD', 'DEL', 1550, 950.0),
# MAGIC   ('MUM', 'DEL', 1420, 850.0),
# MAGIC   ('DEL', 'CCU', 1500, 900.0),
# MAGIC   ('HYD', 'CCU', 1490, 880.0);

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN sql_interview_prep;
