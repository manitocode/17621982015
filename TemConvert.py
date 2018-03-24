#TempConvert.py
TempStr = input("input 28F or 82C , please: ")
if TempStr[-1] in ['F','f']:
	C = (eval(TempStr[0:-1]) - 32)/1.8
	print("The F -> C is {:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
	C = 1.8*eval(TempStr[0:-1]) + 32
	print("The C -> F is {:.2f}F".format(C))
else:
	print("Error input.")
