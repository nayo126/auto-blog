---
title: "Claude MCP設定方法を15分で完了する2026最新手順"
description: "Claude MCP（Model Context Protocol）の設定方法を初心者向けに解説。Claude Desktop/Codeでの導入手順、おすすめサーバー5選、トラブル対処までまとめました。"
pubDate: 2026-05-17
category: "Claude活用"
tags: ["Claude", "MCP", "AI副業", "Claude Desktop"]
keyword: "claude mcp 設定 方法"
draft: false
image: "/auto-blog/ogp/claude-mcp設定方法を15分で完了する2026最新手順.png"
---

「Claude MCPを使えば作業が爆速になる」と聞いて設定しようとしたものの、公式ドキュメントが英語で挫折した――そんな経験はないでしょうか。

JSONの編集、サーバーの追加、再起動してもツールが表示されない。初めて触る人がつまずく場所はだいたい同じです。

この記事では、Claude MCPの設定方法を「ゼロから15分で完了する手順」に絞って解説します。Claude DesktopとClaude Codeの両方に対応し、つまずきやすいポイントは先回りで潰しています。

## Claude MCPとは？設定する前に知っておきたい基本

<!-- INLINE_IMG -->
![Claude MCP設定方法を15分で完了する2026最新手順 - Claude MCPとは？設定する前に知っておきたい基本](/auto-blog/inline-images/claude-mcp-15-2026--0.jpg)


結論：MCP（Model Context Protocol）はAnthropicが2024年11月に公開した規格で、Claudeを外部ツールやデータと接続するための共通プロトコルです。

これまでClaudeに「自分のNotionを読ませる」「ローカルファイルを操作させる」といった連携をするには、個別のAPI実装が必要でした。MCPはこの連携を「サーバー」という単位で標準化し、設定ファイル一つで複数のツールを横断できるようにします。

### MCPで何ができるのか

主な用途は次の3つです。

- **ローカルファイル操作**：デスクトップやドキュメントフォルダの読み書き
- **外部サービス連携**：GitHub、Notion、Slack、Google Driveなど
- **DB・API接続**：PostgreSQL、SQLite、任意のREST API

副業文脈で言えば、「クライアント案件の資料を全てClaudeに読み込ませて議事録を自動生成」「リサーチ結果をそのままNotionに保存」といったワークフローが、コードを書かずに組めます。

### Claude DesktopとClaude Codeの違い

MCPはClaude DesktopアプリとClaude Code（CLI）の両方で利用できますが、設定ファイルの場所と書き方が微妙に異なります。Desktopは`claude_desktop_config.json`、Claude Codeは`.mcp.json`またはCLIコマンドで管理する点を、まず押さえておきましょう。





<aside class="affiliate-card">
<div class="label">Claude Pro に関連する書籍・ツール</div>
<p>「Claude Pro」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FClaude%2520Pro%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「Claude Pro」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=Claude%20Pro" target="_blank" rel="sponsored noopener">▶ Amazonで「Claude Pro」関連を見る</a></p>
</aside>





## Claude Desktop での MCP 設定方法（5ステップ）

<!-- INLINE_IMG -->
![Claude MCP設定方法を15分で完了する2026最新手順 - Claude Desktop での MCP 設定方法（5ステップ）](/auto-blog/inline-images/claude-mcp-15-2026--1.jpg)


結論：Claude DesktopでのMCP設定は、設定ファイルにサーバー情報をJSONで追記してアプリを再起動するだけです。

### ステップ1：設定ファイルの場所を開く

OS別の設定ファイルパスは次の通りです。

- **macOS**：`~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**：`%APPDATA%\Claude\claude_desktop_config.json`

Claude Desktopを起動し、メニューバーの「Claude」→「Settings」→「Developer」タブ→「Edit Config」をクリックすると、該当のJSONファイルが直接開きます。手動でパスを辿るより確実です。

### ステップ2：mcpServers セクションを記述する

ファイルが空、または`{}`のみの場合は次のテンプレートを貼り付けます。

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/yourname/Documents"
      ]
    }
  }
}
```

`/Users/yourname/Documents`の部分は、Claudeにアクセスを許可したいフォルダの絶対パスに置き換えてください。

### ステップ3：Node.jsの導入確認

`npx`コマンドが必要なので、Node.jsがインストールされていない場合は[公式サイト](https://nodejs.org/)からLTS版を入れます。`node -v`でバージョンが表示されればOKです。

### ステップ4：Claude Desktopを完全に再起動

メニューから「Quit Claude」を選び、アプリを完全終了してから再起動します。ウィンドウを閉じるだけでは設定が反映されません。

### ステップ5：接続確認

入力欄の左下に「🔨」アイコンが表示されていれば成功です。クリックするとMCPサーバーが提供するツール一覧が確認できます。

## Claude Code での MCP 設定方法

結論：Claude Code（CLI）ではコマンド一発でサーバーを追加できるため、JSONを手で書く必要はほぼありません。

### CLI コマンドでサーバーを追加

ターミナルで以下を実行します。

```bash
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem /Users/yourname/Documents
```

`--`の後ろが実行コマンドになります。追加後、`claude mcp list`で登録済みサーバーを確認できます。

### スコープの使い分け

Claude Codeでは3種類のスコープが選べます。

- **local**（デフォルト）：自分のマシンのみ
- **project**：`.mcp.json`としてプロジェクトに保存、チーム共有可能
- **user**：全プロジェクトで共有

チームで使う場合は`-s project`オプションを付けると、リポジトリにコミットして共有できます。

## 入れておきたいMCPサーバー5選

結論：用途別に必要なものだけ入れるのがコツで、最初から大量に入れると起動が重くなります。

- **filesystem**：ローカルファイル操作の定番。Anthropic公式
- **github**：Issue・PR・コード検索を直接実行
- **postgres**：データベースに自然言語でクエリ
- **brave-search**：Web検索（APIキー要、無料枠2000回/月）
- **memory**：Claudeに長期記憶を持たせる

公式のMCPサーバー一覧は[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)で随時更新されています。サードパーティ製も含めると100以上の選択肢があります。





<aside class="affiliate-card">
<div class="label">Notion に関連する書籍・ツール</div>
<p>「Notion」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FNotion%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「Notion」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=Notion" target="_blank" rel="sponsored noopener">▶ Amazonで「Notion」関連を見る</a></p>
</aside>





## 設定でつまずいた時の対処法

結論：MCPが動かない原因の9割は「JSON構文エラー」「Node.js未導入」「再起動忘れ」の3つです。

### ツールアイコンが表示されない

まずは設定ファイルを[JSONLint](https://jsonlint.com/)に貼り付けて構文をチェック。カンマの過不足、ダブルクォートの全角化が頻出ミスです。

### Server disconnected エラー

ログを確認します。macOSなら`~/Library/Logs/Claude/mcp*.log`に出力されているので、`tail -f`でリアルタイム監視しながら再起動すると原因が掴めます。多くの場合、`command`に指定したコマンドのパスが通っていないか、必要な環境変数が不足しています。

### npx が遅い・タイムアウトする

初回起動時はパッケージダウンロードで30秒ほどかかるのが普通です。改善したい場合は`npm install -g @modelcontextprotocol/server-filesystem`でグローバルインストールし、`command`を`mcp-server-filesystem`に直接指定する方法があります。

### 権限エラー

filesystemサーバーで「Permission denied」が出る場合、macOSのフルディスクアクセス設定でClaudeに権限を付与する必要があります。システム設定→プライバシーとセキュリティ→フルディスクアクセスから追加してください。

## まとめ

Claude MCPの設定は、設定ファイルにJSONを追記してアプリを再起動するだけのシンプルな仕組みです。最初の一つ（filesystem）が動けば、あとは同じパターンでGitHubやNotionも追加できます。

副業や業務効率化でClaudeを使うなら、MCPの導入は必須レベルの投資対効果があります。まずは15分かけて、自分のドキュメントフォルダにアクセスできる状態を作るところから始めてみてください。

## 関連記事

- [Claude Desktop MCPは無料プランで使える？2026年最新の始め方5選](/auto-blog/blog/claude-desktop-mcpは無料プランで使える2026年最新の始め方5選/)
- [Claude AIで稼ぐ副業7選｜月10万円ロードマップ2026](/auto-blog/blog/claude-aiで稼ぐ副業7選月10万円ロードマップ2026/)
- [Claude副業の始め方｜2026年5月最新7ステップ](/auto-blog/blog/claude副業の始め方2026年5月最新7ステップ/)

<!-- CROSS_LINKS -->
## 他サイトの最新AI記事

- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html)
- [今週のAIニュース10選 (2026/05/17付)](https://nayo126.github.io/ai-news-jp/posts/ai-weekly-roundup-20260517.html)
- [Claude's first day at Dunder Mifflin？AIキャラ動画がr/ClaudeAIで話題](https://nayo126.github.io/ai-news-jp/posts/claude-s-first-day-at-dunder-mifflin-ai-r-claudeai.html)

<!-- SEO_MESH_START -->

## 関連する記事

- [Claude Desktop MCPは無料プランで使える？2026年最新の始め方5選](https://nayo126.github.io/auto-blog/blog/claude-desktop-mcpは無料プランで使える2026年最新の始め方5選/)
- [Claude AIで稼ぐ副業7選｜月10万円ロードマップ2026](https://nayo126.github.io/auto-blog/blog/claude-aiで稼ぐ副業7選月10万円ロードマップ2026/)
- [AI副業で月5万は現実か？2026年最新の稼ぎ方5選](https://nayo126.github.io/auto-blog/blog/ai副業で月5万は現実か2026年最新の稼ぎ方5選/)

### 姉妹サイトの関連記事
- [Claude AIで激変するLinkedInプロフィール作成術2026年最新版](https://nayo126.github.io/ai-news-jp/posts/claude-ai-linkedin-2026.html) — AI News JP
- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html) — AI News JP
- [今週のAIニュース10選 (2026/05/17付)](https://nayo126.github.io/ai-news-jp/posts/ai-weekly-roundup-20260517.html) — AI News JP

<!-- SEO_MESH_END -->
