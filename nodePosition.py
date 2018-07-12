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
import pandas as pd
import numpy as np


##############
## FUNCTION ##
##############

def singleNodeAddition(df_nodes,s):

	intlist=[*map(float, re.findall(r"[-+]?\d*\.\d+|\d+", s))]
	df_nodes[int(intlist[0])]=[str(int(intlist[0]))] + intlist[1:] # str for Number as workaround - consider Number as a name
	# df_nodes.loc[int(intlist[0])]=[int(intlist[0])] + intlist[1:] # trial01
	# df_nodes.loc['Number',int(intlist[0])]=int(intlist[0]) # trial02
	# df_nodes.loc[['X','Y','Z'],int(intlist[0])]=intlist[1:] # trial02

def nodeAddition(df_nodes,s):
	# initialize loop
	SW_readNext=True

	# input string contains NODE - extract as first NODE
	singleNodeAddition(df_nodes,s)

	# continue reading lines and handling
	


	# check if next one is GNODE - otherwise: let code pass through next NODE
	# question: can REPEAT follow NODE as well? (probably yes)

def equidistantNodeAddition(df_nodes,s):
	## generate equidistant nodes from previous node

	# collect last entry
	previousNode=df_nodes[df_nodes.columns[-1]] # pd.Series with last entry

	# info equidistant command
	equilist=[*map(float, re.findall(r"[-+]?\d*\.\d+|\d+", s))]
	endNode=pd.Series([str(int(equilist[0]))] + equilist[1:-1],index=df_nodes.index)

	# generate equidistant nodes betwen previousNode and endNode
	stepsize=int(equilist[-1]) # assumed meaning
	nodes=np.arange(int(previousNode['Number']),int(endNode['Number']))

	X=np.linspace(previousNode['X'],endNode['X'],(int(endNode['Number'])-int(previousNode['Number'])+1)/stepsize,endpoint=False)
	Y=np.linspace(previousNode['Y'],endNode['Y'],(int(endNode['Number'])-int(previousNode['Number'])+1)/stepsize,endpoint=False)
	Z=np.linspace(previousNode['Z'],endNode['Z'],(int(endNode['Number'])-int(previousNode['Number'])+1)/stepsize,endpoint=False)

	# add to df_nodes
	print(int(nodes[1:])) # ERROR - work not completed - future work 'DamageVisualization'
	# df_nodes[int(nodes[1:])]=[str(nodes[1:]),X[1:],Y[1:],Z[1:]]




#####################
## HARDCODED SETUP ##
#####################

highlight='#'*20


##################
## USER DEFINED ##
##################

file_nodeDef='nodeDef.txt'

#############################
## LOCATION SHELL ELEMENTS ##
#############################


##########
## CODE ##
##########

# initialize spacing output
print("\n") 

## Reading data from nodeDef-file ##
####################################

# open file - use 'with' to ensure closing in case of exception
with open(file_nodeDef,'r') as f: # read-only opening of nodDef-file

	s=f.readline() # first line NODES - hardcoded syntax

	# initialize DataFrame nodes
	df_nodes=pd.DataFrame(index=['Number','X','Y','Z'])
	
	while s: # empty string returns false - end of file returns empty string
		s=f.readline()
		if 'GNODE' in s: equidistantNodeAddition(df_nodes,s)
		elif 'NODE' in s: singleNodeAddition(df_nodes,s)


	
	# ## initialize seekers (seeking in order)
	# SW_seek01=True # indicates seeking for first keyword - idea: can seek for list of keywords
	# SW_seek02=True 

	# ## number of shell elements
	# while SW_seek01: # iterate over file till 
	# 	s=f.readline()
	# 	if seek01 in s: 
	# 		SW_seek01=False
	# 		intlist=[*map(int, re.findall(r'\d+', s))]
	# 		nSHELL=intlist[0]

	# ## nodes and locations => print to external *.txt for independent processing
	# with open(prntNodeDef,'w') as ff:
	# 	while SW_seek02: 
	# 		s=f.readline()
	# 		print(s)
	# 		if seek02 in s: SW_nodeDef=True
	# 		if seek03 in s: SW_nodeDef=False; SW_seek02=False
	# 		if SW_nodeDef: ff.write(s)

## Processing nodeDef info ##
#############################



##########
## TEST ##
##########

print(highlight+'\n'+highlight)
print(f.closed)
print(df_nodes)


