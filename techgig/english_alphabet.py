__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '04-01-2020'


def get_vowel_consonants_count(word):
    vowel_count = len([char for char in word.lower() if char in ['a', 'e', 'i', 'o', 'u']])
    consonants_count = len(word) - vowel_count

    return vowel_count, consonants_count, vowel_count*consonants_count


if __name__ == "__main__":
    number_of_test_case = int(input())
    result = []
    for name in range(number_of_test_case):
        vowel, consonants, product = get_vowel_consonants_count(input())
        result.append(f"{vowel} {consonants} {product}")

    result_sting = "\n".join(result)
    print(result_sting)