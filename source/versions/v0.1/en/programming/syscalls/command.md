# command

Purpose

Execute an arbitrary SQL command or runtime command string.

Behavior

- Sends a single SQL statement or command to the kernel for execution and returns results or status.
- Commands may be subject to parameterization, authorization, and transactional rules.

Notes

- Prefer typed syscall primitives for structured access when available; command is useful for free-form SQL and administrative operations.
