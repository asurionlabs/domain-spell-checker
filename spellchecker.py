﻿###
# Domain Spell Checker is an AWS Lambda interface to perform spell checks using a domain 
# specific dictionary.
# 
# Copyright (C) 2018-2019  Asurion, LLC
#
# Domain Spell Checker is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Domain Spell Checker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Domain Spell Checker.  If not, see <https://www.gnu.org/licenses/>.
###

import json
from collections import defaultdict
import regex as re

def words(text):
    return re.findall("[a-z0-9'.]+", text.lower())


def train(features):
    model = defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

with open('dictionary.txt', 'r') as content_file:
    NWORDS = train(words(content_file.read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
MAX_WORDLENGTH = 23


def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)


def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)


def known(words): return set(w for w in words if w in NWORDS)


def correct(word):
    if (len(word) > MAX_WORDLENGTH):
        return word
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)


def check_spelling(word_input):
    wordlist = words(word_input)
    correct_wordlist = []
    output = {}
    for word in wordlist:
        output_word = correct(word)
        correct_wordlist.append(output_word)
    wordsout = " ".join(correct_wordlist)
    output['words'] = wordsout
    return output
