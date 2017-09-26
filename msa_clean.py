##########################################################################################
## This program cleans Pfam domain sequences taking of the dots "." and lower case      ##
## residues, in order to reduce file size. These positions are ignored in DCA analysis. ##
## rikchicfb@gmail.com - 09/26/2017							##
##########################################################################################

import linecache
import textwrap
import sys

data = sys.argv[1]
size = open(data,"r")

i=1
l = len(size.readlines())

output = open(data.split(".")[0]+"_clean","w")

####################################################################################
nseq = 0
####################################################################################

while i < l:
	sequence = ""
	n = linecache.getline(data,i)	
	counter = 0	
	if n[0] == ">":
		name = n
		next = linecache.getline(data, i+1)
		try:
			while next[0] != ">":
				sequence=sequence+next
				i+=1
				next =  linecache.getline(data, i+1)
			nseq+=1
		except IndexError:
			pass
	i+=1
	x=""
	for j in range(0,len(sequence)):
		if sequence[j]!="." and sequence[j]!="\n" and sequence[j].islower()==False:
			x+=sequence[j]
	output.write(name+x+"\n")
output.close()


print "\n\tTotal number of sequences: "+str(nseq)
print "\n\tFile saved as: "+data.split(".")[0]+"_clean\n"



