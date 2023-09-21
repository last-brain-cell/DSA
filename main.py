# Stack
# Queue

# Sorting -
# # bubble_sort
#
# import random
# from Algorithms.sorting import bubble_sort
#
# arr = [random.randint(1, 100) for _ in range(10)]
#
# print(f"unsorted: {arr}")
#
#
#
# print(arr)

import phonenumbers
from phonenumbers import geocoder

p = [phonenumbers.parse("+917722087410"), phonenumbers.parse("+919823807410"), phonenumbers.parse("+919225508858"), phonenumbers.parse("+919823057410")]

[print(geocoder.description_for_number(p[i], "en")) for i in range(len(p))]
