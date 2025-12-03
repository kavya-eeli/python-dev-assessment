def calculate_average(numbers):
    try:   #Debugging Challenge
        total = 0
        for i in numbers:
            total += i
        return total / len(numbers)
    except ZeroDivisionError: 
        return 0
def get_list_element(my_list, index): #Error Handling Challenge
    try:
        return my_list[index] 
    except IndexError:
        print("Error: The index is out of bounds")
        return None
    except TypeError:
        print("Error: Must be an Integer")
        return None
data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")
#Samples of get_list_element
print(get_list_element(data1,1))
print(get_list_element(data1,"a"))
