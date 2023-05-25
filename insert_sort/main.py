def insertion_sort(unsorted_list):
  sorted_list = list()

  while unsorted_list:
    value = unsorted_list.pop(0)

    n = len(sorted_list)
    insert_index = n

    for i in range(n):
      if value < sorted_list[i]:
        insert_index = i
        break

    sorted_list.insert(insert_index, value)
    
  return sorted_list

unsorted_list = [27, 10, 12, 20, 25, 13]

print(insertion_sort(unsorted_list))
