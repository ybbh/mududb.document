# The SQL Language

MuduDB uses a SQL dialect parsed by a tree-sitter grammar tailored to its storage and execution model. The dialect covers DDL for schema definition, DML for data mutation, and SELECT for single-table queries. This section describes each category, the syntax MuduDB accepts, and the limits of what is currently supported.

```{toctree}
:maxdepth: 2

ddl/index
dml/index
query
data_types/index
```
