import os
import sys
from sklearn.metrics import *
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

'''
Input - two file names: 
1. groundtruthfile
2. predictedcommunityfile
It is assumed that predictedcommunityfile will have ------- in its first line

Return value: nmi value
'''
def makeplot(dest, nmidict, param_dir):
  xval = []
  yval = []
  for k in nmidict.keys():
    xval.append(float(k))
  xval.sort()
  for x in xval:
    if(x == 0.0):
      yval.append(np.mean(nmidict['0']))
    else:
      yval.append(np.mean(nmidict[str(x)]))
    #yval.append(np.mean(nmidict[k]))  
  plt.figure()
  matplotlib.style.use('ggplot')
  plt.axis([min(xval), max(xval),0,1])
  plt.plot(xval, yval, marker = 'o')
  plt.title("NMI", fontsize = 11)
  plt.xlabel(param_dir)
  plt.ylabel("NMI value")
  plt.axis([min(xval), max(xval),0,1])
  #plt.show()
  plt.savefig(dest+"nmi.png")
  plt.clf()
  plt.close()
  
def compute_nmi(groundtruthfile, predictedcommunityfile):
  true_file = open(groundtruthfile, 'r')
  pred_file = open(predictedcommunityfile, 'r')

  num_nodes = 200
  true_labels = [None]*num_nodes
  pred_labels = [None]*num_nodes

  linenum = 1
  for line in true_file:
    l = line.strip().split()
    l = [int(item.strip()) for item in l]
    for item in l:
      if(item>200):
        print(item)
      else:
        true_labels[item-1] = linenum
    linenum+=1
  
  pred_file.readline()
  linenum = 1
  for line in pred_file:
    l = line.rstrip().split()
    l = [int(item.strip()) for item in l]
    for item in l:
      #print(item)
      pred_labels[item-1] = linenum
    linenum+=1

  #Normalised mutual information. Function present in sklearn.metrics. Do not forget to import.
  nmi = normalized_mutual_info_score(true_labels, pred_labels) 
  return nmi



test_dirs = [d for d in os.listdir('./params/mu') if os.path.isdir(os.path.join('./params/mu', d))]

param_dirs = [d for d in os.listdir('./params') if os.path.isdir(os.path.join('./params', d))]

for param_dir in param_dirs:
  str1 = './params/' + param_dir +'/'
  nmidict = defaultdict(list)
  for test_dir in test_dirs:
    str2 = str1 + test_dir +'/'
    #fout = open(str2+"nmi",'w')
    dirs = [d for d in os.listdir(str2) if os.path.isdir(os.path.join(str2, d))]
    for dir1 in dirs:
      str3 = str2+dir1+'/'
      #print(str3 + '\n')
      true_file_name = str3+ "ground_truth_communities"
      pred_file_name = str3 +"predicted_communities"
      param_val = dir1[dir1.find('0'):]
      nmi = compute_nmi(true_file_name, pred_file_name)
      nmidict[param_val].append(nmi)
      #fout.write(param_val +' '+str(nmi)+'\n')
      #print(nmi)
    #fout.close()
  fout = open(str1+"nmi", 'w')
  for k in nmidict.keys():
    fout.write(str(k)+' '+str(np.mean(nmidict[k]))+'\n')
  fout.close()
  makeplot(str1, nmidict, param_dir)
