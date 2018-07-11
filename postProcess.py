# __author__ = "RVC"
# __email__= "ruben.vancoile@gmail.com"
# __date__= "2018-07-11"

#
# post process SAFIR *.OUT file
# cfr. limitations capabilities DIAMOND
#


####################
## MODULE IMPORTS ##
####################

import re


##############
## FUNCTION ##
##############

#####################
## HARDCODED SETUP ##
#####################

highlight='#'*20

SW_nodeDef=False


##################
## USER DEFINED ##
##################

OUTfile="C:/Users/rvcoile/Google Drive/Research/Codes/Python3.6/SAFIRpy/refSim01/struct-ME__1.OUT"

seek01='SHELL'
seek02='NODES'
seek03='FIXATIONS'

prntNodeDef='nodeDef.txt'


#############################
## LOCATION SHELL ELEMENTS ##
#############################


##########
## CODE ##
##########

# initialize spacing output
print("\n") 

## Reading data from *.OUT file ##
##################################

# open out file - use with to ensure closing in case of exception
with open(OUTfile,'r') as f: # read-only opening of *.OUT file
	
	## initialize seekers (seeking in order)
	SW_seek01=True # indicates seeking for first keyword - idea: can seek for list of keywords
	SW_seek02=True 

	## number of shell elements
	while SW_seek01: # iterate over file till 
		s=f.readline()
		if seek01 in s: 
			SW_seek01=False
			intlist=[*map(int, re.findall(r'\d+', s))]
			nSHELL=intlist[0]

	## nodes and locations => print to external *.txt for independent processing
	with open(prntNodeDef,'w') as ff:
		while SW_seek02: 
			s=f.readline()
			print(s)
			if seek02 in s: SW_nodeDef=True
			if seek03 in s: SW_nodeDef=False; SW_seek02=False
			if SW_nodeDef: ff.write(s)

## Processing nodeDef info ##
#############################



##########
## TEST ##
##########

print(highlight+'\n'+highlight)
print(f.closed)
print(nSHELL)


