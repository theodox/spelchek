spelchek
--------

A cheap-ass, pure-python spellchecker based on `Peter Norvig's Python
Bayes demo <http://norvig.com/spell-correct.html>`__ All the interesting
work is his.

The interesting external methods are

-  ``known()`` filters a list of words and returns only those in the
   dictionary,
-  ``correct()`` returns the best guess for the supplied word
-  ``guesses()`` returns all guesses for the supplied word
-  ``add()`` adds a word to the dictionary, with an optional priority
   value

So simple uses would be something like

::

    import spelchek
    print spelchek.correct('eaxmple')
    # 'example'

The current corpus of words includes about 75,000 entries. It does not
include punction such as hyphens, apostrophes or spaces. The module also
supports optional user-supplied dictionaries, see the documentation of
``spelchek.py`` for details.

Important Caveat
=================

The heart of a spell checker is the dictionary, and the dictionary here
is cadged together out of a bunch of free online sources. No real effort
has been made to check it for accuracy, and although it's trivially
correct with several tens of thousands of words involved errors are
pretty much inevitable (if you find one, feel free to submit a pull
request and I'll update ``corpus.txt`` as needed).

The algorithm is language agnostic so it should be easy to create 
dictionaries for languages other than English.  If you come up with a 
non-English dictionary submit a pull request and we can extend the module
to support language choice.

Installation
============

the module is a simple python module with no binary dependencies.
The default dictionary is the file `corpus.txt` which lives inside 
the spelchek package.

You can extend the built in dictionary in two ways.

1. You can add words to the corpus.txt file; its's a plain text file
   with words and frequency scores separated by a comma. High frequency
   scores make a word more likely to be suggested as a correction, where
   low frequencies are 'rarer' and so less likely to be suggested.  This
   method is easiest if you are working with a source distributions from
   the github repository
2. You can add a custom dictionary of your own using the same , format
   and point to it be setting an envrionment variable called SPELCHEK. These 
   entries will be added to the default dictionary at import time (note that
   they will replace the assigned priorities of existing words).  This is a
   low-friction way to try adding non-English language support.

