from os import system
import time
hh=int(input("enter hour"))
mm=int(input("enter minutes"))
ss=int(input("enter seconds"))
for i in range(hh,-1,-1):
	for j in range(mm,-1,-1):
		
		for k in range(ss,-1,-1):
			
			print('%2d:%2d:%2d' %(i,j,k))
			time.sleep(1)
			print("\033[H\033[j")
		ss=59
	mm=59
