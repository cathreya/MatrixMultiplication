
import subprocess 
import time

with open("dump5.csv","a") as outf:
	for i  in range (1,2000,10):
		initial = time.perf_counter()
		print(i)
		p = subprocess.Popen(["./second", str(i)], shell=False)
		p.wait()

		final = time.perf_counter()

		if(p.returncode != 0):
			break
		# print(i,final - initial, p.returncode)
		outf.write(str(i)+","+str(final-initial)+"\n")



