# Contract boundary

`opto-sync-api-server.rs` consumes Opto Sync contracts; it does not author a competing wire schema.

Authoritative payload/config contracts belong in `opto-sync/opto-sync-interfaces` as independent human-authored TypeSpec and JSON Schema Draft 2020-12 peers. TJSV is the fail-closed peer-admission gate. `contract-admission/contract-ir-consumer.json` and generated Rust artifacts are downstream evidence only.

The current v1 route surface exposes the `SyncEnvelope` catalog; future mutating endpoints must preserve the protocol wire names and semantics defined by the interface authority rather than inventing route-local variants.

No application startup path may silently run server-schema migrations. Database desired-state changes are coordinated through Declarative Migrations and qualified against disposable databases.
