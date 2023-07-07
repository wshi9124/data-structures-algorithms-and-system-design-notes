"""
Consider a string, sentence of words separated by spaces where each word is a substring consisting of english alphebetic letters only. 
Find first word that has even length and is greater than any other word of even length.
Return "00" if there is no answer

ex: sentence = "it is a pleasant day today"
output: pleasant
"""

def isEvenStr(self, str):
    return str % 2 == 0

def longestEvenWord(self, sentence):
    splitSentence = sentence.split(" ")
    foundWord = ""
    currMaxLen = -1

    for word in splitSentence:
        if isEvenStr(word) and len(word) > currMaxLen:
            foundWord = word
            currMaxLen = len(word)
    return foundWord if foundWord != "" else "00"

