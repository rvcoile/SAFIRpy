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
# NONE

# local function reads
from runSAFIR import SAFIR_exe

# distant function reads
# directory="C:/Users/rvcoile/Google Drive/Research/Codes/Python3.6/REF/rvcpy"
# sys.path.append(directory)
# from PrintAuxiliary import Print_DataFrame


##############
## FUNCTION ##
##############

def userInput():

	## filename
	filename=input("\nPlease provide path to input file (*.in): ")
	if filename[0]=="\"": filename=filename[1:-1] # strips quotes from path

	return filename


#########################
## STAND ALONE - DEBUG ##
#########################

if __name__ == "__main__": 

	## system path SAFIR executable ##
	SAFIRpath="C:/SAFIR/SAFIR.exe"

	## *.in file with extension ##
	infile=userInput()

	## testing ##
	print(infile)

	## execution ##
	SAFIR_exe(SAFIRpath,infile)

