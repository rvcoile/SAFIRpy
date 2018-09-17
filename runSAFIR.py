# __author__ = "RVC"
# __email__= "ruben.vancoile@gmail.com"
# __date__= "2018-09-17"

#
# run SAFIR through Python shell
#


####################
## MODULE IMPORTS ##
####################

# standard module reads
import os
import subprocess

# local function reads
# NONE

# distant function reads
# directory="C:/Users/rvcoile/Google Drive/Research/Codes/Python3.6/REF/rvcpy"
# sys.path.append(directory)
# from PrintAuxiliary import Print_DataFrame


##############
## FUNCTION ##
##############

def SAFIR_exe(path,file):

	## run through os
	# os.system(path)

	## run through subprocess
	subprocess.call([path,file])


#####################
## HARDCODED SETUP ##
#####################

##################
## USER DEFINED ##
##################


##########
## CODE ##
##########


##########
## TEST ##
##########

###########
## PRINT ##
###########

# Print_DataFrame([df_nodes],'nodeTest',['df'])

#########################
## STAND ALONE - DEBUG ##
#########################

if __name__ == "__main__": 

	## system path SAFIR executable ##
	SAFIRpath="C:/SAFIR/SAFIR.exe"

	## *.in file without extension ##
	infile="C:/Users/rvcoile/Documents/SAFIR/3DsteelbeamPy/w21x44"

	## execution ##
	SAFIR_exe(SAFIRpath,infile)