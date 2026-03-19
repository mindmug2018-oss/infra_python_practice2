# Step05_Function.py

def test1():
    print('test() check')

test1()
result1 = test1()

def test2(arg):
    print('Received:', arg)
    print(f'Received: {arg}')

test2(10.1)
test2(10)
test2('Chihiro')


def print_sum(num1, num2):
    sum = num1+num2
    print(f'{num1} + {num2} = {sum}')

print_sum(10, 20)

def print_info(name: str, addr: str):
    print(f'Name {name} Address{addr}')

print_info('Chihiro', 'Yuseong')
print_info(addr="Beach", name='Port')

def get_sum(num1: int, num2: int):
    sum=num1+num2
    return sum

result2 = get_sum(10,20)

 
print('Sucess')