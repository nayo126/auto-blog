---
title: "ChatGPTプロンプトで改行する方法5選｜Shift+Enterの使い方"
description: "ChatGPTで改行できずに困っていませんか？Shift+Enterや\\nの使い方、長文プロンプトを整理する5つの方法を具体例付きで解説。副業効率が3倍変わる入力術です。"
pubDate: 2026-05-18
category: "ChatGPT活用"
tags: ["ChatGPT", "プロンプト", "改行", "効率化"]
keyword: "chatgpt プロンプト 改行 方法"
draft: false
image: "/auto-blog/ogp/chatgptプロンプトで改行する方法5選shiftenterの使い方.png"
---

ChatGPTに長いプロンプトを送ろうとしてEnterを押した瞬間、未完成のまま送信されてしまった経験はありませんか。指示が途中で切れて意図しない回答が返ってきたり、毎回1行ずつしか送れずに作業効率が落ちたり。実はChatGPTの入力欄には、知っているかどうかで生産性が3倍変わる「改行の作法」があります。

副業でChatGPTを使い倒している人ほど、長文プロンプトを整理して送る技術を当たり前に使っています。この記事では、ブラウザ版・スマホアプリ版・API利用時のそれぞれで使える改行方法を5つに分けて解説します。

## 結論：ChatGPTの改行はShift+Enterが基本

<!-- INLINE_IMG -->
![ChatGPTプロンプトで改行する方法5選｜Shift+Enterの使い方 - 結論：ChatGPTの改行はShift+Enterが基本](/auto-blog/inline-images/chatgpt-5-shiftenter--0.jpg)


結論から言うと、ChatGPTのブラウザ版で改行したい場合は **Shift+Enter** を押せば送信されずに改行できます。Enter単体は「送信」、Shift+Enterは「改行」と覚えておけば、ほとんどのケースで困ることはありません。

理由はシンプルで、ChatGPTの入力欄はチャットアプリと同じUI設計だからです。SlackやDiscordと同じ仕様なので、これらに慣れている人は無意識に使えているはず。ただし環境によってショートカットが微妙に異なるため、整理しておきましょう。

| 環境 | 送信 | 改行 |
|------|------|------|
| ブラウザ版(PC) | Enter | Shift+Enter |
| Mac版アプリ | Enter | Shift+Enter または Option+Enter |
| Windows版アプリ | Enter | Shift+Enter |
| スマホアプリ(iOS/Android) | 送信ボタン | Enter(改行のみ) |

スマホ版だけは挙動が逆で、Enterキーが改行扱いになり、送信は右下のボタンを押す仕組みです。PCの感覚で「Enter押したら送られない！」と焦る必要はありません。

## 方法1：Shift+Enterで段落を分けて送る

<!-- INLINE_IMG -->
![ChatGPTプロンプトで改行する方法5選｜Shift+Enterの使い方 - 方法1：Shift+Enterで段落を分けて送る](/auto-blog/inline-images/chatgpt-5-shiftenter--1.jpg)


最も基本的なやり方が、Shift+Enterで段落を視覚的に整理する方法です。例えば「役割→前提→指示→出力形式」の4ブロックに分けて指示を出すと、ChatGPTの回答精度が体感で2倍ほど変わります。

実際の入力例はこうなります。

```
あなたはSEOライターです。
(Shift+Enter)
前提：読者は副業初心者の20代です。
(Shift+Enter)
指示：以下のキーワードで2000字の記事構成を作ってください。
キーワード:「AI副業 始め方」
(Shift+Enter)
出力形式：H2見出し5本+各H2の要点を箇条書き
```

ベタ書きで1行に詰め込むより、ブロック単位で改行を入れたほうがChatGPTは指示を正確に理解します。これは内部的に空行が文脈の区切りとして解釈されるため。長文プロンプトを書く人ほど、Shift+Enterを連打する癖をつけるべきです。



<aside class="affiliate-card">
<div class="label">ChatGPT プロンプト 書籍 に関連する書籍・ツール</div>
<p>「ChatGPT プロンプト 書籍」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FChatGPT%2520%25E3%2583%2597%25E3%2583%25AD%25E3%2583%25B3%25E3%2583%2597%25E3%2583%2588%2520%25E6%259B%25B8%25E7%25B1%258D%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「ChatGPT プロンプト 書籍」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=ChatGPT%20%E3%83%97%E3%83%AD%E3%83%B3%E3%83%97%E3%83%88%20%E6%9B%B8%E7%B1%8D" target="_blank" rel="sponsored noopener">▶ Amazonで「ChatGPT プロンプト 書籍」関連を見る</a></p>
</aside>



## 方法2：「\n」を使って強制的に改行を埋め込む

API経由でChatGPTを使う場合や、プロンプトをテキストファイルに保存しておく場合は、改行コード `\n` を直接書く方法が便利です。これはプログラミングで使われる改行記号で、ChatGPTもこれを改行として解釈してくれます。

例えばこう書きます。

```
役割：プロのコピーライター\n前提：30代女性向けの美容商材\n指示：キャッチコピーを5案提案してください
```

実際にこのテキストを貼り付けると、ChatGPT側では `\n` の部分が改行されて表示され、構造化された指示として認識されます。Pythonでopenaiライブラリを使ってAPI連携する人にとっては必須テクで、複数行のシステムプロンプトを1つの文字列にまとめる際に欠かせません。

ただしブラウザ版で直接 `\n` と打っても文字列としてそのまま渡されるので、混在を避けるなら通常はShift+Enterを使う方が無難です。

## 方法3：Markdownで構造化して見やすくする

ChatGPTはMarkdown記法を理解するため、改行と組み合わせて見出しやリストを使うと、長文プロンプトが劇的に整理されます。例えば見出しを `##` 、箇条書きを `-` で区切る形です。

```
## 役割
あなたはマーケティングのプロです。

## 前提
- 商材：AI自動化ツール
- ターゲット：個人事業主
- 予算：月1万円以下

## 指示
- 訴求文を3パターン作成
- それぞれにキャッチコピーと本文をセット
```

Markdownで整理されたプロンプトは、ChatGPT 5世代のモデルになってから特に精度が上がりました。Claude Sonnet 4.6など他のAIでも同じ書き方が通用するので、覚えておくと使い回しが効きます。副業でAIライティングをやっている人なら、この形式をテンプレ化して保存しておくと月50時間は浮きます。

## 方法4：スマホアプリでの改行テクニック

スマホ版ChatGPTでは、キーボードのEnter(改行)キーを押しても送信されません。送信は画面右下の上向き矢印アイコンをタップする必要があります。これを知らずに「改行できない」と勘違いしている人が意外と多い。

iPhone・Androidとも共通の挙動ですが、Bluetoothキーボードを接続している場合は挙動が変わることがあります。物理キーボード接続時はPC版と同じく、Enter送信・Shift+Enter改行の仕様になるケースがほとんど。

スマホで長文を打つのが面倒な場合は、音声入力との組み合わせがおすすめです。マイクアイコンから音声で文章を流し込み、必要なところで手動でEnterを押して段落分けする。この方法だと通勤中の電車内でも、3分で1000字級のプロンプトを作れます。



<aside class="affiliate-card">
<div class="label">ChatGPT 副業 始め方 に関連する書籍・ツール</div>
<p>「ChatGPT 副業 始め方」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FChatGPT%2520%25E5%2589%25AF%25E6%25A5%25AD%2520%25E5%25A7%258B%25E3%2582%2581%25E6%2596%25B9%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「ChatGPT 副業 始め方」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=ChatGPT%20%E5%89%AF%E6%A5%AD%20%E5%A7%8B%E3%82%81%E6%96%B9" target="_blank" rel="sponsored noopener">▶ Amazonで「ChatGPT 副業 始め方」関連を見る</a></p>
</aside>



## 方法5：改行が反映されないときの対処法

たまに「Shift+Enterを押しても改行されない」「コピペした文章の改行が消える」というトラブルが起きます。原因は主に3つあります。

1. **ブラウザの拡張機能が干渉している**：広告ブロッカーやキーボードショートカット系の拡張を一時停止して試す
2. **入力欄ではなく検索バーやサイドバーにフォーカスしている**：チャット入力欄をクリックし直す
3. **コピー元の改行コードが特殊文字**：一度メモ帳に貼って、そこから再コピーすると解決することが多い

特に3つ目はWordや海外サイトからコピーするときに頻発します。改行コードがCRLFかLFかで挙動が変わるためで、シンプルなテキストエディタを経由させるのが確実な対処法です。

それでも直らない場合はブラウザのキャッシュをクリアするか、Chrome/Edge/Safariなど別ブラウザで試してみると解決することが多いです。

## まとめ

ChatGPTの改行は基本Shift+Enter、スマホはEnterで改行・ボタンで送信。この2つを押さえれば日常の操作で困ることはありません。さらに長文プロンプトを書くなら、Markdownで構造化し、ブロックごとに空行を入れて視覚的に整理する習慣をつけましょう。

たかが改行ですが、AIへの指示の伝わり方が変わり、回答精度に直結します。副業でChatGPTを使うなら、この小さな差が月収の差になって返ってくるはずです。今日からプロンプトの書き方を一段アップグレードしてみてください。

## 関連記事

- [ChatGPTプロンプト本おすすめ7選｜2026年最新](/auto-blog/blog/chatgptプロンプト本おすすめ7選2026年最新/)
- [ChatGPT×Excel自動化副業｜2026年最新7つの稼ぎ方](/auto-blog/blog/chatgptexcel自動化副業2026年最新7つの稼ぎ方/)
- [ChatGPT GPT Store収益化2026完全攻略5選](/auto-blog/blog/chatgpt-gpt-store収益化2026完全攻略5選/)

<!-- CROSS_LINKS -->
## 他サイトの最新AI記事

- [ChatGPTで画像比較『left or right?』が話題、AI画像判定の使い方とは](https://nayo126.github.io/ai-news-jp/posts/chatgpt-left-or-right-ai.html)
- [ChatGPTで話題『Love at first prompt』Reddit投稿が示すAIとの関係性の変化](https://nayo126.github.io/ai-news-jp/posts/chatgpt-love-at-first-prompt-reddit-ai.html)
- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html)

<!-- FAQ_START -->

## よくある質問

### ChatGPTのスマホアプリで改行するには？

iOS・Androidアプリともにキーボードの改行キー(return/Enter)を押せば改行され、画面下の送信ボタン(紙飛行機アイコン)をタップして初めて送信されます。PC版と違い誤送信の心配はありません。

### Shift+Enterが効かない場合の対処法は？

ブラウザ拡張機能の干渉が原因のことが多いです。一度シークレットモードで試し、効くなら拡張機能を1つずつ無効化して特定します。Grammarlyや翻訳系拡張がよく競合します。

### Macで改行するショートカットは？

Macのブラウザ版でもShift+Enter(Shift+Return)で改行できます。Command+EnterやOption+Enterではなく、Windowsと同じShift+Enterが正解です。

### ChatGPTのAPIでプロンプトに改行を入れるには？

API利用時は文字列内に\n(バックスラッシュn)を入れれば改行されます。Pythonならトリプルクォート(""")で複数行をそのまま記述する方法が一般的で、可読性も高くなります。

<script type="application/ld+json">
{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "ChatGPTのスマホアプリで改行するには？", "acceptedAnswer": {"@type": "Answer", "text": "iOS・Androidアプリともにキーボードの改行キー(return/Enter)を押せば改行され、画面下の送信ボタン(紙飛行機アイコン)をタップして初めて送信されます。PC版と違い誤送信の心配はありません。"}}, {"@type": "Question", "name": "Shift+Enterが効かない場合の対処法は？", "acceptedAnswer": {"@type": "Answer", "text": "ブラウザ拡張機能の干渉が原因のことが多いです。一度シークレットモードで試し、効くなら拡張機能を1つずつ無効化して特定します。Grammarlyや翻訳系拡張がよく競合します。"}}, {"@type": "Question", "name": "Macで改行するショートカットは？", "acceptedAnswer": {"@type": "Answer", "text": "Macのブラウザ版でもShift+Enter(Shift+Return)で改行できます。Command+EnterやOption+Enterではなく、Windowsと同じShift+Enterが正解です。"}}, {"@type": "Question", "name": "ChatGPTのAPIでプロンプトに改行を入れるには？", "acceptedAnswer": {"@type": "Answer", "text": "API利用時は文字列内に\\n(バックスラッシュn)を入れれば改行されます。Pythonならトリプルクォート(\"\"\")で複数行をそのまま記述する方法が一般的で、可読性も高くなります。"}}]}
</script>

<!-- FAQ_END -->

<!-- SEO_MESH_START -->

## 関連する記事

- [ChatGPTプロンプト書き方の基本7原則と実例集2026](https://nayo126.github.io/auto-blog/blog/chatgptプロンプト書き方の基本7原則と実例集2026/)
- [プロンプト入力で副業を始める7つの型｜月5万への最短ルート](https://nayo126.github.io/auto-blog/blog/プロンプト入力で副業を始める7つの型月5万への最短ルート/)
- [ChatGPTプロンプト本おすすめ7選｜2026年最新](https://nayo126.github.io/auto-blog/blog/chatgptプロンプト本おすすめ7選2026年最新/)

### 姉妹サイトの関連記事
- [ChatGPTで画像比較『left or right?』が話題、AI画像判定の使い方とは](https://nayo126.github.io/ai-news-jp/posts/chatgpt-left-or-right-ai.html) — AI News JP
- [ChatGPTで話題『Love at first prompt』Reddit投稿が示すAIとの関係性の変化](https://nayo126.github.io/ai-news-jp/posts/chatgpt-love-at-first-prompt-reddit-ai.html) — AI News JP
- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html) — AI News JP

<!-- SEO_MESH_END -->
