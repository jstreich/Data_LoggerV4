print"---------------------------------------------------"
print"-  Data Logger                                    -"
print"-  Version: 4.0.0                                 -"
print"-  Author: Jared Streich                          -"
print"-  Created 2019-07-22                             -"
print"---------------------------------------------------"
print"- Make sure scanline is installed and working     -"
print"- scanline https://github.com/klep/scanline       -"
print"- Type 'End' at anytime to stop script            -"
print"- Using the same name for a data sheet will       -"
print"-  erase the previous sheet, use unique names.    -"
print"- Handheld scanner, 1D or 2D compatible           -"
print"---------------------------------------------------"
print"- Usage:                                          -"
print"- Name outputfile:   Example: Exp_Date.txt        -"
print"- Step 1: Script starts, Enter sample name        -"
print"- Step 2: Enter Petiole Diameter                  -"
print"- Step 3: Enter Petiole Length                    -"
print"- Step 3: SPAD                                    -"
print"- Step 4: Take Three Measures of Leaf Thinkness   -"
print"- Step 5: Press Enter when leaf is ready Scaning  -"
print"---------------------------------------------------"



################################ Required software: ###################################
# scanline https://github.com/klep/scanline


################################# Import packages #####################################
from datetime import datetime
import subprocess
import os
from decimal import Decimal
import os.path
from os import path


################################# Set preset Variables ###################################
##### Define continuously adjusted variables
number_of_plants = 0
step=1
lfthk=0.00
SPAD=0.0

##### Create averaging function
def Average(lst):
	return sum(lst) / len(lst)

##### Print current directory
dirpath = os.getcwd()
print("current directory is : " + dirpath)


print '\n'

#define file UID
filename = raw_input('Input the filename record to save as, without extension .txt:\n')


###################################### Set Step ##########################################
step=1


while step != 0:
#step 1 get plant ID
	if step == 1:
		plant = raw_input('Input Accession ID %i:\n' % (number_of_plants + 1))
		if plant=='end' or plant=='END' or plant=='End':
			print 'Program Ended %i plants' % (number_of_plants)
			step = 0
			continue
		step = 2
#step 2 get Petiole diameter
	if step == 2:
		p1a = raw_input('Petiole Small Diameter 1 of 2:\n')
		if p1a=='end' or p1a=='END' or p1a=='End':
			print 'Recorded traits of %i plants' % (number_of_plants)
			step = 0
			continue
		if p1a[0]>0:
			step = 3
		else:
			print 'Measurement too samll! Please try again'
			continue
#step 3 get Petiole diameter
	if step == 3:
		p1b = raw_input('Petiole Large Diameter 2 of 2, 90 deg of Measure 1:\n')
		if p1b=='end' or p1b=='END' or p1b=='End':
			print 'Recorded traits of %i plants' % (number_of_plants)
			step = 0
			continue
		if p1b[0]>0:
			step = 4
		else:
			print 'Measurement too samll! Please try again'
			continue
#step 3 get Petiole length
	if step == 4:
		p2 = raw_input('Petiole Length:\n')
		if p2=='end' or plant=='END' or plant=='End':
			print 'Recorded traits of %i plants' % (number_of_plants)
			step = 0
			continue
		if p2[0]>0:
			step = 5
		else:
			print 'Measurement too small! Please try again'
			continue
#step 4 get leaf thickness measurement
	print 'Get 4 Leaf Thinkness Measurements'
	if step == 5:
		lfthk1 = raw_input('Leaf Thinkness Near Petiole:\n')
		if lfthk1=='end' or lfthk1=='END' or lfthk1=='End':
			print 'Recorded traits of %i plants' % (number_of_plants)
			step = 0
			continue
		if lfthk1[0]>0:
			step = 6
		else:
			print 'Measurement too small! Please try again'
			continue
#step 5 get Leaf Thinkness 2
	if step == 6:
		lfthk2 = raw_input('Get Leaf Thinkness Near Tip 1 of 2:\n')
		if lfthk2=='end' or lfthk2=='END' or lfthk2=='End':
			print 'Recorded traits of %i plants' % (number_of_plants)
			step = 0
			continue
		if lfthk2[0]>0:
			step = 7
		else:
			print 'Measurement too small! Please try again'
			continue
#step 6 get Leaf Thickness 3
	if step == 7:
		lfthk3 = raw_input('Get Leaf Thinkness Near Tip 2 of 2:\n')
		if lfthk3=='end' or lfthk3=='END' or lfthk3=='End':
			print 'Recorded traits of %i plants' % (number_of_plants)
			step = 0
			continue
		if lfthk3[0]>0:
			step = 8
		else:
			print 'Measurement too small! Please try again'
			continue
#step 7 get Leaf Thickness 4
	if step == 8:
		lfthk4 = raw_input('Get Leaf Thinkness Near Petiole:\n')
		if lfthk4=='end' or lfthk4=='END' or lfthk4=='End':
			print 'Recorded traits of %i plants' % (number_of_plants)
			step = 0
			continue
		if lfthk4[0]>0:
			step = 9
		else:
			print 'Measurement too small! Please try again'
			continue
	lst = [Decimal(lfthk1), Decimal(lfthk2), Decimal(lfthk3), Decimal(lfthk4)] 
	lfthk = round(Average(lst), 3)
	lstt = [Decimal(lfthk1), Decimal(lfthk4)]
	lstp = [Decimal(lfthk2), Decimal(lfthk3)]
	lfthkp = round(Average(lstp))
	lfthkt = round(Average(lstt))
#step 8 Perform Flatbed Scan
	if step == 9:
		waitlf = raw_input('Press Enter When Leaf is Ready to Flatbed Scan')
		if waitlf =='end' or waitlf=='END' or waitlf=='End':
			print 'Recorded traits of %i plants' % (number_of_plants)
			step = 0
		else:
			subprocess.call(['/Users/ju0/Downloads/scanline', '-flatbed', '-dir', os.getcwd(), '-name', 'leaves', '-jpeg', '-res', '600'])
			os.rename("leaves.jpg", plant+".jpg")
			step = 10
	if step == 10: #traits collected, write them out
		time=datetime.now() #format date as year:month:day:hour:min:sec
		f_time = str(time.year) + ':' + str(time.month) + ":" + str(time.day) + ":" + str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)
		print 'Plant barcodes scanned:\n'
		print '(time--plant_ID--PetioleDia--PetioleLen--SPAD--LeafThinkness)\n'

		number_of_plants = number_of_plants + 1 #add to plant count number
		#write out results, tab-delim to file YEAR_MONTH_DAY_fileUID_plant_heights.txt
		file = open('%i_%i_%i_%s_plant_traits.txt' % (time.year,time.month,time.day,filename),'a')
		file.write(str(f_time) + "\t" + str(plant) + "\t" + str(p1a) + "\t" + str(p1b) + "\t" + str(p2) + "\t" + str(lfthk) + str(lfthkp) + str(lfthkt) + "\t" "\n")
		file.close()
		#start again
		step = 1






##################################### Citation ###########################################
# 1. https://www.geeksforgeeks.org/find-average-list-python/


