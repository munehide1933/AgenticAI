# Public + Private Strategy

This project is split into two layers:

1. Public capability layer (this repo)
- Multi-agent orchestration
- Streamlit demo UI
- Baseline workflow and persistence
- Interview/demo materials

2. Private commercial layer (separate private repo/package)
- Cost control policies
- Enterprise auth/RBAC/billing
- Production safety policy packs
- Custom ranking/routing/IP-specific logic

## How private hooks are loaded

Public code supports optional hooks from a private package.

- Env var: `AGENTICAI_PRIVATE_HOOKS_MODULE`
- Expected exports in that module:
  - `get_private_hooks()` factory, or
  - `PrivateHooks` class

Hook methods (all optional):
- `enrich_initial_state(state) -> state`
- `after_workflow(state) -> state`
- `mutate_response(response, state=...) -> response`

If private hooks are missing or fail, the app falls back to no-op behavior.

## Recommended repo split

Keep this repo public:
- `agents/`, `core/`, `workflows/`, `ui/` (baseline)
- `docs/interview/*`

Keep private repo:
- `agenticai_private/*` commercial logic
- deployment/infrastructure configs
- billing and tenant management
- internal runbooks and production SLO dashboards

## Public release checklist

- Ensure `.env` and keys are excluded by `.gitignore`
- Keep `config/.encryption_key` out of VCS
- Run a quick smoke test in public mode
- Verify no private package paths are committed
- Ensure release script replaced `README.md` with EN/JA version
- Ensure release script replaced core internals with public stubs

## Licensing Boundary

The code and documentation included in this public repository are licensed under the Apache License 2.0, unless otherwise noted.

The Apache-2.0 license applies only to files actually included in this repository. It does not grant rights to private repositories, private packages, excluded implementation assets, deployment infrastructure, secrets, credentials, datasets, internal runbooks, production dashboards, trademarks, or commercial service offerings.

The private commercial layer described in this document is not included in this repository and is not licensed by this repository.

The `AGENTICAI_PRIVATE_HOOKS_MODULE` interface is an extension boundary. It documents how private hooks may be loaded, but it does not grant access to or rights in any private implementation.
