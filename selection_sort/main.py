# hard way
def selection_sort(unsorted_list):
  length = len(unsorted_list)

  for i in range(length):
    min_index = i

    for j in range(i + 1, length):
      if unsorted_list[min_index] > unsorted_list[j]:
        temp = unsorted_list[min_index]
        unsorted_list[min_index] = unsorted_list[j]
        unsorted_list[j] = temp
      
    print("Step {} : {}".format(i + 1, unsorted_list))

unsorted_list = [27, 10, 12, 20, 25, 13]

print(selection_sort(unsorted_list))
