from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語音合成.閩南語音韻.變調判斷 import 變調判斷
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
import re

fo = open('changed_dash.txt', 'w')
with open('hanlo_tauphahji.txt', 'r') as f1:
    with open('text.txt', 'r') as f2:
        for x,y in zip(f1.readlines(),f2.readlines()):
            句物件 = 拆文分析器.對齊句物件(x.strip(), y.strip())
            結果句物件 = 句物件.轉音(臺灣閩南語羅馬字拼音, 函式='音值')
            判斷陣列 = 變調判斷.判斷(結果句物件)
            i = 0
            for 詞物件, 原底詞 in zip(結果句物件.網出詞物件(), 句物件.網出詞物件()):
                新陣列 = []
                for 字物件, 原底字 in zip(詞物件.內底字, 原底詞.內底字):
                    變調方式 = 判斷陣列[i]
                    if 變調方式 == 變調判斷.愛提掉的:
                        pass
                    else:
                        if 字物件.音 == (None,):
                            新陣列.append(原底字.khóopih字())
                        else:
                            字物件.音 = ''.join(變調方式.變調(字物件.音))
                            a = re.split(' |--|-', y.strip())[i][:-1] #變調前的拼音(需要的台羅拼音)，拿掉數字調
                            b = 字物件.音[-1]  # 變調後的拼音(含有不要的國際拼音)，保留數字調(數字10只留下0)
                            字物件.音 = a + b
                            if '--' in 字物件.型:
                                字物件.音 = '--' + 字物件.音
                            新陣列.append(字物件)
                    i += 1
                詞物件.內底字 = 新陣列
            target = 結果句物件.看音()
            fo.write(target + '\n')
f1.close()
f2.close()
fo.close()
