MAXSIZE = 8
stack = [0] * MAXSIZE
top = -1
def isfull():
 if(top == MAXSIZE):
  return 1
 else:
  return 0
 

def push(data):
 global top
 if(isfull() != 1):
  top = top +1
  stack[top] = data
 else:
  print("Could not insert data, Stack is full")
 return data

push(44)
push(10)
push(62)
push(87)
push(34)
push(24)
push(4524)
push(324)
print("Stack Element: ")
for i in range(MAXSIZE):
 print(stack[i], end=" ")