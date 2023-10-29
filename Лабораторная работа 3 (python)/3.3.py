


def count_letters(text):
    l1=l2=l3=l4=l5=l6=l7=l8=l9=l10=l11=l12=l13=l14=l15=l16=\
    l17=l18=l19=l20=l21=l22=l23=l24=l25=l26=l27=l28=l29=l30=\
    l31=l32=l33=0
    text.lower()
    l1=text.count('а')
    l2=text.count('б')
    l3=text.count('в')
    l4 = text.count('г')
    l5 = text.count('д')
    l6 = text.count('е')
    l7 = text.count('ё')
    l8 = text.count('ж')
    l9 = text.count('з')
    l10 = text.count('и')
    l11 = text.count('й')
    l12 = text.count('к')
    l13 = text.count('л')
    l14 = text.count('м')
    l15 = text.count('н')
    l16 = text.count('о')
    l17 = text.count('п')
    l18= text.count('р')
    l19 = text.count('с')
    l20 = text.count('т')
    l21 = text.count('у')
    l22 = text.count('ф')
    l23 = text.count('х')
    l24 = text.count('ц')
    l25= text.count('ч')
    l26 = text.count('ш')
    l27 = text.count('щ')
    l28 = text.count('ъ')
    l29 = text.count('ы')
    l30 = text.count('ь')
    l31 = text.count('э')
    l32 = text.count('ю')
    l33 = text.count('я')
    dict_letters={'a':l1,
                      'б':l2,
                      'в':l3,
                      'г':l4,
                      'д':l5,
                      'е':l6,
                      'ё':l7,
                      'ж': l8,
                      'з': l9,
                      'и': l10,
                      'й': l11,
                      'к': l12,
                      'л': l13,
                      'м': l14,
                      'н': l15,
                      'о': l16,
                      'п': l17,
                      'р': l18,
                      'с': l19,
                      'т': l20,
                      'у': l21,
                      'ф': l22,
                      'х': l23,
                      'ц': l24,
                      'ч': l25,
                      'ш': l26,
                      'щ': l27,
                      'ъ': l28,
                      'ы': l29,
                      'ь': l30,
                      'э': l31,
                      'ю': l32,
                      'я': l33}
    calculate_frequency(dict_letters)
    return dict_letters

def calculate_frequency (letters):
    total_letters = sum(letters.values())
    for i in letters.values():
        i=i/total_letters
        letters.values()[i]=round(i, 2)
    return letters


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
print(calculate_frequency(main_str))

# TODO Распечатайте в столбик букву и её частоту в тексте
