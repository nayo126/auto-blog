---
title: "Copilotプロンプトテンプレ厳選7選｜2026年最新版"
description: "GitHub CopilotとMicrosoft 365 Copilotで使えるプロンプトテンプレートを7パターン厳選。コピペで使える具体例付きで、副業の生産性を3倍にする実践的な書き方を解説します。"
pubDate: 2026-05-19
category: "プロンプトエンジニアリング"
tags: ["Copilot", "プロンプトテンプレート", "AI副業", "GitHub Copilot"]
keyword: "プロンプト テンプレート copilot"
draft: false
image: "/auto-blog/ogp/copilotプロンプトテンプレ厳選7選2026年最新版.png"
---

「Copilotに指示を出しているのに、思った通りのコードや文章が返ってこない」。そんな経験はありませんか。同じツールを使っていても、稼いでいる人と稼げない人の差は、ほぼ100%プロンプトの質で決まります。

特にGitHub CopilotやMicrosoft 365 Copilotは、ChatGPTやClaudeとは違う「コンテキスト依存型」のAIです。エディタの周辺コードや開いているドキュメントを読み込む特性があるため、プロンプトの書き方も独自の工夫が必要になります。

この記事では、副業で月10万円以上を狙う人向けに、コピペですぐ使えるCopilot専用プロンプトテンプレートを7つ紹介します。

## なぜCopilotのプロンプトはChatGPTと違うのか

結論:Copilotは「周辺の文脈」を最も重視するAIだからです。理由は、GitHub CopilotがVS Codeの開いているファイル全体・タブ・カーソル位置を読み込む設計になっているためで、Microsoft 365 CopilotもWordやExcelの既存内容を前提に応答を生成します。

ChatGPTやClaude Sonnet 4.6に「ブログを書いて」と指示するときは、長文プロンプトで条件を細かく指定するのが定石でした。一方Copilotでは、プロンプトを短くして、代わりに**周辺情報を整える**ことが重要になります。

具体的には次の3点を意識すると精度が跳ね上がります。

- **ファイル冒頭にコメントで意図を書く**:1〜3行の自然言語コメントが最強のプロンプト
- **変数名・関数名を明確にする**:`data`より`userPurchaseHistory`の方が予測精度が上がる
- **直前の例を1つ提示する**:Few-shot promptingに近い動作をする

海外の開発者コミュニティでも、Copilotの精度を上げる最大のコツは「ファイル名と変数名を英語で具体的にする」と繰り返し報告されています。日本語のローカル変数名でも動きますが、英語の方が学習データの量で圧倒的に有利です。



<aside class="affiliate-card">
<div class="label">GitHub Copilot に関連する書籍・ツール</div>
<p>「GitHub Copilot」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FGitHub%2520Copilot%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「GitHub Copilot」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=GitHub%20Copilot" target="_blank" rel="sponsored noopener">▶ Amazonで「GitHub Copilot」関連を見る</a></p>
</aside>



## コード生成で使える基本テンプレ3選

### テンプレ1:関数仕様書型

```
// 関数名: calculateMonthlyRevenue
// 入力: 売上配列 [{date: 'YYYY-MM-DD', amount: number}]
// 出力: 月別合計 {'2026-05': 150000, ...}
// エラー処理: dateが不正な場合は無視
```

このコメントをファイルに書いてからEnterを押すと、Copilotはほぼ100%の精度で実装を提案します。仕様を箇条書きで示すのがポイントです。

### テンプレ2:テストファースト型

先に`describe`と`it`のテストケースだけ書いてしまう方法です。Jest・Vitest・Pytestいずれでも有効で、テストを見たCopilotが逆算して実装コードを書いてくれます。TDD的なアプローチが好きな人には特に相性が良い手法です。

### テンプレ3:リファクタリング指示型

既存コードの直前にコメントを挿入します。「// 上のコードをasync/awaitに書き換え」「// 上のループをmap/filterに変換」のように、変換ルールを1行で指示するだけで、選択範囲を読み取って書き直してくれます。

## 文章作成で使えるMicrosoft 365 Copilotテンプレ

### テンプレ4:議事録要約型

Wordに会議の文字起こしを貼り付けた後、サイドパネルで以下を入力します。

```
このドキュメントから決定事項・宿題・期限を表形式で抽出。
担当者が不明な項目は「未定」と記入。
3行以内の自然な日本語で。
```

「表形式で」と明示するのが効きます。曖昧に「まとめて」と書くと箇条書きになりがちです。

### テンプレ5:メール返信型

Outlook Copilotで使えるテンプレートです。「丁寧度3/5・200字以内・代替日程を3つ提示・絵文字なし」のように、**数値で制約を入れる**と精度が安定します。形容詞だけだと結果がぶれやすいので注意してください。



<aside class="affiliate-card">
<div class="label">Microsoft 365 Copilot に関連する書籍・ツール</div>
<p>「Microsoft 365 Copilot」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FMicrosoft%2520365%2520Copilot%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「Microsoft 365 Copilot」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=Microsoft%20365%20Copilot" target="_blank" rel="sponsored noopener">▶ Amazonで「Microsoft 365 Copilot」関連を見る</a></p>
</aside>



## 副業で差がつく応用テンプレ2選

### テンプレ6:競合分析プロンプト

ExcelにスクレイピングしたデータをCopilotで分析するときに有効です。

```
A列の競合サービス名、B列の月額料金、C列の機能数から
「コスパ最強TOP3」を理由付きで抽出。
理由は各50字以内、数字を必ず含めること。
```

「数字を必ず含めること」の一文があるだけで、抽象的な回答を防げます。ライティング副業でリサーチ時間を短縮したい人には強力な武器になります。

### テンプレ7:SEO記事構成テンプレ

WordとMicrosoft 365 Copilotの組み合わせで使います。

```
キーワード:[ここに入れる]
ターゲット:30代会社員・副業初心者
構成:結論先出し型・H2は5本・各H2は400字目安
含めるべき要素:具体例2つ・数字3つ・反論1つ
NG表現:「〜ではないでしょうか」「〜と言えるでしょう」
```

NG表現を明示するのが最大のコツです。AIが好む定型句を禁止することで、自然な日本語に近づきます。

## まとめ:テンプレは「自分用」に育てるのが正解

7つのテンプレを紹介しましたが、最も重要なのはこれをベースに自分専用版へ改造することです。Copilotは使うたびに学習するわけではないので、勝ちパターンを見つけたらNotionやテキストファイルに保存し、毎回コピペで呼び出す運用が現実的です。

副業で成果を出す人ほど、プロンプトを「資産」として蓄積しています。今日から1日1つ、自分のテンプレを増やしていけば、3ヶ月後には誰にも真似できない作業効率を手に入れられます。

## 関連記事

- [プロンプトを売る方法2026｜PromptBaseで月3万稼ぐ5ステップ](/auto-blog/blog/プロンプトを売る方法2026promptbaseで月3万稼ぐ5ステップ/)
- [プロンプト副業で月収10万円を狙う2026年の実践ロードマップ](/auto-blog/blog/プロンプト副業で月収10万円を狙う2026年の実践ロードマップ/)
- [Chain-of-Thought副業活用法5選｜AI思考連鎖で月10万稼ぐ](/auto-blog/blog/chain-of-thought副業活用法5選ai思考連鎖で月10万稼ぐ/)

<!-- CROSS_LINKS -->
## 他サイトの最新AI記事

- [ChatGPTで画像比較『left or right?』が話題、AI画像判定の使い方とは](https://nayo126.github.io/ai-news-jp/posts/chatgpt-left-or-right-ai.html)
- [ChatGPTで話題『Love at first prompt』Reddit投稿が示すAIとの関係性の変化](https://nayo126.github.io/ai-news-jp/posts/chatgpt-love-at-first-prompt-reddit-ai.html)
- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html)

<!-- SEO_MESH_START -->

## 関連する記事

- [Copilotプロンプト作り方｜成果10倍の7ステップ2026](https://nayo126.github.io/auto-blog/blog/copilotプロンプト作り方成果10倍の7ステップ2026/)
- [AI副業ラボ、はじめます](https://nayo126.github.io/auto-blog/blog/welcome/)
- [プロンプトを売る方法2026｜PromptBaseで月3万稼ぐ5ステップ](https://nayo126.github.io/auto-blog/blog/プロンプトを売る方法2026promptbaseで月3万稼ぐ5ステップ/)

<!-- SEO_MESH_END -->

<!-- FAQ_START -->

## よくある質問

### GitHub CopilotとMicrosoft 365 Copilotはプロンプトの書き方が違いますか？

違います。GitHub CopilotはVS Codeの開いているファイルやカーソル位置を読むため、関数名やコメントで意図を示すのが有効です。Microsoft 365 CopilotはWordやExcelの既存内容を前提にするので、対象範囲を明示した短い指示が効きます。

### Copilotで思った通りのコードが出ないときの対処法は？

まず関連ファイルを開きタブに残し、対象コードの直前にコメントで仕様を書きます。型定義や関数シグネチャを先に書くと精度が上がります。それでもズレる場合はCopilot Chatに「/explain」「/fix」を使い対話で絞り込みます。

### Copilotは無料で使えますか？料金はいくらですか？

GitHub Copilotは個人向けが月10ドル、年額100ドルです。学生や有名OSSメンテナーは無料。Microsoft 365 Copilotは1ユーザー月30ドル（年契約）で、365の対象ライセンスが別途必要です。

### CopilotとChatGPTはどちらを使うべきですか？

コード補完やエディタ内作業はCopilot、ゼロからの設計や長文生成はChatGPTやClaudeが向きます。実務では既存コードの続きをCopilot、仕様検討やレビューをChatGPTと役割分担するのが効率的です。

<script type="application/ld+json">
{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "GitHub CopilotとMicrosoft 365 Copilotはプロンプトの書き方が違いますか？", "acceptedAnswer": {"@type": "Answer", "text": "違います。GitHub CopilotはVS Codeの開いているファイルやカーソル位置を読むため、関数名やコメントで意図を示すのが有効です。Microsoft 365 CopilotはWordやExcelの既存内容を前提にするので、対象範囲を明示した短い指示が効きます。"}}, {"@type": "Question", "name": "Copilotで思った通りのコードが出ないときの対処法は？", "acceptedAnswer": {"@type": "Answer", "text": "まず関連ファイルを開きタブに残し、対象コードの直前にコメントで仕様を書きます。型定義や関数シグネチャを先に書くと精度が上がります。それでもズレる場合はCopilot Chatに「/explain」「/fix」を使い対話で絞り込みます。"}}, {"@type": "Question", "name": "Copilotは無料で使えますか？料金はいくらですか？", "acceptedAnswer": {"@type": "Answer", "text": "GitHub Copilotは個人向けが月10ドル、年額100ドルです。学生や有名OSSメンテナーは無料。Microsoft 365 Copilotは1ユーザー月30ドル（年契約）で、365の対象ライセンスが別途必要です。"}}, {"@type": "Question", "name": "CopilotとChatGPTはどちらを使うべきですか？", "acceptedAnswer": {"@type": "Answer", "text": "コード補完やエディタ内作業はCopilot、ゼロからの設計や長文生成はChatGPTやClaudeが向きます。実務では既存コードの続きをCopilot、仕様検討やレビューをChatGPTと役割分担するのが効率的です。"}}]}
</script>

<!-- FAQ_END -->
