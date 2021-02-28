# pip install googletrans==4.0.0-rc1
from googletrans import Translator
import re
import time


# Avoid translating non-dialogue lines
number_pattern = '^[0-9]+$'
timestamp_re = '^[0-9:\-\>,\s]+$'

translator = Translator()
f = open(r"original-subtitle-file-path.srt", "r", encoding='utf-8')
temp = f.read().splitlines()
f.close()

f = open("name-of-output-file.srt", "w", encoding='utf-8')

for item in temp:
    if re.match(number_pattern, item):
        f.write(item + '\n')
        print(item)
        # Check progress
    elif re.match(timestamp_re, item):
        f.write(item + '\n')
    elif item == '':
        f.write('\n')
    else:
        item = re.sub('(</i>)|<i>', '', str(item))
        translation = translator.translate(str(item), src='en', dest='fr')
        item = translation.text
        # src: Original file's language, google translate will attempt to detect the language if not given
        # dest: Language to translate to
        # LANGUAGE CODES: https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
        if translation is None:
            f.write('\n')
            # If no translation was returned
        else:
            f.write(translation.text + '\n')
            print(translation.text + '\n')
            # Check translations
        time.sleep(3)
        # Avoid ip ban by waiting between translations, lower/remove at own risk

f.close()
