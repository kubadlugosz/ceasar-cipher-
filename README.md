# ceasar-cipher-
'''
Problem 1. Write a function with the following description:

def encryption(S, n):
    """
    input: A string S consisting of only lower case letters and empty spaces of arbitrary length.
           n, an integer;

    output: A string W = T+str(n). T is a string which has been encrypted by replacing each letter in the string S by a letter n
            letters ahead in the alphabet. For example, encryption("hello", 0) return hello0. encryption("hello world", 1)
            returns "ifmmp xpsme1", that is, each letter has been replaced by one letter ahead of it. Empty space character
            remains unchanged.

    Note that the alphabet shifting is circular. Shifting z by 1 letter gives a.
    """

Problem 2. Write a function with the follwoing description:

def decryption(W):
    """
    input: A string W, encrypted as described in Problem 1;
    output: Based on the trailing integer in W, return the original content of the string S.
    For example, decryption("ifmmp xpsme1") returns "hello world".
    """
'''
