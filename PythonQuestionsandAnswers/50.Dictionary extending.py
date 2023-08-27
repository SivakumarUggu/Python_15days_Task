#Add a new key-value pair to an existing dictionary.
dict={1:'one',2:'two',3:'three'}
print(dict)
dict[4]='four'
print(dict)
dict['tinky']='pinky'
print(dict)
print(dict.get('tinky'))
print(dict.get('sony','not found'))
