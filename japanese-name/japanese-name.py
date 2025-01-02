inp = input("Enter your name/word: ")
name = inp.lower()

# Replacement rules and transliteration definitions
double_letter = ("aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", "kk", "ll", "mm", "nn", "oo", "pp", "qq", "rr", "ss", "tt", "uu", "vv", "ww", "xx", "yy", "zz")
consonant = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z")
exceptions = {
    "wi": "bi", "vi": "bi", "ph": "f", "ds": "ts", "uc": "us", "l": "r", "ck": "k", "v": "w", "sch": "sh",
    "ing": "in", "ny": "nu", "ä": "e", "ü": "u", "ö": "o", "q": "k", "j": "y", "c": "k", "tz": "z", "gh": "h", "th": "s"
}

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
for exception, insertion in exceptions.items():
    name = name.replace(exception, insertion)

# Final rules for consonants and endings
if name and name[-1] in consonant:  # Check if the last character is a consonant
    name += "u"

if name.endswith("r"):
    name = name[:-1] + "ru"

# Transliteration to Katakana
katakana_name = ""
original_name = name

while len(name) > 0:
    # Prioritize longer substrings first
    for size in range(3, 0, -1):  # Check substrings of size 3, 2, 1
        current_slice = name[:size]
        if current_slice in katakana_translation:
            katakana_name += katakana_translation[current_slice]
            name = name[size:]
            break
    else:
        # If no match, add the first character as it is
        katakana_name += name[0]
        name = name[1:]

# Final output
print(f'''
Your original name/word: {inp}
Japanese pronunciation: {original_name}
Katakana translation: {katakana_name}
''')
