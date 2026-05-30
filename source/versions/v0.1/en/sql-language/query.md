# Query

MuduDB supports single-table `SELECT` queries with a `WHERE` clause for filtering rows. The query engine evaluates predicates and returns a result set to the caller.

## 3.1 Overview

A query in MuduDB is executed in the context of the current transaction. All reads are consistent with the transaction's isolation level. Results are returned as a row set that the client can iterate over.

The current query capability is intentionally scoped to single-table lookups and scans. Complex analytics, joins, and aggregations are not supported in v0.1.

## 3.2 Select

### Syntax

```sql
SELECT select_term [, select_term ...]
FROM table_name
[WHERE predicate [AND predicate ...]];
```

### Select Terms

A `select_term` is one of:

- `*` — select all columns in table order.
- `column_name` — select a single column.
- An arithmetic expression involving columns and literals (e.g., `amount * 2`, `count + 1`).

### WHERE Predicates

Each predicate has the form:

```
expression comparison_operator expression
```

**Comparison operators:**

| Operator | Meaning |
|---|---|
| `=` | Equal |
| `!=` | Not equal |
| `<` | Less than |
| `<=` | Less than or equal |
| `>` | Greater than |
| `>=` | Greater than or equal |

Predicates are combined with the `AND` logical connective only. `OR` and `NOT` are not supported in v0.1.

### Expressions

An expression can be:

- A column reference
- A numeric, string, or temporal literal
- A placeholder (`?`)
- An arithmetic expression: `+`, `-`, `*`, `/` with standard precedence

### Examples

Select all columns:

```sql
SELECT * FROM users;
```

Select specific columns with a filter:

```sql
SELECT id, name FROM users WHERE id = 1;
```

Select with multiple predicates:

```sql
SELECT ol_i_id, ol_amount
FROM order_line
WHERE ol_w_id = 1 AND ol_d_id = 2 AND ol_o_id = 100;
```

Select with placeholders (prepared statement):

```sql
SELECT * FROM stock WHERE s_w_id = ? AND s_i_id = ?;
```

Select with a reversed comparison (parser normalises the shape):

```sql
SELECT id FROM users WHERE 7 > id;
-- internally normalised to: id < 7
```

Select with an arithmetic expression in the term list:

```sql
SELECT id, amount * 2 FROM ledger WHERE id = 1;
```

## Unsupported Query Features

The following are not available in v0.1:

- `JOIN` (inner, outer, cross)
- `GROUP BY` / `HAVING`
- `ORDER BY`
- `LIMIT` / `OFFSET`
- `DISTINCT`
- Subqueries (`SELECT ... FROM (SELECT ...)`)
- Window functions
- Common Table Expressions (`WITH`)
- Set operations (`UNION`, `INTERSECT`, `EXCEPT`)
