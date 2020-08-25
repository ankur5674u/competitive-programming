"""
You are write a letter to your lover. However before reciving the letter intruders rotate each word from left to right.

Write a function to count number of correct words after k rotation.

"""


def correct_word_count_using_deque(word, rotation_count):
    from collections import deque
    word_split = word.split(' ')
    correct_count = 0
    for index, item in enumerate(word_split):
        deque_object = deque(item)
        deque_object.rotate(rotation_count)
        rotate_word = "".join(deque_object)
        print(f"Original Word:{item}, rotate_word:{rotate_word}")
        if rotate_word == item:
            correct_count += 1
    return correct_count


def correct_word_count(sentence, rotation_count):
    correct_count = 0
    for word in sentence.split(' '):
        if word == leftShift(word, rotation_count):
            correct_count += 1
    return correct_count


def leftShift(text, n):
    return text[(n % len(text)):] + text[:(n % len(text))]


def rightShift(text, n):
    return text[-(n % len(text)):] + text[:-(n % len(text))]
