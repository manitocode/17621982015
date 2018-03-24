# coding=UTF-8

class Robot:

# 一个类变量，用来计数机器人的数量
	population = 0

	def __init__(self,name):
		'''初始化数据'''
		self.name = name
		print('(Initializing {})'.format(self.name))

		Robot.population += 1

	def die(self):
		'''我挂了'''
		print('{} is be destroyed!'.format(self.name))

		Robot.population -= 1

		if Robot.population == 0:
			print('{} was the last one'.format(self.name))
		else:
			print('There are {:d} robots working.'.format(self.population))

	def say_hello(self):
		'''来自机器人的问候'''
		print('Greeting,my masters call me {}'.format(self.name))

	@classmethod
	def how_many(cls):
		'''打印出当前机器人的数量'''
		print('We have {:d} robots.'.format(cls.population))

droid1 = Robot('R2-D2')
droid1.say_hello()
Robot.how_many()

droid2 = Robot('C-X50')
droid2.say_hello()
Robot.how_many()

print('\n Robots can do some work here.\n')

print(":Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()