
import subprocess 
import time

with open("dump2.csv","a") as outf:
	for i  in range (1,1000,1):
		initial = time.perf_counter()
		print(i)
		p = subprocess.Popen(["./a.out", str(i)], shell=False)
		p.wait()

		final = time.perf_counter()

		if(p.returncode != 0):
			break
		# print(i,final - initial, p.returncode)
		outf.write(str(i)+","+str(final-initial)+"\n")



