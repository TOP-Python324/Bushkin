scores_letters = {
    1: 'АВЁЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}
alfavit ={}
for key,value in scores_letters.items():
    alfavit.update({}.fromkeys(value,key))
amount = sum([alfavit[char]  for char in (input()).upper()])
print(amount)

# синхрофазотрон
# 29