text = " Cloud Infra "
result1 = text.strip()

print('Success')

info = '''{
    'name': 'Chihiro'
    'addr': 'Yuseong'
    'foods': ['Cake', 'Bacon']
}'''
print(result1['name'])
print(result1['addr'])
print(result1['foods'])
print(result1['foods'][0])
print(result1['foods'][1])

result2 = json.dumps(result)

print('Success')

result = yaml.safe_load(info)
print(result)

print('finished')


result = yaml.dump(result, allow_unicode=True, sort_keys=True)

print(result2)

