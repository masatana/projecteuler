# -*- coding: utf-8 -*-
triangle_numbers = []
def gen_triangle_numbers(n):
    i = 0
    while True:
        i += 1
        triangle_number = (1.0 / 2) * i * (i + 1)
        if triangle_number > n:
            break
        yield triangle_number
with open('./words.txt') as f:
    max_word_length = 0
    words = []
    c = 0
    for line in f.readline().split(','):
        words.append(line.replace('"', ''))
        if len(line.replace('"', '')) > max_word_length:
            max_word_length = len(line.replace('"', ''))
    limit = 25 * max_word_length
    triangle_numbers = [x for x in gen_triangle_numbers(limit)]
    for word in words:
        v = 0
        for char in word:
            v += ord(char) - 64
        if v in triangle_numbers:
            c += 1
    print c
