#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum_unique = 0
    unique_set = set()
    for i in my_list:
        if i not in unique_set:
            unique_set.add(i)
            sum_unique += i
    return (sum_unique)
