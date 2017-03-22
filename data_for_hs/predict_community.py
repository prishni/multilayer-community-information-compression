import os
import sys



test_dirs = [d for d in os.listdir('./params/mu') if os.path.isdir(os.path.join('./params/mu', d))]
param_dirs = [d for d in os.listdir('./params') if os.path.isdir(os.path.join('./params', d))]
codepath = 'java -jar /Users/prishni/Documents/sem2/complex/project/hetero_scala/target/scala-2.10/hetcom.jar dir cm /Users/prishni/Documents/sem2/complex/project/data_for_hs/'

for param_dir in param_dirs:
	str1 = 'params/' + param_dir +'/'
	for test_dir in test_dirs:
		str2 = str1 + test_dir +'/'
		dirs = [d for d in os.listdir(str2) if os.path.isdir(os.path.join(str2, d))]
		for dir1 in dirs:
			str3 = str2+dir1+'/'
			print(str3 + '\n')
			syscall = codepath+str3+" > /Users/prishni/Documents/sem2/complex/project/data_for_hs/"+str3+"predicted_communities"
			os.system(syscall)			





	