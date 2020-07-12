from enchant import Dict
from itertools import combinations, permutations
from time import time
from multiprocessing import Pool
from functools import partial


def findem(word, dictionary):
    word = ''.join(word)
    if dictionary.check(word):
        return word


def main():
    letters = 'rilsedxcu'
    dictionary = Dict('en-US')

    pool = Pool(processes=4)
    pfunc = partial(findem, dictionary=dictionary)

    x = [combinations(letters, i+1) for i in range(4, len(letters))]
    valid_word_list = []
    for combo in x:
        for combo1 in combo:
            valid_word_list.append(pool.imap_unordered(pfunc, permutations(combo1)))

    pool.close(), pool.join()

    valid_word_list = [v1 for v in valid_word_list for v1 in v.get() if v1 is not None]
    # print(valid_word_list)
    pass


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