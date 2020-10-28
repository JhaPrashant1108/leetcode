# def marks(english,math=85,science = 80, history):
#     print(english)
#     print(math)
#     print(science)

# marks(science=70,math=90,english=75,history=25)

def trans(n):
    return lambda x:x + n

print(trans(9)(4))