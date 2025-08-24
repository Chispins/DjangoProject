def basic_sorting(arr):
    size = len(arr)
    for i in range(size):
        for j in range(i+1, size):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)

def divide_conquer(arr):
    size = len(arr)
    if size % 2 == 0:
#hoho

if __name__=="__main__":
    basic_sorting([1,5,2,6,3])