---
title: "Claude Code MCP設定方法5分完全ガイド2026"
description: "Claude CodeでMCPサーバーを接続する手順を5分で完了。設定ファイルの書き方、よく使う3つのサーバー例、つまずきやすい認証エラーの対処法まで実例付きで解説。"
pubDate: 2026-05-16
category: "Claude活用"
tags: ["Claude Code", "MCP", "AI開発", "設定方法"]
keyword: "claude code mcp 設定 方法"
draft: false
image: "/auto-blog/ogp/claude-code-mcp設定方法5分完全ガイド2026.png"
---

Claude Codeを使い始めて「MCPサーバーって何？どう設定するの？」と止まっている人は多い。公式ドキュメントを読んでも専門用語が多く、結局どのファイルをどう編集すればいいのか分からないまま放置している――そんな状態に心当たりがあるなら、この記事で一気に解決できる。

ここではClaude Code（Anthropic公式CLIツール）にMCP（Model Context Protocol）サーバーを接続する具体的な手順を、コピペで動く形でまとめた。所要時間は5分。設定ファイルの書き方、よく使う3つの実用サーバー、エラーが出たときの切り分け方まで一通り押さえる。

結論：MCP設定は「設定ファイルにJSONを追記」→「Claude Codeを再起動」の2ステップで終わる。難しさの99%は「どこに何を書くか」を知らないだけだ。

## そもそもMCPとは何か、なぜ設定するのか

<!-- INLINE_IMG -->
![Claude Code MCP設定方法5分完全ガイド2026 - そもそもMCPとは何か、なぜ設定するのか](/auto-blog/inline-images/claude-code-mcp-5-2026-0.jpg)


MCP（Model Context Protocol）はAnthropicが2024年末に公開したオープン規格で、AIアシスタントと外部ツール・データソースを安全に接続するための共通プロトコルだ。Claude CodeにMCPサーバーを設定すると、Claudeが「自分のPC内のファイル」「GitHubリポジトリ」「データベース」「Slack」などに直接アクセスして作業できるようになる。

設定しない状態のClaude Codeは、基本的に現在のディレクトリ内のファイル操作とBashコマンド実行までしかできない。MCPを足すと、たとえば次のようなことが一気に可能になる。

- GitHubのIssue一覧を取得して、優先度別に整理した上で対応コードを書かせる
- ローカルのPostgreSQLに接続し、テーブル構造を見ながらSQLを生成・実行
- Slackの過去スレッドを検索して、要約と次のアクションを提案
- Figmaのデザインデータを読み取り、そのままReactコンポーネント化

要するに「Claudeにできることの上限を引き上げる仕組み」だ。海外のRedditでも、MCPを使い始めた開発者は「もはやMCPなしのClaude Codeには戻れない」という反応が圧倒的に多い。




<aside class="affiliate-card">
<div class="label">Claude Pro に関連する書籍・ツール</div>
<p>「Claude Pro」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://search.rakuten.co.jp/search/mall/Claude%20Pro/" target="_blank" rel="sponsored noopener">▶ 楽天市場で「Claude Pro」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=Claude%20Pro" target="_blank" rel="sponsored noopener">▶ Amazonで「Claude Pro」関連を見る</a></p>
</aside>




## 設定ファイルの場所と基本構造

<!-- INLINE_IMG -->
![Claude Code MCP設定方法5分完全ガイド2026 - 設定ファイルの場所と基本構造](/auto-blog/inline-images/claude-code-mcp-5-2026-1.jpg)


Claude CodeのMCP設定は、ユーザーホーム直下の設定ファイルに記述する。具体的なパスはOSごとに異なる。

- **macOS / Linux**: `~/.claude/claude_desktop_config.json` または `~/.config/claude/config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

プロジェクト単位でMCPを切り替えたい場合は、プロジェクトルートに `.mcp.json` を置く方法もある。チーム開発ならこちらを使い、Gitで共有するのが定番だ。

基本的なJSONの骨格は次の通り。

```json
{
  "mcpServers": {
    "サーバー名": {
      "command": "実行コマンド",
      "args": ["引数1", "引数2"],
      "env": {
        "API_KEY": "値"
      }
    }
  }
}
```

`mcpServers` の中に、接続したいサーバーを名前付きで並べていくだけ。`command` は実行ファイル（多くは `npx` か `uvx`）、`args` はそのコマンドへの引数、`env` は環境変数。書式はこれだけ覚えれば9割応用できる。

注意点として、JSONはカンマの位置とダブルクォートに厳格だ。シングルクォートや末尾カンマがあると起動時にエラーになる。編集後は必ずVS Codeなどのエディタで構文チェックを通してから保存する習慣をつけたい。

## 実用度が高いMCPサーバー3選と設定例

数あるMCPサーバーの中から、最初に入れておくと作業効率が一気に変わる3つを紹介する。

### 1. Filesystem（ファイルシステム）

指定したディレクトリ配下を、Claudeが自由に読み書きできるようになる。Claude Codeの作業ディレクトリの外にあるドキュメントやメモにアクセスさせたいときに必須。

```json
"filesystem": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "/Users/yourname/Documents"
  ]
}
```

### 2. GitHub

Issue、PR、リポジトリの内容を直接操作できる。Personal Access Tokenを発行して環境変数に入れる。

```json
"github": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-github"],
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxxxxxxxxxxx"
  }
}
```

### 3. Postgres

接続文字列を渡すだけで、Claudeがスキーマを把握しSQLを書いて実行する。

```json
"postgres": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-postgres",
    "postgresql://user:pass@localhost:5432/dbname"
  ]
}
```

3つとも `npx` で動くため、Node.js（v18以降推奨）が入っていれば追加インストール不要で立ち上がる。Python製のサーバーを使う場合は `uvx` コマンドに置き換える。




<aside class="affiliate-card">
<div class="label">Cursor に関連する書籍・ツール</div>
<p>「Cursor」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://search.rakuten.co.jp/search/mall/Cursor/" target="_blank" rel="sponsored noopener">▶ 楽天市場で「Cursor」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=Cursor" target="_blank" rel="sponsored noopener">▶ Amazonで「Cursor」関連を見る</a></p>
</aside>




## 設定後の確認とよくあるエラーの切り分け

設定ファイルを保存したら、Claude Codeを完全に再起動する。ターミナルで動かしている場合は一度終了し、`claude` コマンドで再度起動。再起動後、対話画面で `/mcp` と入力するとロード済みのサーバー一覧が表示される。

ここで詰まる代表的な3パターンと対処法をまとめる。

**パターン1：サーバーがリストに出てこない**
JSONの構文エラーが原因のことが大半。`jq . ~/.claude/claude_desktop_config.json` を実行して、エラーが出れば該当箇所を修正する。`jq` が無ければ、VS Codeで開いて赤線が出る場所を確認する。

**パターン2：「connection refused」や認証エラー**
APIキーやアクセストークンの誤りが主因。GitHub MCPなら、トークンに `repo` スコープが付与されているかを `https://github.com/settings/tokens` で確認する。Postgresなら、接続文字列のユーザー名・パスワード・ポート番号を再点検。

**パターン3：`command not found: npx`**
Node.jsが入っていない、もしくはPATHが通っていない。`node -v` で確認し、未インストールなら公式サイトかnvmで導入する。Mac環境で `nvm use` を使っている場合、Claude Codeを起動するシェル環境にもバージョンが反映されているかを必ず見ること。

ログを直接見たい場合は、`~/Library/Logs/Claude/mcp*.log`（macOS）や `%APPDATA%\Claude\logs\`（Windows）に出力されている。エラーメッセージは詳細に書かれているので、原因特定はここを開けばほぼ片付く。

## まとめ：MCP設定はAI開発の生産性を倍にする入口

Claude CodeのMCP設定は「設定ファイルのパスを知る」「JSONを正しく書く」「再起動する」の3点が全て。一度通れば、その後は新しいサーバーをコピペで追加するだけだ。

最初はFilesystemとGitHubの2つから始めて、慣れたらPostgresやSlack、Figmaなど業務に必要なものを足していくのが現実的なロードマップ。MCPを使いこなせるかどうかで、Claude Codeの戦闘力は文字通り倍以上変わる。今日の5分の投資が、来週以降の作業時間を確実に短縮してくれるはずだ。

## 関連記事

- [Claude Code MCPおすすめ7選2026年最新版](/auto-blog/blog/claude-code-mcpおすすめ7選2026年最新版/)
- [Claude Codeおすすめスキル7選｜2026年版作業効率化](/auto-blog/blog/claude-codeおすすめスキル7選2026年版作業効率化/)
- [Claude Codeおすすめターミナル7選｜2026年最新比較](/auto-blog/blog/claude-codeおすすめターミナル7選2026年最新比較/)

<!-- CROSS_LINKS -->
## 他サイトの最新AI記事

- [Claude Code利用者がGit pushで救われた話 - バージョン管理がAI開発で必須な理由](https://nayo126.github.io/ai-news-jp/posts/claude-code-git-push---ai.html)
- [Sea LimitedがOpenAI Codexを全社導入、アジア発のエージェント型開発を加速](https://nayo126.github.io/ai-news-jp/posts/sea-limited-openai-codex.html)
- [Claude Codeが1時間連続編集？AIコーディング長時間自律作業の実態と注意点](https://nayo126.github.io/ai-news-jp/posts/claude-code-1-ai.html)

<!-- SEO_MESH_START -->

## 関連する記事

- [Claude Code MCPおすすめ7選2026年最新版](https://nayo126.github.io/auto-blog/blog/claude-code-mcpおすすめ7選2026年最新版/)
- [Claude Codeおすすめスキル7選｜2026年版作業効率化](https://nayo126.github.io/auto-blog/blog/claude-codeおすすめスキル7選2026年版作業効率化/)
- [bolt.new vs v0徹底比較2026年版｜個人開発で稼ぐ最適解](https://nayo126.github.io/auto-blog/blog/boltnew-vs-v0徹底比較2026年版個人開発で稼ぐ最適解/)

### 姉妹サイトの関連記事
- [Claude Code利用者がGit pushで救われた話 - バージョン管理がAI開発で必須な理由](https://nayo126.github.io/ai-news-jp/posts/claude-code-git-push---ai.html) — AI News JP
- [Sea LimitedがOpenAI Codexを全社導入、アジア発のエージェント型開発を加速](https://nayo126.github.io/ai-news-jp/posts/sea-limited-openai-codex.html) — AI News JP
- [ChatGPTにコードを貼ったら欠陥3つ即指摘されるReddit投稿が話題](https://nayo126.github.io/ai-news-jp/posts/chatgpt-3-reddit.html) — AI News JP

<!-- SEO_MESH_END -->
