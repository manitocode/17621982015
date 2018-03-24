'''question:
	设计一个程序备份所有重要的文件
Analysis and Design:
	1.把需要备份的文件和目录放置一个列表里
	2.备份必须储存在一个主备份目录中
	3备份文件将打包成.zip文件
	4.zip压缩文件命名由当前时间和时间构成
'''
import os,time

# 1.需要备份的文件和目录放置在列表中
# e.g. 在wimdows下：
# source = ['"C:\\My Document"','C:\\Code']   # 使用双引号去除空格的影响
# e.g. 在Mac OS X 和 Linux 下：
source = ['/Users/night/manito_code']

# 2.备份的文件必须放在一个主备份目录中
target_dir = '/Users/night/manito_code/backup'

# 如果目标目录不存在，则创建
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

# 3.备份文件打包成zip文件
# 4.将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

#添加一条来自用户的注释以创建zip文件的name
comment = input('Enter a comment >> ')
if len(comment) == 0:
	target = today + os.sep + now +'.zip'
else:
	target = today + os.sep + now + '_' + \
		comment.replace(' ','_') + '.zip'

#target = today + os.sep + now + '.zip'
#target = target_dir + os.sep + time.strftime('%Y%m%s%H%M%S') + '.zip'

#如果子目录尚不存在，则创建一个
if not os.path.exists(today):
	os.mkdir(today)
	print('Successful created directory',today)

# 5.使用zip命令将文件打包成zip形式
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

# backup.start
print('Zip command is:')
print(zip_command)
print('Running :')
if os.system(zip_command) == 0:
	print('Successful backup to',target)
else:
	print('Backup Failed.')
