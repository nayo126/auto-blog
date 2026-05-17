---
title: "ChatGPTシステムプロンプト設定方法5手順【2026最新】"
description: "ChatGPTのシステムプロンプト設定方法を5手順で解説。Custom Instructions・API・GPTsの3つの設定場所と、副業で使える実践テンプレートも紹介します。"
pubDate: 2026-05-17
category: "ChatGPT活用"
tags: ["ChatGPT", "システムプロンプト", "Custom Instructions", "GPTs"]
keyword: "chatgpt システム プロンプト 設定 方法"
draft: false
image: "/auto-blog/ogp/chatgptシステムプロンプト設定方法5手順2026最新.png"
---

ChatGPTに毎回同じ指示を書くのが面倒だと感じたことはありませんか。「副業ライターとして」「日本語で」「箇条書きで」と、開いたチャットごとに同じ前提を入力し続けるのは、想像以上に時間を奪います。

実はChatGPTには、こうした前提を一度登録すれば全会話に自動適用できる「システムプロンプト」という仕組みが存在します。設定場所は3カ所あり、それぞれ使い分けることで作業効率は数倍変わります。

この記事では、ChatGPTのシステムプロンプト設定方法を5つの手順で解説し、副業や業務ですぐに使えるテンプレートも紹介します。

## システムプロンプトとは?通常プロンプトとの違い

結論から言うと、システムプロンプトはChatGPTに対する「常時有効な前提条件」のことです。一方、通常のプロンプトは1回のチャットで使い捨てになる指示文を指します。

両者の違いを具体的に整理すると、次のようになります。

- **通常プロンプト**:チャット欄に入力する都度の質問・依頼
- **システムプロンプト**:ChatGPTの「人格」「文体」「禁止事項」を裏側で固定する設定
- **メモリ機能**:過去の会話から自動で学習・記憶する補助機能

OpenAI公式の仕様では、システムプロンプトはAPIの`role: system`に相当します。ChatGPT(Web版)ではこれが「Custom Instructions(カスタム指示)」や「GPTs」の設定画面として提供されています。

なぜシステムプロンプトが重要なのか。理由はシンプルで、ChatGPTは前提が曖昧だと毎回汎用的な回答に寄ってしまうためです。たとえば「ブログ記事を要約して」と頼むだけでは硬い文章になりがちですが、システムプロンプトで「20代向けカジュアル文体・絵文字なし・600字以内」と設定しておけば、毎回その条件で出力されます。

副業で複数クライアントの記事を書く場合、案件ごとにGPTsを作って人格を切り替えれば、文体ブレを防げます。





<aside class="affiliate-card">
<div class="label">ChatGPT Plus に関連する書籍・ツール</div>
<p>「ChatGPT Plus」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FChatGPT%2520Plus%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「ChatGPT Plus」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=ChatGPT%20Plus" target="_blank" rel="sponsored noopener">▶ Amazonで「ChatGPT Plus」関連を見る</a></p>
</aside>





## ChatGPT Web版のCustom Instructionsで設定する手順

無料・有料問わず最も手軽な設定方法が、Custom Instructions(カスタム指示)を使う方法です。所要時間は約3分です。

設定手順は以下の5ステップで完了します。

1. ChatGPT画面右上のプロフィールアイコンをクリック
2. 「Customize ChatGPT(ChatGPTをカスタマイズ)」を選択
3. 「What would you like ChatGPT to know about you?」欄に自分の属性を入力
4. 「How would you like ChatGPT to respond?」欄に希望する回答スタイルを入力
5. 右下の「Save(保存)」をクリック

各欄はそれぞれ1500文字までの制限があります。ここに書いた内容は、以後すべての新規チャットに自動適用されます。

入力例として、副業ブロガーの方なら次のようなテンプレートが有効です。

**自分について欄の記入例**

- 副業でSEOブログを運営している会社員
- 主な執筆ジャンルはAI・ガジェット・節約
- 文章スキルは中級、SEOの基礎知識あり

**回答スタイル欄の記入例**

- 結論先出し型で答える
- 箇条書きを多用し可読性を高める
- 専門用語は初出時に必ず注釈を入れる
- 「〜と思います」など曖昧な語尾は避ける

設定後は既存のチャットには反映されないため、新規チャットを開いて動作確認しましょう。スマホアプリ版でも同じ手順で設定でき、PC設定とアカウント連携で同期されます。

## GPTsで案件別・用途別の専用ChatGPTを作る方法

ChatGPT Plus(月額20ドル)以上の有料プランを契約している場合、GPTsという機能で「特定用途専用のChatGPT」を作れます。Custom Instructionsとの違いは、複数のシステムプロンプトを切り替えて使える点です。

GPTs作成の流れは次の通りです。

1. 左サイドバーの「GPTを探す」→右上「+作成する」をクリック
2. 「Configure(構成)」タブを開く
3. Name(名前)、Description(説明)、Instructions(指示)を入力
4. 必要に応じてKnowledge(参考ファイル)をアップロード
5. 右上の「Create(作成)」→「Only me(自分のみ)」で保存

Instructions欄が実質的なシステムプロンプトです。ここに2000〜8000文字程度で詳細な役割定義を書きます。

副業で使える具体的なGPTs設計例として、「SEO記事構成案ジェネレーター」を作る場合の指示文骨子を紹介します。

```
あなたはSEOコンサルタントです。
ユーザーがキーワードを入力したら以下を出力してください。

1. 想定読者ペルソナ(年齢/職業/悩み)
2. 検索意図(Knowクエリ/Doクエリ/Buyクエリの分類)
3. H2見出し案を5〜7本
4. 各H2に含めるべきキーワード共起語
5. 競合上位3記事の想定内容と差別化ポイント

禁止事項:断定的な数値の捏造、医療・法律の個別アドバイス
```

このように役割・出力フォーマット・禁止事項を明示すると、毎回安定した品質の回答が得られます。作成したGPTsは左サイドバーから1クリックで呼び出せるため、Custom Instructionsを書き換える手間がなくなります。

## API経由でシステムプロンプトを設定する方法

開発者やNotion・Slack連携などの自動化を組む人向けに、APIでの設定方法も押さえておきましょう。APIではsystem roleを明示的に指定できます。

Python(openaiライブラリ)での基本コードは以下のようになります。

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": "あなたは経験豊富な編集者です。誤字脱字を指摘し、簡潔な日本語に修正してください。"},
        {"role": "user", "content": "ここに校正したい文章を貼り付け"}
    ]
)
print(response.choices[0].message.content)
```

APIで設定する利点は3つあります。第一に、Web版より細かい制御が可能で、temperatureやmax_tokensと組み合わせて出力のブレ幅を調整できる点です。第二に、ZapierやMake、n8nといった自動化ツールから呼び出せるため、定型業務を完全自動化できる点です。第三に、料金が従量課金のため、使った分だけ支払えば済む点です。

ただしAPI利用には費用がかかります。海外の事例として、月に数千リクエスト処理するブロガーが月額5〜30ドル程度に収まっているケースが多く報告されています。Custom InstructionsやGPTsで足りる用途なら、まずはWeb版から始めるのが無難です。

## システムプロンプト作成のコツとよくある失敗

最後に、効果的なシステムプロンプトを作るためのコツと、よくある失敗パターンを紹介します。

**効果が出やすい書き方の原則**

- **役割を1つに絞る**:「ライターかつ編集者かつSEOコンサル」と詰め込むより、用途別にGPTsを分ける方が精度が上がる
- **出力フォーマットを例示する**:「箇条書きで」だけでなく「`- 項目名:説明`の形式で」と具体化する
- **禁止事項を明示する**:「絵文字禁止」「断定表現禁止」など、避けたい挙動を先に書く
- **トーンを形容詞で指定**:「フランク」「論理的」「初心者目線」など方向性を限定する

**逆にやりがちな失敗パターン**

「あなたは優秀なAIアシスタントです」のような抽象的な役割定義は、ほぼ効果がありません。GPT-5やClaude Sonnet 4.6といった最新モデルは標準でも十分優秀なため、わざわざ「優秀な」と書いても挙動は変わらないからです。

また、システムプロンプトに長文の知識ベースを丸ごと貼り付けるのも非効率です。トークンを浪費する上、肝心の指示が埋もれてしまいます。参考資料はGPTsのKnowledge機能やRAG構築で対応するのが正解です。

定期的な見直しも欠かせません。設定して終わりにせず、3カ月に1度は出力結果を振り返り、不要な指示の削除や新しいルールの追加を行いましょう。

## まとめ

ChatGPTのシステムプロンプト設定方法は、Custom Instructions・GPTs・APIの3パターンがあり、用途と予算に応じて選ぶのが正解です。手軽さ重視ならCustom Instructions、案件別に使い分けたいならGPTs、自動化を組むならAPIという基準で判断しましょう。

重要なのは、抽象的な指示ではなく具体的な役割・出力形式・禁止事項を書き込むことです。まずは今日紹介した5手順でCustom Instructionsを設定し、3日後に出力結果を見直すところから始めてみてください。作業効率の変化を実感できるはずです。

## 関連記事

- [ChatGPT×Excel自動化副業｜2026年最新7つの稼ぎ方](/auto-blog/blog/chatgptexcel自動化副業2026年最新7つの稼ぎ方/)
- [ChatGPT GPT Store収益化2026完全攻略5選](/auto-blog/blog/chatgpt-gpt-store収益化2026完全攻略5選/)
- [ChatGPTでYouTube台本を10分作成する完全手順2026](/auto-blog/blog/chatgptでyoutube台本を10分作成する完全手順2026/)

<!-- CROSS_LINKS -->
## 他サイトの最新AI記事

- [ChatGPTで画像比較『left or right?』が話題、AI画像判定の使い方とは](https://nayo126.github.io/ai-news-jp/posts/chatgpt-left-or-right-ai.html)
- [ChatGPTで話題『Love at first prompt』Reddit投稿が示すAIとの関係性の変化](https://nayo126.github.io/ai-news-jp/posts/chatgpt-love-at-first-prompt-reddit-ai.html)
- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html)
