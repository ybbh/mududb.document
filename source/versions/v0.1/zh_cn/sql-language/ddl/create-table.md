# 创建表

## 语法

```sql
CREATE TABLE table_name (
    column_definition [, column_definition ...]
    [, PRIMARY KEY (column_name [, column_name ...])]
) [PARTITION BY GLOBAL RULE rule_name REFERENCES (column_name [, column_name ...])];
```

## 示例

单列主键行内声明：

```sql
CREATE TABLE item (
    i_id    INT           NOT NULL,
    i_name  VARCHAR(24)   NOT NULL,
    i_price DECIMAL(5, 2) NOT NULL,
    i_data  VARCHAR(50)   NOT NULL,
    PRIMARY KEY (i_id)
);
```

复合主键在表级别声明：

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

带分区绑定的表（规则必须预先创建）：

```sql
CREATE TABLE orders (
    region_id INT,
    order_id  INT,
    amount    INT,
    PRIMARY KEY (region_id, order_id)
)
PARTITION BY GLOBAL RULE r_orders REFERENCES (region_id, order_id);
```

## 分区 DDL

分区规则和放置位置在表定义之外声明。

创建范围分区规则：

```sql
CREATE PARTITION RULE r_orders RANGE (
    PARTITION p0 VALUES FROM (MINVALUE, MINVALUE) TO (1000, MINVALUE),
    PARTITION p1 VALUES FROM (1000, MINVALUE) TO (MAXVALUE, MAXVALUE)
);
```

将分区绑定到工作节点：

```sql
CREATE PARTITION PLACEMENT FOR RULE r_orders (
    PARTITION p0 ON WORKER 11,
    PARTITION p1 ON WORKER 12
);
```
