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


# Problem 1

def encryption(S, n):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    L = ' '

    for i in S:
        if i == ' ':
            L += i
        if i in alphabet:
            L += alphabet[(alphabet.index(i) + n) % len(alphabet)]
    return L + str(n)


def decryption(W):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    cipher = ' '
    index = ' '
    my_cipher = ' '

    for i in W:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            index += i
            index_number = int(index)
        else:
            cipher += i

    for i in cipher:
        if i == ' ':
            my_cipher += i
        if i in alphabet:
            my_cipher += alphabet[(alphabet.index(i) - index_number) % len(alphabet)]
    return my_cipher


def main():
    print( encryption("fdsahfkjaHAFOI"))

    print(decryption())
main()


