# Public + Private Strategy

This project is split into two layers:

## Public Capability Layer

This public repository contains the product-safe public capability layer of AgenticAI.

The public layer includes:

* Baseline multi-agent interfaces
* Product-safe orchestration stubs and workflow patterns
* Streamlit demo UI
* Baseline session, message, and artifact persistence patterns
* Prompt organization and composition utilities
* Interview/demo materials
* Public architecture and implementation-pattern documentation

This layer is intended to demonstrate the product architecture, engineering approach, interaction model, and extension boundary without exposing proprietary commercial internals.

## Private Commercial Layer

The private commercial layer is maintained separately in a private repository or private package.

The private layer may include:

* Cost control policies
* Enterprise authentication, RBAC, billing, and tenant management
* Production safety policy packs
* Custom ranking, routing, and domain-specific logic
* Proprietary workflow construction and orchestration internals
* Deployment and infrastructure configurations
* Internal runbooks, observability assets, and production SLO dashboards
* Customer-specific or business-specific implementation assets

These private assets are not included in this public repository.

## Private Hook Loading Pattern

The public code supports optional hooks from a private package through an environment-based extension boundary.

Environment variable:

`AGENTICAI_PRIVATE_HOOKS_MODULE`

Expected exports in the private hooks module:

* `get_private_hooks()` factory, or
* `PrivateHooks` class

Supported hook methods are optional:

* `enrich_initial_state(state) -> state`
* `after_workflow(state) -> state`
* `mutate_response(response, state=...) -> response`

If private hooks are missing, unavailable, or fail to load, the application falls back to no-op behavior.

This allows the public repository to remain runnable in public mode while supporting private commercial extensions outside this repository.

## Recommended Repository Split

Keep this public repository focused on:

* `agents/` public-safe agent interfaces and baseline implementations
* `core/` public-safe core interfaces and stubs
* `workflows/` public-safe workflow interfaces and stubs
* `ui/` Streamlit demo UI
* `docs/public/*`
* `docs/interview/*`

Keep the following in a private repository or private package:

* `agenticai_private/*`
* Commercial routing and ranking logic
* Enterprise authentication, RBAC, billing, and tenant management
* Deployment and infrastructure configurations
* Internal runbooks
* Production observability assets
* Production SLO dashboards
* Customer-specific implementation assets
* Proprietary policy packs and operational logic

## Public Release Checklist

Before publishing or updating the public repository, verify the following:

* `.env` files are excluded by `.gitignore`
* API keys, tokens, credentials, and secrets are not committed
* `config/.encryption_key` is excluded from version control
* Local databases, generated artifacts, logs, and archives are excluded
* Private package paths and private import paths are not committed
* Public mode runs without the private hooks package
* A quick smoke test has been completed in public mode
* Public release scripts have replaced private orchestration internals with public-safe stubs
* Public release scripts have replaced private workflow routing internals with public-safe stubs
* README and public documentation describe the repository as a public product edition
* Git history has been reviewed for secrets, private code, local data, and proprietary configs before publication

## Licensing Boundary

The code and documentation included in this public repository are licensed under the Apache License 2.0, unless otherwise noted.

The Apache-2.0 license applies only to files actually included in this repository.

The Apache-2.0 license does not grant rights to:

* Private repositories
* Private packages
* Excluded implementation assets
* Deployment or infrastructure assets not included in this repository
* Secrets, credentials, API keys, or environment files
* Local databases, generated data, logs, or archives
* Internal runbooks
* Production dashboards or observability assets
* Customer-specific implementation assets
* Proprietary policy packs
* Trademarks, product names, or brand assets
* External model providers, API services, or third-party services

The private commercial layer described in this document is not included in this repository and is not licensed by this repository.

The `AGENTICAI_PRIVATE_HOOKS_MODULE` interface is an extension boundary. It documents how private hooks may be loaded, but it does not grant access to or rights in any private implementation.

## Apache-2.0 Public Layer

The public layer may be used, modified, and redistributed under the terms of the Apache License 2.0.

Commercial access to any separate private extension layer, hosted product, enterprise feature set, deployment package, customer-specific implementation, or proprietary service offering is outside the scope of this public repository.
