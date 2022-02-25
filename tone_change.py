from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語音合成.閩南語音韻.變調判斷 import 變調判斷
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音

f = open('text.txt')
fo = open('changed.txt', 'w')
for line in f.readlines():
    print('變調前：' + line.strip())
    taibun = '###' + line
    taibun = taibun.replace('gua2', '我').replace('--li2', '--裡').replace('li2', '你')\
        .replace('--i1 ', '--伊 ').replace(' i1--', ' 伊--').replace('--i1\n', '--伊\n')\
        .replace('-i1 ', '-伊 ').replace(' i1-', ' 伊-').replace('-i1\n', '-伊\n')\
        .replace(' i1 ', ' 伊 ').replace('###i1', '###伊')\
        .replace('lan2', '咱').replace('gun2', '阮').replace('lin2', '恁')\
        .replace('--in1 ', '--𪜶 ').replace(' in1--', ' 𪜶--').replace('--in1\n', '--𪜶\n')\
        .replace('-in1 ', '-𪜶 ').replace(' in1-', ' 𪜶-').replace('-in1\n', '-𪜶\n')\
        .replace(' in1 ', ' 𪜶 ').replace('###in1', '###𪜶')\
        .replace('--a2 ', '--仔 ').replace(' a2--', ' 仔--').replace('--a2\n', '--仔\n')\
        .replace('-a2 ', '-仔 ').replace(' a2-', ' 仔-').replace('-a2\n', '-仔\n')\
        .replace(' a2 ', ' 仔 ').replace('###a2', '###仔')\
        .replace('khi3', '去').replace('teh4', '咧')\
        .replace('--e5 ', '--的 ').replace(' e5--', ' 的--').replace('--e5\n', '--的\n')\
        .replace('-e5 ', '-的 ').replace(' e5-', ' 的-').replace('-e5\n', '-的\n')\
        .replace(' e5 ', ' 的 ').replace('###e5', '###的') #.replace('guan2', '阮')
    taibun = taibun.replace('###', '').strip()
    句物件 = 拆文分析器.對齊句物件(taibun, line.strip())
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
                    a = 字物件.音[:len(字物件.音) - 1]  # 變調後的拼音(含有不要的國際拼音)，拿掉數字調
                    b = 字物件.型.replace('我', 'gua2').replace('裡', 'li2').replace('你', 'li2').replace('伊', 'i1')\
                        .replace('咱', 'lan2').replace('阮', 'gun2').replace('恁', 'lin2').replace('𪜶', 'in1')\
                        .replace('仔', 'a2').replace('去', 'khi3').replace('咧', 'teh4').replace('的', 'e5')
                    b = b[:len(b) - 1]  # 變調前的拼音(需要的台羅拼音)，拿掉數字調
                    字物件.音 = 字物件.音.replace(a, b)
                    新陣列.append(字物件)
            i += 1
        詞物件.內底字 = 新陣列
    target = 結果句物件.看音()
    print('變調後：' + target)
    fo.write(target + '\n')
f.close()
fo.close()
