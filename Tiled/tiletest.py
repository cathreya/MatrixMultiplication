
import subprocess 


with open("tileO1.csv","a") as outf:
	for i  in range (1,2000,1):		
		if(1500%i != 0):
			continue
		print(i)

		p = subprocess.Popen(["./a.out", str(i)], shell=False, stdout=subprocess.PIPE)
		tim = p.communicate()[0]
		p.wait()

		print(tim)


		if(p.returncode != 0):
			break
		# print(i,final - initial, p.returncode)
		outf.write(str(i)+","+str(tim)+"\n")



