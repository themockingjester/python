from os import system
import time
hh=int(input("enter hour"))
mm=int(input("enter minutes"))
ss=int(input("enter seconds"))
for i in range(hh,-1,-1):
	for j in range(mm,-1,-1):
		
		for k in range(ss,-1,-1):
			_ = system('cls')
			print('%02d:%02d:%02d' %(i,j,k))
			time.sleep(1)
			 
		ss=59
	mm=59
