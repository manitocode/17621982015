#-*- coding:utf-8 -*-

class aQueue(object):

    def __init__(self):
        self.data_list = []

    #def init_queue(self):
        #self.data_list = []

    def insert(self, data):
        self.data_list.append(data)

    def pop(self):
        if len(self.data_list) == 0:
            return None
        data = self.data_list[0]
        # stack:{ data = self.data_list[-1] }
        del self.data_list[0] # queue 先进先出
        # stack后进先出:{ del self.data_list[-1] }
        return data

    def size(self):
        return len(self.data_list)


queue = aQueue()
print(queue.size())
queue.insert(1)
queue.insert(2)
queue.insert(3)
print("lenth:{}".format(queue.size()))
head = queue.pop()
print(head)
head = queue.pop()
print(head)
head = queue.pop()
print(head)
head = queue.pop()
print(head)