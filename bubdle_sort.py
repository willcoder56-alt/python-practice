

def bubble_sort(arr):
    n = len(arr)
    end_boundary = n - 1
    while end_boundary > 0:
        swapped = False
        last_swap_index = 0
        for i in range(end_boundary):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                last_swap_index = i
        if not swapped:
            break
        end_boundary = last_swap_index     
    return arr


a = [64, 34, 25, 12, 22, 11, 90]
b = [2,3,4,5,6,7,8,9,1]
c = [45,75,34,654,23,543,65,876,98,23,656,3,54,9,999]
print(bubble_sort(a))
print(bubble_sort(b))
print(bubble_sort(c))
