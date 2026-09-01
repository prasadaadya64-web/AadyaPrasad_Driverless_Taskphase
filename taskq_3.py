class SelectionSort:

     def sort(self,arr):
        n = len(arr)


        for i in range(n):

            min_index = i


            for j in range(i+1,n):

                if arr[j] < arr[min_index]:
                    

                    min_index = j


                    arr[i],arr[min_index] = arr[min_index],arr[i]


            return arr 

class BinarySearch:

    def Search(self,arr,target):
        low = 0
        high = len(arr) - 1

        while low <= high:

            mid = (low + high) // 2

            if arr[mid] == target:
                return mid

            elif arr[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return 0


n = int(input("Enter number of strings: "))

arr = []


for i in range(n):
    s = input("Enter string: ")
    arr.append(s)

sorter = SelectionSort()
sorter.sort(arr)

print("sorted list:",arr)

target = input("Enter string to search:")

searcher = BinarySearch()

result = searcher.Search(arr,target)

if result == -1:
    print("String not found")
else:
    print("string found at index",result)


