def filter_and_sort_evens(numbers):
    even = [ ]
    for num in numbers:
        if num%2 ==0:
            even.append(num)
    sorted_evens = sorted(even)       
    return sorted_evens 
#Example
sample =[3, 1, 4, 1, 5, 9, 2, 6]
print(filter_and_sort_evens(sample))

#count_character_frequency(text)

def count_character_frequency(text):
    txt = text.lower()
    freq = {}
    for char in txt:
        if char in freq:
            freq[char] =  freq[char]+1
        else:
            freq[char]    = 1 
    return freq
#Example
print(count_character_frequency("Hello World"))

