# 空のリスト
hoge = []
print(hoge)
# []

print(len(hoge))
# 0

hoge = hoge + ['a','b']
print(hoge)
#['a','b']

hoge = ['c'] + hoge
print(hoge)
#['c','a','b']

print(len(hoge))
# 3