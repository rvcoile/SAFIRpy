# __author__ = "RVC"
# __email__= "ruben.vancoile@gmail.com"
# __date__= "2018-09-26"

#
# updates SAFIR *.in file
#


####################
## MODULE IMPORTS ##
####################

## standard module reads ##
import pandas as pd


##############
## FUNCTION ##
##############

def mod_inSAFIR(filein,fileout,modDict):

	# read original (reference) *.in
	f = open(filein,'r')
	filedata = f.read()
	f.close()

	# replace text
	for key in modDict.keys():
		newdata = filedata.replace(key,modDict[key])

	# write update *.in file
	f = open(fileout,'w')
	f.write(newdata)
	f.close()


#########################
## STAND ALONE - DEBUG ##
#########################

if __name__ == "__main__": 

	## *.in file to be modified ##
	reffile="C:\\Users\\rvcoile\\Documents\\SAFIR\\SAFIRpyTest\\modfileTest\\Fsearch_N.in"

	## target *.in path ##
	outfile="C:\\Users\\rvcoile\\Documents\\SAFIR\\SAFIRpyTest\\modfileTest\\mod.in"

	## Variables to be modified ##
	# variable 00
	ref00='Fsearch'
	sub00=str(6*10**6)
	# combination into Dict
	modDict={
	ref00:sub00
	}

	## Modification of *.in file ##
	mod_inSAFIR(reffile,outfile,modDict)

	## Testing ##
	# print(modDict)
	# print(modDict.keys)


