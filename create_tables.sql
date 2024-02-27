-- nation
CREATE TABLE IF NOT EXISTS "nation" (
  "n_nationkey"  INT,
  "n_name"       INT,
  "n_regionkey"  INT,
  "n_comment"    INT,
  "n_dummy"      INT
  );
--   PRIMARY KEY ("n_nationkey")

-- region
CREATE TABLE IF NOT EXISTS "region" (
  "r_regionkey"  INT,
  "r_name"       INT,
  "r_comment"    INT,
  "r_dummy"      INT
  );
--   PRIMARY KEY ("r_regionkey")

-- supplier
CREATE TABLE IF NOT EXISTS "supplier" (
  "s_suppkey"     INT,
  "s_name"        INT,
  "s_address"     INT,
  "s_nationkey"   INT,
  "s_phone"       INT,
  "s_acctbal"     INT,
  "s_comment"     INT,
  "s_dummy"       INT
  );
--   PRIMARY KEY ("s_suppkey")

-- customer
CREATE TABLE IF NOT EXISTS "customer" (
  "c_custkey"     INT,
  "c_name"        INT,
  "c_address"     INT,
  "c_nationkey"   INT,
  "c_phone"       INT,
  "c_acctbal"     INT,
  "c_mktsegment"  INT,
  "c_comment"     INT,
  "c_dummy"       INT
  );
--   PRIMARY KEY ("c_custkey")

-- part
CREATE TABLE IF NOT EXISTS "part" (
  "p_partkey"     INT,
  "p_name"        INT,
  "p_mfgr"        INT,
  "p_brand"       INT,
  "p_type"        INT,
  "p_size"        INT,
  "p_container"   INT,
  "p_retailprice" INT,
  "p_comment"     INT,
  "p_dummy"       INT
  );
--   PRIMARY KEY ("p_partkey")

-- partsupp
CREATE TABLE IF NOT EXISTS "partsupp" (
  "ps_partkey"     INT,
  "ps_suppkey"     INT,
  "ps_availqty"    INT,
  "ps_supplycost"  INT,
  "ps_comment"     INT
  );
--   PRIMARY KEY ("ps_partkey")

-- orders
CREATE TABLE IF NOT EXISTS "orders" (
  "o_orderkey"       INT,
  "o_custkey"        INT,
  "o_orderstatus"    INT,
  "o_totalprice"     INT,
  "o_orderdate"      INT,
  "o_orderpriority"  INT,
  "o_clerk"          INT,
  "o_shippriority"   INT,
  "o_comment"        INT,
  "o_dummy"          INT
  );
--   PRIMARY KEY ("o_orderkey")

-- lineitem
CREATE TABLE IF NOT EXISTS "lineitem"(
  "l_orderkey"          INT,
  "l_partkey"           INT,
  "l_suppkey"           INT,
  "l_linenumber"        INT,
  "l_quantity"          INT,
  "l_extendedprice"     INT,
  "l_discount"          INT,
  "l_tax"               INT,
  "l_returnflag"        INT,
  "l_linestatus"        INT,
  "l_shipdate"          INT,
  "l_commitdate"        INT,
  "l_receiptdate"       INT,
  "l_shipinstruct"      INT,
  "l_shipmode"          INT,
  "l_comment"           INT,
  "l_dummy"             INT);
