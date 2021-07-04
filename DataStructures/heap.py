class Heap:
    """
    Array based implementation
    """

    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def size(self): return len(self.heap)

    def get_parent_index(self, index): return (index-1)//2

    def get_left_index(self, index): return 2*index + 1

    def get_right_index(self, index): return 2*index + 2

    def has_left(self, index): return self.get_left_index(index) < self.size()

    def has_right(self, index): return self.get_right_index(index) < self.size()

    def has_parent(self, index): return self.get_parent_index(index) >= 0

    def parent(self, index):
        if not self.has_parent(index):
            return None
        return self.heap[self.get_parent_index(index)]

    def left(self, index):
        if not self.has_left(index):
            return None
        return self.heap[self.get_left_index(index)]

    def right(self, index):
        if not self.has_right(index):
            return None
        return self.heap[self.get_right_index(index)]

    def add(self, value):
        """
        Insert new element to list
        """
        self.heap.append(value)
        self.heapify_up()

    def poll(self):
        """
        Return the root node and re-adjust
        """
        if self.size() < 1: return None
        top = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down()
        return top

    def peek(self):
        if self.size() < 1:
            return None
        return self.heap[0]

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def heapify_down(self):
        raise Exception('Unimplemented method: heapify_down')

    def heapify_up(self):
        raise Exception('Unimplemented method: heapify_up')

class MinHeap(Heap):
    def heapify_up(self):
        """
        Check whether last index is less than its parent else go up
        and break whereever the parent is smaller
        """  
        last_index = self.size()-1
        while self.has_parent(last_index) and (self.parent(last_index) > self.heap[last_index]):
            self.swap(self.get_parent_index(last_index), last_index)
            last_index = self.get_parent_index(last_index)

    def heapify_down(self):
        """
        Check children are smaller than parent then swap and go down
        break when children present or greater than
        """
        index = 0
        while self.has_left(index):
            min_index = self.get_left_index(index)
            if self.has_right(index) and self.heap[min_index] > self.right(index):
                min_index = self.get_right_index(index)
            if self.heap[min_index] > self.heap[index]:
                break
            self.swap(index, min_index)
            index = min_index


if __name__ == "__main__":
    heap = MinHeap()
    numbers_list = [15, 3, 5, 4, -1, 0]

    for num in numbers_list:
        heap.add(num)
        print(heap)

    print(heap.peek())
    print("Polled result:", heap.poll())
    print(heap)
    