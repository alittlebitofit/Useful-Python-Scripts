#! /usr/bin/python

import pyperclip

text = pyperclip.paste()
pyperclip.copy(text[::-1])

print(text)
print()
print(pyperclip.paste())
