#spelchek

A cheap-ass, pure-python spellchecker based on [Peter Norvig's Python Bayes demo](http://norvig.com/spell-correct.html)

The interesting external methods are

   * `known()` filters a list of words and returns only those in the dictionary,
   * `correct()` returns the best guess for the supplied word
   * `guesses()` returns all guesses for the supplied word
   * `add()` adds a word to the dictionary, with an optional priority value

So simple uses would be something like


    import spelchek
    print spelchek.correct('eaxmple')
    # 'example'
  
   
# caveat
This is a quickie hack, because it does not use a real statistical analysis to spice the guesses! The 'right' thing to do is to make a real game-development wordlist corpus by dumping some relevant text to a huge file and word-counting it (the original example linked above contains the code, I baked it in here to cut down on load times).  This really just looks for tokens in the word list using Peter's original transposition and deletion guesses, with a mild priority boost to nouns relative to verbs and adjectives. However the 'right' Bayesian thing to do is to have much more fine-grained prioritization of common words.
