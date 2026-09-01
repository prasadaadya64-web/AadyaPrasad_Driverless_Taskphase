
def find_position(arr,num):

    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2

        if arr[mid] < num:
           low = mid +1

        else:

            high = mid

    return low


n = int(input("Enter number of integers:"))

hash_table = [[] for _ in range(10)]

for i in range(n):
    num = int(input("Enter number:"))

    index = num % 10

    hash_table[index].append(num)

print("hash table:")

for i in range(10):
    print(i,":",hash_table[i])
    

          

       
        