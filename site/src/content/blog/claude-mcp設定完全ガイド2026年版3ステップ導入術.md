---
title: "Claude MCP設定完全ガイド｜2026年版3ステップ導入術"
description: "Claude MCPの設定方法を初心者向けに解説。Claude Desktop・Claude Codeで使えるMCPサーバーの導入手順、おすすめサーバー5選、トラブル対処までこの1記事でわかる。"
pubDate: 2026-05-22
category: "Claude活用"
tags: ["Claude", "MCP", "設定", "AI副業"]
keyword: "claude mcp 設定"
draft: false
image: "/auto-blog/ogp/claude-mcp設定完全ガイド2026年版3ステップ導入術.png"
---

「Claudeに自分のローカルファイルを読ませたい」「データベースを直接叩かせたい」「Slackに自動投稿させたい」——2026年に入ってから、こうした声が一気に増えてきた。

その願いを叶える仕組みが**MCP（Model Context Protocol）**だ。Anthropicが公開したこの規格は、すでに公式サーバーだけで100種類を超え、コミュニティ製を含めると1000を突破している。

ただ、いざ設定しようとすると「JSONファイルがどこにあるかわからない」「再起動してもアイコンが出ない」と詰まる人が後を絶たない。本記事では、Claude Desktop・Claude Codeそれぞれの最短手順から、入れて損しないMCPサーバー、トラブル対処まで一気に解説する。

## そもそもMCPとは何か

結論：MCPはClaudeに「外部世界へのアクセス権」を与える共通規格である。

従来のClaudeはチャットウィンドウの中で完結していた。ファイルを読むにはコピペが必要、最新情報は拾えない、外部サービスとの連携も手動。MCPはこの壁を壊す存在だ。サーバーを介してファイルシステム・GitHub・Slack・データベース・ブラウザなどに接続でき、Claudeが自分でツールを呼んで仕事を進められるようになる。

イメージは「Claudeに手足を生やすUSB規格」。MCPサーバーが手足の役割を担い、Claudeはそのインターフェースを通じて操作する。

メリットを整理すると以下の通りだ。

- **作業の自動化**：手動コピペが激減する
- **コンテキストの拡張**：自社ドキュメントを丸ごと参照可能
- **ツール統合**：複数SaaSをClaude一画面で操作

仕様はオープンソースで、TypeScriptとPython両方のSDKが揃っているため、自作サーバーも数十行で書ける。

## Claude Desktopでの設定手順

結論：設定ファイル1つを編集して再起動するだけ。

手順は次の3ステップで完結する。

1. **設定ファイルを開く**
   - Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. **mcpServersブロックを追記**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/yourname/Documents"]
    }
  }
}
```

3. **Claude Desktopを完全終了して再起動**

再起動後、入力欄の下部に金槌アイコンが出ていれば成功だ。「Documents内のファイル一覧を出して」と打てば、MCP経由でローカルを読みに行く。

事前にNode.jsとnpxがインストールされていること、JSONのカンマや括弧が正しいことを確認しよう。動かない原因の9割はこの2点に集約される。



<aside class="affiliate-card">
<div class="label">claude pro に関連する書籍・ツール</div>
<p>「claude pro」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2Fclaude%2520pro%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「claude pro」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=claude%20pro" target="_blank" rel="sponsored noopener">▶ Amazonで「claude pro」関連を見る</a></p>
</aside>



## Claude Codeでの設定方法

Claude Codeの場合、CLIから1コマンドで追加できるのが大きな利点だ。

```bash
claude mcp add filesystem npx -y @modelcontextprotocol/server-filesystem ~/projects
```

このコマンドで設定ファイルへの書き込みが自動化される。確認は `claude mcp list`、削除は `claude mcp remove <name>`、状態チェックは `/mcp` と打てば一覧表示される。

スコープを使い分けられるのもポイントだ。

- `--scope user`：全プロジェクト共通で読み込む
- `--scope project`：リポジトリ限定。`.mcp.json`にコミットしてチーム共有可能
- `--scope local`：自分のローカル設定のみ

チーム開発では`project`スコープで`.mcp.json`をコミットしておけば、メンバー全員が同じツールセットを引き継げる。新メンバーのオンボーディングが劇的に短くなるパターンだ。

## 入れて損しないMCPサーバー5選

ジャンル別に、現時点で実用度が高いものを挙げる。

- **filesystem**：ローカルファイルの読み書き。まず最初に入れるべき定番
- **github**：Issue作成・PRレビュー・コード検索を直接Claudeから実行可能
- **playwright**：ブラウザ自動操作。Webスクレイピングや定型作業の自動化に強い
- **postgres**：SQLクエリをClaudeに丸投げできる。データ分析副業と相性◎
- **slack**：チャンネル投稿・履歴検索・DM送信が一画面で完結

AI副業の用途なら、**filesystem + github + playwright**の3点セットで作業時間が半分以下になるケースも珍しくない。海外のRedditでは「MCPを導入してから月の作業時間が40時間減った」という報告も上がっている。

## よくあるトラブルと対処法

設定でハマる箇所はだいたい決まっている。先に押さえておこう。

- **アイコンが表示されない**：JSON構文エラーが大半。VSCodeなどで開いて赤線が出ていないか確認
- **コマンドが見つからない**：ターミナルで`which npx`と打ち、出てきたフルパスを`command`に絶対パスで書き直す
- **権限エラー**：Macは初回にアクセシビリティ・フルディスクアクセスの許可が必要
- **環境変数を渡したい**：`env`キーでAPIキーなどを個別指定する
- **特定ディレクトリだけ許可したい**：filesystem引数で対象パスを限定する

ログは設定画面の「開発者」タブから確認できる。エラー文をそのままコピーしてClaudeに貼れば、原因と修正案を返してくれることも多い。

## まとめ

Claude MCPの設定は、Desktop版ならJSONファイルを1つ編集、Claude Codeなら1コマンド打つだけで完了する。一度設定してしまえば、ファイル管理・GitHub操作・ブラウザ自動化といった作業がチャット内で完結し、副業効率が劇的に上がる。まずはfilesystemから入れて、慣れてきたら自分の業務に合うサーバーを順に追加していくのがおすすめだ。

## 関連記事

- [Claude MCP設定方法を15分で完了する2026最新手順](/auto-blog/blog/claude-mcp設定方法を15分で完了する2026最新手順/)
- [claude mcp addの使い方完全ガイド2026年最新7手順](/auto-blog/blog/claude-mcp-addの使い方完全ガイド2026年最新7手順/)
- [Claude AIで稼ぐ副業7選｜月10万円ロードマップ2026](/auto-blog/blog/claude-aiで稼ぐ副業7選月10万円ロードマップ2026/)

<!-- CROSS_LINKS -->
## 他サイトの最新AI記事

- [Claude AIで激変するLinkedInプロフィール作成術2026年最新版](https://nayo126.github.io/ai-news-jp/posts/claude-ai-linkedin-2026.html)
- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html)
- [今週のAIニュース10選 (2026/05/17付)](https://nayo126.github.io/ai-news-jp/posts/ai-weekly-roundup-20260517.html)
