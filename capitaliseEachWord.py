#! /usr/bin/python

import pyperclip

text = pyperclip.paste()
pyperclip.copy(text.title())

print(text)
print()
print(pyperclip.paste())
