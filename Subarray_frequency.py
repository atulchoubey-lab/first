'''
Given an array, A. 
Let x be an element in the array. x has the maximum frequency in the array. 
Find the smallest subarray length of the array which also has x as the maximum frequency element.
'''

def findSmallestSubarrayWithMaxFrequency(arr):
    freq_dict = {}
    max_element = None
    max_frequency = 0
    start = 0
    min_length = float('inf')

    for end, element in enumerate(arr):
        if element not in freq_dict:
            freq_dict[element] = 0
        freq_dict[element] += 1

        if freq_dict[element] > max_frequency:
            max_frequency = freq_dict[element]
            max_element = element

        while freq_dict[max_element] == max_frequency and start <= end:
            min_length = min(min_length, end - start + 1)
            freq_dict[arr[start]] -= 1
            start += 1

    return min_length

# Example usage:
arr = [4, 2, 2, 7, 8, 2, 6, 5, 8, 2]
result = findSmallestSubarrayWithMaxFrequency(arr)
print("Smallest subarray length with maximum frequency element:", result)
