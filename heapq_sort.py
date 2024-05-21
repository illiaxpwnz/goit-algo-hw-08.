import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    while h:
        result.append(heapq.heappop(h))

    return result

unsorted_list = [8, 4, 6, 12, 15, 2, 10]
sorted_list = heapsort(unsorted_list)
print("Відсортований список:", sorted_list)
