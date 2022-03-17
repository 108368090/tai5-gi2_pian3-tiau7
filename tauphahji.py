from tauphahji_cmd import tàuphahjī

with open('text.txt', 'r') as rf:
    for text in rf.readlines():
        a = tàuphahjī(text.strip())
        b = a['漢字']
        f = open('hanlo_tauphahji.txt', 'a')
        print(b, file=f)
        print(b)
f.close()
