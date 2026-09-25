# Conformance

Conformance must exercise the API server that exists on the candidate head. Current evidence includes the Rust build/tests, container/argv checks, source-policy checks, and TypeSpec/JSON-Schema peer-authority admission already wired in `.github/workflows/`.

The present v1 route implementation exposes a catalog entry for `SyncEnvelope`; it does not yet implement a general mutating sync endpoint with authenticated tenant/idempotency/version-precondition admission. Therefore that proposed admission rule is a **future design gate**, not current implementation conformance.

When mutating routes land, their conformance suite must exercise at minimum:

- authenticated versus anonymous/degraded identity;
- tenant binding and cross-tenant refusal;
- stable idempotency/mutation identity and duplicate delivery;
- version/base-revision preconditions and stale clients;
- explicit conflict/rejection responses distinct from transport retry;
- replay after lost acknowledgement without double application.

Only exact-head, actually executed, stepful green evidence counts. Queued, skipped, zero-step, stale-head, billing/admission-blocked, missing-run, and historical-only results do not.
