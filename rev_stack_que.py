class Node:
    def __init__(self,value):
        self.data = value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def __int__(self,value):
        self.data = value
        self.next = None
st = stack()
st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(34))
st.push(Node(78))
st.print(st)

def reverse_stack(s1):
    q1=LQueue()
    while not s1.isempty():
        q1.enqueue(Node(s1.pop()))
    while not q1.isempty():
        s1

