# Implementation Patterns (EN / JA)

## English

This document summarizes architecture patterns and implementation methods without exposing private source internals.

### 1) Layered Architecture
- `UI Layer`: user interaction and streaming rendering
- `Orchestration Layer`: state transitions and execution lifecycle
- `Agent Layer`: intent understanding, search, analysis, synthesis
- `Data Layer`: session persistence and encrypted message storage

### 2) State Machine Workflow Pattern
- A typed state object carries context across steps.
- Nodes are isolated by responsibility.
- Routing is condition-driven (domain/mode/capability flags).
- Failure paths map to explicit error outputs.

### 3) Agent Composition Pattern
- Each agent has one primary responsibility.
- Input context is normalized before model invocation.
- Structured outputs are preferred for machine-readable routing.
- Synthesis combines intermediate outputs into final user output.

### 4) Streaming UX Pattern
- Status events are emitted before expensive steps.
- Content chunks stream incrementally.
- Final metadata is attached at completion.

### 5) Reliability Methods
- Parse fallbacks for model output robustness.
- Optional external dependency behavior (graceful degradation).
- Session-level tracing metadata and rotating logs.

### 6) Public/Private Split Method
- Public repo keeps architecture and base implementation examples.
- Proprietary logic is injected from private packages via runtime hooks.
- Release pipeline strips keys/db/artifacts and replaces private modules with stubs.

## 日本語

本ドキュメントは、非公開ソースを開示せずに、設計パターンと実装方針を説明するためのものです。

### 1) レイヤードアーキテクチャ
- `UI Layer`: ユーザー操作とストリーミング表示
- `Orchestration Layer`: 状態遷移と実行ライフサイクル
- `Agent Layer`: 意図理解・検索・分析・統合
- `Data Layer`: セッション永続化と暗号化メッセージ保存

### 2) 状態機械ワークフローパターン
- 型付き状態オブジェクトで文脈を各ステップへ伝播
- ノードごとに責務を分離
- ドメイン/モード/フラグに基づく条件ルーティング
- 失敗経路を明示的なエラー出力にマッピング

### 3) エージェント合成パターン
- 各エージェントは単一責務を持つ
- モデル呼び出し前に入力文脈を正規化
- ルーティングしやすい構造化出力を優先
- 中間結果を統合して最終回答を生成

### 4) ストリーミング UX パターン
- 重い処理の前にステータスイベントを送出
- コンテンツをチャンクで段階的に配信
- 完了時にメタデータを付与

### 5) 信頼性向上の実装方法
- モデル出力パースのフォールバック
- 外部依存の劣化運転（Graceful Degradation）
- セッション単位のトレース情報とローテーションログ

### 6) 公開/非公開分離の方法
- 公開リポジトリには設計と基礎実装例を保持
- 独自ロジックは実行時フックで非公開パッケージから注入
- リリース時に鍵/DB/成果物を除外し、非公開モジュールをスタブへ差し替え

