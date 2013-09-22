from 資料庫.整合.教育部閩南語常用詞辭典 import 揣釋義
from 資料庫.欄位資訊 import 國語臺員腔
from 資料庫.欄位資訊 import 語句
from 資料庫.整合.教育部閩南語常用詞辭典 import 教育部閩南語辭典名
from 資料庫.整合.教育部閩南語常用詞辭典 import 教育部閩南語辭典地區
from 資料庫.整合.教育部閩南語常用詞辭典 import 教育部閩南語辭典年代
from 資料庫.欄位資訊 import 版本正常
from 資料庫.整合.整合入言語 import 加文字佮版本
from 資料庫.整合.整合入言語 import 揣文字上大流水號
from 資料庫.整合.教育部閩南語常用詞辭典 import 用釋義揣例句
from 資料庫.整合.教育部閩南語常用詞辭典 import 用主碼號揣流水號
from 資料佮語料匯入整合.教育部臺灣閩南語常用詞辭典.造字處理 import 共造字換做統一碼表示法
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.轉物件音家私 import 轉物件音家私
from 資料庫.整合.整合入言語 import 用流水號揣文字
from 資料庫.欄位資訊 import 閩南語
from 資料庫.欄位資訊 import 義近
from 資料庫.欄位資訊 import 袂當替換
from 資料庫.整合.整合入言語 import 加關係
from 資料庫.整合.教育部閩南語常用詞辭典 import 設定詞性
from 資料庫.整合.整合入言語 import 揣關係上大流水號
from 資料庫.整合.教育部閩南語常用詞辭典 import 詞性對照表
from 資料庫.整合.教育部閩南語常用詞辭典 import 設定來源
from 資料庫.整合.教育部閩南語常用詞辭典 import 文字無音設定
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 資料庫.整合.教育部閩南語常用詞辭典 import 用流水號揣腔口
from 資料庫.欄位資訊 import 文字組合符號
from 資料庫.欄位資訊 import 會當替換
from 資料庫.整合.整合入言語 import 設定文字組合


初胚工具 = 文章初胚工具()
分析器 = 拆文分析器()
轉音家私 = 轉物件音家私()
來源資料 = []
for 釋義編號, 主編號, 義項順序, 詞性, 釋義 in 揣釋義():
	print(釋義編號)
	if 主編號 == 5843:
		if 義項順序 == 0:
			if 釋義 == '麻雀。見【粟鳥仔】<font class=tlsound>tshik-tsiáu-á </font>條。':
				釋義 = '麻雀。見【粟鳥仔】tshik-tsiáu-á 條。'
		else:
			continue

	加文字佮版本(教育部閩南語辭典名, 語句, 國語臺員腔, 教育部閩南語辭典地區,
		教育部閩南語辭典年代, 釋義, '', 版本正常)
	釋義流水號 = 揣文字上大流水號()
	來源資料.append((釋義流水號, 主編號))
	例句資料 = 用釋義揣例句(釋義編號)
	臺語流水號集 = 用主碼號揣流水號(主編號)
	for 例句, 標音, 例句翻譯 in 例句資料:
		if 例句翻譯 == '':
			例句翻譯 = 例句
		加文字佮版本(教育部閩南語辭典名, 語句, 國語臺員腔, 教育部閩南語辭典地區,
			教育部閩南語辭典年代, 例句翻譯, '', 版本正常)
		國語例句流水號 = 揣文字上大流水號()
		來源資料.append((國語例句流水號, 主編號))


		if 標音[0].isupper():
			種類 = '語句'
		else:
			種類 = '字詞'

		例句 = 共造字換做統一碼表示法(例句)
		組字式型 = 初胚工具.符號邊仔加空白(例句).strip()
		標音 = 標音.replace('--', '-0')
		標音 = 初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 標音)
		標音 = 初胚工具.符號邊仔加空白(標音).strip()
		原音句物件 = 分析器.產生對齊句(組字式型, 標音)
		轉音家私.轉做標準音標(臺灣閩南語羅馬字拼音, 原音句物件)

		例句內底漢字 = None
		例句內底音標 = None
		for 臺語流水號 in 臺語流水號集:
			文字資料 = 用流水號揣文字(臺語流水號[0])
			if 文字資料[2].startswith(閩南語):
				if 文字資料[6] in 例句 and 文字資料[7] in 標音:
					例句內底漢字 = 文字資料[6]
					例句內底音標 = 文字資料[7]

		if 例句內底漢字 == None or 例句內底音標 == None:
			raise 解析錯誤('揣無元素')
		# 共句切開
		漢字頭前, 漢字後壁 = 例句.split(例句內底漢字, 1)
		音標頭前, 音標後壁 = 標音.split(例句內底音標, 1)
		分析器.產生對齊句(漢字頭前, 音標頭前)
		分析器.產生對齊句(漢字後壁, 音標後壁)

		for 臺語流水號 in 臺語流水號集:
			文字資料 = 用流水號揣文字(臺語流水號[0])
			if not 文字資料[2].startswith(閩南語):
				continue

			加關係(臺語流水號[0], 釋義流水號, 義近, 袂當替換)
			解釋關係流水號 = 揣關係上大流水號()
			設定詞性(解釋關係流水號, 詞性對照表[詞性])

			臺語資料腔口 = 用流水號揣腔口(臺語流水號[0])

			加文字佮版本(教育部閩南語辭典名, 種類, 臺語資料腔口, 教育部閩南語辭典地區,
				教育部閩南語辭典年代, 例句.replace(例句內底漢字, 文字資料[6], 1),
				標音.replace(例句內底音標, 文字資料[7], 1), 版本正常)

			例句流水號 = 揣文字上大流水號()
			設定文字組合(例句流水號, 文字組合符號 + str(解釋關係流水號) + 文字組合符號)
# 			設定編修狀況(例句流水號, 臺語腔口 + "的例句")
			加關係(例句流水號, 國語例句流水號, 義近, 會當替換)
			加關係(國語例句流水號, 例句流水號, 義近, 會當替換)

文字無音設定()
for 來源流水號, 來源主編號 in 來源資料:
	設定來源(來源流水號, 來源主編號)
