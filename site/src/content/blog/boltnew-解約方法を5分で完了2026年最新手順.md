---
title: "bolt.new 解約方法を5分で完了｜2026年最新手順"
description: "bolt.newの解約手順を画面遷移に沿って解説。請求停止のタイミング、データ保持期間、解約前に確認すべき3つのポイントまで2026年5月時点の最新情報でまとめました。"
pubDate: 2026-05-23
category: "個人開発"
tags: ["bolt.new", "解約", "AI開発ツール", "サブスク管理"]
keyword: "bolt.new 解約"
draft: false
image: "/auto-blog/ogp/boltnew-解約方法を5分で完了2026年最新手順.png"
---

bolt.newを契約したものの「思ったより使わなかった」「Claude CodeやCursorに移行したい」と感じている人は少なくありません。月額20ドル〜200ドルの料金は、使わない月が続くと地味に効いてきます。

ただ、bolt.newの解約画面は英語表記でわかりにくく、「Cancel Subscription」を押した後に複数の確認ステップが続くため、途中で離脱してしまうケースもあります。気づいたら翌月も課金されていた、という声もよく見かけます。

この記事では、bolt.new(StackBlitz社が提供するAI Web開発プラットフォーム)の解約手順を、画面遷移に沿って具体的に解説します。あわせて、解約前に確認すべき3つのポイントと、解約後のデータ扱いについても整理しました。

## 結論：bolt.newの解約は管理画面から3クリックで完了

<!-- INLINE_IMG -->
![bolt.new 解約方法を5分で完了｜2026年最新手順 - 結論：bolt.newの解約は管理画面から3クリックで完了](/auto-blog/inline-images/boltnew-5-2026--0.jpg)


結論から書くと、bolt.newの解約はアカウント設定の「Subscription」ページから3クリックで完了します。電話やメールでの問い合わせは不要で、解約フォームのような長い理由入力もありません。

ただし、注意点が2つあります。

- **解約後も契約期間の終了日までは利用可能**（日割り返金は原則なし）
- **生成したプロジェクトデータは解約後30日間は保持**されるが、その後は段階的に閲覧制限がかかる

つまり「今月分はすでに払っているから損したくない」という場合は、契約更新日の前日までに解約手続きをすればOKです。逆に、年額プランで途中解約する場合は残り期間の返金が原則ないため、月額プランで様子を見る選択肢も検討する価値があります。

bolt.newは2024年後半から急速に伸びたAI開発ツールで、StackBlitzのWebContainer技術をベースにブラウザ上で完結する開発環境を提供しています。料金プランは無料枠(1日150kトークン程度)から、Pro($20)、Teams($30)、Enterprise相当まで複数あり、トークン消費の多い人ほど解約判断がシビアになります。


<aside class="affiliate-card">
<div class="label">bolt.new 代替 に関連する書籍・ツール</div>
<p>「bolt.new 代替」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2Fbolt.new%2520%25E4%25BB%25A3%25E6%259B%25BF%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「bolt.new 代替」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=bolt.new%20%E4%BB%A3%E6%9B%BF" target="_blank" rel="sponsored noopener">▶ Amazonで「bolt.new 代替」関連を見る</a></p>
</aside>


## bolt.new解約の具体手順｜画面遷移を5ステップで

<!-- INLINE_IMG -->
![bolt.new 解約方法を5分で完了｜2026年最新手順 - bolt.new解約の具体手順｜画面遷移を5ステップで](/auto-blog/inline-images/boltnew-5-2026--1.jpg)


実際の解約手順を順を追って説明します。所要時間は2〜3分程度です。

### ステップ1：bolt.newにログインしてプロフィール設定を開く

bolt.new(URL: bolt.new)にアクセスし、右上のプロフィールアイコンをクリックします。ドロップダウンメニューから「Settings」を選択。GitHub連携でログインしている場合は、GitHubアカウントの認証が再度求められることがあります。

### ステップ2：左サイドバーから「Subscription」を選択

設定画面の左サイドバーに「Profile」「Subscription」「Tokens」「Billing」といった項目が並んでいます。このうち「Subscription」をクリック。現在のプラン名、次回更新日、トークン残量が表示されます。

### ステップ3：「Manage Subscription」からStripeの管理画面に遷移

bolt.newの決済はStripeを利用しているため、解約自体はStripeの顧客ポータル経由で行います。「Manage Subscription」または「Manage Billing」というボタンをクリックすると、StackBlitz名義のStripeページに遷移します。

### ステップ4：「Cancel plan」をクリック

Stripeの画面で「現在のプラン」「次回請求日」「請求先カード情報」が確認できます。下部の「Cancel plan」または「プランをキャンセル」をクリック。

### ステップ5：キャンセル理由を選択して確定

簡単なアンケート(任意回答可)が表示されます。「Too expensive」「Not using it enough」「Found a better alternative」などの選択肢があり、選んでも選ばなくても進めます。最後に「Confirm cancellation」を押せば解約完了。登録メールアドレスに英語の確認メールが届きます。

メールの件名は「Your subscription has been canceled」で、契約期間の終了日が明記されています。この日付までは通常通り使えるので、必要なプロジェクトのエクスポートはこの期間内に済ませましょう。

## 解約前に必ず確認すべき3つのポイント

解約手続きは簡単ですが、その前にチェックしておきたい項目があります。後から「やっぱり戻したい」となっても、再契約時の特典価格が適用されないケースもあるためです。

### ポイント1：生成済みプロジェクトのエクスポート

bolt.newで作ったプロジェクトは、GitHub連携でリポジトリにプッシュするか、ZIPダウンロードで手元に保存できます。解約後30日を過ぎると編集ができなくなる可能性があるため、残しておきたいコードは事前にエクスポート推奨です。プロジェクト画面右上の「Download」または「Push to GitHub」から実行できます。

### ポイント2：年額プランの場合は返金条件を確認

月額プランは日割り返金なし、契約期間終了で停止という扱いが基本です。一方、年額プランで契約してから日が浅い場合、StackBlitzのサポート(support@stackblitz.com)に英語で連絡すると、ケースバイケースで部分返金に応じてくれることがあります。海外のRedditでは「契約3日以内の連絡で全額返金された」という報告も見られますが、公式の返金ポリシーに明記されているわけではないため、過度な期待は禁物です。

### ポイント3：一時停止(Pause)オプションの有無

2026年5月時点で、bolt.newには明確な「サブスク一時停止」機能はありません。「今月は使わないけど来月使うかも」という場合は、いったん解約してから必要になったタイミングで再契約する流れになります。ただし、解約と再契約を繰り返すと、初回登録時のプロモーションコードや割引が適用されないため、頻繁に使う見込みなら継続のほうが結果的に安いケースもあります。


<aside class="affiliate-card">
<div class="label">Claude Code に関連する書籍・ツール</div>
<p>「Claude Code」について実践的に学ぶための参考リソースを集めました。</p>
<p><a href="https://hb.afl.rakuten.co.jp/hgc/53e5cb42.c97243c2.53e5cb43.ebbba8e6/?pc=https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FClaude%2520Code%2F&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D" target="_blank" rel="sponsored noopener">▶ 楽天市場で「Claude Code」関連を見る</a></p>
<p><a href="https://www.amazon.co.jp/s?k=Claude%20Code" target="_blank" rel="sponsored noopener">▶ Amazonで「Claude Code」関連を見る</a></p>
</aside>


## 解約後のデータと再契約時の注意点

解約後、アカウント自体は無料プラン相当に戻ります。完全にアカウントを削除したい場合は別途「Delete Account」を実行する必要があり、こちらは設定画面の「Profile」最下部から手続きできます。

データ保持期間については、bolt.new公式ヘルプによると「解約後も一定期間はプロジェクトの閲覧が可能」とされていますが、編集や新規実行は無料プランの制限内に戻ります。具体的には1日あたりのトークン数が大幅に減るため、規模の大きいプロジェクトの継続開発は難しくなります。

再契約する場合は、同じメールアドレス・同じGitHub連携で再度サブスクライブすれば、以前のプロジェクトデータをそのまま引き継げます。ただし初回登録時のキャンペーン価格(年額プランの2ヶ月分無料など)は再適用されないため、解約のタイミングは慎重に判断したいところです。

代替ツールとして検討されることが多いのは、Claude Code(Anthropic公式のCLI型コーディング支援)、Cursor、v0、Replit Agentあたりです。bolt.newはブラウザ完結型のフルスタック開発に強い一方、ローカル開発を主軸にしたい人にはClaude CodeやCursorのほうが向いているという意見も増えています。

## まとめ：解約は3クリック、ただし事前準備を忘れずに

bolt.newの解約は、設定画面のSubscriptionからStripeポータルに進み、Cancel planを押すだけで完了します。日割り返金はない代わりに契約期間終了まで使えるため、更新日直前の手続きが無駄になりにくいタイミングです。

解約前にやっておきたいのは、プロジェクトデータのGitHubプッシュまたはZIP保存、年額プランなら返金条件の確認の2点。再契約時に過去データは引き継げますが、キャンペーン価格は再適用されないため、解約と再契約の頻度はほどほどに留めるのが賢明です。

## 関連記事

- [Bolt.new 解約方法を3分で完了！2026年最新手順と注意点](/auto-blog/blog/boltnew-解約方法を3分で完了2026年最新手順と注意点/)
- [bolt.new vs v0徹底比較2026年版｜個人開発で稼ぐ最適解](/auto-blog/blog/boltnew-vs-v0徹底比較2026年版個人開発で稼ぐ最適解/)
- [bolt.new 評判は本当？AI開発の実力を徹底検証2026](/auto-blog/blog/boltnew-評判は本当ai開発の実力を徹底検証2026/)

<!-- CROSS_LINKS -->
## 他サイトの最新AI記事

- [Claude CodeとAntigravity、Cursorはどこまで進化したか｜2026年AI開発ツール最新評価](https://nayo126.github.io/ai-news-jp/posts/claude-code-antigravity-cursor-2026-ai.html)
- [Sea LimitedがOpenAI Codexを全社導入、アジア発のエージェント型開発を加速](https://nayo126.github.io/ai-news-jp/posts/sea-limited-openai-codex.html)
- [ChatGPTにコードを貼ったら欠陥3つ即指摘されるReddit投稿が話題](https://nayo126.github.io/ai-news-jp/posts/chatgpt-3-reddit.html)

<!-- FAQ_START -->

## よくある質問

### bolt.newの解約後、残りの契約期間は使えますか？

解約後も契約期間の終了日までは通常通り利用できます。例えば月途中で解約しても、次回課金予定日までは全機能が使えますが、日割りでの返金は原則ありません。

### bolt.newを解約するとプロジェクトデータは消えますか？

解約後30日間はプロジェクトデータが保持されますが、その後は段階的に閲覧制限がかかります。重要なコードはGitHubへエクスポートするか、ZIPでダウンロードして保管してください。

### bolt.newの解約は日本語でできますか？

解約画面は英語表記のみです。Account Settings→Subscription→Cancel Subscriptionの3クリックで完了し、ブラウザの翻訳機能を使えば日本語表示でも操作できます。

### bolt.newからClaude CodeやCursorに乗り換えるメリットは？

Claude Code(月額20ドル〜)やCursor(月額20ドル)はローカル環境で動作し、bolt.newの最上位プラン200ドルと比べてコストを大幅に抑えられます。既存コードベースの編集にも強く、長期開発向きです。

<script type="application/ld+json">
{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "bolt.newの解約後、残りの契約期間は使えますか？", "acceptedAnswer": {"@type": "Answer", "text": "解約後も契約期間の終了日までは通常通り利用できます。例えば月途中で解約しても、次回課金予定日までは全機能が使えますが、日割りでの返金は原則ありません。"}}, {"@type": "Question", "name": "bolt.newを解約するとプロジェクトデータは消えますか？", "acceptedAnswer": {"@type": "Answer", "text": "解約後30日間はプロジェクトデータが保持されますが、その後は段階的に閲覧制限がかかります。重要なコードはGitHubへエクスポートするか、ZIPでダウンロードして保管してください。"}}, {"@type": "Question", "name": "bolt.newの解約は日本語でできますか？", "acceptedAnswer": {"@type": "Answer", "text": "解約画面は英語表記のみです。Account Settings→Subscription→Cancel Subscriptionの3クリックで完了し、ブラウザの翻訳機能を使えば日本語表示でも操作できます。"}}, {"@type": "Question", "name": "bolt.newからClaude CodeやCursorに乗り換えるメリットは？", "acceptedAnswer": {"@type": "Answer", "text": "Claude Code(月額20ドル〜)やCursor(月額20ドル)はローカル環境で動作し、bolt.newの最上位プラン200ドルと比べてコストを大幅に抑えられます。既存コードベースの編集にも強く、長期開発向きです。"}}]}
</script>

<!-- FAQ_END -->

<!-- SEO_MESH_START -->

## 関連する記事

- [Bolt.new 解約方法を3分で完了！2026年最新手順と注意点](https://nayo126.github.io/auto-blog/blog/boltnew-解約方法を3分で完了2026年最新手順と注意点/)
- [bolt.new vs v0徹底比較2026年版｜個人開発で稼ぐ最適解](https://nayo126.github.io/auto-blog/blog/boltnew-vs-v0徹底比較2026年版個人開発で稼ぐ最適解/)
- [bolt.new 評判は本当？AI開発の実力を徹底検証2026](https://nayo126.github.io/auto-blog/blog/boltnew-評判は本当ai開発の実力を徹底検証2026/)

### 姉妹サイトの関連記事
- [Claude CodeとAntigravity、Cursorはどこまで進化したか｜2026年AI開発ツール最新評価](https://nayo126.github.io/ai-news-jp/posts/claude-code-antigravity-cursor-2026-ai.html) — AI News JP

<!-- SEO_MESH_END -->
