#coding:utf-8

class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack(object):
    def __init__(self):
        self.top = None
        self.__size = 0

    def size(self):                 #获取size
            return self.__size
   


    def pop(self):                  #弹出栈顶数据
        if self.top == None:
            return None
        else:
            tmp = self.top.val
            self.top = self.top.next
            self.__size -= 1
            return tmp



    def push(self,n):               #添加到栈
        n = Node(n)
        n.next = self.top
        self.top = n
        self.__size += 1
        return n.val
    



class Queue(object):
    def __init__(self):
        self.stack_In = Stack()
        self.stack_Out = Stack()


    def pop(self):
        if self.stack_Out.size() == 0:     
            while self.stack_In.size() > 0:
                tmp = self.stack_In.pop()
                self.stack_Out.push(tmp)
        return self.stack_Out.pop() 

    def push(self,n):
        return self.stack_In.push(n)

    def size(self):
        return self.stack_In.size() + self.stack_Out.size()



if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print s.pop()
    print s.size()
    
    p = Queue()
    p.push(1)
    p.push(2)
    p.push(3)

    print p.pop()

    print p.size()























