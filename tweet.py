"""Assignment 1.
"""

import math

# Maximum number of characters in a valid tweet.
MAX_TWEET_LENGTH = 50

# The first character in a hashtag.
HASHTAG_SYMBOL = '#'

# The first character in a mention.
MENTION_SYMBOL = '@'

# Underscore is the only non-alphanumeric character that can be part
# of a word (or username) in a tweet.
UNDERSCORE = '_'

SPACE = ' '


def is_valid_tweet(text: str) -> bool:
    """Return True if and only if text contains between 1 and
    MAX_TWEET_LENGTH characters (inclusive).

    >>>is_valid_tweet('Hello Twitter!')
    True
    >>>is_valid_tweet('')
    False
    >>>is_valid_tweet(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    False
    """
    return 0 < len(text) <= MAX_TWEET_LENGTH 

def compare_tweet_lengths(text1: str, text2: str) -> int:
    """Return either 1, 0, or -1 to represent whether the first tweet is longer 
    than the second tweet, the first and second tweets are the same length, or 
    the second tweet is longer than the first tweet, respectively. 
    
    Precondition: Tweet length must be between 0 to MAX_TWEET_LENGTH characters. 
    
    >>>compare_tweet_lengths('laptop', 'ipad')
    1
    >>>compare_tweet_lengths('and', 'ten')
    0
    >>>compare_tweet_lengths('fun', 'funny')
    -1
    """
    if len(text1) > len(text2): 
        return 1 
    elif len(text1) < len(text2):
        return -1
    else:
        return 0
 
def add_hashtag(parameter1: str, parameter2: str) -> str: 
    """Return potential tweet if it is a valid tweet with a space, hash symbol 
    and tweet word at the end of the original tweet. Return original tweet if
    potential tweet is not valid. 
    
    Precondition: Tweet length of parameter1 must be between 0 to 
    MAX_TWEET_LENGTH characters. 
        
    >>>add_hashtag('I love', 'university')
    'I love #university' 
    >>>add_hashtag('the university of', 'abcdefghijklmnopqrstuvwxyz123456789')
    'the university of' 
    """
    text = parameter1 + SPACE + HASHTAG_SYMBOL + parameter2
    valid = is_valid_tweet(text)
    if valid:
        return text
    else:
        return parameter1
    
def contains_hashtag(parameter1: str, parameter2: str) -> bool:
    """Return True if and only if tweet includes a hashtag containing a hash 
    symbol and tweet word.
    
    Precondtiion: Tweet length must be between 0 to MAX_TWEET_LENGTH characters.
    
    >>>contains_hashtag('I eat #cake', 'cake')
    True
    >>>contains_hashtag('I sleep #now', 'no')
    False
    """
    text = clean(parameter1) + SPACE
    return HASHTAG_SYMBOL + parameter2 + SPACE in text

def is_mentioned(parameter1: str, parameter2: str) -> bool: 
    """Return True if and only if tweet includes a mention containing a mention 
    symbol and a tweet word.
    
    Precondition: Tweet length must be between 0 to MAX_TWEET_LENGTH characters.
    
    >>>is_mentioned('Love @Toronto!', 'Toronto')
    True
    >>>is_mentioned('Love @Toronto!', 'To')
    False
    """
    text = clean(parameter1) + SPACE
    return MENTION_SYMBOL + parameter2 + SPACE in text 

def add_mention_exclusive(parameter1: str, parameter2: str) -> str:
    """Return potential tweet if it is a valid tweet with a space, mention 
    symbol, and a tweet word at the end of the original tweet, and the original 
    tweet does not mention the given tweet word. Return original tweet if 
    potential tweet is not valid. 
    
    Precondition: Tweet length must be between 0 to MAX_TWEET_LENGTH characters.

    >>>add_mention_exclusive('Love @Toronto!', 'Toronto')
    'Love @Toronto!'
    >>>add_mention_exclusive('Love Toronto!', 'Toronto')
    'Love Toronto! @Toronto'
    """
    if is_mentioned(parameter1, parameter2):
        return parameter1
    else:
        return parameter1 + SPACE + MENTION_SYMBOL + parameter2
    
def num_tweets_required(parameter: str) -> int:
    """Return the minimum number of tweets required to communicate an entire 
    message. 
    
    Precondition: Each tweet length must be between 0 to MAX_TWEET_LENGTH 
    characters. 
    
    >>>num_tweets_required('Go Raptors!')
    1
    >>>num_tweets_required('I love studying the course CSC108 in University of 
    Toronto!')
    2
    """
    text = parameter
    return math.ceil((len(text))/50)
    
def get_nth_tweet(parameter1: str, parameter2: int) -> str:
    """Return the nth valid tweet within a sequence of tweets.
    
    Precondition: Each tweet length must be between 0 to MAX_TWEET_LENGTH 
    characters.
    
    >>>get_nth_tweet('I love studying the course CSC108 in University of 
    Toronto!', 1)
    ' Toronto!'
    >>>get_nth_tweet('Go Raptors!', 2)
    ''
    """
    text = parameter1
    index_start = parameter2*50
    index_stop = index_start + 49
    if parameter2 <= num_tweets_required(text): 
        return text[index_start:index_stop]
    else:
        return ''

 
# Now define the other functions described in the handout.

# A helper function.  Do not modify this function, but you are welcome
# to call it.

def clean(text: str) -> str:
    """Return text with every non-alphanumeric character, except for
    HASHTAG_SYMBOL, MENTION_SYMBOL, and UNDERSCORE, replaced with a
    SPACE, and each HASHTAG_SYMBOL replaced with a SPACE followed by
    the HASHTAG_SYMBOL, and each MENTION_SYMBOL replaced with a SPACE
    followed by a MENTION_SYMBOL.

    >>> clean('A! lot,of punctuation?!!')
    'A  lot of punctuation   '
    >>> clean('With#hash#tags? and@mentions?in#twe_et #end')
    'With #hash #tags  and @mentions in #twe_et  #end'
    """

    clean_str = ''
    for char in text:
        if char.isalnum() or char == UNDERSCORE:
            clean_str = clean_str + char
        elif char == HASHTAG_SYMBOL or char == MENTION_SYMBOL:
            clean_str = clean_str + SPACE + char
        else:
            clean_str = clean_str + SPACE
    return clean_str