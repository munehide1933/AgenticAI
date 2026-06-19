# AgenticAI v1.0 (Public Product Edition)

## English

## License

This public repository is licensed under the Apache License 2.0. See [LICENSE](./LICENSE).

The Apache-2.0 license applies only to the source code and documentation included in this repository. Private commercial modules, private repositories, deployment assets, secrets, datasets, internal runbooks, production dashboards, trademarks, and external service credentials are not included and are not licensed by this repository.

See [PUBLIC_PRIVATE_STRATEGY.md](./docs/PUBLIC_PRIVATE_STRATEGY.md) for the public/private architecture boundary.

### Product Summary

AgenticAI is a multi-agent AI assistant framework for structured reasoning, technical analysis, and guided response generation.
It is designed for product-grade interaction patterns including workflow routing, streaming output, and persistent session context.

### Product Value

- Multi-step reasoning pipeline for complex user requests.
- Domain-aware behavior with configurable processing paths.
- Real-time interaction model with streaming status and content events.
- Session lifecycle management with audit-oriented data persistence.
- Extensible architecture for private/commercial capability injection.

### System Architecture

```text
Presentation Layer (Streamlit UI)
  -> Orchestration Layer (state + routing + execution lifecycle)
  -> Agent Layer (understanding/search/analysis/reflection/synthesis)
  -> Data Layer (sessions/messages/artifacts)
  -> External Services (LLM provider, web retrieval provider)
```

### Implemented Functional Scope

- Intent and domain understanding.
- Optional web retrieval flow.
- Initial and detailed analysis flows.
- Reflection-based answer refinement flow.
- Synthesis flow for structured final output.
- Session CRUD and soft-delete audit pattern.
- Encrypted content storage interface.
- Prompt organization and composition utilities.

### Processing Modes

- `Basic`: Understanding -> Analysis -> Synthesis
- `Deep Thinking`: Understanding -> Analysis -> Reflection -> Synthesis
- `Web Search`: Understanding -> Search -> Analysis -> Synthesis
- `Code-Oriented Path`: Understanding -> Analysis -> Detailed Analysis -> Code Path -> Synthesis

### Engineering Methods

- Layered architecture for maintainability and isolation.
- State-machine workflow for deterministic orchestration.
- Single-responsibility agent decomposition.
- Structured output contracts for robust downstream routing.
- Streaming event protocol (`status`, `content`, `final`) for responsive UX.
- Graceful degradation when optional external dependencies are unavailable.
- Public/private runtime extension pattern via `AGENTICAI_PRIVATE_HOOKS_MODULE`.

### Security and Governance Pattern

- Environment-based secret configuration.
- Encrypted storage interface for message/artifact content.
- Public release hardening script to exclude secrets, local data, and private assets.
- Source-available licensing and commercial boundary documentation.

### Public Product Edition Boundary

To protect proprietary implementation assets, the public release intentionally redacts:
- core orchestration internals (`core/pipeline.py`)
- workflow construction and routing internals (`workflows/builder.py`, `workflows/routers.py`)

In public release output, these files are replaced with product-safe stubs.

### Documentation

- Architecture and methods: `docs/public/IMPLEMENTATION_PATTERNS_EN_JA.md`
- Public/private policy: `docs/PUBLIC_PRIVATE_STRATEGY.md`
- Interview package templates: `docs/interview/*`

### Quick Start

```bash
uv sync
uv run streamlit run app.py
```



---

## 日本語

### 製品概要

AgenticAI は、構造化推論・技術分析・ガイド付き応答生成を目的としたマルチエージェント AI アシスタント基盤です。
ワークフロールーティング、ストリーミング応答、セッション永続化など、製品利用を意識した実装パターンを備えています。

### 提供価値

- 複雑な問い合わせに対応する多段推論パイプライン
- ドメイン判定に基づく処理分岐
- ステータス/本文のストリーミング応答
- 監査性を意識したセッション永続化
- 非公開・商用機能を追加できる拡張設計

### システムアーキテクチャ

```text
Presentation Layer (Streamlit UI)
  -> Orchestration Layer (状態管理 + ルーティング + 実行制御)
  -> Agent Layer (理解/検索/分析/反省/統合)
  -> Data Layer (セッション/メッセージ/成果物)
  -> External Services (LLM, Web 検索)
```

### 実装済み機能範囲

- 意図理解・ドメイン判定
- Web 検索フロー（任意）
- 初期分析・詳細分析フロー
- 反省（自己評価）による回答改善フロー
- 最終回答の統合フロー
- セッション CRUD と論理削除監査パターン
- 暗号化保存インターフェース
- Prompt 構成管理ユーティリティ

### 処理モード

- `Basic`: Understanding -> Analysis -> Synthesis
- `Deep Thinking`: Understanding -> Analysis -> Reflection -> Synthesis
- `Web Search`: Understanding -> Search -> Analysis -> Synthesis
- `Code-Oriented Path`: Understanding -> Analysis -> Detailed Analysis -> Code Path -> Synthesis

### 設計・実装手法

- 保守性と分離性を高めるレイヤードアーキテクチャ
- 決定性を持つ状態機械ベースのオーケストレーション
- 単一責務で分割したエージェント設計
- 下流処理を安定化する構造化出力契約
- `status` / `content` / `final` のストリーミングイベント設計
- 外部依存が使えない場合の劣化運転（Graceful Degradation）
- `AGENTICAI_PRIVATE_HOOKS_MODULE` による公開/非公開拡張方式

### セキュリティと運用ガバナンス

- 環境変数ベースの秘密情報設定
- メッセージ/成果物に対する暗号化保存インターフェース
- 公開時に秘密情報・ローカルデータを除外するハードニングスクリプト
- source-available ライセンスと商用境界の明示

### 公開版の非公開境界

独自資産を保護するため、公開版では以下を意図的に非公開にしています。
- コアオーケストレーション内部（`core/pipeline.py`）
- ワークフロー構築・ルーティング内部（`workflows/builder.py`, `workflows/routers.py`）

公開パッケージ生成時には、上記を安全なスタブ実装に置換します。

### ドキュメント

- 設計と実装方針: `docs/public/IMPLEMENTATION_PATTERNS_EN_JA.md`
- 公開/非公開ポリシー: `docs/PUBLIC_PRIVATE_STRATEGY.md`
- 資料テンプレート: `docs/interview/*`

### クイックスタート

```bash
uv sync
uv run streamlit run app.py
```

