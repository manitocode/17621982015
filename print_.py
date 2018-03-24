#

Myname = 'wangwg'
Myage = 23
Myheight = 173
Myweight = 54
Myeye = 'black'
Myteeth = 'white'
Mahair = 'black'

print ("Myname is %s." %Myname)
print ("Myage is %d." % Myage) 
print ("He has %s eyes and %s teeth." %(Myeye,Myteeth))

#while True:
#	for i in ["/","-","|","\\","|"]:
#		print ("%s\r" %i)

# - - - - - - - - - - - - - - - - - - - - - - 
#print ("How old are you?",)
#age = input()
#print ("How tall are you?",)
#height = input()
#print ("How much do you weigh?",)
#weight = input()

#print ("So, you're %r old, %r tall and %r heavy." % (
#    age, height, weight))

# - - - - - - - - - - - - - - - - - - - - - - 

'''It is a test for list
And it is the first time.
'''

shoplist = ['Apple','Banana','mango','Carrot']
print("I have",len(shoplist),'items to bought')
print('These items are:',end = ' ')
for items in shoplist:
	print(items, end = ' ')

print('\nI also hava to buy rice.')
shoplist.append('rice')
print('My shoplist is now',shoplist)

print('I will list my shoplist now.')
shoplist.sort()
print('Sorted shoplist is now.',shoplist)

print('The first item that i will buy is',shoplist[0])
oldItem = shoplist[0]
del shoplist[0]
print('I bought the',oldItem)
print('My shoplist is now',shoplist)

# - - - - - - - - - - - - - - - - - - - - - - 

'''It is a test for Tuple
And it is the first time.
'''
Zoo = ('python','elephant','penguin')
print('The numbers of Zoo is',len(Zoo))

new_zoo = ('monkey','camel',Zoo)
print('The numbers of new zoo is',len(new_zoo))
print('All animals in new_zoo are',new_zoo)
print('All animals from Zoo are',new_zoo[2])
print('Last animal from Zoo is',new_zoo[2][2])
print('All animals numbers is',len(new_zoo) - 1 + len(new_zoo[2]))

# - - - - - - - - - - - - - - - - - - - - - - 

'''It is a test for dict
And it is the first time.
'''

dict_1 = {
	'Swaroop':'Swaroop@qq.com',
	'Larry':'Larry@qq.com',
	'Matsadsad':'Matsadsad@qq.com',
	'Spanner':'Spanner@qq.com'
}
print('Swaroop address is',dict_1['Swaroop'])

del dict_1['Swaroop']
print('\nThere are {} contacts in the address-book \n'.format(len(dict_1)))

for name,address in dict_1.items():
	print('contacts {} at {}'.format(name,address))

dict_1['wangwg'] = 'wangwg@qq.com'

if 'wangwg' in dict_1:
	print('\nwangwg address is',dict_1['wangwg'])

# - - - - - - - - - - - - - - - - - - - - - - 

'''It is a test for set
And it is the first time.
'''

print('Simple Assignment')

shoplist = ['apple','mango','Banana','Carrot']
mylist = shoplist
del shoplist[0]

print('shoplist is',shoplist)
print('mylist is',mylist)

print('Copy by making a full slice')  #备份一个序列的副本，需要使用切片操作来复制
shoplist.append('apple')
mylist = shoplist[:]
del shoplist[0]

print('shoplist is',shoplist)
print('mylist is',mylist)












