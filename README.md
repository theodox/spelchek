spelchek
----------

A cheap-ass, pure-python spellchecker based on [Peter Norvig's Python Bayes demo](http://norvig.com/spell-correct.html) All the interesting work is his.

The interesting external methods are

   * `known()` filters a list of words and returns only those in the dictionary,
   * `correct()` returns the best guess for the supplied word
   * `guesses()` returns all guesses for the supplied word
   * `add()` adds a word to the dictionary, with an optional priority value

So simple uses would be something like

    import spelchek
    print spelchek.correct('eaxmple')
    # 'example'

The current corpus of words includes about 75,000 entries. It does not include punction such as hyphens, apostrophes or spaces.  The module also supports optional user-supplied dictionaries, see the documentation of `spelchek.py` for details.
   
#Important Caveat
========
The heart of a spell checker is the dictionary, and the dictionary here is cadged together out of a bunch of free online sources.  No really effort has been made to check it for accuracy, and although it's trivially correct with several tens of thousands of words involved errors are pretty much inevitable (if you find one, feel free to submit a pull request and I'll update `corpus.txt` as needed).

Installation
============
the module is a single file python module with no binary dependencies. You do, however, need to keep the `corpus.txt` file in the same location as `spelchek.py`.

You can extend the built in dictionary in two ways.

1. You can add words to the corpus.txt file; its's a plain text file with words and frequency scores separated by a comma.  High frequency scores make a word more likely to be suggested as a correction, where low frequencies are 'rarer' and so less likely to be suggested.
2. You can add a custom dictionary of your own using the same <word>,<score> format and point to it be setting an envrionment variable called SPELCHEK.