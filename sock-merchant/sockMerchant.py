# Author: Betül Tekne
# Interview Preperation Kit -> First of Warm-up Challanges
# Problem Definiton: John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
# I have solved this problem by simply changing the first one of the pair to 0.


def sockMerchant(n, arr):
    pair = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] != 0:
                if arr[i] == arr[j]:
                    pair = pair + 1
                    arr[j] = 0
                    arr[i] = 0
    return pair

n = int(input())
numbers = str(input())
arr = list(numbers.split(' '))
result = sockMerchant(n, arr)
print(result)