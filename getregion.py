##############################################################################################
### Revised on 08/30/17 ######################################################################
##############################################################################################

import sys
import linecache 

#take the name of files
try:
	align = sys.argv[1]
	pdb = sys.argv[2]
except: 
	print("\n\tIncomplete arguments given!\n\tUsage: python getregion.py mapped_sequence_hmmscan model_pdbformat\n")
	quit(0)


#get position of alignment data
w=1
while (len(linecache.getline(align, w).split("== domain"))<2):
	w=w+1

#get information from alignment file
prot = linecache.getline(align,w+4).split()
domain = linecache.getline(align,w+2).split()[0]

p_init = int(prot[1])
p_end = int(prot[3]) 

print '\n\tfamily '+domain+' spans from residue '+str(p_init)+' to residue '+str(p_end)+" of protein sequence\n"
print '\n\tgenerating pruned model...\n'

output = open(pdb.split(".pdb")[0]+"_pruned.pdb", "w")

for k in range(p_init,p_end+1):
	counter=0
	for i in open(pdb):
		if (i[0:4]=="ATOM" and i[13:15]=="CA" and int(i[22:27])==k):
			counter=1
			output.write(i)
			break
	if (counter==0): print "\tMissing residue: "+str(k)+"\tCheck you original model!\n"

output.write("END\n")
output.close()

print "\n\tFile saved as: "+pdb.split(".pdb")[0]+"_pruned.pdb\n"
