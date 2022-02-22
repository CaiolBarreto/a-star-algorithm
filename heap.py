class Heap:
    def __init__(self, heap_list):
        self.heap = heap_list

    @staticmethod
    def __getParent(index):
        return (index - 1) // 2

    def __getLeftChild(self, index):
        left_index = 2 * index + 1
        if left_index < len(self.heap) - 1:
            return left_index

    def __getRightChild(self, index):
        right_index = 2 * index + 2
        if right_index < len(self.heap) - 1:
            return right_index

    def __hasParent(self, index):
        return self.__getParent(index) > 0

    def __hasChildren(self, index):
        left = self.__getLeftChild(index)
        right = self.__getRightChild(index)
        if left is None and right is None:
            return False
        else:
            return True

    def __smallestChild(self, left_child_index, right_child_index):
        if left_child_index is None:
            return right_child_index
        elif right_child_index is None:
            return left_child_index
        elif self.heap[left_child_index][0] <= self.heap[right_child_index][0]:
            return left_child_index
        else:
            return right_child_index

    def __bubble_up(self, index):
        while self.__hasParent(index):
            if self.heap[index][0] < self.heap[self.__getParent(index)][0]:
                self.heap[index], self.heap[self.__getParent(index)] = self.heap[self.__getParent(index)], self.heap[index]
            index = self.__getParent(index)

    def __bubble_down(self, index):
        left_child_index, right_child_index = self.__getLeftChild(index), self.__getRightChild(index)
        while left_child_index is not None and right_child_index is not None:
            smallest_index = self.__smallestChild(left_child_index, right_child_index)
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            left_child_index, right_child_index = self.__getLeftChild(smallest_index), self.__getRightChild(smallest_index)

    def push(self, value):
        self.heap.append(value)
        self.__bubble_up(len(self.heap) - 1)

    def heap_pop(self, index):
        self.heap[index], self.heap[-1] = self.heap[-1], self.heap[index]
        elim = self.heap.pop(len(self.heap) - 1)
        if self.__hasChildren(index):
            self.__bubble_down(index)
        return elim