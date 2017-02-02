import csv

farmer_with_maxmass= None
farmer_with_minmass = None
max_biomass = None
min_biomass = None


file = open('data.csv', 'rb') 
next(file)

for line in file:
	line  = line.rstrip("\n")
	# farmers_name is value of interest
	# get the farmers_name by taking the index at 0
	# get the total_biomass column 
	farmers_name = (line.split(",")[0])
	total_biomass = float((line.split(","))[11])
	# print list((farmers_name, total_biomass))

	if farmer_with_maxmass is None and max_biomass is None:
		farmer_with_maxmass = farmers_name
		max_biomass = total_biomass

		# checks for the farmer with the maximum biomass
	else:
		if total_biomass > max_biomass:
			max_biomass = total_biomass
			farmer_with_maxmass = farmers_name 

		# checks for the farmer with the minimum biomass
		# returns name of farmern with the minimum biomass

	if farmer_with_minmass is None and min_biomass is None:
		farmer_with_minmass = farmers_name
		min_biomass = total_biomass
	
	else:
		if total_biomass < min_biomass:
			min_biomass  =  total_biomass
			farmer_with_minmass = farmers_name
 
file.close()
# farmer with the minimum biomass
print (farmer_with_minmass, min_biomass)
print (farmer_with_maxmass , max_biomass)