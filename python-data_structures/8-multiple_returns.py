#!/usr/bin/python3
def multiple_returns(sentence):
    new_string = tuple()

    if len(sentence) == 0:
        new_string = ('None',)
        return (len(new_string), new_string[0])
    else:
        return (len(sentence), sentence[0])
