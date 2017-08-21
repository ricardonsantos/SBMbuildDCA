##############################################################################################
### Revised on 10/02/13 ######################################################################
##############################################################################################

import sys
import linecache 

#take the name of files
try:
	align = sys.argv[1]
	ranked = sys.argv[2]
except: 
	print("\n\tIncomplete arguments given!\n\tUsage: python map_dca.py mapped_sequence_hmmscan ranked_dca_pairs\n")
	quit(0)


#get position of alignment data
w=1
while (len(linecache.getline(align, w).split("== domain"))<2):
	w=w+1

#get information from alignment file
domain = linecache.getline(align,w+2).split()
prot = linecache.getline(align,w+4).split()

print '\n\tDomain:\t'+domain[0].rjust(10)+'\n\tProtein ID:\t'+prot[0].rjust(10)+'\n'
print '\tgenerating matched alignment...\n'

d_init = int(domain[1])
d_end = int(domain[3]) 
p_init = int(prot[1])
p_end = int(prot[3]) 

#domain sequence string
l1 = domain[2]
#protein sequence string
l2 = prot[2]

x1 = len(l1)
x2 = len(l2)

output1 = open(align+"_reference.txt", "w")
output1.write('Domain \t n \t Protein \t n\n')

#get the difference between initial positions
delta = max(x1,x2)
#delta = max(d_end-d_init,p_end-p_init)



#domain code and respective number
d = []
dn = []
#protein code and respective number
p = []
pn = []

#fill d and p arrays with domain and protein sequences
for i in range(0,delta):
	d.append(l1[i])
	p.append(l2[i])

#compute the original positions in the system

j1=-1
j2=-1
for i in range(0,len(d)):
	if d[i]!='.':
		j1+=1
		dn.append(str(d_init+j1))
	if d[i]=='.':
		dn.append('')
	if p[i]!='-':
		j2+=1
		pn.append(str(p_init+j2))
	if p[i]=='-':
		pn.append('')
	output1.write(d[i]+'\t'+str(dn[i])+'\t'+p[i]+'\t'+str(pn[i])+'\n')


output1.close()

## Matching

output2 = open(align+"_ranked_matched.DI", "w")

#open the ID file with ranking pairs
f=open(ranked,'r')

dic = {}

for i in range(0,len(dn)):
	if d[i]!='.' and p[i]!='-':
		dic[dn[i]]=pn[i]

#outer loop runs along all DCA pairs

for i in range(1,len(f.readlines())):
	pair = linecache.getline(ranked, i)
	pair1 = pair.split()[0]
	pair2 = pair.split()[1]
	try:
		if pair1 and pair2 in dic:	
			output2.write(dic[pair1]+'\t'+dic[pair2]+'\n')
	except KeyError:
		pass
     
output2.close()

print "\n\tFile of mapped pairs saved as "+align+"_ranked_matched.DI\n"
print "\n\tFile of sequence correspondence saved as "+align+"_reference.txt\n\n"

