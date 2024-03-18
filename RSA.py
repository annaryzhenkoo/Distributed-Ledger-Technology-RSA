import math
import random
from typing import Tuple


def is_prime(value: int) -> bool:
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True


def creating_value(start: int, end: int) -> int:
    probably_prime_number = random.randint(start, end)
    while not is_prime(probably_prime_number):
        probably_prime_number = random.randint(start, end)
    return probably_prime_number


def search_mutually_prime_number(value: int) -> int:
    probably_mutually_prime_number = creating_value(2, 10 ** 15)
    while not is_prime(probably_mutually_prime_number) or probably_mutually_prime_number == value:
        probably_mutually_prime_number = creating_value(2, 10 ** 15)
    return probably_mutually_prime_number


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def find_d(m: int) -> int:
    d = random.randint(2, m - 1)
    while gcd(d, m) != 1:
        d = random.randint(2, m - 1)
    return d


def find_e(d: int, m: int) -> int:
    for e in range(2, m):
        if (e * d) % m == 1:
            return e


def generate_keypair() -> Tuple[Tuple[int, int], Tuple[int, int]]:
    prime_numbers1 = creating_value(10 ** 3, 10 ** 4)
    prime_numbers2 = creating_value(10 ** 3, 10 ** 4)
    n = prime_numbers1 * prime_numbers2
    m = (prime_numbers1 - 1) * (prime_numbers2 - 1)
    d = find_d(m)
    e = find_e(d, m)
    public_keys = (e, n)
    private_keys = (d, n)
    return public_keys, private_keys


def encryption(public_keys: Tuple[int, int], message: int) -> int:
    e, n = public_keys
    return pow(message, e, n)


def decryption(private_keys: Tuple[int, int], ciphertext: int) -> int:
    d, n = private_keys
    return pow(ciphertext, d, n)


def test():
    message = 234
    print("Message: ", message)
    public_keys, private_keys = generate_keypair()
    ciphertext = encryption(public_keys, message)
    print("Ciphertext:", ciphertext)
    decrypted_message = decryption(private_keys, ciphertext)
    print("Decrypted message:", decrypted_message)


test()