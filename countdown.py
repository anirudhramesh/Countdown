from enchant import Dict
from itertools import combinations, permutations
from time import time
from multiprocessing import Pool, Manager
from functools import partial


def main():
    letters = 'rilsedxcu'
    dictionary = Dict('en-US')

    all_length_combinations = [combinations(letters, i+1) for i in range(4, len(letters))]
    all_words_list = []
    for single_length_combination in all_length_combinations:
        for combo in single_length_combination:
            all_words_list.extend([''.join(p) for p in permutations(combo)])

    pool = Pool(processes=4)
    in_dictionary = pool.map(dictionary.check, all_words_list)
    pool.close(), pool.join()

    valid_word_list = [word for word, result in zip(all_words_list, in_dictionary) if result == True]

    print(valid_word_list)


if __name__ == '__main__':
    start_time = time()
    main()
    print('time taken: ', round(time() - start_time, 2), ' seconds.')

# my implementation
# def sub_permutations(scrambled_word, uptil_now, start):
#     start += 1
#     if start == len(scrambled_word):
#         return []
#     final_permutations = []
#     for i in range(start, len(scrambled_word)):
#         new_uptil_now = uptil_now + scrambled_word[i]
#         final_permutations.extend(set([''.join(p) for p in permutations(new_uptil_now)]))
#         final_permutations.extend(sub_permutations(scrambled_word, new_uptil_now, i))
#     return final_permutations


# a = 'esratinda'
# # a_ = list(set(a))
# a_ = a
# x = sub_permutations(a_, a_[:2], 1)
# valid_list = [i for i in x if dictionary.check(i)]
# pass