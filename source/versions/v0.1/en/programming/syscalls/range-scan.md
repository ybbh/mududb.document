# range-scan

Purpose

Iterate over a key range or index range, producing a stream of rows.

Behavior

- Returns an iterator/stream object that the procedure can advance to fetch rows.
- Range scans honor transaction visibility and may observe a consistent snapshot depending on isolation.

Notes

- Long-running scans should yield or be paginated to avoid blocking resources.
