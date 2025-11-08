from turtle import heading


class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        #print(i)
        print(f'before: {self.heap}')

        #percolate up
        while i > 1 and self.heap[i] <  self.heap[i//2]:
            tmp = self.heap[i]
            self.heap[i]= self.heap[i//2]
            self.heap[i//2] = tmp
            i = i//2

        print(f'after: {self.heap}')

    def pop(self):
        if len(self.heap) == 1:
            return 
        if len(self.heap) == 2:
            return self.heap.pop() #remove the last element which is the second one

        res = self.heap[1]
        #remove the 1st element
        #so replace the 1st element by the last element
        self.heap[1] = self.heap.pop()
        #after popping the heap is not heap anymore
        #we have to check for structure & order property
        i = 1
        #percolate down
        print("After Pop")
        print(self.heap)
        print(len(self.heap))

        while 2 * i < len(self.heap):
            if(2*i+1 < len(self.heap)) and self.heap[2*i+1] < self.heap[2*i] and self.heap[i] > self.heap[2*i+1]:
                #if ith value is greater than the right chile, swap the values
                tmp = self.heap[i]
                self.heap[i] = self.heap[2*i+1]
                self.heap[2*i+1] = tmp
                i = 2*i+1

            elif self.heap[i] > self.heap[2*i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[2*i]
                self.heap[2*i] = tmp
                i = 2*i
            else:
                #everthing is already heapified so break from the loop
                break
        return res
    
    def top(self):
        if len(self.heap) > 1:
            return self.heap[1]

        return None

    def heapify(self, arr):
        arr.append(arr[0])
        #0th position is moved to the end
        self.heap = arr
        cur = (len(self.heap) - 1)//2
        #self.heap[i//2] it's the parent node of the child node
        
        while cur > 0:
            i = cur
            while 2 * i < len(self.heap):
                if(2 * i + 1 < len(self.heap)) and self.heap[2 * i + 1] < self.heap[2*i] and self.heap[i] > self.heap[2*i+1]:
                    #swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2*i+1]
                    self.heap[2*i+1] = tmp
                    i = 2*i+1

                elif self.heap[i] > self.heap[2*i]: #left child is greater than root
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2*i]
                    self.heap[2*i] = tmp
                    i = 2*i
                else:
                    break
            cur -= 1
        

if __name__ == "__main__":
    S = Heap()

    S.push(10)
    S.push(5)
    S.push(20)
    S.push(2)
    S.push(7)
    S.pop()
