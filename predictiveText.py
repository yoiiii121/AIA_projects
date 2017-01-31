# coding=utf-8
import re
import string
def read_text():
    fichero = "Nietzshe - Mas alla del bien y del mal.txt"
    infile = open("./" + fichero, encoding="utf8")
    cad = []
    for i in infile:
        cad.append(i + "\n")
    infile.close()
    return cad
def count_letters():
    for i in text:
        for c in i:
            stadistics[c.lower()] += 1
def predict_letter(num):
    charList = keyboard[num]
    stadisticsList = []
    res = 'a'
    for letter in charList:
        stadisticsList.append(stadistics[letter])
        res = stadisticsList.index(max(stadisticsList))
    return res

text = re.findall(r"[\w.]+", str(read_text()))
file = "Nietzshe - Mas alla del bien y del mal.txt"
Nletter = sum((len(i) for i in text))
keyboard = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'ñ', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}
stadistics = {}
for i in keyboard.values():
    for v in i:
        stadistics[v] = 0
count_letters()
print(predict_letter(4))