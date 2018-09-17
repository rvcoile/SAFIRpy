# __author__ = "RVC"
# __email__= "ruben.vancoile@gmail.com"
# __date__= "2018-07-11"

#
# node positions SAFIR based on extracted nodeDef.txt file
#,'nodeTest',['df']


####################
## MODULE IMPORTS ##
####################

import re
import pandas as pd
import numpy as np
import sys
from copy import deepcopy
import json

directory="C:/Users/rvcoile/Google Drive/Research/Codes/Python3.6/REF/rvcpy"
sys.path.append(directory)

from PrintAuxiliary import Print_DataFrame


##############
## FUNCTION ##
##############

def singleNodeAddition(df_nodes,s):

	intlist=[*map(float, re.findall(r"[-+]?\d*\.\d+|\d+", s))]
	df_nodes[int(intlist[0])]=[str(int(intlist[0]))] + intlist[1:] # str for Number as workaround - consider Number as a name
	# df_nodes.loc[int(intlist[0])]=[int(intlist[0])] + intlist[1:] # trial01
	# df_nodes.loc['Number',int(intlist[0])]=int(intlist[0]) # trial02
	# df_nodes.loc[['X','Y','Z'],int(intlist[0])]=intlist[1:] # trial02

def equidistantNodeAddition(df_nodes,s):
	## generate equidistant nodes from previous node

	# collect last entry
	previousNode=df_nodes[df_nodes.columns[-1]] # pd.Series with last entry

	# info equidistant command
	equilist=[*map(float, re.findall(r"[-+]?\d*\.\d+|\d+", s))]
	endNode=pd.Series([str(int(equilist[0]))] + equilist[1:-1],index=df_nodes.index)

	# generate equidistant nodes betwen previousNode and endNode
	stepsize=int(equilist[-1]) # assumed meaning
	nodes=np.arange(int(previousNode['Number']),int(endNode['Number'])+1)

	X=list(np.linspace(previousNode['X'],endNode['X'],(int(endNode['Number'])-int(previousNode['Number'])+1)/stepsize,endpoint=True))
	Y=list(np.linspace(previousNode['Y'],endNode['Y'],(int(endNode['Number'])-int(previousNode['Number'])+1)/stepsize,endpoint=True))
	Z=list(np.linspace(previousNode['Z'],endNode['Z'],(int(endNode['Number'])-int(previousNode['Number'])+1)/stepsize,endpoint=True))
	Number=list(nodes); Number=[str(int(i)) for i in Number]

	# add to df_nodes
	tmp=pd.DataFrame([Number[1:],X[1:],Y[1:],Z[1:]],index=['Number','X','Y','Z'],columns=nodes[1:])
	df_nodes=pd.concat([df_nodes,tmp],axis=1)

	return df_nodes

def repeatNodeAddition(df_nodes,s):
	## repeat N nodes, with specified increment Delta, n times

	# repeat command
	repeat=[*map(float, re.findall(r"[-+]?\d*\.\d+|\d+", s))]
	N=int(repeat[0])
	Delta=repeat[1:4]
	n=int(repeat[-1])

	# perform repeat
	df_local=deepcopy(df_nodes.transpose()) # transpose df_nodes for next handling
	df_local=df_local.tail(N) # select last N rows of dataframe

	for i in np.arange(n):

		# add Delta
		number=df_local.index.values+N; Number=[str(int(i)) for i in number]
		df_local.index=number
		df_local.loc[:,'Number']=Number
		df_local.loc[:,'X']+=Delta[0] # add X-delta
		df_local.loc[:,'Y']+=Delta[1] # add Y-delta
		df_local.loc[:,'Z']+=Delta[2] # add Z-delta

		# add to df_nodes
		df_nodes=pd.concat([df_nodes,df_local.transpose()],axis=1)

	return df_nodes


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
		if 'GNODE' in s: df_nodes=equidistantNodeAddition(df_nodes,s)
		elif 'NODE' in s: singleNodeAddition(df_nodes,s)
		elif 'REPEAT' in s: df_nodes=repeatNodeAddition(df_nodes,s)


	
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

df_nodes=df_nodes.transpose()

##########
## TEST ##
##########

print(highlight+'\n'+highlight)
print(f.closed)
# print(df_nodes)

###########
## PRINT ##
###########

Print_DataFrame([df_nodes],'nodeTest',['df'])

with open('nodeData_JSON','w') as f:
	f.write(df_nodes.to_json())