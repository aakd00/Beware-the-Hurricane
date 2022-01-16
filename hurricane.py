import collections 

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane

areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 
['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], 
['The Bahamas', 'Northeastern United States'], 
['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 
['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], 
['Jamaica', 'Yucatn Peninsula'], 
['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 
['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], 
['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], 
['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], 
['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], 
['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], 
['Mexico'], 
['The Caribbean', 'United States East coast'], 
['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 
['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], 
['The Caribbean', 'United States East Coast'], 
['The Bahamas', 'Florida', 'United States Gulf Coast'], 
['Central America', 'Yucatn Peninsula', 'South Florida'], 
['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], 
['The Caribbean', 'Venezuela', 'United States Gulf Coast'], 
['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], 
['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], 
['Greater Antilles', 'Central America', 'Florida'], 
['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], 
['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], 
['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], 
['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 
['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]



# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# 2 
# Create a Table
def hurricane_damages(damage_list):

    conversion = {"M": 1000000, "B": 1000000000} 
    converted_list = []

    for item in damage_list:
        
        if "M" in item:  
            mill = item.strip("M")
            num = float(mill) * conversion["M"]
            converted_list.append(num)                
        
        elif "B" in item:
            bill = item.strip("B")
            numb = float(bill) * conversion["B"]
            converted_list.append(numb)     

        else:
            converted_list.append(item) #missing data 
    
    return converted_list

print(hurricane_damages(damages))

# Create and view the hurricanes dictionary
def hurricane_details(name, month, year, max_wind, area_affected, damage, death):

    updated_damages = hurricane_damages(damages)
    hurricanes = {}
    for index in range(len(names)):

        hurr = {"Name": names[index], "Month": months[index], "Year": years[index], "Max Sustained Winds": max_sustained_winds[index], "Areas Affected":
        areas_affected[index], "Damages": updated_damages[index], "Deaths": deaths[index]}

        hurricanes[names[index]] = hurr

    return hurricanes

print(hurricane_details(names,months,years, max_sustained_winds, areas_affected, damages, deaths))
print("\n")
def hurricanes_by_years():

    hurricanes_by_name = hurricane_details(names,months,years, max_sustained_winds, areas_affected, damages, deaths)

    hurricane_by_year = collections.defaultdict(list)

    for key, value in hurricanes_by_name.items():

        current_year = hurricanes_by_name[key]["Year"]
        current_cane = hurricanes_by_name[key]
        
        hurricane_by_year[current_year].append(current_cane)   

    return hurricane_by_year

print(hurricanes_by_years())


def frequency_areas_affected():

    hurricanes_by_name = hurricane_details(names,months,years, max_sustained_winds, areas_affected, damages, deaths)
    
    freq_area_affected = collections.defaultdict(int) #setting defaultdict to int makes it useful for counting
    
    for key,value in hurricanes_by_name.items():
        
        getting_areas = hurricanes_by_name[key]["Areas Affected"]

        for area in getting_areas:
            freq_area_affected[area] +=1 #each time an area(the key) is hit by a hurricane the value adds 1
                  
    return freq_area_affected



print(frequency_areas_affected())

def most_affected_area():

    all_areas_affected = frequency_areas_affected() 

    for area in all_areas_affected:
        
        if all_areas_affected[area] == max(all_areas_affected.values()):
            return "The area affected by the most hurricanes is " + area + " with a hit frequency of " + str(max(all_areas_affected.values()))

        else:
            continue    
         

print(most_affected_area())
print("\n")
def greatest_num_of_deaths():

    hurricanes_by_name = hurricane_details(names,months,years, max_sustained_winds, areas_affected, damages, deaths)
    

    for key, value in hurricanes_by_name.items():

        if hurricanes_by_name[key]["Deaths"] == max(deaths):
            return "Greatest number of deaths were " + str(max(deaths)) + " caused by Hurricane " + hurricanes_by_name[key]["Name"] + " in year " + str(hurricanes_by_name[key]["Year"])

        else:
            continue


print(greatest_num_of_deaths())

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}



def hurricane_on_mortality_scale():

    hurricanes_by_name = hurricane_details(names,months,years, max_sustained_winds, areas_affected, damages, deaths)

    hurricane_mortality_scale = {0: [], 1:[], 2:[], 3:[], 4:[],5:[]}

    for key, value in hurricanes_by_name.items():

        hurricane_deaths = hurricanes_by_name[key]["Deaths"]
        hurricanes_dictionary = hurricanes_by_name[key]

        if  hurricane_deaths <= 100:
            hurricane_mortality_scale[1].append(hurricanes_dictionary)

        elif 100 < hurricane_deaths <= 500:
            hurricane_mortality_scale[2].append(hurricanes_dictionary)

        elif 500 < hurricane_deaths <= 1000:
            hurricane_mortality_scale[3].append(hurricanes_dictionary)

        elif 1000 < hurricane_deaths <= 10000:
            hurricane_mortality_scale[4].append(hurricanes_dictionary)

        elif hurricane_deaths > 10000:
            hurricane_mortality_scale[5].append(hurricanes_dictionary)

    
    return hurricane_mortality_scale


print()
print(hurricane_on_mortality_scale())


def greatest_damage_by_hurricane():

    hurricanes_by_name = hurricane_details(names,months,years, max_sustained_winds, areas_affected, damages, deaths)
    max_damage = 0

    for key, value in hurricanes_by_name.items():

        if hurricanes_by_name[key]["Damages"] == "Damages not recorded":
            continue

        elif hurricanes_by_name[key]["Damages"] > max_damage:
            max_damage = hurricanes_by_name[key]["Damages"]
            hurricane_responsible = hurricanes_by_name[key]["Name"]
        
    return "Maximum damage was $" + str(max_damage) + " caused by Hurricane " + hurricane_responsible

print()
print(greatest_damage_by_hurricane())

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}


def hurricane_on_damage_scale():

    hurricanes_by_name = hurricane_details(names,months,years, max_sustained_winds, areas_affected, damages, deaths)

    hurricane_damage_scale = {"Not Recorded": [], 1:[], 2:[], 3:[], 4:[], 5:[]}

    for key, value in hurricanes_by_name.items():

        hurricane_damages = hurricanes_by_name[key]["Damages"]
        hurricanes_dictionary = hurricanes_by_name[key]

        if  hurricane_damages == "Damages not recorded":
            hurricane_damage_scale["Not Recorded"].append(hurricanes_dictionary)

        elif 100 < hurricane_damages <= 100000000:
            hurricane_damage_scale[1].append(hurricanes_dictionary)

        elif 100000000 < hurricane_damages <= 1000000000:
            hurricane_damage_scale[2].append(hurricanes_dictionary)

        elif 1000000000 < hurricane_damages <= 10000000000:
            hurricane_damage_scale[3].append(hurricanes_dictionary)

        elif 10000000000 < hurricane_damages <= 50000000000:
            hurricane_damage_scale[4].append(hurricanes_dictionary)

        elif hurricane_damages > 50000000000:
            hurricane_damage_scale[5].append(hurricanes_dictionary)


    
    return hurricane_damage_scale

print()
print(hurricane_on_damage_scale())
