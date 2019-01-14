

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
    print( encryption("hello world"))

    print(decryption())
main()


