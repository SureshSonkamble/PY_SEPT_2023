d={
    'a':'100',
    'b':'200',
    'monika':'5555'
    }

# Taking input key = 1, value = Geek
k=input("Enter key")
v=input("enter value")
d.update({k: v})

print(d)
print(d['monika'])
s=input("enter student name:")
print(d[s])
