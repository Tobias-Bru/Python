#mylist = [7, 3, 9, 12, 11]
#
#n = len(mylist)
#for i in range(n-1):
#  swapped = False
#  for j in range(n-i-1):
#    if mylist[j] > mylist[j+1]:
#      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
#      swapped = True
#  if not swapped:
#    break
#
#print(mylist)

arr_numbers = [64,34,25,12,22,11,90]
arr_length = len(arr_numbers)

for pass_counter in range(arr_length):
    comparison_limit = arr_length - pass_counter - 1
    for current_index in range(0, comparison_limit):
        current_value = arr_numbers[current_index]
        next_value = arr_numbers[current_index + 1]
        if current_value>next_value:
            arr_numbers[current_index] = next_value
            arr_numbers[current_index + 1] = current_value

print("Sortiere Liste:", arr_numbers)