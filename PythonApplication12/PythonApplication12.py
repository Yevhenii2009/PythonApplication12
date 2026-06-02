def square (x):
    return x ** 2 
def multiply (x):
    return x * 2 
def subrtact (x):
    return x - 2 


def combine (type):
    if type == 'squere':
        return  square
    elif type == 'multiply':
        return  multiply 
    elif type == 'subtrct':
        return  subrtact
     
        

result = combine('squere')
print(result(2))
result = combine ('multiply') 
print(result(2))  
result = combine('subtrct')
print(result(3))

names = 'Nazar' 'Yevhennii dolbaeb '
user_name_upper = (lambda user_name:user_name.upper(),names)
print(list(user_name_upper ))