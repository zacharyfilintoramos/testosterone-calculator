##Testosterone Calculator
##Zachary Ramos

days = 1
weeks = 1

print("Please input your Testosterone level. (ng/L)")
t = int(input())

while t <= 1000:
	#calculate testosterone
	t = t * 1.01

	#calculate how long it takes
	days = days + 10
	weeks = days / 7

	#display how long it takes and how high the T will be at each time interval
	print (str(int(t)) + ' ng/L')
	print ('after ' + str(int(weeks)) + ' weeks of nofap')
	print (" ")
