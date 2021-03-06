#### PATTERN | VECTOR | WORDLIST #####################################################################
# Copyright (c) 2010 University of Antwerp, Belgium
# Author: Tom De Smedt <tom@organisms.be>
# License: BSD (see LICENSE.txt for details).
# http://www.clips.ua.ac.be/pages/pattern

######################################################################################################

import os

try:
    MODULE = os.path.dirname(__file__)
except:
    MODULE = ""

class Wordlist:
    
    def __init__(self, name, data=[]):
        """ Lazy read-only list of words.
        """
        self._name = name
        self._data = data
    
    def _load(self):
        if not self._data:
            self._data = open(os.path.join(MODULE, self._name+".txt")).read().split(", ")
        
    def __repr__(self):
        self._load(); return repr(self._data)
    def __iter__(self):
        self._load(); return iter(self._data)
    def __len__(self):
        self._load(); return len(self._data)
    def __getitem__(self, i):
        self._load(); return self._data[i]
    def __contains__(self, w):
        self._load(); return w in self._data
    def __add__(self, iterable):
        self._load(); return Wordlist(None, data=sorted(self._data + list(iterable)))

ACADEMIC  = Wordlist("academic")  # English academic words.
BASIC     = Wordlist("basic")     # English basic words (850) that express 90% of concepts.
PROFANITY = Wordlist("profanity") # English swear words.
TIME      = Wordlist("time")      # English time and date words.
STOPWORDS = Wordlist("stopwords") # English stop words ("a", "the", ...).

# Note: if used for lookups, performance can be increased by using a dict:
# blacklist = dict.fromkeys(PROFANITY+TIME, True)
# for i in range(1000):
#    corpus.append(Document(src[i], exclude=blacklist))
