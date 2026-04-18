import re

def toza_matn(matnlar):
    toza_matnlar = []
    for matn in matnlar:
        toza_matn = re.sub(r'[^\w\s]', '', matn)
        toza_matnlar.append(toza_matn)
    return toza_matnlar

matnlar = ["Assalomu alaykum 🌟", "Python dasturlash tili @#"]
print(toza_matn(matnlar))
