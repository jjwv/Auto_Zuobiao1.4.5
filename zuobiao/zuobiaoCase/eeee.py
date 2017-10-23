import json
dict_a={}
dict_b=dict()
dict_a['a1']='b1'
dict_a['a2']='b2'
dict_a['a3']='b3'
#print(dict_a)
vs=dict_a.values()
#print(vs,type(vs))
dd=dict_a.get('a1')
#print(dd)
dict_a['a1']=dict_a['a3']
dict_a['a3']=dd
#print(dict_a)
ff=dict_a.pop('a1')
#print(dict_a)
dict_b.update(dict_a)
#print(dict_b)
dict_b['a1']='a1'
dict_b['a4']='null'
#print(dict_b,type(dict_b))

json_c=json.dumps(dict_b)
#print(json_c,type(json_c))

dict_c=json.loads(json_c)
print(dict_c,type(dict_c))


#dict_b=dict(a=1,b=2)
#dict_b=dict({'a':1,'b':2})
#dict_b=dict((('a',1),('b',2)))
#print(dict_b,type(dict_b))




