---
title: "Claude Code 起動方法を5分で解説｜初心者向け完全手順2026"
description: "Claude Codeの起動方法をターミナル操作が苦手な人向けに解説。インストールから初回ログイン、起動できない時の対処まで具体的な手順を5分で理解できます。"
pubDate: 2026-05-23
category: "Claude活用"
tags: ["Claude Code", "起動方法", "AI副業", "ターミナル"]
keyword: "claude code 起動 方法"
draft: false
image: "/auto-blog/ogp/claude-code-起動方法を5分で解説初心者向け完全手順2026.png"
---

「Claude Codeをインストールしたのに、どうやって起動するのか分からない」——そんな状態で手が止まっていませんか。コマンド入力に慣れていないと、最初の一歩でつまずきがちです。

実は、Claude Codeの起動はたった1つのコマンドで完了します。難しいのは「起動」そのものではなく、その前後の準備とエラー対処です。

この記事では、インストール直後から実際にコードを書き始めるまでの手順を、ターミナル操作が初めての人でも追えるように整理しました。AIを副業ツールとして使いこなす最初のハードルを、ここで越えてしまいましょう。

## 結論：起動コマンドは「claude」の1語だけ

<!-- INLINE_IMG -->
![Claude Code 起動方法を5分で解説｜初心者向け完全手順2026 - 結論：起動コマンドは「claude」の1語だけ](/auto-blog/inline-images/claude-code-5-2026-0.jpg)


結論から言うと、Claude Codeの起動方法は、ターミナルで `claude` と打ってEnterを押すだけです。理由は、Claude CodeがCLI（コマンドラインインターフェース）ツールとして設計されており、グローバルコマンドとして登録されるためです。

```bash
claude
```

これを実行すると、対話モードが立ち上がり、すぐに指示を入力できる状態になります。

ただし、この1語が通るには前提条件が2つあります。1つ目はNode.js（バージョン18以上）がインストールされていること。2つ目はClaude Code本体のインストールが完了していること。この2つが揃っていないと「command not found」と表示されます。

まだインストールしていない場合は、次のコマンドで導入します。

```bash
npm install -g @anthropic-ai/claude-code
```

`-g` はグローバルインストールを意味し、これでどのフォルダからでも `claude` が使えるようになります。インストールには通常1〜2分ほどかかります。


<aside class="affiliate-card">
<div class="label">Claude Code に関連する書籍・ツール</div>
<p>「Claude Code」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FClaude%2520Code%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「Claude Code」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=Claude%20Code" target="_blank" rel="sponsored noopener">▶ Amazonで「Claude Code」関連を見る</a></p>
</aside>


## 起動前にやっておく3つの準備

<!-- INLINE_IMG -->
![Claude Code 起動方法を5分で解説｜初心者向け完全手順2026 - 起動前にやっておく3つの準備](/auto-blog/inline-images/claude-code-5-2026-1.jpg)


スムーズに起動するために、事前に済ませておきたい準備が3つあります。順番に確認していきましょう。

**1. 作業フォルダに移動する**

Claude Codeは「起動したフォルダ」を作業ディレクトリとして認識します。そのため、いきなり `claude` と打つのではなく、まず触りたいプロジェクトのフォルダへ移動するのが正解です。

```bash
cd ~/projects/my-app
claude
```

デスクトップに作ったフォルダなら `cd ~/Desktop/フォルダ名` のように指定します。

**2. Node.jsのバージョンを確認する**

`node -v` と打って、表示される数字が18以上かをチェックしてください。古いバージョンだと起動時にエラーが出ることがあります。数字が低い、あるいは何も表示されない場合は、Node.js公式サイトから最新版を入れ直します。

**3. ログイン認証を準備する**

初回起動時には、Anthropicアカウントでのログインが求められます。Claude Pro/Maxプランの契約者ならそのアカウントで、APIキー利用者はキーを手元に用意しておくと、認証画面で迷わずに済みます。

## 初回起動からログインまでの流れ

実際に `claude` を初めて実行すると、ブラウザが自動的に開き、ログイン画面に飛びます。ここでの流れを具体的に見ていきます。

最初に表示されるのは認証方法の選択です。Claude Max（月額プラン）を契約している人は、画面の案内に従ってアカウント連携を選びます。連携が完了すると、ターミナルに戻って「Login successful」と出ます。これで準備完了です。

認証が終わると、ターミナルにプロンプト（入力待ちの記号）が表示されます。試しに「このフォルダにある全ファイルを一覧表示して」と日本語で打ってみてください。Claude Codeがフォルダの中身を読み取り、内容を返してくれます。

ここで覚えておきたいのが、終了方法です。作業を終えるときは `/exit` と入力するか、`Ctrl + C` を2回押します。次回からは、同じフォルダで `claude` と打てば、認証なしですぐ起動します。一度ログインすれば、トークンが保存されるためです。

なお、過去の会話を引き継いで再開したいときは `claude --continue` で直前のセッションを呼び戻せます。

## 起動できない時のチェックリスト

「コマンドを打っても起動しない」という相談は海外のフォーラムでも頻出します。原因はだいたいパターン化されているので、上から順に試してください。

**「command not found」と出る場合**

インストールが正しく通っていないか、PATHが通っていない可能性が高いです。まず `npm list -g` でClaude Codeが一覧に出るか確認します。出ていなければインストールし直します。それでも駄目なら、ターミナルを一度完全に閉じて開き直すと反映されることがあります。

**権限エラー（permission denied）が出る場合**

`npm install` の段階でアクセス権がなく失敗しているケースです。Macなら `sudo` を付けて再実行するか、npmのインストール先を自分のホームディレクトリに変更すると解決します。

**ログイン画面が開かない場合**

ブラウザが自動起動しないときは、ターミナルに表示されるURLを手動でコピーしてブラウザに貼り付けます。社内ネットワークやVPN環境では認証が弾かれることもあるため、その場合は一時的にVPNを切って試すのが有効です。

困ったときは `claude --help` でコマンド一覧を表示できるので、まずはここを確認する習慣をつけておくと安心です。

## まとめ

Claude Codeの起動は `claude` の1コマンドで完結しますが、その手前にあるNode.jsの導入、作業フォルダへの移動、初回ログインを押さえておくことが、スムーズなスタートの鍵になります。

起動できない時も、原因はほぼ「インストール未完了」「権限不足」「PATH未設定」の3つに集約されます。落ち着いて上から潰していけば必ず動きます。まずは小さなフォルダで起動を試し、AIにコードを任せる感覚をつかんでみてください。

## 関連記事

- [Claude Codeおすすめターミナル7選｜2026年最新比較](/auto-blog/blog/claude-codeおすすめターミナル7選2026年最新比較/)
- [Claude Code無料の制限まとめ｜2026年最新の上限と回避3手](/auto-blog/blog/claude-code無料の制限まとめ2026年最新の上限と回避3手/)
- [Claude Code活用術7選｜副業の作業時間を3倍速に](/auto-blog/blog/claude-code活用術7選副業の作業時間を3倍速に/)

<!-- CROSS_LINKS -->
## 他サイトの最新AI記事

- [Claude Code利用者がGit pushで救われた話 - バージョン管理がAI開発で必須な理由](https://nayo126.github.io/ai-news-jp/posts/claude-code-git-push---ai.html)
- [Claude Codeが1時間連続編集？AIコーディング長時間自律作業の実態と注意点](https://nayo126.github.io/ai-news-jp/posts/claude-code-1-ai.html)
- [Claude CodeとAntigravity、Cursorはどこまで進化したか｜2026年AI開発ツール最新評価](https://nayo126.github.io/ai-news-jp/posts/claude-code-antigravity-cursor-2026-ai.html)

<!-- FAQ_START -->

## よくある質問

### Claude Codeで「command not found: claude」と出るのはなぜ？

インストールが未完了か、PATHが通っていないのが原因です。npm install -g @anthropic-ai/claude-code を再実行し、ターミナルを開き直してください。npmのグローバルパスがシェル設定に追加されていない場合も発生します。

### Claude Codeの起動にNode.jsはどのバージョンが必要？

Node.js 18以上が必須です。node -v で確認し、18未満なら公式サイトかnvmで20系などにアップデートしてください。バージョンが古いと起動時にエラーで止まります。

### Claude Codeを終了するにはどうすればいい？

対話モード中に /exit と入力するか、Ctrl+C を2回押すと終了します。1回だけだと現在の処理がキャンセルされるだけで、対話モードは継続します。

### Claude Codeは無料で使える？課金は必要？

Claude ProやMaxの月額プラン契約、またはAPIキーの従量課金が必要です。Maxプランは月額約3万円で、起動後に表示される指示に従ってログイン連携すれば使えます。

<script type="application/ld+json">
{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "Claude Codeで「command not found: claude」と出るのはなぜ？", "acceptedAnswer": {"@type": "Answer", "text": "インストールが未完了か、PATHが通っていないのが原因です。npm install -g @anthropic-ai/claude-code を再実行し、ターミナルを開き直してください。npmのグローバルパスがシェル設定に追加されていない場合も発生します。"}}, {"@type": "Question", "name": "Claude Codeの起動にNode.jsはどのバージョンが必要？", "acceptedAnswer": {"@type": "Answer", "text": "Node.js 18以上が必須です。node -v で確認し、18未満なら公式サイトかnvmで20系などにアップデートしてください。バージョンが古いと起動時にエラーで止まります。"}}, {"@type": "Question", "name": "Claude Codeを終了するにはどうすればいい？", "acceptedAnswer": {"@type": "Answer", "text": "対話モード中に /exit と入力するか、Ctrl+C を2回押すと終了します。1回だけだと現在の処理がキャンセルされるだけで、対話モードは継続します。"}}, {"@type": "Question", "name": "Claude Codeは無料で使える？課金は必要？", "acceptedAnswer": {"@type": "Answer", "text": "Claude ProやMaxの月額プラン契約、またはAPIキーの従量課金が必要です。Maxプランは月額約3万円で、起動後に表示される指示に従ってログイン連携すれば使えます。"}}]}
</script>

<!-- FAQ_END -->

<!-- SEO_MESH_START -->

## 関連する記事

- [Claude CodeとGemini徹底比較2026｜副業で使うべきはどっち](https://nayo126.github.io/auto-blog/blog/claude-codeとgemini徹底比較2026副業で使うべきはどっち/)
- [Claude Codeおすすめターミナル7選｜2026年最新比較](https://nayo126.github.io/auto-blog/blog/claude-codeおすすめターミナル7選2026年最新比較/)
- [Claude Code無料の制限まとめ｜2026年最新の上限と回避3手](https://nayo126.github.io/auto-blog/blog/claude-code無料の制限まとめ2026年最新の上限と回避3手/)

### 姉妹サイトの関連記事
- [Claude Code利用者がGit pushで救われた話 - バージョン管理がAI開発で必須な理由](https://nayo126.github.io/ai-news-jp/posts/claude-code-git-push---ai.html) — AI News JP
- [Claude Codeが1時間連続編集？AIコーディング長時間自律作業の実態と注意点](https://nayo126.github.io/ai-news-jp/posts/claude-code-1-ai.html) — AI News JP
- [Claude CodeとAntigravity、Cursorはどこまで進化したか｜2026年AI開発ツール最新評価](https://nayo126.github.io/ai-news-jp/posts/claude-code-antigravity-cursor-2026-ai.html) — AI News JP

<!-- SEO_MESH_END -->
