# 判断一个字符串是否是回文：
# 原文 = 倒序后的文本

def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)

something = input('Enter a str:')

if is_palindrome(something):
	print('yes, it is a palindrome.')
else:
	print('no, it is not a palindrome.')