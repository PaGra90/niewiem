rasa = 'spaniel bretonski'
rasa2 = 'spaniel bretonski'

lista_grupa_VII = [
        'pointer',
        'wyzel niemiecki',
        'wyzel weimarski',
        'pointer',
        'seter angielski',
]
lista_inne_grupy = [
        'owczarek niemiecki',
        'charcik wloski',
        'gryfonik',
        'pudel miniaturowy',
        'cocker spaniel',
        'york',
]

if rasa == rasa2:
        print('Najmniejszy posrod wyzlow, najlepszy towarzysz!')

elif rasa in lista_grupa_VII:
        print('Witaj wsrod posiadaczy wyzlow')
elif rasa in  lista_inne_grupy:
        print('Fajna rasa, ale wole wyzla')
else:
        print('Nie znam tej rasy')
