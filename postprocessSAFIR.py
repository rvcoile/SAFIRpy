# __author__ = "RVC"
# __email__= "ruben.vancoile@gmail.com"
# __date__= "2018-09-26"

#
# postprocess SAFIR calculation
#


####################
## MODULE IMPORTS ##
####################

# standard module reads
import os
import subprocess
import shutil

# local function reads
# NONE

# distant function reads
# directory="C:/Users/rvcoile/Google Drive/Research/Codes/Python3.6/REF/rvcpy"
# sys.path.append(directory)
# from PrintAuxiliary import Print_DataFrame


##############
## FUNCTION ##
##############

def SAFIR_maxTIME(file):
	# determine last converged timestep in *.out file

	## read *.out file
	f = open(file,'r')
	filedata = f.read()
	f.close()

	## find converged timesteps
	codeword='TIME =' # found to be unique reference to converged timesteps
	index=filedata.rfind(codeword) # index of last occurrence codeword
	maxTime=filedata[index+6:index+12] # string-selection: 6 digits till decimal point - neglect after decimal
	maxTime=int(maxTime)

	return maxTime



#########################
## STAND ALONE - DEBUG ##
#########################

if __name__ == "__main__": 

	## outfile ##
	outfile="C:\\Users\\rvcoile\\Documents\\SAFIR\\SAFIRpyTest\\modfileTest\\mod_02b.OUT"

	## determine max time-step ##
	SAFIR_maxTIME(outfile)
