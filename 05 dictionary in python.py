'''
data = {1:'abhay',2:'kiran',4:'harsh'}
data
{1: 'abhay', 2: 'kiran', 4: 'harsh'}
data[4]
'harsh'
data[1]
'abhay'
data[3]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data[3]
KeyError: 3
data.get(1)
'abhay'
data.get(3)
print(data.get(1))
abhay
data.get(3, )
data.get(3,not found)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    data.get(3,not found)
NameError: name 'found' is not defined. Did you mean: 'round'?
data.get(3,'not found')
'not found'
keys = ['abhay','kiran','harsh']
values = ['Python','java','JS']
data = dict(zip(keys,values))
data
{'abhay': 'Python', 'kiran': 'java', 'harsh': 'JS'}
data['monika']
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    data['monika']
KeyError: 'monika'
data['monika']= 'CS'
data
{'abhay': 'Python', 'kiran': 'java', 'harsh': 'JS', 'monika': 'CS'}
del data['harsh']
data
{'abhay': 'Python', 'kiran': 'java', 'monika': 'CS'}




prog = {'js','atom','cs':'vs','python':['pycharm',sublime]}
SyntaxError: invalid syntax
prog = {'js','atom','cs':'vs','python':['pycharm','sublime'],'Java':{'jse':'Netbeans','jee':'eclips'}}
SyntaxError: invalid syntax
prog = {'js':'atom','cs':'vs','python':['pycharm','sublime'],'Java':{'jse':'Netbeans','jee':'eclips'}}
prog['js']
'atom'
prog['python']
['pycharm', 'sublime']
prog['python'][1]
'sublime'
prog['java']
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    prog['java']
KeyError: 'java'
prog['Java']
{'jse': 'Netbeans', 'jee': 'eclips'}
prog['java']['jee']
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    prog['java']['jee']
KeyError: 'java'
prog['Java']['jee']
'eclips'
'''