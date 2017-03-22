import os
import sys
from shutil import copy2

alpha =[0.4,0.6,0.8,1.0]
density = [0.01,0.04,0.004,0.07,0.025,0.055]
p =[0.1,0.4,0.6,0.8,0.25]
mu =[0.2,0.4,0.05,0.55,0.75]

aname = "networks_alpha"
dname = "networks_density"
pname  ="networks_p"
muname = "networks_mu"

vary_alpha = "networks_p0.8/networks_mu0.4/networks_density0.04/" 
vary_p = "networks_mu0.4/networks_density0.04/" 
vary_mu = "networks_density0.04/" 


srcdir = ["/Users/prishni/Documents/MTP/All_Networks_New/","/Users/prishni/Documents/MTP/All_Networks_New1/"]

for src in srcdir:
	test_dirs = [d for d in os.listdir(src) if os.path.isdir(os.path.join(src, d))]
	for d in test_dirs:
		#Vary alpha. Parameters. p = 0.8, mu = 0.4, density = 0.04. 
		#Alpha is the top level directory
		#Hierarchy: alpha -> p -> mu -> density
		str1 = src + d + '/'
		alpha_dirs = [d2 for d2 in os.listdir(str1) if os.path.isdir(os.path.join(str1, d2))]
		for alpha_dir in alpha_dirs:
			str2 = str1 + alpha_dir +'/'
			str3 = str2 + vary_alpha + 'new_format' 
			dest_alpha ='./params/alpha/'+d+'/' + alpha_dir +'/'
			print(d)
		
			if not os.path.exists(dest_alpha):
			    os.makedirs(dest_alpha)

			copy2(str3,dest_alpha + 'new_format')


		#Vary p. Parameters. alpha = 0.6, mu = 0.4, density = 0.04. 
		#p is the top level directory
		#Hierarchy: alpha -> p -> mu -> density
		if d != 'test4':
			str1 = src + d + '/'
			alpha_dir = 'networks_alpha0.4/'
			str2 = str1 + alpha_dir
			p_dirs = [d2 for d2 in os.listdir(str2) if os.path.isdir(os.path.join(str2, d2))]
			for p_dir in p_dirs:
				str3 = str2 + p_dir +'/'
				str4 = str3 + vary_p + 'new_format' 
				desp_p ='./params/p/'+d+'/' + p_dir + '/'
				print(d)
			
				if not os.path.exists(desp_p):
				    os.makedirs(desp_p)

				copy2(str4,desp_p + 'new_format')


		#Vary mu. Parameters. p = 0.8, alpha = 0.6, density = 0.04. 
		#mu is the top level directory
		#Hierarchy: alpha -> p -> mu -> density
		if d != 'test4':
			str1 = src + d + '/'
			alpha_p_dir = 'networks_alpha0.6/networks_p0.8/'
			str2 = str1 + alpha_p_dir
			mu_dirs = [d2 for d2 in os.listdir(str2) if os.path.isdir(os.path.join(str2, d2))]
			for mu_dir in mu_dirs:
				str3 = str2 + mu_dir +'/'
				str4 = str3 + vary_mu + 'new_format' 
				desp_mu ='./params/mu/'+d+'/' + mu_dir + '/'
				print(d)
			
				if not os.path.exists(desp_mu):
				    os.makedirs(desp_mu)

				copy2(str4,desp_mu + 'new_format')


		#Vary density. Parameters. p = 0.8, alpha = 0.6, mu = 0.05. 
		#density is the top level directory
		#Hierarchy: alpha -> p -> mu -> density
		str1 = src + d + '/'
		alpha_p_mu_dir = 'networks_alpha0.6/networks_p0.4/networks_mu0.05/'
		str2 = str1 + alpha_p_mu_dir
		density_dirs = [d2 for d2 in os.listdir(str2) if os.path.isdir(os.path.join(str2, d2))]
		for density_dir in density_dirs:
			str3 = str2 + density_dir +'/'
			str4 = str3 + 'new_format' 
			desp_density ='./params/density/'+d+'/' + density_dir + '/'
			print(d)
		
			if not os.path.exists(desp_density):
			    os.makedirs(desp_density)

			copy2(str4,desp_density + 'new_format')

