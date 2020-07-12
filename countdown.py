from enchant import Dict
from itertools import combinations, permutations
from time import time
from multiprocessing import Pool
from functools import partial


def findem(scrambled_word, dictionary, i):
    valid_word_list = []
    # for i in range(6, len(scrambled_word)):
    for c in combinations(scrambled_word, i+1):
        for p in permutations(c):
            p = ''.join(p)
            if dictionary.check(p):
                valid_word_list.append(p)
    return valid_word_list


def main():
    letters = 'rilsedxcu'
    dictionary = Dict('en-US')
    # pfunc = partial(findem, scrambled_word=letters, dictionary=dictionary)

    start_time = time()
    pool = Pool(processes=5)
    valid_word_list = pool.starmap(findem, [(letters, dictionary, j) for j in range(4, len(letters))])
    pool.close(), pool.join()
    print('time taken: ', round(time() - start_time, 2), ' seconds.')
    
    print(valid_word_list)


def findem1(word, dictionary):
    word = ''.join(word)
    if dictionary.check(word):
        return word


def main1():
    letters = 'rilsedxcu'
    dictionary = Dict('en-US')

    pool = Pool(processes=4)
    pfunc = partial(findem1, dictionary=dictionary)

    x = [combinations(letters, i+1) for i in range(4, len(letters))]
    valid_word_list = []
    for combo in x:
        for combo1 in combo:
            valid_word_list.append(pool.map_async(pfunc, permutations(combo1)))

    pool.close(), pool.join()

    valid_word_list = [v.get() for v in valid_word_list]
    print(valid_word_list)
    pass


if __name__ == '__main__':
    start_time = time()
    main1()
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