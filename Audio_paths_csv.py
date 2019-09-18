import os
import csv
path='F:\\Respiratory_Sound_Database'
files=[]
for r,d,f in os.walk(path):
	for file in f:
		if '.wav' in file:
			files.append(os.path.join(r,file))
with open('F://audio_paths.csv','w') as myfile:
	wr=csv.writer(myfile,quoting=csv.QUOTE_ALL)
	wr.writerow(files)
