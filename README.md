# AgenticAI v1.0

Public Product Edition

## License

This public repository is licensed under the Apache License 2.0. See [LICENSE](./LICENSE).

The Apache-2.0 license applies only to the source code and documentation included in this repository.

Private commercial modules, private repositories, deployment assets, secrets, credentials, datasets, local data, internal runbooks, production dashboards, customer-specific implementation assets, trademarks, and external service credentials are not included and are not licensed by this repository.

See [PUBLIC_PRIVATE_STRATEGY.md](./docs/PUBLIC_PRIVATE_STRATEGY.md) for the public/private architecture boundary.

---

# English

## Product Summary

AgenticAI is a multi-agent AI assistant framework for structured reasoning, technical analysis, and guided response generation.

It is designed for product-grade interaction patterns including workflow routing, streaming output, persistent session context, audit-oriented data persistence, and optional private extension points.

This public repository is a public product edition. It demonstrates the architecture, engineering methods, interaction model, and extension boundary while keeping proprietary commercial implementation assets outside this repository.

## Product Value

* Multi-step reasoning pipeline for complex user requests
* Domain-aware behavior with configurable processing paths
* Real-time interaction model with streaming status and content events
* Session lifecycle management with audit-oriented data persistence
* Extensible architecture for optional private/commercial capability injection outside this public repository
* Public/private split that keeps the public layer reviewable while protecting proprietary commercial internals

## System Architecture

```text
Presentation Layer (Streamlit UI)
  -> Orchestration Layer (state + routing + execution lifecycle)
  -> Agent Layer (understanding/search/analysis/reflection/synthesis)
  -> Data Layer (sessions/messages/artifacts)
  -> External Services (LLM provider, web retrieval provider)
```

## Implemented Functional Scope

* Intent and domain understanding
* Optional web retrieval flow
* Initial and detailed analysis flows
* Reflection-based answer refinement flow
* Synthesis flow for structured final output
* Session CRUD and soft-delete audit pattern
* Encrypted content storage interface
* Prompt organization and composition utilities
* Public/private runtime extension interface

## Processing Modes

```text
Basic:
Understanding -> Analysis -> Synthesis

Deep Thinking:
Understanding -> Analysis -> Reflection -> Synthesis

Web Search:
Understanding -> Search -> Analysis -> Synthesis

Code-Oriented Path:
Understanding -> Analysis -> Detailed Analysis -> Code Path -> Synthesis
```

## Engineering Methods

* Layered architecture for maintainability and isolation
* State-machine workflow pattern for deterministic orchestration
* Single-responsibility agent decomposition
* Structured output contracts for robust downstream routing
* Streaming event protocol with `status`, `content`, and `final` events for responsive UX
* Graceful degradation when optional external dependencies are unavailable
* Public/private runtime extension pattern via `AGENTICAI_PRIVATE_HOOKS_MODULE`
* Apache-2.0 public-layer licensing with explicit private commercial boundary documentation

## Security and Governance Pattern

* Environment-based secret configuration
* Encrypted storage interface for message and artifact content
* Public release hardening process to exclude secrets, local data, and private assets
* Public/private repository split for commercial logic and production operations
* Public-safe stubs for proprietary orchestration and routing internals

## Public Product Edition Boundary

This public repository intentionally excludes proprietary commercial implementation assets.

To protect private implementation details, the public release may replace the following internals with product-safe stubs:

* Core orchestration internals: `core/pipeline.py`
* Workflow construction internals: `workflows/builder.py`
* Workflow routing internals: `workflows/routers.py`

The public stubs are intended to preserve the repository structure, demonstrate extension points, and support public review without exposing private commercial logic.

The private commercial layer may include cost control, enterprise authentication, RBAC, billing, production safety policy packs, proprietary routing/ranking logic, deployment infrastructure, internal runbooks, and production observability assets.

Those private assets are not included in this repository and are not licensed by this repository.

## Private Extension Boundary

The public code supports optional private hooks through:

```text
AGENTICAI_PRIVATE_HOOKS_MODULE
```

Expected private module exports:

* `get_private_hooks()` factory, or
* `PrivateHooks` class

Supported optional hook methods:

* `enrich_initial_state(state) -> state`
* `after_workflow(state) -> state`
* `mutate_response(response, state=...) -> response`

If private hooks are missing, unavailable, or fail to load, the application falls back to no-op behavior.

## Documentation

* Architecture and implementation patterns: `docs/public/IMPLEMENTATION_PATTERNS_EN_JA.md`
* Public/private policy: `docs/PUBLIC_PRIVATE_STRATEGY.md`
* Interview package templates: `docs/interview/*`

## Quick Start

```bash
uv sync
uv run streamlit run app.py
```

---

# 日本語

## 製品概要

AgenticAI は、構造化推論、技術分析、ガイド付き応答生成を目的としたマルチエージェント AI アシスタント基盤です。

ワークフロールーティング、ストリーミング応答、セッション永続化、監査性を意識したデータ保存、任意の非公開拡張ポイントなど、製品利用を意識した実装パターンを備えています。

この公開リポジトリは Public Product Edition です。アーキテクチャ、設計・実装手法、インタラクションモデル、拡張境界を示す一方で、独自の商用実装資産はこのリポジトリの外に保持します。

## 提供価値

* 複雑な問い合わせに対応する多段推論パイプライン
* ドメイン判定に基づく処理分岐
* ステータスと本文のリアルタイムストリーミング応答
* 監査性を意識したセッションライフサイクル管理
* この公開リポジトリの外側で非公開・商用機能を追加できる拡張設計
* 公開レビュー可能なレイヤーと独自商用実装を分離する公開/非公開構成

## システムアーキテクチャ

```text
Presentation Layer (Streamlit UI)
  -> Orchestration Layer (状態管理 + ルーティング + 実行制御)
  -> Agent Layer (理解/検索/分析/反省/統合)
  -> Data Layer (セッション/メッセージ/成果物)
  -> External Services (LLM, Web 検索)
```

## 実装済み機能範囲

* 意図理解・ドメイン判定
* 任意の Web 検索フロー
* 初期分析・詳細分析フロー
* 反省、自己評価による回答改善フロー
* 構造化された最終回答の統合フロー
* セッション CRUD と論理削除監査パターン
* メッセージ/成果物に対する暗号化保存インターフェース
* Prompt 構成管理ユーティリティ
* 公開/非公開ランタイム拡張インターフェース

## 処理モード

```text
Basic:
Understanding -> Analysis -> Synthesis

Deep Thinking:
Understanding -> Analysis -> Reflection -> Synthesis

Web Search:
Understanding -> Search -> Analysis -> Synthesis

Code-Oriented Path:
Understanding -> Analysis -> Detailed Analysis -> Code Path -> Synthesis
```

## 設計・実装手法

* 保守性と分離性を高めるレイヤードアーキテクチャ
* 決定性を持つ状態機械ベースのワークフローパターン
* 単一責務で分割したエージェント設計
* 下流処理を安定化する構造化出力契約
* `status`、`content`、`final` イベントによるストリーミングイベント設計
* 外部依存が利用できない場合の劣化運転
* `AGENTICAI_PRIVATE_HOOKS_MODULE` による公開/非公開ランタイム拡張方式
* Apache-2.0 による公開レイヤーのライセンスと、非公開商用レイヤーの境界の明示

## セキュリティと運用ガバナンス

* 環境変数ベースの秘密情報設定
* メッセージ/成果物に対する暗号化保存インターフェース
* 秘密情報、ローカルデータ、非公開資産を除外する公開リリース用ハードニングプロセス
* 商用ロジックと本番運用資産を分離する公開/非公開リポジトリ構成
* 独自のオーケストレーションおよびルーティング内部を保護する公開用スタブ

## Public Product Edition の境界

この公開リポジトリでは、独自の商用実装資産を意図的に含めていません。

非公開の実装詳細を保護するため、公開版では以下の内部実装が product-safe なスタブに置き換えられる場合があります。

* コアオーケストレーション内部: `core/pipeline.py`
* ワークフロー構築内部: `workflows/builder.py`
* ワークフロールーティング内部: `workflows/routers.py`

公開用スタブは、リポジトリ構造、拡張ポイント、設計方針を示すためのものであり、非公開の商用ロジックを公開するものではありません。

非公開の商用レイヤーには、コスト制御、エンタープライズ認証、RBAC、課金、プロダクション安全性ポリシー、独自ルーティング/ランキングロジック、デプロイ基盤、内部 runbook、本番監視資産などが含まれる場合があります。

これらの非公開資産はこのリポジトリには含まれておらず、このリポジトリによってライセンスされるものではありません。

## 非公開拡張境界

公開コードは、以下の環境変数を通じて任意の非公開 hooks を読み込める設計になっています。

```text
AGENTICAI_PRIVATE_HOOKS_MODULE
```

想定される非公開モジュールの export:

* `get_private_hooks()` factory
* `PrivateHooks` class

対応する任意 hook method:

* `enrich_initial_state(state) -> state`
* `after_workflow(state) -> state`
* `mutate_response(response, state=...) -> response`

非公開 hooks が存在しない場合、利用できない場合、または読み込みに失敗した場合、アプリケーションは no-op 動作にフォールバックします。

## ドキュメント

* 設計と実装方針: `docs/public/IMPLEMENTATION_PATTERNS_EN_JA.md`
* 公開/非公開ポリシー: `docs/PUBLIC_PRIVATE_STRATEGY.md`
* 面接・説明用テンプレート: `docs/interview/*`

## クイックスタート

```bash
uv sync
uv run streamlit run app.py
```
