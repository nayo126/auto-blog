---
title: "claude mcp addの使い方完全ガイド2026年最新7手順"
description: "claude mcp addコマンドでMCPサーバーを追加する方法を初心者向けに解説。引数の意味、scope指定、トラブル対処まで2026年最新版で網羅。"
pubDate: 2026-05-19
category: "Claude活用"
tags: ["Claude", "MCP", "Claude Code", "AI副業"]
keyword: "claude mcp add"
draft: false
image: "/auto-blog/ogp/claude-mcp-addの使い方完全ガイド2026年最新7手順.png"
---

「claude mcp addって打ってみたけど、結局どの引数を渡せばいいのかわからない」——Claude Codeを触り始めて最初にぶつかる壁が、まさにこのコマンドの使い方です。公式ドキュメントは英語ベースで断片的、日本語の解説記事も古いバージョンのままという状況。設定を間違えるとMCPサーバーが起動せず、AIの作業効率はむしろ落ちてしまいます。

この記事では、`claude mcp add` コマンドの基本構文から、スコープ指定の使い分け、よくあるエラーの直し方までを2026年5月時点の最新仕様でまとめました。読み終わるころには、自分のプロジェクトに合わせて任意のMCPサーバーを5分で追加できるようになります。

## claude mcp addとは何か：3分でわかる基本構造

<!-- INLINE_IMG -->
![claude mcp addの使い方完全ガイド2026年最新7手順 - claude mcp addとは何か：3分でわかる基本構造](/auto-blog/inline-images/claude-mcp-add-2026-7--0.jpg)


結論：`claude mcp add` は、Claude CodeにMCP(Model Context Protocol)サーバーを登録するためのコマンドです。理由は、Claude単体だとファイルシステムや外部API、データベースに直接アクセスできないため、MCPサーバー経由で「拡張機能」を追加する必要があるからです。

基本構文は次のとおりです。

```bash
claude mcp add <名前> <コマンド> [引数...]
```

たとえばGitHub連携用のMCPサーバーを追加するなら、

```bash
claude mcp add github npx -y @modelcontextprotocol/server-github
```

と打ちます。`github` が登録名(任意)、`npx` 以降が実際に起動するコマンドです。登録後は `claude mcp list` で一覧確認、`claude mcp remove github` で削除できます。

ポイントは「MCPサーバーは別プロセスとして常駐するわけではない」こと。Claude Codeがセッション開始時にコマンドを起動し、終了時にプロセスも閉じます。そのため軽量で、複数プロジェクトに同じMCPを使い回しても干渉しません。



<aside class="affiliate-card">
<div class="label">Claude Pro に関連する書籍・ツール</div>
<p>「Claude Pro」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FClaude%2520Pro%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「Claude Pro」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=Claude%20Pro" target="_blank" rel="sponsored noopener">▶ Amazonで「Claude Pro」関連を見る</a></p>
</aside>



## scope引数の使い分け：local・user・projectの違い

<!-- INLINE_IMG -->
![claude mcp addの使い方完全ガイド2026年最新7手順 - scope引数の使い分け：local・user・projectの違い](/auto-blog/inline-images/claude-mcp-add-2026-7--1.jpg)


`claude mcp add` には `-s` または `--scope` オプションがあり、3種類のスコープから選べます。これを理解しないと「家のPCでは動くのに会社のPCで動かない」という事故が起きます。

- **local**(デフォルト):現在のディレクトリにのみ有効。`.claude/settings.local.json` に保存
- **user**:ユーザー全体に有効。`~/.claude.json` に保存され、全プロジェクトで使える
- **project**:プロジェクト内で共有。`.mcp.json` に保存され、Gitで他メンバーと共有可能

具体的な使い分けは次のとおりです。GitHub MCPやSlack MCPなど個人トークンを使うものは `user` にしておくと毎回設定し直さずに済みます。一方、プロジェクト固有のデータベース接続などは `project` にしてチーム全員に配ります。

```bash
claude mcp add -s user github npx -y @modelcontextprotocol/server-github
claude mcp add -s project db node ./scripts/db-mcp.js
```

`local` は試運転用と割り切るのが無難です。スコープを間違えて追加した場合は一度removeして付け直します。

## 環境変数とAPIキーの安全な渡し方

MCPサーバーの多くはAPIキーを必要とします。`claude mcp add` では `-e KEY=VALUE` 形式で環境変数を注入できます。

```bash
claude mcp add -s user github \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=ghp_xxxxx \
  -- npx -y @modelcontextprotocol/server-github
```

注意点が3つあります。第一に、コマンド本体と引数の間に `--` を入れること。これがないと `-e` 以降のフラグがClaude側に吸われてしまいます。第二に、設定ファイル(`.mcp.json` など)に平文でトークンが書き込まれるため、`project` スコープでGitにコミットする際は要注意。

第三の対策として、シェルの環境変数を参照させる書き方が推奨されます。`.mcp.json` を直接編集して `"env": {"TOKEN": "${env:GITHUB_TOKEN}"}` のように書けば、実トークンを `~/.zshrc` などに置いてリポジトリには漏らさずに済みます。海外のRedditでも「APIキーの誤コミットでアカウント停止された」という報告が定期的に上がっており、軽視できないポイントです。



<aside class="affiliate-card">
<div class="label">プログラミングスクール に関連する書籍・ツール</div>
<p>「プログラミングスクール」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2F%25E3%2583%2597%25E3%2583%25AD%25E3%2582%25B0%25E3%2583%25A9%25E3%2583%259F%25E3%2583%25B3%25E3%2582%25B0%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25BC%25E3%2583%25AB%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「プログラミングスクール」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%82%B9%E3%82%AF%E3%83%BC%E3%83%AB" target="_blank" rel="sponsored noopener">▶ Amazonで「プログラミングスクール」関連を見る</a></p>
</aside>



## よくあるエラーと対処法5選

`claude mcp add` 周りで頻発するエラーをまとめました。

1. **「Server failed to start」**:コマンドのパスが通っていないケースが大半。`which npx` で確認し、フルパスを書くと解決することが多いです
2. **「Connection closed」**:MCPサーバー側のクラッシュ。`claude --mcp-debug` でログを見ると原因が出ます
3. **「Unknown tool」**:登録は成功しているがClaude側が認識していない。Claude Codeを一度終了して再起動します
4. **「Permission denied」**:Node.js製のMCPサーバーで `chmod +x` 漏れ。ローカルスクリプトを直接指定する場合に発生
5. **「Duplicate name」**:同名で再登録しようとした。先に `claude mcp remove <名前>` する必要があります

特に2番のデバッグログは強力で、JSONパースエラーから認証失敗まで詳細に表示されます。困ったらまず `--mcp-debug` フラグで起動し直すのが鉄則です。

## 実用的なMCPサーバー追加例7選

最後に、追加しておくと作業効率が跳ね上がる定番MCPサーバーを紹介します。

- **filesystem**:任意ディレクトリの読み書き。`npx -y @modelcontextprotocol/server-filesystem /path`
- **github**:Issue・PR操作。プログラマーなら必須級
- **slack**:チャンネル投稿・履歴取得。チーム連携に便利
- **postgres**:DB直接クエリ。ローカル開発で重宝
- **puppeteer**:ブラウザ自動操作。スクレイピングや動作確認に
- **memory**:セッション横断のメモ。長期プロジェクトで効く
- **sequential-thinking**:思考の連鎖を可視化。複雑なタスクで精度が上がります

これらを `user` スコープでまとめて入れておけば、新規プロジェクトでも即座に開発体制が整います。1つずつ動作確認しながら追加するのがおすすめです。

## まとめ

`claude mcp add` は、Claude Codeを単なるチャットツールから本格的な開発エージェントに変える鍵となるコマンドです。基本構文・スコープ指定・環境変数の渡し方・エラー対処の4点さえ押さえれば、あとは必要なMCPサーバーを足していくだけ。まずは `filesystem` と `github` の2つを `user` スコープで追加し、実際の作業で効果を体感してみてください。設定の手間以上のリターンが、確実に返ってきます。

## 関連記事

- [Claude MCP設定方法を15分で完了する2026最新手順](/auto-blog/blog/claude-mcp設定方法を15分で完了する2026最新手順/)
- [Claude AIで稼ぐ副業7選｜月10万円ロードマップ2026](/auto-blog/blog/claude-aiで稼ぐ副業7選月10万円ロードマップ2026/)
- [claude mcp add serenaの設定方法5ステップ完全版](/auto-blog/blog/claude-mcp-add-serenaの設定方法5ステップ完全版/)

<!-- CROSS_LINKS -->
## 他サイトの最新AI記事

- [Claude AIで激変するLinkedInプロフィール作成術2026年最新版](https://nayo126.github.io/ai-news-jp/posts/claude-ai-linkedin-2026.html)
- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html)
- [今週のAIニュース10選 (2026/05/17付)](https://nayo126.github.io/ai-news-jp/posts/ai-weekly-roundup-20260517.html)

<!-- SEO_MESH_START -->

## 関連する記事

- [Claude MCP設定方法を15分で完了する2026最新手順](https://nayo126.github.io/auto-blog/blog/claude-mcp設定方法を15分で完了する2026最新手順/)
- [Claude MCPおすすめ厳選7選｜2026年最新版](https://nayo126.github.io/auto-blog/blog/claude-mcpおすすめ厳選7選2026年最新版/)
- [Claude MCP追加方法を3手順で解説｜初心者向け](https://nayo126.github.io/auto-blog/blog/claude-mcp追加方法を3手順で解説初心者向け/)

### 姉妹サイトの関連記事
- [Claude（Anthropic）が不調？r/ClaudeAIで朝のエラー・応答遅延が報告される](https://nayo126.github.io/ai-news-jp/posts/claude-anthropic-r-claudeai.html) — AI News JP
- [Claude AIで激変するLinkedInプロフィール作成術2026年最新版](https://nayo126.github.io/ai-news-jp/posts/claude-ai-linkedin-2026.html) — AI News JP
- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html) — AI News JP

<!-- SEO_MESH_END -->

<!-- FAQ_START -->

## よくある質問

### claude mcp addのスコープはlocal・project・userのどれを選べばいい?

個人の検証はlocal、チーム共有はproject(.mcp.jsonをGit管理)、全プロジェクト共通はuserを選びます。デフォルトはlocalで、--scope projectを付けるとリポジトリ直下に設定が書き出されます。

### claude mcp addで登録したのにサーバーが起動しないときの対処法は?

claude mcp listで登録確認後、claude mcp get <name>でコマンドパスを点検します。失敗の8割はnpxやuvxの絶対パス未指定か環境変数不足で、--env KEY=VALUEで認証情報を追加すれば解決します。

### claude mcp addとclaude mcp add-jsonの違いは?

addは引数を1個ずつ渡す簡易版、add-jsonはコマンド・args・envをJSONで一括指定する詳細版です。複雑な引数や3個以上の環境変数を持つサーバーはadd-jsonの方が事故が少なく推奨されます。

### claude mcp addで追加したMCPサーバーを削除するには?

claude mcp remove <name>で削除できます。スコープを間違えて登録した場合は--scopeを明示して削除し、設定ファイル(~/.claude.jsonまたは.mcp.json)を直接編集してもOKです。

<script type="application/ld+json">
{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "claude mcp addのスコープはlocal・project・userのどれを選べばいい?", "acceptedAnswer": {"@type": "Answer", "text": "個人の検証はlocal、チーム共有はproject(.mcp.jsonをGit管理)、全プロジェクト共通はuserを選びます。デフォルトはlocalで、--scope projectを付けるとリポジトリ直下に設定が書き出されます。"}}, {"@type": "Question", "name": "claude mcp addで登録したのにサーバーが起動しないときの対処法は?", "acceptedAnswer": {"@type": "Answer", "text": "claude mcp listで登録確認後、claude mcp get <name>でコマンドパスを点検します。失敗の8割はnpxやuvxの絶対パス未指定か環境変数不足で、--env KEY=VALUEで認証情報を追加すれば解決します。"}}, {"@type": "Question", "name": "claude mcp addとclaude mcp add-jsonの違いは?", "acceptedAnswer": {"@type": "Answer", "text": "addは引数を1個ずつ渡す簡易版、add-jsonはコマンド・args・envをJSONで一括指定する詳細版です。複雑な引数や3個以上の環境変数を持つサーバーはadd-jsonの方が事故が少なく推奨されます。"}}, {"@type": "Question", "name": "claude mcp addで追加したMCPサーバーを削除するには?", "acceptedAnswer": {"@type": "Answer", "text": "claude mcp remove <name>で削除できます。スコープを間違えて登録した場合は--scopeを明示して削除し、設定ファイル(~/.claude.jsonまたは.mcp.json)を直接編集してもOKです。"}}]}
</script>

<!-- FAQ_END -->
