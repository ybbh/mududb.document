# Syscalls

MuduDB procedures access database capabilities through controlled syscalls. This boundary keeps procedure execution, transaction management, and data access under kernel control.

Common capabilities include:

- opening and closing sessions
- reading one record
- writing key-value or table records
- range scans
- batch operations
- command execution

Shared semantics can be migrated from `mududb_p/doc/lang.common` into stable versioned reference pages over time.
