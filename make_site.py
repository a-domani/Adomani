from pathlib import Path
root=Path('/mnt/data/adomani_site')
nav='''<header><div class="nav"><div class="brand">訪問看護ステーションあどまーに<small>また明日を支える訪問看護</small></div><nav class="navlinks"><a href="index.html">トップ</a><a href="features.html">特徴</a><a href="services.html">サービス</a><a href="diseases.html">疾患・医療的ケア</a><a href="system.html">制度</a><a href="recruit.html">採用</a><a href="contact.html">お問い合わせ</a></nav></div></header>'''
foot='''<footer><div class="footer-inner"><strong>訪問看護ステーションあどまーに</strong><br>〒000-0000 石川県○○市○○　TEL：000-0000-0000<br>営業時間：平日 9:00〜17:00　24時間対応体制あり<br><small>© Adomani Home Nursing Station</small></div></footer>'''
def page(title, body, desc=''):
    return f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}｜訪問看護ステーションあどまーに</title><meta name="description" content="{desc or title}"><link rel="stylesheet" href="style.css"></head><body>{nav}<div class="page-title"><div><h1>{title}</h1></div></div><main>{body}</main>{foot}</body></html>'''

def sec(h, content): return f'<section class="section"><h2>{h}</h2>{content}</section>'
def cards(items):
    return '<div class="grid">' + ''.join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h,p in items) + '</div>'
def ul(items): return '<ul class="list">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'

index='''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>訪問看護ステーションあどまーに｜金沢・野々市・白山・津幡・内灘</title><meta name="description" content="神経難病、医療的ケア、緩和ケア、皮膚・排泄ケアを強みとする訪問看護ステーション。"><link rel="stylesheet" href="style.css"></head><body>'''+nav+'''<section class="hero"><div class="hero-inner"><div class="eyebrow">金沢市・野々市市・白山市・津幡町・内灘町</div><h1>また明日を、安心して迎えるために。</h1><p>訪問看護ステーションあどまーには、神経難病や医療的ケアを強みとしながら、病気の種類にかかわらず、その人らしい生活を支える訪問看護を行います。</p><div class="buttons"><a class="btn" href="contact.html">相談する</a><a class="btn secondary" href="features.html">特徴を見る</a></div></div></section><main>'''
index+=sec('あどまーにの特徴', cards([
('神経難病への支援','筋萎縮性側索硬化症、パーキンソン病、多系統萎縮症など、長期支援が必要な方の在宅療養を支えます。'),
('医療的ケアに対応','吸引、気管切開、人工呼吸器、胃ろう、在宅中心静脈栄養などに対応します。'),
('重度訪問介護との連携','生活を支える重度訪問介護と、医療を支える訪問看護が連携し、切れ目ない支援を目指します。'),
('専門資格を活かした支援','皮膚・排泄ケア認定看護師、緩和ケア認定看護師の専門性を活かします。')]))
index+=sec('対応エリア', '<p>金沢市、野々市市、白山市、津幡町、内灘町を中心に訪問します。その他の地域についてもご相談ください。</p>')
index+=sec('まずはご相談ください','<div class="notice">訪問看護を利用するか決まっていない段階でも構いません。退院前の相談、制度利用、医療的ケア、介護負担について一緒に整理します。</div>')
index+='</main>'+foot+'</body></html>'
(root/'index.html').write_text(index,encoding='utf-8')

features=sec('神経難病を強みとしています','<p>あどまーには神経難病への支援を強みとしています。病状の変化に合わせて、医療的ケア、介護、障害福祉、住環境、ご家族支援まで生活全体を見据えて支援します。</p>')
features+=sec('神経難病だけを支援するわけではありません','<p>がん、慢性疾患、医療的ケアが必要な方、褥瘡やストーマ管理が必要な方など、さまざまな在宅療養に対応します。</p>')
features+=sec('主な特徴', cards([('24時間対応','緊急時には必要に応じて電話相談や緊急訪問を行います。'),('退院前から相談可能','退院前カンファレンスへの参加や在宅移行の準備に対応します。'),('皮膚・排泄ケア','褥瘡、ストーマ、排尿・排便管理、失禁関連皮膚炎に対応します。'),('緩和ケア','痛み、呼吸苦、不安などを含め、ご本人とご家族を支援します。')]))
(root/'features.html').write_text(page('あどまーにの特徴',features),encoding='utf-8')

services=sec('サービス内容', cards([('健康状態の観察','体調管理、血圧や脈拍の確認、病状変化の早期発見を行います。'),('医療的ケア','吸引、気管切開管理、人工呼吸器管理、胃ろう管理、在宅中心静脈栄養、点滴管理に対応します。'),('日常生活支援','清潔ケア、排泄支援、食事支援、介護方法の相談を行います。'),('ご家族支援','介護負担、制度利用、緊急時対応について一緒に考えます。')]))
services+=sec('ご利用の流れ','<ol><li>お問い合わせ</li><li>ご相談・ご説明</li><li>主治医との連携</li><li>訪問開始</li><li>継続的なサポート</li></ol>')
services+=sec('訪問看護でできないこと','<p>長時間の見守り、家事代行、買い物代行、掃除や洗濯のみの支援、通院付き添いのみなどは訪問看護だけでは対応できません。必要に応じて訪問介護や重度訪問介護などと連携します。</p>')
(root/'services.html').write_text(page('サービス内容・ご利用の流れ',services),encoding='utf-8')

diseases=sec('疾患への支援', cards([('筋萎縮性側索硬化症','呼吸管理、胃ろう、人工呼吸器、意思決定支援、重度訪問介護との連携を含めて支援します。'),('パーキンソン病','転倒予防、服薬管理、嚥下支援、排便管理、生活環境調整を行います。'),('多系統萎縮症','血圧変動、排尿・排便管理、嚥下障害、呼吸障害に対応します。'),('進行性核上性麻痺','転倒予防、嚥下支援、コミュニケーション支援、ご家族支援を行います。'),('脊髄小脳変性症','ふらつき、転倒、嚥下障害、排尿・排便の悩みに対応します。')]))
diseases+=sec('医療的ケア', cards([('人工呼吸器','呼吸状態の観察、機器管理、肺炎予防、口腔ケア、緊急時対応を支援します。'),('気管切開','カニューレ管理、吸引、肺炎予防、窒息・閉塞予防に取り組みます。'),('吸引','口腔内・鼻腔・気管内吸引、排痰ケア、窒息予防、ご家族への指導を行います。'),('胃ろう','胃ろう管理、栄養管理、誤嚥性肺炎予防、口から食べる楽しみの支援を行います。'),('在宅中心静脈栄養','カテーテル管理、輸液管理、感染予防、感染兆候の早期発見を行います。')]))
diseases+=sec('専門ケア', cards([('皮膚・排泄ケア','褥瘡、失禁関連皮膚炎、排尿・排便管理、人工肛門・人工膀胱に対応します。'),('緩和ケア','痛み、呼吸苦、倦怠感、不安、不眠などに対応し、自宅での療養を支えます。'),('在宅看取り','人生の最終段階をご自宅で過ごしたい方とご家族を支援します。')]))
(root/'diseases.html').write_text(page('疾患・医療的ケア',diseases),encoding='utf-8')

system=sec('利用できる主な制度', cards([('医療保険・介護保険','年齢、病気、介護認定の有無などによって利用する制度が異なります。'),('指定難病医療費助成制度','指定難病の方は、所得や病状に応じて医療費負担が軽減される場合があります。'),('身体障害者手帳','障害福祉サービス、補装具、日常生活用具などにつながる場合があります。'),('障害福祉サービス','居宅介護、重度訪問介護、短期入所、日常生活用具給付などを利用できる場合があります。')]))
system+=sec('重度訪問介護との連携','<p>神経難病や人工呼吸器を使用している方が地域で生活を続けるためには、訪問看護だけでは十分ではありません。あどまーには重度訪問介護事業所との情報共有を大切にし、医療と生活を切れ目なく支えます。</p>')
(root/'system.html').write_text(page('保険・制度について',system),encoding='utf-8')

recruit=sec('採用情報','<p>訪問看護ステーションあどまーにでは、一緒に利用者さんの生活を支える仲間を募集しています。</p>')
recruit+=sec('こんな方を歓迎します', ul(['一人ひとりと丁寧に関わりたい方','神経難病看護に興味がある方','在宅医療に興味がある方','利用者さんやご家族の思いを大切にしたい方']))
recruit+=sec('働く特徴', cards([('専門性を学べる','神経難病、緩和ケア、皮膚・排泄ケア、医療的ケアについて学べる環境を目指します。'),('多職種連携','医師、重度訪問介護、相談支援専門員、ケアマネジャーなどと連携します。'),('暮らしを支える看護','病気だけではなく、その人の生活を支える訪問看護を大切にします。')]))
(root/'recruit.html').write_text(page('採用情報',recruit),encoding='utf-8')

about=sec('あどまーにについて','<p>「あどまーに」はイタリア語で「また明日」を意味します。安心して今日を過ごし、また明日を迎えること。その当たり前の日常を支える訪問看護を目指しています。</p>')
about+=sec('代表挨拶','<p>訪問看護ステーションあどまーにのホームページをご覧いただき、ありがとうございます。</p><p>私たちは、病気や障害があっても住み慣れた地域で安心して暮らし続けられるよう支援したいという思いから、訪問看護ステーションあどまーにを開設しました。</p><p>あどまーには神経難病への支援を強みとしています。しかし、支援するのは神経難病の方だけではありません。がん、慢性疾患、医療的ケアが必要な方など、さまざまな在宅療養に対応しています。</p><p>地域の皆さまにとって、困った時に気軽に相談できる存在でありたいと考えています。</p>')
about+=sec('会社概要','<table><tr><th>事業所名</th><td>訪問看護ステーションあどまーに</td></tr><tr><th>所在地</th><td>〒000-0000 石川県○○市○○</td></tr><tr><th>電話番号</th><td>000-0000-0000</td></tr><tr><th>営業時間</th><td>平日 9:00〜17:00</td></tr><tr><th>緊急対応</th><td>24時間対応</td></tr><tr><th>訪問エリア</th><td>金沢市・野々市市・白山市・津幡町・内灘町</td></tr></table>')
(root/'about.html').write_text(page('あどまーにについて',about),encoding='utf-8')

contact=sec('お問い合わせ','<p>訪問看護の利用についてのご相談やご質問は、お気軽にお問い合わせください。</p><div class="notice"><p>TEL：000-0000-0000</p><p>受付時間：平日 9:00〜17:00</p><p>メール：example@example.com</p></div>')
contact+=sec('お問い合わせフォーム項目', ul(['お名前','お電話番号','メールアドレス','お問い合わせ内容']))
(root/'contact.html').write_text(page('お問い合わせ',contact),encoding='utf-8')

# README
(root/'README.md').write_text('''# 訪問看護ステーションあどまーに GitHub Pages用サイト\n\n## 公開方法\n1. GitHubでリポジトリを作成\n2. このフォルダ内のファイルをすべてアップロード\n3. Settings → Pages → Branch を `main` / `/root` に設定\n4. 数分後に `https://ユーザー名.github.io/リポジトリ名/` で公開\n\n## 公開前に差し替える項目\n- 住所\n- 電話番号\n- メールアドレス\n- 代表者名\n- 管理者名\n- 指定事業所番号\n- ロゴ画像\n- 写真\n- Googleフォームまたは問い合わせフォームURL\n''',encoding='utf-8')
