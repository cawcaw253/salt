def merge_sort(unsorted_list):
  if len(unsorted_list) <= 1:
    return unsorted_list

  mid = len(unsorted_list)//2
  left = unsorted_list[:mid]
  right = unsorted_list[mid:]

  sorted_left = merge_sort(left)
  sorted_right = merge_sort(right)

  return merge(sorted_left, sorted_right)

def merge(left, right):
  i, j = 0, 0
  sorted_list = []

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      sorted_list.append(left[i])
      i += 1
    else:
      sorted_list.append(right[j])
      j += 1
  while i < len(left):
    sorted_list.append(left[i])
    i += 1
  while j < len(right):
    sorted_list.append(right[j])
    j += 1

  return sorted_list

unsorted_list = [27, 10, 12, 20, 25, 13]

print(merge_sort(unsorted_list))
