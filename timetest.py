
import subprocess 


with open("onlyMulO3.csv","a") as outf:
	for i  in range (1,2000,10):		
		print(i)
		p = subprocess.Popen(["./third", str(i)], shell=False, stdout=subprocess.PIPE)
		tim = p.communicate()[0]
		p.wait()

		print(tim)


		if(p.returncode != 0):
			break
		# print(i,final - initial, p.returncode)
		outf.write(str(i)+","+str(tim)+"\n")



