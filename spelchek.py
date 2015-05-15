"""
spelchek

A cheap-ass, pure-python spellchecker based on Peter Norvig's python bayes demo at http://norvig.com/spell-correct.html

The interesting external methods are
    * known() filters a list of words and returns only those in the dictionary,
    * correct() returns the best guess for the supplied word
    * guesses() returns all guesses for the supplied word

The dictionary is stored in corpus.txt. It's not very scientific or exact, I kludged it together from a variety of
public domain sources. Values over 5 are from the [GSL word list](http://jbauman.com/aboutgsl.html), the rest are
guesstimated from other word lists.  It's not guaranteed to be error free! If you discover mistakes, feel free to
submit a pull request.

Still, it works as is. Do remember to double check that the result of 'correct' is 'known': the `correct()` will return
the original word unchanged if it finds no candidates!

"""
__author__ = 'stevet'

import collections
import pkgutil

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def first_order_variants(word):
    """
    return all the possibile spelling variants of <word>
    """
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def second_order_variants(word):
    "return second-order candidates"
    return set(e2 for e1 in first_order_variants(word) for e2 in first_order_variants(e1) if e2 in _DICTIONARY)


def known(*words):
    """
    Return all the words in *words which are in the dictionary
    """
    return set(w for w in words if w in _DICTIONARY)


def correct(word):
    """
    pick the 'best' candidate based on stored score of the possibilities.  If nothing else is close
    returns the original word, so don't assume its always right!
    """
    candidates = known(word) or known(*first_order_variants(word)) or second_order_variants(word) or [word]
    return max(candidates, key=_DICTIONARY.get)


def guesses(word):
    """
    return all of the first and second order guesses for this word
    """
    result = list(known(*first_order_variants(word)))
    result.sort()
    return result


def add(word, priority=4):
    """
    Adds <word> to the dictionary with the specified priority (default is 4).

    IMPORTANT NOTE: this is temporary! The addition is not saved to disk, so it won't persist between loads!
    """
    _DICTIONARY[word.lower().strip()] = priority

# this is the bayes dictionary
# this version is hardly scientific; the top 2000 words from the GSL list have good values,
# everything else is cadged together from random word list sources with an arbitrary values of 4 for
# 'ordinary' and 3 for 'plurals, adjectives, and participials'


_DICTIONARY = {}
for line in pkgutil.get_data("spelchek", "corpus.txt").splitlines():
    name, val = line.split(",")
    val = int(val)
    _DICTIONARY[name] = val

