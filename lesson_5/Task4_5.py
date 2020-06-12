import googletrans
t = open ('text_4.txt', 'r', encoding='utf-8')
contents = t.read()
from googletrans import Translator
t_translate = Translator()
result = t_translate.translate(contents, dest='ru')
print(result.text)
with open ('text_4_1.txt', 'x', encoding='utf-8') as t:
    t.write(result.text)


