# -*- coding: utf-8 -*-
import re
def checkio(text):
    p = re.compile('[^a-zA-Z]*')
    text = p.sub('', text).lower()
    ac1 = {a: text.count(a) for a in text}
    ac2 = [a for a in ac1 if ac1[a] == max(ac1.values())]
    return min(ac2)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
