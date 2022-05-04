#이진탐색 알고리즘

def binarySearch(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        midIndex = (start+end) // 2
        if arr[midIndex] == key:
            return midIndex
        elif arr[midIndex] < key :
            start = midIndex + 1
        elif arr[midIndex] > key :
            end = midIndex - 1
    return -1

arr = [1,2,3,5,6,7,8,9,10,11]
print(binarySearch(arr, 1)) # 목표 숫자의 인덱스 반환 없으면 -1
