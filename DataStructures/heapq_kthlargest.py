# credit: educative.io
import heapq


class KthLargest:
    # constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.k = k
        self.top_k_heap = nums
        heapq.heapify(self.top_k_heap)
        while len(self.top_k_heap) > k:
            heapq.heappop(self.top_k_heap)
            
    # adds element in the heap
    def add(self, val):
        heapq.heappush(self.top_k_heap, val)
        if len(self.top_k_heap) > self.k:
            heapq.heappop(self.top_k_heap)
        return self.return_Kth_largest()
        
    # returns kth largest element from heap
    def return_Kth_largest(self):
        return self.top_k_heap[0]


def main():
    nums = [3, 6, 9, 10]
    temp = [3, 6, 9, 10]
    print("Initial stream: ", nums, sep = "")
    print("k: ", 3, sep = "")
    KLargest = KthLargest(3, nums)
    val = [4, 7, 10, 8, 15]
    print()
    for i in range(len(val)):
        print("\tAdding a new number ", val[i], " to the stream", sep = "")
        temp.append(val[i])
        print("\tNumber stream: ", temp, sep = "")
        print("\tKth largest element in the stream: ", KLargest.add(val[i]))
        print("-"*100)


if __name__ == "__main__":
    main()
