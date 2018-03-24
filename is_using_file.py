poem = '''\
Programing is fun
When the work is done
if you wanna make your work also fun:
	use Python!
'''

# 打开文件以编辑（‘w’riting）
f = open('poem.txt','w')

# 想文件中写入文本
f.write(poem)
f.close()

f = open('poem.txt')
while True:
	line = f.readline()
	# 零长度只是EOF
	if len(line) == 0:
		break

	print(line,end=' ')
f.close()