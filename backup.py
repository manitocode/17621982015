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

# 3.备份文件打包成zip文件
# 4.zip压缩文件命名由当前时间和时间构成
target = target_dir + os.sep + time.strftime('%Y%m%s%H%M%S') + '.zip'

# 如果目标目录不存在，则创建
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

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
