# -*- coding: utf-8 -*-
"""WordReplacement_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DLdFxHA61ur-K56BZp_OTPv-Ibw98Mgb

# **Word Replacement App**
"""

def replace_word():
  str=input("Enter the Paragraph or statement:")
  word_to_replace=input("Enter the Word to Replace:")
  word_replacement=input("Enter the word replacement:")
  print(str.replace(word_to_replace ,word_replacement))

replace_word()