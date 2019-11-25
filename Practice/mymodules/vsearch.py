def search4vowels(phrase: str) -> set:
    """Return any vowel's found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Returns a set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
