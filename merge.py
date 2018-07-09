
with open("dumpo1.csv","w") as outf:
	cnt = 1;
	need  = 1;
	with open("dump3.csv","r") as inf:
		for i in inf:
			if(cnt == need):
				need+=10
				outf.write(i)
			cnt+=1
	with open("dump4.csv","r") as inf:
		for i in inf:
			if(cnt == need):
				need+=10
				outf.write(i)
			cnt+=1

		
		