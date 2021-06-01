from string import ascii_uppercase, ascii_letters


class Caesar:
    def __init__(self, key: int, icase: bool = True, alphabet: str = ascii_uppercase):
        self._icase = icase

        self._alphabet = alphabet
        if icase:
            self._alphabet = self._alphabet.upper()

        self._key = key % len(self._alphabet)

    def encrypt(self, message: str) -> str:
        if self._icase:
            message = message.upper()

        return self._apply_shift(message, self._key)

    def decrypt(self, encrypted: str) -> str:
        return self._apply_shift(encrypted, -self._key)

    def _apply_shift(self, string: str, shift: int) -> str:
        return ''.join([self._i2c(self._c2i(c) + shift) if c in self._alphabet else c for c in string])

    def _c2i(self, c: str) -> int:
        return self._alphabet.find(c)

    def _i2c(self, i: int) -> str:
        return self._alphabet[i % len(self._alphabet)]


def brute_decrypt(encrypted: str, alphabet: str = ascii_letters) -> dict[int, str]:
    return {key: Caesar(key, icase=False, alphabet=alphabet).decrypt(encrypted) for key in range(1, len(alphabet))}


def frequency_decrypt(encrypted: str, alphabet: str = ascii_letters + ' ') -> tuple[int, str]:
    space = ' '
    alphabet = alphabet if space in alphabet else alphabet + space
    _c2i = alphabet.find

    expected_space_ord = _c2i(space)

    frequency_dict = {}
    for c in encrypted:
        if c in alphabet:
            i = _c2i(c)
            frequency_dict[i] = frequency_dict[i] + \
                1 if i in frequency_dict else 1

    possible_key = len(alphabet) + max(frequency_dict,
                                       key=frequency_dict.get) - expected_space_ord

    return possible_key, Caesar(possible_key, icase=False, alphabet=alphabet).decrypt(encrypted)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
