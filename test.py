from functools import reduce

def isAnagram(s: str, t: str) -> bool:
    def bubble_sort(str_arr: list[str]):
        for j in range(len(str_arr), 1, -1):
            for i in range(1, j):
                if str_arr[i] > str_arr[i - 1]:
                    str_arr[i], str_arr[i - 1] = str_arr[i - 1], str_arr[i]
        print(str_arr)
        return str_arr
    return bubble_sort(list(s)) == bubble_sort(list(t))



# def isAnagram_compre(s, t):
#     def bubble_sort(str_arr: list[str]):
#         [str_arr[i], str_arr[i - 1]] = [str_arr[i - 1], str_arr[i]] for i in range(1, j) if str_arr[i] > str_arr[i - 1]

#
# # print(isAnagram("cat", "rat"))
# def isAnagram_shorter(s: str, t: str) -> bool:
#     return not [list(s).__setitem__(i, list(s)[i - 1]) for j in range(len(list(s)), 1, -1) for i in range(1, j) if list(s)[i] > list(s)[i - 1]] == [list(t).__setitem__(i, list(t)[i - 1]) for j in range(len(list(t)), 1, -1) for i in range(1, j) if list(t)[i] > list(t)[i - 1]]
#
#
# print(isAnagram_shorter("anagram", "nagaram"))
# print(isAnagram_shorter("cat", "rat"))
# print(isAnagram_shorter("a", "a"))
#
# # s = 'cat'
# # t = 'rat'
# # print([list(s).__setitem__(i, list(s)[i - 1]) for j in range(len(list(s)), 1, -1) for i in range(1, j) if list(s)[i] > list(s)[i - 1]] == [list(t).__setitem__(i, list(t)[i - 1]) for j in range(len(list(t)), 1, -1) for i in range(1, j) if list(t)[i] > list(t)[i - 1]])
# # are_anagrams = ''.join([list(s).__setitem__(i, list(s)[i - 1]) for j in range(len(list(s)), 1, -1) for i in range(1, j) if list(s)[i] > list(s)[i - 1]]) == ''.join([list(t).__setitem__(i, list(t)[i - 1]) for j in range(len(list(t)), 1, -1) for i in range(1, j) if list(t)[i] > list(t)[i - 1]])
#
# # s = 'cat'
# # t = 'rat'
# #
# # are_anagrams = ''.join(sorted(s, key=lambda x: x, reverse=True)) == ''.join(sorted(t, key=lambda x: x, reverse=True))
# # print(are_anagrams)
#
# # s = 'cat'
# # t = 'rat'
# #
# # are_anagrams = ''.join([c for c in s if c in t]) == ''.join([c for c in t if c in s]) and len(s) == len(t)
# #
# # print(are_anagrams)

# print(['a', 'b', 'c'] == ['b', 'a', 'c'])

arr = list('nagaram')
arr2 = list('anagram')


# [[str_arr[i], str_arr[i - 1]] = [str_arr[i - 1], str_arr[i]] for i in range(1, j) if str_arr[i] > str_arr[i - 1]]
# for j in range(len(str_arr), 1, -1):
#     print([str_arr.__setitem__(i, str_arr[i - 1]) for i in range(1, j) if str_arr[i] > str_arr[i - 1]])
#
# print(str_arr)
#
# bubble_sort = lambda arr: reduce(lambda x, _: x[:-1] + [min(x[-1], x[-2])] + [max(x[-1], x[-2])] if x[-1] < x[-2] else x[:-1] + [x[-2]] + [x[-1]], range(len(arr) - 1), arr)
#
# print(bubble_sort(['a']))
# print(bubble_sort(['a']))


# print(lambda x, _: x[:-1] + [min(x[-1], x[-2])] + [max(x[-1], x[-2])] if x[-1] < x[-2] else x[:-1] + [x[-2]] + [x[-1]], range(len(arr) - 1), arr == lambda x, _: x[:-1] + [min(x[-1], x[-2])] + [max(x[-1], x[-2])] if x[-1] < x[-2] else x[:-1] + [x[-2]] + [x[-1]], range(len(arr2) - 1), arr2

