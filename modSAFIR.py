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
import os
import shutil
import pandas as pd
from copy import deepcopy

# local function reads
from runSAFIR import SAFIR_type,SAFIR_TEMinIN

##############
## FUNCTION ##
##############

def mod_inSAFIR(filein,fileout,modDict):

	# read original (reference) *.in
	f = open(filein,'r')
	filedata = f.read()
	f.close()

	# replace text
	newdata=deepcopy(filedata)
	for key in modDict.keys():
		# substitute must be string
		if not isinstance(modDict[key],str): modDict[key]=str(modDict[key])
		newdata = newdata.replace(key,modDict[key])

	# write update *.in file
	f = open(fileout,'w')
	f.write(newdata)
	f.close()

def mod_inSAFIR_multifile(df,reffile,SW_newfolder=False,SW_copytem=True):
	## function generates multiple *.in files ##
	# df : pd.DataFrame with variables to change
		# one row per *.in file
		# column headers indicate pointer in reference *.in file
	# reffile as *.in file with pointers for substitution
		# folder of reffile considered as folder for *.in (or new subfolder, see SW_newfolder) generation
	# SW_newfolder : boolean, indicating if *.in files are generated in their own folder
		# if True : generate *.in file in subfolder, with foldername = index pd.DataFrame
	# SW_copytem : boolean, allows to suppress copying *.tem file to target path - possibly future usage if *.tem file would be calculated as part of realization

	## df to dict
	modDict=df.to_dict(orient='index')
	## determine folder of reffile ##
	reffolder='\\'.join(reffile.split('\\')[0:-1])
	## *.in type and *.tem file path ## - only needed for SW_newfolder and structural analysis
	filetype=SAFIR_type(reffile)
	if not filetype=='Thermal2D' and SW_newfolder:
		temfilepath,temname=SAFIR_TEMinIN(reffile) # path to *.tem file

	## *.in generation for each realization ##
	# includes subfolder creation if SW_newfolder
	for sim in df.index:
		## simname as string if not already string ##
		# integer filled up to 5 characters with zeros
		if not isinstance(sim,str): simname='{0}'.format(sim).zfill(5) # assumes index is (integer) number
		else: simname=sim
		## new sub-folder creation if requested ##
		# existing folder emptied
		if SW_newfolder:
			newfolder=reffolder+'\\'+simname
			create_empty_folder(newfolder)
			if not filetype=='Thermal2D' and SW_copytem:
				temtargetpath=newfolder+'\\'+temname
				shutil.copy(temfilepath,temtargetpath) # copy *.tem file to SAFIRpy working directory

		## *.in file updating ##
		outfile=newfolder+'\\'+simname+'.in'
		localmodDict=modDict[sim] # modDict conform f[mod_inSAFIR] syntax
		mod_inSAFIR(reffile,outfile,localmodDict)
		

def create_empty_folder(newfolder):

	if os.path.exists(newfolder):
		# remove folder and all its contents if existing - avoid confusion on version run 
		# shutil.rmtree(newfolder) - issue encountered when immediately recreating folder
		for the_file in os.listdir(newfolder):
			file_path = os.path.join(newfolder, the_file)
			try:
				if os.path.isfile(file_path):
					os.unlink(file_path)
				elif os.path.isdir(file_path): shutil.rmtree(file_path)
			except Exception as e:
				print(e)
	else: os.mkdir(newfolder)





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


