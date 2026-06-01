---
title: "Claude Codeおすすめプロンプト10選｜副業効率3倍の実例集"
description: "Claude Codeで成果を出すおすすめプロンプトを10個厳選。コード生成・修正・テスト・リファクタの実例つきで、AI副業の作業時間を大幅短縮するコツを解説します。"
pubDate: 2026-06-02
category: "Claude活用"
tags: ["Claude Code", "プロンプト", "AI副業", "コード生成"]
keyword: "claude code プロンプト おすすめ"
draft: false
image: "/auto-blog/ogp/claude-codeおすすめプロンプト10選副業効率3倍の実例集.png"
---

「Claude Codeを使い始めたけど、思ったほどコードがうまく出てこない」——そう感じている人は多い。同じツールなのに、人によって生産性が2倍も3倍も変わる。その差はスキルではなく、ほとんどが**プロンプトの書き方**にある。

実は、Claude Code（Claude Sonnet 4.6やOpus 4.8を搭載したターミナル型のAIコーディング環境）は、曖昧な指示には曖昧な答えを返し、具体的な指示には驚くほど正確に応える。プログラミング初心者がAI副業で月数万円を狙うなら、ここを押さえるだけで作業時間が一気に縮む。

この記事では、すぐコピペして使えるおすすめプロンプトを10個、実例つきで紹介する。

## まず押さえるべきプロンプトの基本構造

結論：Claude Codeのプロンプトは「**役割 → 文脈 → タスク → 制約 → 出力形式**」の順で書くと精度が上がる。理由は、AIが何を前提に、何を、どこまでやればいいかを迷わず判断できるからだ。

例えば「ログイン機能作って」だけでは、言語もフレームワークも認証方式も不明で、的外れな提案が返ってくる。これを次のように書き換える。

```
あなたは経験豊富なバックエンドエンジニアです。
このプロジェクトはNext.js 15 + TypeScriptで動いています。
メールとパスワードによるログインAPIを作成してください。
制約: パスワードはbcryptでハッシュ化、エラーは日本語で返す。
出力: app/api/login/route.ts のコードのみ。
```

たった5行加えるだけで、戻ってくるコードの完成度がまるで変わる。海外の開発者コミュニティでも「context is everything（文脈がすべて）」という言葉がよく共有されており、これはClaude Codeでも例外ではない。

最初は面倒に感じるが、テンプレ化しておけば毎回数秒で済む。


<aside class="affiliate-card">
<div class="label">Claude Pro に関連する書籍・ツール</div>
<p>「Claude Pro」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FClaude%2520Pro%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「Claude Pro」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=Claude%20Pro" target="_blank" rel="sponsored noopener">▶ Amazonで「Claude Pro」関連を見る</a></p>
</aside>


## コード生成・修正で使えるおすすめプロンプト

ここからは実際にコピペで使える定番を紹介する。

**1. 既存コードの全体把握**
```
このリポジトリの構成を読み取り、主要なファイルの役割を
箇条書きで日本語でまとめてください。
```
新しい案件を受けたときの最初の一手として優秀だ。

**2. バグ修正（再現条件つき）**
```
このエラーが出ます: [エラーログを貼る]
原因の候補を3つ挙げ、最も可能性が高いものから
修正案を提示してください。憶測ではなく該当箇所を引用すること。
```

**3. 部分リファクタ**
```
この関数を、動作を変えずに可読性重視で書き直してください。
変更点はコメントではなく、変更理由を別途3行で説明してください。
```

**4. テストコード生成**
```
この関数に対するユニットテストをVitestで書いてください。
正常系2つ・異常系2つ・境界値1つを含めること。
```

ポイントは「数を指定する」こと。「テスト書いて」だと1つしか出ないことがあるが、「正常系2つ・異常系2つ」と数字で縛ると網羅性が上がる。AIは曖昧な量より具体的な数に強い。

## 副業の作業効率を上げる応用プロンプト

クラウドソーシングやスポット案件をこなすなら、コードを書く以外の場面でもClaude Codeは効く。

**5. ドキュメント自動生成**
```
このプロジェクトのREADMEを作成してください。
セットアップ手順・環境変数・起動コマンドを含め、
非エンジニアでも読める日本語で。
```
納品物にREADMEが付くだけで、クライアントからの評価が上がりやすい。

**6. コミットメッセージの提案**
```
今の変更内容を確認し、Conventional Commits形式で
コミットメッセージを3案提示してください。
```

**7. 設計レビュー**
```
この実装方針のリスクを、保守性・パフォーマンス・
セキュリティの3観点で指摘してください。褒めなくてよい。
```
「褒めなくてよい」の一言が地味に効く。これを入れないとAIは肯定から入りがちで、肝心の問題点が薄まる。

**8. 学習用の逆質問**
```
このコードで僕が理解していない可能性が高い概念を3つ挙げ、
それぞれ初心者向けに例えで説明してください。
```

副業は「速く納品する」だけでなく「自分の理解を深めて単価を上げる」ことも重要だ。Claude Codeを先生役として使えば、案件をこなすほどスキルが積み上がる。


<aside class="affiliate-card">
<div class="label">プログラミングスクール に関連する書籍・ツール</div>
<p>「プログラミングスクール」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2F%25E3%2583%2597%25E3%2583%25AD%25E3%2582%25B0%25E3%2583%25A9%25E3%2583%259F%25E3%2583%25B3%25E3%2582%25B0%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25BC%25E3%2583%25AB%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「プログラミングスクール」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%82%B9%E3%82%AF%E3%83%BC%E3%83%AB" target="_blank" rel="sponsored noopener">▶ Amazonで「プログラミングスクール」関連を見る</a></p>
</aside>


## やってはいけないNGプロンプトと対策

最後に、効率を落とす典型パターンを押さえておく。

**NG1：一度に詰め込みすぎる**
「ログインも決済もメール送信も全部作って」と一括で頼むと、どれも中途半端になりやすい。タスクは分割し、1プロンプト1目的を基本にする。

**NG2：丸投げで放置**
```
いい感じにアプリ作っといて
```
これは最も成果が出ない。Claude Codeは優秀だが、ゴールが定義されていなければ「それっぽいだけ」のコードを返す。最低でも機能・技術・制約の3点は明示する。

**NG3：エラーを貼らずに「動かない」とだけ言う**
ログやスクリーンショットなしの相談は、医者に症状を言わず「治して」と頼むようなもの。**9. 状況共有テンプレ**として、
```
やりたいこと / 実際の挙動 / エラー全文 / 試したこと
```
の4点をセットで貼る癖をつけたい。

そして**10. 反復改善**。一発で完璧を狙わず、「ここをこう直して」と会話を重ねる前提で使うと結果的に速い。Claude Codeは直前の文脈を保持しているため、差分指示が通りやすいのが強みだ。

## まとめ

Claude Codeの成果は、ツールの性能よりプロンプトの設計で決まる。「役割・文脈・タスク・制約・出力形式」の型を持ち、数を指定し、エラーは全文で共有する——この3つだけでも作業時間は目に見えて縮む。

今回の10個はすべてコピペで使えるので、まずは案件の最初の一手として試してほしい。小さな改善の積み重ねが、AI副業の単価とスピードを押し上げていく。

## 関連記事

- [Claude CodeとGemini徹底比較2026｜副業で使うべきはどっち](/auto-blog/blog/claude-codeとgemini徹底比較2026副業で使うべきはどっち/)
- [Claude Code 無料トライアルは可能？2026年最新の始め方](/auto-blog/blog/claude-code-free-trial/)
- [Claude Code 起動方法を5分で解説｜初心者向け完全手順2026](/auto-blog/blog/claude-code-起動方法を5分で解説初心者向け完全手順2026/)

<!-- CROSS_LINKS -->
## 他サイトの最新AI記事

- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html)
- [Claude's first day at Dunder Mifflin？AIキャラ動画がr/ClaudeAIで話題](https://nayo126.github.io/ai-news-jp/posts/claude-s-first-day-at-dunder-mifflin-ai-r-claudeai.html)
- [ChatGPTで画像比較『left or right?』が話題、AI画像判定の使い方とは](https://nayo126.github.io/ai-news-jp/posts/chatgpt-left-or-right-ai.html)

<!-- SEO_MESH_START -->

## 関連する記事

- [Claude CodeとGemini徹底比較2026｜副業で使うべきはどっち](https://nayo126.github.io/auto-blog/blog/claude-codeとgemini徹底比較2026副業で使うべきはどっち/)
- [ChatGPTプロンプトジェネレーター7選｜2026最新活用術](https://nayo126.github.io/auto-blog/blog/chatgptプロンプトジェネレーター7選2026最新活用術/)
- [ChatGPTプロンプト集｜コピペで使える15例と作り方](https://nayo126.github.io/auto-blog/blog/chatgptプロンプト集コピペで使える15例と作り方/)

### 姉妹サイトの関連記事
- [ChatGPTで画像比較『left or right?』が話題、AI画像判定の使い方とは](https://nayo126.github.io/ai-news-jp/posts/chatgpt-left-or-right-ai.html) — AI News JP
- [ChatGPTで話題『Love at first prompt』Reddit投稿が示すAIとの関係性の変化](https://nayo126.github.io/ai-news-jp/posts/chatgpt-love-at-first-prompt-reddit-ai.html) — AI News JP
- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html) — AI News JP

<!-- SEO_MESH_END -->
