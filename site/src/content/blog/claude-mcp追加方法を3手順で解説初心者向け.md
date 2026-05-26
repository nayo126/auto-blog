---
title: "Claude MCP追加方法を3手順で解説｜初心者向け"
description: "Claude MCPの追加方法を最新仕様で解説。Claude Desktopの設定ファイル編集とClaude Codeのコマンド、両方をコピペ実例つきで紹介。よくあるエラー対処も網羅した完全ガイド。"
pubDate: 2026-05-26
category: "Claude活用"
tags: ["Claude", "MCP", "AI副業", "業務効率化"]
keyword: "claude mcp 追加 方法"
draft: false
image: "/auto-blog/ogp/claude-mcp追加方法を3手順で解説初心者向け.png"
---

「Claudeに自分のファイルやツールを連携させたいのに、MCPの追加方法がよくわからない」——そう感じて検索した人は多いはずだ。設定ファイルの場所、コマンドの書き方、再起動のタイミング。公式情報は英語が中心で、断片的にしか出てこない。

結論から言うと、Claude MCPの追加方法は「Claude Desktopで設定ファイルを編集する」か「Claude Codeでコマンドを打つ」かの2系統で、どちらも10分あれば終わる。本記事では2026年時点の仕様にもとづき、コピペでそのまま使える実例つきで手順を整理した。副業や業務効率化でClaudeを本気で使いたい人ほど、MCPの設定は避けて通れない。

## 結論：Claude MCPの追加方法は2系統だけ

最初に全体像をつかんでおくと迷わない。MCP（Model Context Protocol）はAnthropicが2024年末に公開した規格で、Claudeを外部のファイル・データベース・APIとつなぐ「共通プラグイン」のような仕組みだ。追加の入り口は次の2つに集約される。

- **Claude Desktopアプリ**：`claude_desktop_config.json` という設定ファイルにサーバー情報を書き込む方式
- **Claude Code（CLI）**：`claude mcp add` コマンドを1行打つ方式

GUI中心で使うならDesktop、ターミナルで開発するならClaude Codeが向く。どちらの場合も「サーバーを定義する → 起動・再起動する → 接続を確認する」という3手順は共通だ。この流れさえ押さえれば、後述するファイル操作系・GitHub連携・データベース接続など、どのMCPサーバーでも同じ要領で追加できる。


<aside class="affiliate-card">
<div class="label">Claude Pro に関連する書籍・ツール</div>
<p>「Claude Pro」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FClaude%2520Pro%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「Claude Pro」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=Claude%20Pro" target="_blank" rel="sponsored noopener">▶ Amazonで「Claude Pro」関連を見る</a></p>
</aside>


## MCPを追加すると何ができるのか

手順の前に、追加する価値を30秒で確認しておきたい。MCPを入れると、Claudeが「会話だけのAI」から「自分の環境を操作できるAI」に変わる。

代表的な用途は次の通りだ。

1. **ローカルファイル操作**：`@modelcontextprotocol/server-filesystem` を入れると、指定フォルダ内のファイルをClaudeが直接読み書きできる
2. **GitHub連携**：Issue作成やコードレビューをClaudeに任せられる
3. **データベース接続**：PostgreSQLなどに接続し、自然言語でSQLを生成・実行
4. **ブラウザ自動操作**：Puppeteer系サーバーでスクレイピングや画面操作

たとえば「Documentsフォルダ内の請求書PDFを全部読んで一覧表にして」といった指示が、コピペなしで通るようになる。海外のRedditでも、MCPで社内ドキュメント検索を自動化して作業時間を半分以下にしたという報告が複数共有されている。副業ライターなら過去記事の参照、エンジニアならコードベースの横断検索と、使い方は職種ごとに広い。

## Claude Desktopでmcpを追加する手順

GUI派はこちらが基本となる。実際の流れは3ステップだ。

**手順1：設定ファイルを開く**
Claude Desktopを起動し、「設定（Settings）」→「開発者（Developer）」→「Edit Config」をクリックする。すると設定ファイルが開く。ファイルの場所は以下の通り。

- macOS：`~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows：`%APPDATA%\Claude\claude_desktop_config.json`

**手順2：mcpServersを書き込む**
ファイルが空なら、次のように記述する。ファイル操作サーバーを追加する例だ。

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/あなたの名前/Documents"]
    }
  }
}
```

`command` に実行コマンド、`args` に引数を配列で並べる。最後のパスがアクセスを許可するフォルダになる。

**手順3：アプリを完全に再起動する**
ここが見落としやすい。ウィンドウを閉じるだけでは反映されないため、アプリを終了（macOSは⌘+Q）してから再度開く。入力欄の近くにツールアイコンが表示されれば追加成功だ。事前にNode.jsをインストールしておくと `npx` が確実に動く。

## Claude Code（CLI）でmcpを追加する方法

ターミナルで開発する人は、コマンド1行で済むClaude Codeが圧倒的に速い。基本構文は次の形だ。

```bash
claude mcp add <名前> -- <実行コマンド> [引数...]
```

先ほどと同じファイル操作サーバーを追加するなら、こう打つ。

```bash
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem ~/Documents
```

`--` の後ろに実行コマンドを書くのがポイントで、これを忘れると引数が正しく渡らない。リモートのHTTP/SSEサーバーを追加する場合は `--transport` を使う。

```bash
claude mcp add --transport sse 名前 https://example.com/sse
```

追加後の管理コマンドも覚えておくと便利だ。

- `claude mcp list`：追加済みサーバーの一覧を確認
- `claude mcp get filesystem`：個別の設定内容を表示
- `claude mcp remove filesystem`：削除

スコープは `-s local`（自分専用・初期値）、`-s project`（チームで共有、`.mcp.json` に保存）、`-s user`（全プロジェクト共通）の3種類から選べる。チーム開発でMCP構成を共有したいときは `-s project` を指定すると、リポジトリ経由で同じ設定をメンバー全員に配布できる。


<aside class="affiliate-card">
<div class="label">プログラミングスクール に関連する書籍・ツール</div>
<p>「プログラミングスクール」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2F%25E3%2583%2597%25E3%2583%25AD%25E3%2582%25B0%25E3%2583%25A9%25E3%2583%259F%25E3%2583%25B3%25E3%2582%25B0%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25BC%25E3%2583%25AB%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「プログラミングスクール」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%82%B9%E3%82%AF%E3%83%BC%E3%83%AB" target="_blank" rel="sponsored noopener">▶ Amazonで「プログラミングスクール」関連を見る</a></p>
</aside>


## MCP追加でよくあるエラーと対処法

うまく動かないときは、原因の大半が次のどれかに当てはまる。

- **ツールアイコンが出ない**：再起動が不完全なケースが最多。アプリを完全終了してから開き直す
- **`command not found` 系のエラー**：Node.jsやnpxが未インストール。`node -v` で導入を確認する
- **JSONの構文エラー**：カンマの付け忘れや閉じ括弧の不足が原因。エラーが出たら設定ファイル全体をJSONチェッカーに通すと一発で特定できる
- **パスが認識されない**：Windowsでパスを書くときは `\` を `\\` と二重にエスケープする必要がある

それでも接続できない場合は、サーバーを単体でターミナルから直接起動し、エラーログを読むのが近道だ。Claude Code側なら `claude mcp get 名前` で登録内容を確認し、コマンドや引数のスペルミスを潰していく。多くの不具合は「再起動」「Node.js」「JSON構文」の3点を順に確認すれば解消する。

## まとめ

Claude MCPの追加方法は、Claude Desktopなら設定ファイル `claude_desktop_config.json` への記述、Claude Codeなら `claude mcp add` コマンドの2系統だ。どちらも「定義 → 再起動 → 確認」の3手順で完結する。まずはファイル操作サーバーを1つ追加し、動く体験を作るのが上達の最短ルートだ。MCPを使いこなせば、Claudeは単なる相談相手から、自分の環境を動かす実働アシスタントへと変わる。今日の設定が、明日の作業時間を確実に削ってくれる。

## 関連記事

- [Claude MCPサーバーおすすめ7選｜2026年最新の選び方](/auto-blog/blog/claude-mcpサーバーおすすめ7選2026年最新の選び方/)
- [Claude MCP設定方法を15分で完了する2026最新手順](/auto-blog/blog/claude-mcp設定方法を15分で完了する2026最新手順/)
- [Claude MCPおすすめ厳選7選｜2026年最新版](/auto-blog/blog/claude-mcpおすすめ厳選7選2026年最新版/)

<!-- CROSS_LINKS -->
## 他サイトの最新AI記事

- [Claude（Anthropic）が不調？r/ClaudeAIで朝のエラー・応答遅延が報告される](https://nayo126.github.io/ai-news-jp/posts/claude-anthropic-r-claudeai.html)
- [Claude AIで激変するLinkedInプロフィール作成術2026年最新版](https://nayo126.github.io/ai-news-jp/posts/claude-ai-linkedin-2026.html)
- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html)

<!-- FAQ_START -->

## よくある質問

### claude_desktop_config.jsonはどこにある？

Macは「~/Library/Application Support/Claude/claude_desktop_config.json」、Windowsは「%APPDATA%\Claude\claude_desktop_config.json」にある。ファイルがなければ同じ場所に新規作成する。設定→開発者→「構成を編集」からも開ける。

### MCPを追加した後にClaudeの再起動は必要？

Claude Desktopは設定ファイル編集後、Cmd+Q（WindowsはタスクトレイからExit）でアプリを完全終了し、再度起動すると反映される。Claude Codeの「claude mcp add」はコマンド実行直後に有効で、再起動は不要。

### MCPサーバーが認識されない・表示されないときの対処法は？

9割はJSONの構文ミス（カンマ抜け・括弧閉じ忘れ）が原因なので最初に確認する。次にnpxやnodeのパスが通っているか調べ、commandをフルパスで指定し直す。Claude Desktopはツールアイコンで接続状況を確認できる。

### Claude MCPは無料で使える？課金は必要？

MCP規格自体は無料で、Claude DesktopやClaude Codeへの追加に追加料金はかからない。filesystemやgitなど公式サーバーも無料。ただし連携先のAPI（外部データベースや有料API等）には別途利用料が発生する場合がある。

<script type="application/ld+json">
{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "claude_desktop_config.jsonはどこにある？", "acceptedAnswer": {"@type": "Answer", "text": "Macは「~/Library/Application Support/Claude/claude_desktop_config.json」、Windowsは「%APPDATA%\\Claude\\claude_desktop_config.json」にある。ファイルがなければ同じ場所に新規作成する。設定→開発者→「構成を編集」からも開ける。"}}, {"@type": "Question", "name": "MCPを追加した後にClaudeの再起動は必要？", "acceptedAnswer": {"@type": "Answer", "text": "Claude Desktopは設定ファイル編集後、Cmd+Q（WindowsはタスクトレイからExit）でアプリを完全終了し、再度起動すると反映される。Claude Codeの「claude mcp add」はコマンド実行直後に有効で、再起動は不要。"}}, {"@type": "Question", "name": "MCPサーバーが認識されない・表示されないときの対処法は？", "acceptedAnswer": {"@type": "Answer", "text": "9割はJSONの構文ミス（カンマ抜け・括弧閉じ忘れ）が原因なので最初に確認する。次にnpxやnodeのパスが通っているか調べ、commandをフルパスで指定し直す。Claude Desktopはツールアイコンで接続状況を確認できる。"}}, {"@type": "Question", "name": "Claude MCPは無料で使える？課金は必要？", "acceptedAnswer": {"@type": "Answer", "text": "MCP規格自体は無料で、Claude DesktopやClaude Codeへの追加に追加料金はかからない。filesystemやgitなど公式サーバーも無料。ただし連携先のAPI（外部データベースや有料API等）には別途利用料が発生する場合がある。"}}]}
</script>

<!-- FAQ_END -->
