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

	########################
	## SWITCH FOR TESTING ##
	########################

	SW_testcase=2

	###############
	## EXECUTION ##
	###############

	## system path SAFIR executable ##
	SAFIRpath="C:/SAFIR/SAFIR.exe"

	## *.in file without extension ##
	# NOTES
	# *.in file path should not include a "."
	if SW_testcase==1:
		# temperature calculation - steel profile
		infile="C:/Users/rvcoile/Documents/SAFIR/SAFIRpyTest/3DsteelbeamPy/w21x44"
		# success confirmed
	if SW_testcase==2:
		# structural calculation - frame (concrete columns, steel beam) example case JHU training
		infile="C:/Users/rvcoile/Documents/SAFIR/SAFIRpyTest/3Dframe_mod/3dframe"
		# seemingly limitation on *.in file path length
		# *.tem files should be copied to directory SAFIRpy
		# TO DO
		# - check if run refers to structural calc or thermal calc
		# - copy *.tem files in case of structural calc to SAFIRpy directory

	## execution ##
	SAFIR_exe(SAFIRpath,infile)