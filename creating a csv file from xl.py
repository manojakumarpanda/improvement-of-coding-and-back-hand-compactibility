#programs for the file handling and creatin a csv file out of the msexcell office
import csv


with open('E:/csvfiles.csv',mode='w') as cf:
	header=['id','risk_factor','definition','Rare','Possible','Almost Certain']
	cs=csv.DictWriter(cf,fieldnames=header)
	cs.writeheader()

	for obj in dictanray:
		temp_dict={}
		for key,value in obj.items():
			temp_dict['key']=value
		cs.writerows(temp_dict)

