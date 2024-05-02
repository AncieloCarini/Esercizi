#questa funzione implementa il bubble sort
'''
a: list = [1,3,2,4,6,5,7,8]
for i in range(len(a)):
    for y in range(len(a) - i - 1):
        if (a[y] > a[y+1]):
            #Swap(a[y], a[y+1])
            temp: int = a[y]
            a[y] = a[y+1]
            a[y+1] = temp

    return time.time() - start
print(a)

'''
import time
start: int = time.time()
print(time.time() - start)

a: list = [r for r in range(1, 10**3)]
def bubble_sort(list):
    start: int = time.time()
    for x in range(len(list)):
            swap_flag: bool = False
            for y in range(len(list) - x - 1):
                if (a[y] > a[y + 1]):
                    swap_flag: bool = True
                    temp: int = a[y]
                    a[y] = a[y + 1]
                    a[y + 1] = temp
            if swap_flag is False:
                return a, time.time() - start
    return a, time.time() - start
print(bubble_sort(a))


