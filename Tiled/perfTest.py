import subprocess 

commandList = [
"sudo perf stat -B -e mem_load_uops_retired.l1_miss",
"sudo perf stat -B -e mem_load_uops_retired.l2_miss",
"sudo perf stat -B -e mem_load_uops_retired.llc_miss",
"sudo perf stat -B -e stalled-cycles-frontend",
"sudo perf stat -B -e dtlb_load_misses.stlb_hit",
"sudo perf stat -B -e dtlb_load_misses.miss_causes_a_walk",
"sudo perf stat -B -e page-faults"]



with open("perfDeeper.csv","a") as outf:
	for i  in range (1,1501,1):		
		if(1500%i != 0):
			continue
		print(i)

		outf.write(str(i)+";")
		for command in commandList:
			print("executing "+ command)
			# p = subprocess.Popen(["./a.out", str(i)], shell=False, stdout=subprocess.PIPE)
			# p = subprocess.Popen("sudo perf stat -o tmp.txt -e cache-misses ./a.out "+str(i),shell=True, stdout=subprocess.PIPE)
			p = subprocess.Popen(command + " -o tmp.txt ./a.out " + str(i), shell=True, stdout=subprocess.PIPE )
			p.wait()


			with open("tmp.txt","r") as pd:
				outf.write(pd.read().splitlines()[5].split()[0]+";")

			# with open("tmp.txt","r") as pd:

			# 	for j in pd:
			# 		if(j.find("cache") != -1):
			# 			# print(j.split()[0])	
			# 			outf.write(str(i)+";"+j.split()[0]+" ")

		outf.write("\n")


