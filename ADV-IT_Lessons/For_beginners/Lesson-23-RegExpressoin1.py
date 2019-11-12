#Для использования RegExp нужна библиотека re
import re

mytext = "Vasya aaaaaaaaaa 1972 Kolya -1972, Olesya 1981, aaaaaaa@interl.com" \
         "bbbbbbbbbbbbbb@intel.com" \
         "Hello, Yandex" \
         "tutututt@giv.hot"

textlookfor = r"Yandex"
allresults = re.findall(textlookfor, mytext) # что / где ищем
print(allresults)