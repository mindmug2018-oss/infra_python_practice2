isMan=True
isWoman=False
isDifferent=True
isRun=False
mem1 = {'num': 1, 'name':'Chihiro', 'isMan':True}
info1 = [1,'Chihiro', True]
print(mem1['num'])
print(mem1['isMan'])

a = mem1['num']
b = mem1['name']
c = mem1 ['isMan']

mem1['num']=2
mem1['name'] = 'Chihiro'
mem1['isMan'] = False

mem2={'num':2, 'name': "Solution", 'isMan': False}

del mem1['isMan']

mem1.clear()
print('You are finished')