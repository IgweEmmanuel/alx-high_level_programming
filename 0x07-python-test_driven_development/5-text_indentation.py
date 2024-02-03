#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after some characters
    Args:
        text: this is the text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for s in text:
        print(s, end='')
        """if s == '.' or s == '?' or s == ':':"""
        if s in ['.','?',':']:
            print('\n\n', end='')
