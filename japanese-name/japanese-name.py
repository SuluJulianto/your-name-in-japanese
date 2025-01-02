inp = input("Enter your name/word: ")
name = inp.lower()

# Replacement rules and transliteration definitions
double_letter = ("aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", "kk", "ll", "mm", "nn", "oo", "pp", "qq", "rr", "ss", "tt", "uu", "vv", "ww", "xx", "yy", "zz")
consonant = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z")
exceptions = ("wi", "vi", "ph", "ds", "uc", "l", "ck", "v", "sch", "ing", "ny", "ä", "ü", "ö", "q", "j", "c", "tz", "gh", "th")
insertions = ("bi", "bi", "f", "ts", "us", "r", "k", "w", "sh", "in", "nu", "e", "u", "o", "k", "y", "k", "z", "h", "s")

# Katakana transliteration dictionary
katakana_translation = {
    'a': 'ア', 'i': 'イ', 'u': 'ウ', 'e': 'エ', 'o': 'オ',
    'ka': 'カ', 'ki': 'キ', 'ku': 'ク', 'ke': 'ケ', 'ko': 'コ',
    'sa': 'サ', 'shi': 'シ', 'su': 'ス', 'se': 'セ', 'so': 'ソ',
    'ta': 'タ', 'chi': 'チ', 'tsu': 'ツ', 'te': 'テ', 'to': 'ト',
    'na': 'ナ', 'ni': 'ニ', 'nu': 'ヌ', 'ne': 'ネ', 'no': 'ノ',
    'ha': 'ハ', 'hi': 'ヒ', 'fu': 'フ', 'he': 'ヘ', 'ho': 'ホ',
    'ma': 'マ', 'mi': 'ミ', 'mu': 'ム', 'me': 'メ', 'mo': 'モ',
    'ya': 'ヤ', 'yu': 'ユ', 'yo': 'ヨ',
    'ra': 'ラ', 'ri': 'リ', 'ru': 'ル', 're': 'レ', 'ro': 'ロ',
    'wa': 'ワ', 'wo': 'ヲ', 'n': 'ン',
    'ga': 'ガ', 'gi': 'ギ', 'gu': 'グ', 'ge': 'ゲ', 'go': 'ゴ',
    'za': 'ザ', 'ji': 'ジ', 'zu': 'ズ', 'ze': 'ゼ', 'zo': 'ゾ',
    'da': 'ダ', 'di': 'ヂ', 'du': 'ヅ', 'de': 'デ', 'do': 'ド',
    'ba': 'バ', 'bi': 'ビ', 'bu': 'ブ', 'be': 'ベ', 'bo': 'ボ',
    'pa': 'パ', 'pi': 'ピ', 'pu': 'プ', 'pe': 'ペ', 'po': 'ポ',
}

# Process replacement rules for "Japanese pronunciation"
for i in double_letter:
    if i in name:
        name = name.replace(i, i[0])

for i in range(len(exceptions)):
    if exceptions[i] in name:
        name = name.replace(exceptions[i], insertions[i])

# Final rules for consonants and endings
if name.endswith(consonant):
    name += "u"

if name.endswith("r"):
    name = name[:-1] + "ru"

# Transliteration to Katakana
katakana_name = ""
original_name = name

while len(name) > 0:
    for size in range(2, 0, -1):
        current_slice = name[:size]
        if current_slice in katakana_translation:
            katakana_name += katakana_translation[current_slice]
            name = name[size:]
            break
    else:
        katakana_name += name[0]
        name = name[1:]

# Final output
print(f'''
Your original name/word: {inp}
Japanese pronunciation: {original_name}
Katakana translation: {katakana_name}
''')
