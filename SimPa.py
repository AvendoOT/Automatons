from collections import deque  

class Stack(deque):
    def __init__(self, z0=None):
        super().__init__(self)
        self.append('$')   
        if z0 is not None:
            self.push(z0)  
        return
    def __repr__(self):
        a = "".join(self)
        if a == '$':
            return a
        else:
            return a[:-1]
    def peek(self):
        return self[0]

    def isEmpty(self):
        return self.peek() == '$'
    
    def push(self, a):
        if a != '$':
            for t in a[::-1]:
                self.appendleft(t)
        return
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.popleft()
    
   

nizovi = input().split("|")
stanja = input().split(",")
simboli = input().split(",")
stog_simboli = input().split(",")
prihvatljivaStanja = input().split(",")
q0 = input()
z0 = input()
omega = dict() 

prijelaz = input()
while (prijelaz != "" and prijelaz != "\n"):
    prijelaz = prijelaz.split("->")
    stanje, znak, stog_znak = tuple(prijelaz[0].split(','))
    omega[(stanje, znak, stog_znak)] = tuple(prijelaz[1].split(","))
    try:
        prijelaz = input()
    except:
        prijelaz = ""
        
for s in nizovi:
    s = s.split(",")    
    q = q0              
    z = z0              
    stack = Stack()
    print("{}#{}".format(q0, z0), end="|")
    greska = False      
    for sim in s:
        while (q, '$', z) in omega:
            q, zNovi = omega[(q, '$', z)]
            stack.push(zNovi)
            print("{}#{}".format(q, stack), end="|")    
            z = stack.pop()
            if z is None:                               
                greska = True                           
                break                                   

        if not greska:
            if (q, sim, z) in omega:            
                q, zNovi = omega[(q, sim, z)]  
                stack.push(zNovi)
                print("{}#{}".format(q, stack), end="|")
                z = stack.pop()
                if z is None:
                    greska = True
            else:
                greska = True                           
                
        if greska:                                       
            print("fail|0")
            break
    if not greska:
        while (q, '$', z) in omega and q not in prihvatljivaStanja:
            q, zNovi = omega[(q, '$', z)]
            stack.push(zNovi)
            print("{}#{}".format(q, stack), end="|")
            z = stack.pop()
            if z is None:
                greska = True
                break 
        print(1 if q in prihvatljivaStanja else 0)
    del(stack)  
            
