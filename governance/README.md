# Governance

API-server promotion is fail-closed and claim-scoped.

A check may certify only behavior exercised by code present on the exact candidate head. A model for a future endpoint is design evidence until the route/middleware/storage path exists and the model is linked to executable refinement tests.

## Mutating-route admission gate

Before any new mutating sync route is promoted, require explicit contracts and executable tests for authentication, tenant isolation, idempotent mutation identity, and version/base-revision conflict admission. Transport retry must remain distinct from application conflict/rejection semantics.

For a version/base-revision precondition, the implementation-linked qualification must prove at minimum:

- a stale or mismatched expected revision is rejected before mutation side effects;
- rejection does not advance the authoritative revision or partially write state;
- an admitted write advances the authoritative revision according to the declared contract;
- duplicate delivery/retry cannot create a second logical mutation;
- concurrent/reordered writes have an explicit conflict outcome rather than silently falling through to last-arrival wins unless LWW is the authored contract.

These are future admission requirements until a mutating route/storage path implements them.

## Contract authority

TypeSpec and Draft 2020-12 JSON Schema in `opto-sync-interfaces` remain independent authored peers. Generated OpenAPI/Contract IR/Rust code is evidence only. Peer disagreement fails closed through TJSV.

## Evidence

Do not call queued, skipped, zero-step, stale-head, billing/admission-blocked, missing-run, or historical-only checks green. Do not infer full sync correctness from health/catalog/container tests.
