import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    while h:
        result.append(heapq.heappop(h))
    return result

def heapsort_nested(nested_iterable):
    sorted_sublists = []
    for sublist in nested_iterable:
        sorted_sublists.append(heapsort(sublist))
    return sorted_sublists

unsorted_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
sorted_lists = heapsort_nested(unsorted_lists)
print("Відсортовані списки:", sorted_lists)
