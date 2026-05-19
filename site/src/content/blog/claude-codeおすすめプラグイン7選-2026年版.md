---
title: "Claude Codeおすすめプラグイン7選 2026年版"
description: "Claude Codeの作業効率を激変させるおすすめプラグインを7つ厳選。導入手順、使い分け、実際の作業時間短縮効果まで2026年最新情報で解説します。"
pubDate: 2026-05-17
category: "Claude活用"
tags: ["Claude Code", "プラグイン", "AI開発", "副業"]
keyword: "claude code おすすめプラグイン"
draft: false
image: "/auto-blog/ogp/claude-codeおすすめプラグイン7選-2026年版.png"
---

「Claude Codeを入れたはいいけど、デフォルトのまま使ってるな」——そんな状態になっていないでしょうか。実はClaude Codeの真価は、プラグインや拡張機能を組み合わせて初めて発揮されます。素のままだとChatGPTやCursorとの違いを感じにくく、月20,000円超の課金が重く感じるはずです。

結論から書きます。Claude Codeは「MCPサーバー」と「カスタムスラッシュコマンド」「VS Code拡張」を入れた瞬間に別物になります。本記事では、副業エンジニアやAIで稼ぎたい人が最初に入れるべき7つのおすすめプラグインを、実際の使用シーンと一緒に紹介します。



<aside class="affiliate-card">
<div class="label">Claude Pro に関連する書籍・ツール</div>
<p>「Claude Pro」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FClaude%2520Pro%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「Claude Pro」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=Claude%20Pro" target="_blank" rel="sponsored noopener">▶ Amazonで「Claude Pro」関連を見る</a></p>
</aside>



## Claude Codeのプラグイン構造を理解する

<!-- INLINE_IMG -->
![Claude Codeおすすめプラグイン7選 2026年版 - Claude Codeのプラグイン構造を理解する](/auto-blog/inline-images/claude-code-7-2026--0.jpg)


Claude Codeで「プラグイン」と呼ばれているものは、厳密には3種類に分かれます。この前提を押さえないと、何を入れていいか迷子になります。

1つ目は**MCP(Model Context Protocol)サーバー**。Claudeに外部ツールへのアクセス能力を与える拡張で、2026年現在もっとも注目されているのがこの仕組みです。FigmaやNotion、SlackなどとClaudeを直結できます。

2つ目は**カスタムスラッシュコマンド**。`/test` `/review` のように自分専用のショートカットを作る機能で、`.claude/commands/`配下にMarkdownを置くだけで動きます。同じ指示を毎回打ち込む手間が消えます。

3つ目は**VS Code/JetBrains拡張**。IDE内でClaude Codeを呼び出せるようになる公式拡張で、ターミナルを行き来する時間がなくなります。

この3層を組み合わせるのが正攻法です。以下、具体的な7つを紹介していきます。

## 必須級MCPサーバー4選

<!-- INLINE_IMG -->
![Claude Codeおすすめプラグイン7選 2026年版 - 必須級MCPサーバー4選](/auto-blog/inline-images/claude-code-7-2026--1.jpg)


### 1. Filesystem MCP

公式が提供する最重要MCP。Claudeに任意ディレクトリへの読み書き権限を渡せます。デフォルトのClaude Codeはカレントディレクトリしか見られませんが、これを入れると複数プロジェクト横断で参照可能になります。副業で複数案件を並行する人には必須です。

### 2. GitHub MCP

GitHubの公式MCPサーバー。Issue起票、PR作成、コードレビュー、Actions監視まで自然言語でこなせます。「先週マージしたPRの一覧を出して」と言うだけで返ってくる体験は、一度味わうと戻れません。

### 3. Playwright MCP

ブラウザ自動化のためのMCP。「このURLを開いてスクショ撮って」「ログイン後の挙動を確認して」が一発です。E2Eテスト書きやスクレイピング系の副業で時間を半減できます。

### 4. Context7 MCP

各種ライブラリの最新ドキュメントをClaudeに直接食わせるMCP。Next.jsやReactなど、バージョンアップが激しいフレームワークの「古い書き方」を提案される問題を解消します。



<aside class="affiliate-card">
<div class="label">Claude Code に関連する書籍・ツール</div>
<p>「Claude Code」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FClaude%2520Code%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「Claude Code」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=Claude%20Code" target="_blank" rel="sponsored noopener">▶ Amazonで「Claude Code」関連を見る</a></p>
</aside>



## カスタムスラッシュコマンド2選

### 5. /review コマンド

`.claude/commands/review.md` に「現在の差分をセキュリティ・パフォーマンス・可読性の3観点でレビューせよ」と書いておくだけ。`git diff` を渡しながら `/review` と打てば、コードレビュー観点を毎回ブレなく適用できます。

実装例はこんな感じです。

```markdown
現在のgit diffに対し、以下3観点でレビュー:
1. セキュリティ(SQLi/XSS/秘密情報露出)
2. パフォーマンス(N+1/不要なループ)
3. 可読性(命名/責務分離)
```

たったこれだけで、自分専用のレビュアーが完成します。

### 6. /commit コマンド

ステージング済みの変更を解析し、Conventional Commits規約に沿ったメッセージを生成するコマンド。コミット粒度や英文のクセが安定し、複数案件を回す人ほど効きます。海外の開発者コミュニティでは「これ一つで日常的なタイピング量が3割減った」という報告も見かけます。

## IDE統合プラグイン1選

### 7. Claude Code for VS Code

Anthropic公式のVS Code拡張。エディタのサイドバーから直接Claude Codeを呼び出せ、選択範囲を即座にコンテキストに渡せます。ターミナル切り替えのストレスが消え、思考の流れを切らずにコーディングできるのが大きな利点です。

JetBrains版も同時期に公開されており、PyCharm/IntelliJユーザーも恩恵を受けられます。導入手順は拡張機能ストアで「Claude Code」と検索してインストールするだけ、APIキーは既存のClaude Maxプラン契約のものを流用できます。

## プラグイン選びで失敗しないコツ

最後に、プラグインを増やしすぎる失敗パターンを共有します。MCPサーバーは1つ増やすごとにコンテキストウィンドウを消費するため、10個も入れると「肝心のコードが見られない」状態に陥ります。

おすすめの運用は「常時オン3つ＋案件ごとに切替4つ」。Filesystem、GitHub、Context7を常時オンにし、ブラウザ自動化案件のときだけPlaywrightを足す、といった使い分けが現実的です。

カスタムスラッシュコマンドはGitリポジトリに含めてチーム共有もできるため、副業仲間と「俺たちの最強コマンド集」を育てていくのも面白い使い方になります。

## まとめ

Claude Codeのおすすめプラグインを7つ紹介しました。MCPサーバー4種でClaudeに「手足」を与え、カスタムコマンド2種で「定型作業」を消し、VS Code拡張で「往復時間」を削る——この組み合わせが2026年5月時点での最適解です。月額2万円超の投資を回収するためにも、まずはFilesystem MCPとGitHub MCPの2つから今日入れてみてください。30分の設定で、明日からの作業時間が確実に変わります。

## 関連記事

- [Claude Codeおすすめスキル7選｜2026年版作業効率化](/auto-blog/blog/claude-codeおすすめスキル7選2026年版作業効率化/)
- [Claude Codeで個人開発を収益化する5戦略](/auto-blog/blog/claude-codeで個人開発を収益化する5戦略/)
- [Claude Code MCP設定方法5分完全ガイド2026](/auto-blog/blog/claude-code-mcp設定方法5分完全ガイド2026/)

<!-- CROSS_LINKS -->
## 他サイトの最新AI記事

- [Claude Code利用者がGit pushで救われた話 - バージョン管理がAI開発で必須な理由](https://nayo126.github.io/ai-news-jp/posts/claude-code-git-push---ai.html)
- [Sea LimitedがOpenAI Codexを全社導入、アジア発のエージェント型開発を加速](https://nayo126.github.io/ai-news-jp/posts/sea-limited-openai-codex.html)
- [ChatGPTにコードを貼ったら欠陥3つ即指摘されるReddit投稿が話題](https://nayo126.github.io/ai-news-jp/posts/chatgpt-3-reddit.html)

<!-- SEO_MESH_START -->

## 関連する記事

- [Claude Code×VSCode連携｜2026年最新7つの活用術](https://nayo126.github.io/auto-blog/blog/claude-codevscode連携2026年最新7つの活用術/)
- [Claude Code始め方完全ガイド｜2026年最新版5ステップ](https://nayo126.github.io/auto-blog/blog/claude-code始め方完全ガイド2026年最新版5ステップ/)
- [Claude Code比較2026｜主要AI開発5ツールの実力差](https://nayo126.github.io/auto-blog/blog/claude-code比較2026主要ai開発5ツールの実力差/)

### 姉妹サイトの関連記事
- [Claude Code利用者がGit pushで救われた話 - バージョン管理がAI開発で必須な理由](https://nayo126.github.io/ai-news-jp/posts/claude-code-git-push---ai.html) — AI News JP
- [Sea LimitedがOpenAI Codexを全社導入、アジア発のエージェント型開発を加速](https://nayo126.github.io/ai-news-jp/posts/sea-limited-openai-codex.html) — AI News JP
- [ChatGPTにコードを貼ったら欠陥3つ即指摘されるReddit投稿が話題](https://nayo126.github.io/ai-news-jp/posts/chatgpt-3-reddit.html) — AI News JP

<!-- SEO_MESH_END -->

<!-- FAQ_START -->

## よくある質問

### Claude CodeのMCPサーバーとは何ですか？

MCPはClaude Codeに外部ツールやデータソースを接続する仕組みです。GitHub、Slack、データベースなど100以上のサーバーが公開されており、claude mcp addコマンドで1分で追加できます。

### Claude CodeとCursorはどちらがおすすめですか？

長時間の自律作業ならClaude Code、リアルタイム補完中心ならCursorが向いています。Claude Codeは月20,000円〜でターミナル常駐型、Cursorは月20ドルでエディタ統合型です。副業の量産用途ならClaude Codeが有利です。

### Claude Codeのカスタムスラッシュコマンドの作り方は？

プロジェクトルートに.claude/commands/ディレクトリを作り、コマンド名.mdファイルを置くだけです。例えばreview.mdに指示を書けば/reviewで呼び出せます。チームで共有すれば作業時間が約3割短縮できます。

### Claude Codeを無料で試す方法はありますか？

Anthropic公式は有料のみですが、API経由でPay-as-you-go利用なら月数百円から試せます。Claude Pro（月3,000円）契約者はWeb版で同等機能を制限付きで使え、本格運用前のテストに十分です。

<script type="application/ld+json">
{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "Claude CodeのMCPサーバーとは何ですか？", "acceptedAnswer": {"@type": "Answer", "text": "MCPはClaude Codeに外部ツールやデータソースを接続する仕組みです。GitHub、Slack、データベースなど100以上のサーバーが公開されており、claude mcp addコマンドで1分で追加できます。"}}, {"@type": "Question", "name": "Claude CodeとCursorはどちらがおすすめですか？", "acceptedAnswer": {"@type": "Answer", "text": "長時間の自律作業ならClaude Code、リアルタイム補完中心ならCursorが向いています。Claude Codeは月20,000円〜でターミナル常駐型、Cursorは月20ドルでエディタ統合型です。副業の量産用途ならClaude Codeが有利です。"}}, {"@type": "Question", "name": "Claude Codeのカスタムスラッシュコマンドの作り方は？", "acceptedAnswer": {"@type": "Answer", "text": "プロジェクトルートに.claude/commands/ディレクトリを作り、コマンド名.mdファイルを置くだけです。例えばreview.mdに指示を書けば/reviewで呼び出せます。チームで共有すれば作業時間が約3割短縮できます。"}}, {"@type": "Question", "name": "Claude Codeを無料で試す方法はありますか？", "acceptedAnswer": {"@type": "Answer", "text": "Anthropic公式は有料のみですが、API経由でPay-as-you-go利用なら月数百円から試せます。Claude Pro（月3,000円）契約者はWeb版で同等機能を制限付きで使え、本格運用前のテストに十分です。"}}]}
</script>

<!-- FAQ_END -->
