# Create Table

## Syntax

```sql
CREATE TABLE table_name (
    column_definition [, column_definition ...]
    [, PRIMARY KEY (column_name [, column_name ...])]
) [PARTITION BY GLOBAL RULE rule_name REFERENCES (column_name [, column_name ...])];
```

## Examples

Single-column primary key declared inline:

```sql
CREATE TABLE item (
    i_id    INT           NOT NULL,
    i_name  VARCHAR(24)   NOT NULL,
    i_price DECIMAL(5, 2) NOT NULL,
    i_data  VARCHAR(50)   NOT NULL,
    PRIMARY KEY (i_id)
);
```

Composite primary key declared at table level:

```sql
CREATE TABLE stock (
    s_w_id       INT           NOT NULL,
    s_i_id       INT           NOT NULL,
    s_quantity   DECIMAL(4, 0) NOT NULL,
    s_ytd        DECIMAL(8, 2) NOT NULL,
    s_order_cnt  INT           NOT NULL,
    s_remote_cnt INT           NOT NULL,
    s_data       VARCHAR(50)   NOT NULL,
    PRIMARY KEY (s_w_id, s_i_id)
);
```

Table with a partition binding (the rule must have been created beforehand):

```sql
CREATE TABLE orders (
    region_id INT,
    order_id  INT,
    amount    INT,
    PRIMARY KEY (region_id, order_id)
)
PARTITION BY GLOBAL RULE r_orders REFERENCES (region_id, order_id);
```

## Partition DDL

Partition rules and placements are declared outside the table definition.

Create a range partition rule:

```sql
CREATE PARTITION RULE r_orders RANGE (
    PARTITION p0 VALUES FROM (MINVALUE, MINVALUE) TO (1000, MINVALUE),
    PARTITION p1 VALUES FROM (1000, MINVALUE) TO (MAXVALUE, MAXVALUE)
);
```

Bind partitions to workers:

```sql
CREATE PARTITION PLACEMENT FOR RULE r_orders (
    PARTITION p0 ON WORKER 11,
    PARTITION p1 ON WORKER 12
);
```
