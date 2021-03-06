# -*- encoding: utf-8 -*-

__author__ = "David Michael Brown"
__status__ = "Development"

STRESS = u'\u02c8' 
PERIOD = u'\u2016'
COMMA = u'|'
SYLLABLE = u'.'

IPA_SYMBOLS = [u't',u'd',u's',u'z',u'ɬ',u'ɮ',u'θ',u'ð',u'ʃ',u'ʒ',u'c',u'ɟ',u'ç',u'ʝ',u'p',u'b',u'f',u'v',
				u'ɸ',u'β',u'k',u'ɡ',u'x',u'ɣ',u'q',u'ɢ',u'χ',u'ʁ',u'ħ',u'ʕ',u'h',u'ɦ',u'ʔ',u'ʧ',u'ʤ',
				u'ʦ',u'ʣ',u'm',u'n',u'ŋ',u'ɳ',u'ɲ',u'ɴ',u'l',u'ʎ',u'ɾ',u'r',u'ɹ',u'ʀ',u'j',u'w',
				u'ɥ',u'ɰ',u'i',u'ɪ',u'u',u'ʊ',u'e',u'ɛ',u'o',u'ɔ',u'a',u'æ',u'y',u'ʏ',u'ø',u'œ',u'ə',u'ɯ']


VOWELLS = [u'i',u'ɪ',u'u',u'ʊ',u'e',u'ɛ',u'o',u'ɔ',u'a',u'æ',u'y',u'ʏ',u'ø',u'œ',u'ə',u'ɯ']
GLIDES = [u'j',u'w',u'ɥ',u'ɰ']
VOWELLS_GLIDES = [u'j',u'w',u'ɥ',u'ɰ',u'i',u'ɪ',u'u',u'ʊ',u'e',u'ɛ',u'o',u'ɔ',u'a',u'æ',u'y',u'ʏ',u'ø',u'œ',u'ə',u'ɯ']
LIQUIDS = [u'l',u'ʎ',u'ɾ',u'r',u'ɹ',u'ʀ']
NASALS = [u'm',u'n',u'ŋ',u'ɳ',u'ɲ',u'ɴ']
NASALS_LIQUIDS = [u'm',u'n',u'ŋ',u'ɳ',u'ɲ',u'ɴ',u'l',u'ʎ',u'ɾ',u'r',u'ɹ',u'ʀ']
AFFRICATES = [u'ʧ',u'ʤ',u'ʦ',u'ʣ']
LARYNGEALS = [u'h',u'ɦ',u'ʔ']
NONCORONAL_OBSTRUENTS = [u'p',u'b',u'f',u'v',u'ɸ',u'β',u'k',u'ɡ',u'x',u'ɣ',u'q',u'ɢ',u'χ',u'ʁ',u'ħ',u'ʕ']
PALATAL_OBSTRUENTS = [u'c',u'ɟ',u'ç',u'ʝ']
CORONAL_OBSTRUENTS = [u't',u'd',u's',u'z',u'ɬ',u'ɮ',u'θ',u'ð',u'ʃ',u'ʒ']
CONSONANTS = [u't',u'd',u's',u'z',u'ɬ',u'ɮ',u'θ',u'ð',u'ʃ',u'ʒ',u'c',u'ɟ',u'ç',u'ʝ',u'p',u'b',u'f',u'v',
                u'ɸ',u'β',u'k',u'ɡ',u'x',u'ɣ',u'q',u'ɢ',u'χ',u'ʁ',u'ħ',u'ʕ',u'h',u'ɦ',u'ʔ',u'ʧ',u'ʤ',
                u'ʦ',u'ʣ',u'm',u'n',u'ŋ',u'ɳ',u'ɲ',u'ɴ',u'l',u'ʎ',u'ɾ',u'r',u'ɹ',u'ʀ']

DISTINCTIVE_FEATURES = {"cons":"Consonantal","dist":"Distributed","syll":"Syllabic",
                        "back":"Back","son":"Sonorant","ant":"Anterior",
                        "strid":"Strident","ATR":"Advance Tongue Root",
                        "cont":"Continuant","d_rel":"Delayed Release","low":"Low",
                        "CG":"Constricted Glottis","nasal":"Nasal","lab":"Labial",
                        "voi":"Voiced","tense":"Tense","lat":"Lateral",
                        "rnd":"Round","high":"high","cor":"Coronal",
                        "phar":"Pharengeal","dor":"dorsal","SG":"Spread Glottis"}

FEATURE_GROUPS = [CONSONANTS, CORONAL_OBSTRUENTS, PALATAL_OBSTRUENTS, NONCORONAL_OBSTRUENTS, 
                LARYNGEALS, AFFRICATES, NASALS_LIQUIDS, NASALS, LIQUIDS, VOWELLS_GLIDES, 
                GLIDES, VOWELLS ]

FMATRIX = {
"cons": 
["+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+",
"+", "+ ", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+",
"+", "+", "+", "+", "-", "-", "-", "+", "+", "+", "+", "+", "+", "+", "+",
"+", "+", "+", "+", "+", "+", "+", "+", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], 
"dist":
["-", "-", "-", "-", "-", "-", "-", "-", "+", "+", "+", "+", "+ ", "+", "0",
"0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
"0", "0", "0", "+", "+", "-", "-", "0", "-", "0", "-", "0", "0", "-", "0",
"-", "-", "-", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
"0", "0", "0", "0", "0", "0", "0", "0", "0"], 
"syll": 
["-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+",
"+", "+", "+", "+", "+"], 
"back": 
["0", "0", "0", "0", "0", "0", "0", "0",
"0", "0", "-", "-", "-", "-", "0", "0", "0", "0", "0", "0", "+", "+", "+",
"+", "+", "+", "+", "+", "0", "0", "0", "0", "0", "-", "-", "0", "0", "0",
"0", "+", "-", "-", "+", "0", "-", "0", "0", "0", "+", "-", "+", "-", "+",
"-", "-", "+", "+", "-", "-", "+", "+", "-", "-", "-", "-", "-", "-", "+",
"+"], 
"son": 
["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "+", "+", "+", "+", "+",
"+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+",
"+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"], 
"ant": 
["+", "+", "+",
"+", "+", "+", "+", "+", "-", "-", "-", "-", "-", "-", "0", "0", "0", "0",
"0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
"-", "-", "+", "+", "0", "+", "0", "-", "0", "0", "+", "0", "+", "+", "+",
"0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
"0", "0", "0", "0", "0", "0"], 
"strid": 
["-", "-", "+", "+", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "+", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "+", "+", "+",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-"], 
"ATR": 
["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
"0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
"0", "-", "-", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
"0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "+", "-", "+", "-",
"+", "-", "+", "-", "-", "-", "+", "-", "+", "-", "-", "-"], 
"cont": 
["-","-", "+", "+", "+", "+", "+", "+", "+", "+", "-", "-", "+ ", "+", "-", "-",
"+", "+", "+", "+", "-", "-", "+", "+", "-", "-", "+", "+", "+", "+", "+",
"+", "-", "+", "+", "+", "+", "-", "-", "-", "-", "-", "-", "+", "+", "+",
"+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+",
"+", "+", "+", "+", "+", "+", "+", "+"], 
"d_rel": 
["-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "+",
"+", "+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-"], 
"low": 
["0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
"-", "-", "-", "-", "0", "0", "0", "0", "0", "0", "-", "-", "-", "-", "-",
"-", "-", "-", "0", "0", "0", "0", "0", "-", "-", "0", "0", "0", "0", "-",
"-", "-", "-", "0", "-", "0", "0", "0", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "+", "+", "-", "-", "-", "-", "-", "-"], 
"CG":
["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-"], 
"nasal": ["-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "+", "+", "+", "+", "+", "+", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-"], 
"lab": 
["-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "+", "+", "+", "+", "+", "+", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "+", "+", "+", "+",
"+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
"voi": 
["-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+",
"-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-",
"-", "-", "+", "-", "-", "+", "-", "+", "+", "+", "+", "+", "+", "+", "+",
"+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+",
"+", "+", "+", "+", "+", "+", "+", "+", "+", "+"], 
"tense": 
["0", "0", "0",
"0", "0", "0", "0", "0", "0", "0", "-", "-", "-", "-", "0", "0", "0", "0",
"0", "0", "-", "-", "-", "-", "-", "-", "-", "-", "0", "0", "0", "0", "0",
"-", "-", "0", "0", "0", "0", "-", "-", "-", "-", "0", "-", "0", "0", "0",
"-", "-", "-", "-", "-", "+", "-", "+", "-", "+", "-", "+", "-", "-", "+",
"+", "-", "+", "-", "-", "+"], 
"lat": 
["-", "-", "-", "-", "+", "+", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "+", "+", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-"],
"rnd": 
["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
"0", "-", "-", "-", "-", "-", "-", "0", "0", "0", "0", "0", "0", "0", "0",
"0", "0", "0", "0", "0", "0", "0", "0", "0", "-", "0", "0", "0", "0", "0",
"0", "0", "0", "0", "0", "0", "-", "+", "+", "-", "-", "-", "+", "+", "-",
"-", "+", "+", "-", "-", "+", "+", "+", "-", "+", "+"], 
"high": 
["0", "0",
"0", "0", "0", "0", "0", "0", "0", "0", "+", "+", "+ ", "+", "0", "0", "0",
"0", "0", "0", "+", "+", "+", "+", "-", "-", "-", "-", "0", "0", "0", "0",
"0", "+", "+", "0", "0", "0", "0", "+", "-", "+", "-", "0", "+", "0", "0",
"0", "-", "+", "+", "+", "+", "+", "+", "+", "+", "-", "-", "-", "-", "-",
"-", "+", "+", "-", "-", "-", "+"], 
"cor": 
["+", "+", "+", "+", "+", "+", "+",
"+", "+", "+", "+", "+", "+ ", "+", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "+", "+", "+",
"-", "+", "-", "+", "-", "-", "+", "-", "+", "+", "+", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-"], 
"phar": 
["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "+", "+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "+", "+",
"+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"], 
"dor": 
["-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "+", "+ ", "+", "-", "-",
"-", "-", "-", "-", "+", "+", "+", "+", "+", "+", "+", "+", "-", "-", "-",
"-", "-", "+", "+", "-", "-", "-", "-", "+", "+", "+", "+", "-", "+", "-",
"-", "-", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+",
"+", "+", "+", "+", "+", "+", "+", "+"], 
"SG": 
["-", "-", "-", "-", "+", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "+", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
"-", "-", "-"]
}
