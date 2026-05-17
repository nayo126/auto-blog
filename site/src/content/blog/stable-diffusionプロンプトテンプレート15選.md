---
title: "Stable Diffusionプロンプトテンプレート15選"
description: "Stable Diffusionで思い通りの画像を生成するためのプロンプトテンプレート15選を紹介。初心者でもすぐ使える構成・呪文・ネガティブプロンプトの組み立て方を解説します。"
pubDate: 2026-05-16
category: "プロンプトエンジニアリング"
tags: ["Stable Diffusion", "プロンプト", "画像生成AI", "テンプレート"]
keyword: "プロンプト テンプレート stable diffusion"
draft: false
image: "/auto-blog/ogp/stable-diffusionプロンプトテンプレート15選.png"
---

Stable Diffusionで画像を作ろうとして、「思った通りの絵が出てこない」「他の人の作例みたいなクオリティにならない」と感じたことはないだろうか。実はその差は才能やセンスではなく、**プロンプトの「型」を知っているかどうか**で決まる。

英語の単語を並べただけでは、AIは何を優先すべきか判断できない。逆に、テンプレートに当てはめて要素を整理するだけで、出力品質は劇的に変わる。

この記事では、すぐにコピペで使える15個のプロンプトテンプレートと、その背後にある構造を解説する。SDXL 1.0以降のモデルでもFLUX.1でも応用できる、汎用性の高いフォーマットだ。

## Stable Diffusionプロンプトの基本構造

結論：高品質なプロンプトは **「主題 → 詳細 → スタイル → 品質タグ」** の4ブロック構造になっている。理由は、Stable Diffusionが文の前半に書かれた単語を強く解釈する仕組みだからだ。

具体的な並び順は次の通り。

1. **主題（Subject）**:1 girl, a samurai, a futuristic city など
2. **詳細（Details）**:服装・表情・ポーズ・背景
3. **スタイル（Style）**:photorealistic, anime style, oil painting
4. **品質タグ（Quality）**:masterpiece, best quality, 8k, ultra detailed

例えば「夕焼けの海辺に立つ女性」を生成したい場合、こう書く。

```
1girl, standing on the beach, long black hair, white dress, 
sunset, ocean waves, golden hour lighting, 
photorealistic, cinematic composition, 
masterpiece, best quality, 8k, ultra detailed
```

カンマで区切ること、強調したい要素は前に置くこと、`(word:1.3)`の形で重み付けできることを覚えておけば、ほとんどのモデルで通用する。





<aside class="affiliate-card">
<div class="label">Stable Diffusion 入門書 に関連する書籍・ツール</div>
<p>「Stable Diffusion 入門書」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FStable%2520Diffusion%2520%25E5%2585%25A5%25E9%2596%2580%25E6%259B%25B8%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「Stable Diffusion 入門書」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=Stable%20Diffusion%20%E5%85%A5%E9%96%80%E6%9B%B8" target="_blank" rel="sponsored noopener">▶ Amazonで「Stable Diffusion 入門書」関連を見る</a></p>
</aside>





## ジャンル別プロンプトテンプレート10選

ジャンルごとに「型」を持っておくと、毎回ゼロから考えなくて済む。よく使われる10パターンを紹介する。

### 1. リアル系ポートレート
```
portrait of a (年齢) (性別), (髪型), (表情), 
(服装), (背景), natural lighting, 
shot on Canon EOS R5, 85mm lens, f/1.8, 
photorealistic, skin texture, masterpiece
```

### 2. アニメイラスト
```
1girl, (髪色) hair, (瞳の色) eyes, (服装), 
(ポーズ), (背景), 
anime style, detailed face, vibrant colors, 
masterpiece, best quality
```

### 3. ファンタジー風景
```
(場所) landscape, (時間帯), (天候), 
mystical atmosphere, fantasy art, 
trending on artstation, by Greg Rutkowski, 
ultra wide angle, epic composition
```

### 4. サイバーパンク都市
```
cyberpunk city, neon lights, rain, 
flying cars, holographic billboards, 
blade runner style, cinematic, 
volumetric lighting, 8k
```

### 5. プロダクト写真
```
(商品名) on (背景), studio lighting, 
white background, product photography, 
high resolution, commercial photography
```

その他、6.水彩画風、7.油絵風、8.3Dレンダリング、9.チビキャラ、10.ピクセルアート も、上記と同じ「主題+詳細+スタイル+品質」構造で組める。重要なのは**スタイル指定の単語を1〜3個に絞る**こと。混ぜすぎると破綻する。

## ネガティブプロンプトの黄金テンプレート

良いプロンプトと同じくらい重要なのが、**ネガティブプロンプト**(出したくない要素の指定)だ。これを設定しないと、指が6本になったり、画質が粗くなったりする。

リアル系の汎用テンプレートはこれ。

```
lowres, bad anatomy, bad hands, text, error, 
missing fingers, extra digit, fewer digits, 
cropped, worst quality, low quality, 
normal quality, jpeg artifacts, signature, 
watermark, username, blurry, ugly, deformed
```

アニメ系ならさらに `realistic, photo, 3d` を追加すると、画風がブレない。SDXLでは効果が薄い単語もあるが、基本セットとして覚えておけば応用は効く。

ネガティブプロンプトのコツは、**「全部入り」より「対症療法」**。手の崩れが目立つなら手系の単語を、ぼやけが気になるなら`blurry`の重みを上げる、という調整型で運用するのが効率的だ。





<aside class="affiliate-card">
<div class="label">AI画像生成 講座 に関連する書籍・ツール</div>
<p>「AI画像生成 講座」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FAI%25E7%2594%25BB%25E5%2583%258F%25E7%2594%259F%25E6%2588%2590%2520%25E8%25AC%259B%25E5%25BA%25A7%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「AI画像生成 講座」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=AI%E7%94%BB%E5%83%8F%E7%94%9F%E6%88%90%20%E8%AC%9B%E5%BA%A7" target="_blank" rel="sponsored noopener">▶ Amazonで「AI画像生成 講座」関連を見る</a></p>
</aside>





## プロンプトを使いこなす5つのコツ

テンプレートを覚えたら、次は応用の引き出しを増やすフェーズに入る。実践で効くコツを5つ挙げる。

- **重み付けは1.2〜1.4まで**:`(word:1.5)`を超えると画像が破綻しやすい
- **長すぎるプロンプトは逆効果**:75トークンが1ブロック。詰め込みすぎると後半が無視される
- **アーティスト名は具体性が出る**:`by Alphonse Mucha`のように1〜2人指定で世界観が固まる
- **シード値を固定して比較**:同じシードでプロンプトを少しずつ変えると、どの単語が効いているか分かる
- **LoRAは1つから試す**:複数LoRAは干渉する。`<lora:name:0.7>`で重みも調整する

特に「シード固定+変数1つだけ変更」のA/Bテストは、海外のRedditでも推奨される王道の検証法。感覚ではなく実験でプロンプトの感覚が身についていく。

また、ChatGPTやClaudeに「このイメージをStable Diffusion用の英語プロンプトに変換して」と依頼すれば、構造化された呪文をすぐ生成できる。AI同士を組み合わせる発想は、2026年現在のクリエイター界隈では標準的なワークフローだ。

## まとめ

Stable Diffusionのプロンプトは、感覚やセンスではなく**「主題+詳細+スタイル+品質」の型**で組み立てれば誰でも再現できる。今回紹介した10ジャンルのテンプレートとネガティブプロンプトを保存しておけば、生成のたびにゼロから書く必要はなくなる。

最初は型をそのまま使い、慣れてきたら単語を入れ替えたり、重み付けで微調整したりして自分の「呪文ライブラリ」を育てていこう。テンプレートは出発点であり、ゴールではない。手を動かして、自分の表現に変えていく過程こそが、AI画像生成の本当の面白さだ。

## 関連記事

- [プロンプトを売る方法2026｜PromptBaseで月3万稼ぐ5ステップ](/auto-blog/blog/プロンプトを売る方法2026promptbaseで月3万稼ぐ5ステップ/)
- [プロンプト副業で月収10万円を狙う2026年の実践ロードマップ](/auto-blog/blog/プロンプト副業で月収10万円を狙う2026年の実践ロードマップ/)
- [Chain-of-Thought副業活用法5選｜AI思考連鎖で月10万稼ぐ](/auto-blog/blog/chain-of-thought副業活用法5選ai思考連鎖で月10万稼ぐ/)

<!-- CROSS_LINKS -->
## 他サイトの最新AI記事

- [ChatGPTの回答精度が話題に、Reddit r/ChatGPTで「正確すぎる」と共感の声が拡散](https://nayo126.github.io/ai-news-jp/posts/chatgpt-reddit-r-chatgpt.html)
- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html)
- [ChatGPTに「引退後の自分」を想像させる質問が話題｜AIの自己認識を引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/chatgpt-ai.html)

<!-- SEO_MESH_START -->

## 関連する記事

- [ChatGPTプロンプト本おすすめ7選｜2026年最新](https://nayo126.github.io/auto-blog/blog/chatgptプロンプト本おすすめ7選2026年最新/)
- [Claudeプロンプトの書き方7つのコツ｜返答3倍精度UP](https://nayo126.github.io/auto-blog/blog/claudeプロンプトの書き方7つのコツ返答3倍精度up/)
- [Flux AIで月5万円稼ぐ画像生成副業の始め方2026](https://nayo126.github.io/auto-blog/blog/flux-aiで月5万円稼ぐ画像生成副業の始め方2026/)

### 姉妹サイトの関連記事
- [ChatGPTで画像比較『left or right?』が話題、AI画像判定の使い方とは](https://nayo126.github.io/ai-news-jp/posts/chatgpt-left-or-right-ai.html) — AI News JP
- [ChatGPTで話題『Love at first prompt』Reddit投稿が示すAIとの関係性の変化](https://nayo126.github.io/ai-news-jp/posts/chatgpt-love-at-first-prompt-reddit-ai.html) — AI News JP
- [Claude AIの「Yes Man」問題：批判的フィードバックを引き出すプロンプト術](https://nayo126.github.io/ai-news-jp/posts/claude-ai-yes-man.html) — AI News JP

<!-- SEO_MESH_END -->
