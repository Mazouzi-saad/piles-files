##créer une classe pour les piles:
class stack:
    def __init__(self):
        self.elements=[]
    def stack_push(self,s,data):
        s.append(data)
        return data
    def stack_pop(self,s):
        return s.pop()
    def stack_peek(self,s):
        return s[-1]
    def is_empty(self):
        return len(self.elements)==0
    def stack_create(self):
        return []
stack=stack()
##la copie d'une pile:
def stack_copy(s):
    s2=stack.stack_create()
    if len(s)!=0:
        t=stack.stack_create()
        for i in range(len(s)):
            e=stack.stack_peek(s)
            stack.stack_pop(s)
            stack.stack_push(t,e)
        for i in range(len(t)):
            e=stack.stack_peek(t)
            stack.stack_pop(t)
            stack.stack_push(s,e)
            stack.stack_push(s2,e)
    return s2
##inverser une pile:
def stack_reverse(s):
    rs=stack.stack_create()
    if len(s)!=0:
        sc=stack_copy(s)
        for i in range(len(sc)):
            e=stack.stack_peek(sc)
            stack.stack_pop(sc)
            stack.stack_push(rs,e)
    return rs
##une pile circulaire:
def stack_circperm(s,n):
    sc=stack.stack_create()
    for i in range(n,len(s)):
        e=stack.stack_peek(s)
        stack.stack_pop(s)
        stack.stack_push(sc,e)
    rs=stack_reverse(sc)
    for i in range(n):
        stack.stack_push(rs,s[i])
    return rs
##une pile circulaire:
def stack_circperm2(s,k):
    L=stack_circperm(s[:k],1)
    for i in range(k,len(s)):
        stack.stack_push(L,s[i])
    return L
##créer une classe pour les files:
class queue:
    def __init__(self):
        self.elements=[]
    def queue_enqueue(self,s,data):
        s.append(data)
        return data
    def queue_peek(self,s):
        return s[0]
    def queue_dequeue(self,s):
        return s.pop(0)
    def queue_is_empty(self,s):
        return len(s)==0
    def queue_create(self):
        return []
queue=queue()
##copier un file:
def queue_copy(s):
    qc=queue.queue_create()
    if len(s)!=0:
        for i in range(len(s)):
            e=queue.queue_peek(s)
            queue.queue_dequeue(s)
            queue.queue_enqueue(qc,e)
    return qc
##inverser un file:
def queue_reverse(s):
    rs=queue.queue_create()
    if len(s)!=0:
        sc=queue_copy(s)
        for i in range(len(sc)):
            e=queue.queue_peek(sc)
            queue.queue_dequeue(sc)
            queue.queue_enqueue(rs,e)
    return rs
##un file circulaire:
def queue_circperm(s,n):
    sc=queue.queue_create()
    for i in range(n,len(s)):
        e=queue.queue_peek(s)
        queue.queue_dequeue(s)
        queue.queue_enqueue(sc,e)
    rs=queue_reverse(sc)
    for i in range(n):
        queue.queue_dequeue(rs,s[i])
    return rs