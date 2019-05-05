import string
import time
from random import randint
n = 95
s = string.ascii_letters + string.digits + string.punctuation
active = [False]*n
#print("\x1b[1;32;40m")
while True:
	for _ in range(int(n*.2)):
		x = randint(0,n-1)
		active[x] = not active[x]
	temp = ""
	for i in range(n):
		x = randint(0,len(s)-1)
		temp += s[x]+" " if active[i] else "  "
	print(temp)
	time.sleep(1/20)