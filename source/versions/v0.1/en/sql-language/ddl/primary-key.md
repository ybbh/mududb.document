# Primary Key

MuduDB requires every table to have a primary key. The primary key can be:

1. **Inline** — declared directly on a single column:
   ```sql
   id INT PRIMARY KEY
   ```

2. **Table-level** — declared after all columns for composite keys:
   ```sql
   PRIMARY KEY (col_a, col_b)
   ```

The primary key determines row uniqueness and, for partitioned tables, is part of the partitioning key. A column marked `PRIMARY KEY` is implicitly `NOT NULL`.
