#!/usr/bin/python3
# -- coding: utf-8 --

# 12/10/25

__author__ = 'Clara Sedes'

import string

# List of "unimportant" words (feel free to add more)
g_skip_words = [
    'a', 'about', 'abundant', 'all', 'an', 'another', 'any', 'around', 'at',
    'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
    'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
    'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
    'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
    'of', 'off', 'oh', 'on', 'please', 'precious', 'small', 'some', 'soon',
    'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
    'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
    'wish', 'with', 'would']


def filter_words(p_words, p_skip_words):
    """This function takes a list of words and returns a copy of the list from
    which all words provided in the list skip_words have been removed.
    For example:

    >>> filter_words(["help", "me", "please"], ["me", "please"])
    ['help']

    >>> filter_words(["go", "south"], g_skip_words)
    ['go', 'south']

    >>> filter_words(['how', 'about', 'i', 'go', 'through', 'that', 'little', 'passage', 'to', 'the', 'south'], g_skip_words)
    ['go', 'passage', 'south']

    """
    l_words = [l_word for l_word in p_words if l_word not in p_skip_words]
    return l_words

    
def remove_punct(p_text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:

    >>> remove_punct("Hello, World!")
    'Hello World'
    >>> remove_punct("-- ...Hey! -- Yes?!...")
    ' Hey  Yes'
    >>> remove_punct(",go!So.?uTh")
    'goSouTh'
    """
    l_no_punct = ""
    for l_char in p_text:
        if not (l_char in string.punctuation):
            l_no_punct = l_no_punct + l_char

    return l_no_punct
    # Another way to do it using list comprehension and converting the list back to a string
    # l_no_punct = ''.join([l_char for l_char in p_text if l_char not in string.punctuation])


def normalise_input(p_user_input):
    """This function removes all punctuation from the string and converts it to
    lower case. It then splits the string into a list of words (also removing
    any extra spaces between words) and further removes all "unimportant"
    words from the list of words using the filter_words() function. The
    resulting list of "important" words is returned. For example:

    >>> normalise_input("  Go   south! ")
    ['go', 'south']
    >>> normalise_input("!!!  tAkE,.    LAmp!?! ")
    ['take', 'lamp']
    >>> normalise_input("HELP!!!!!!!")
    ['help']
    >>> normalise_input("Now, drop the sword please.")
    ['drop', 'sword']
    >>> normalise_input("Kill ~ tHe :-  gObLiN,. wiTH my SWORD!!!")
    ['kill', 'goblin', 'sword']
    >>> normalise_input("I would like to drop my laptop here.")
    ['drop', 'laptop']
    >>> normalise_input("I wish to take this large gem now!")
    ['take', 'gem']
    >>> normalise_input("How about I go through that little passage to the south...")
    ['go', 'passage', 'south']

    """
    # Remove punctuation and convert to lower case
    l_no_punct = remove_punct(p_user_input).lower()

    return filter_words(l_no_punct.split(), g_skip_words)

