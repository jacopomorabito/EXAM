import numpy as np
import os
import json
import matplotlib.pyplot as plt

#question a

# upload data
path = os.path.join(os.getcwd(), 'MPHYG001_files', 'python_language_1', 
        'python_language_1_data.csv')
data = np.genfromtxt(path, delimiter=',', skip_header=1)

# creation of dictionary
f_data = {}
for line in data:
    key = str(int(line[0]))
    if key in f_data.keys():
        f_data[key].append(line[2])
    else:
        f_data[key] = [line[2]]

# upload data to disk in JSON format
json_data = json.dumps(f_data, indent=4)
with open ('python_language.json', 'w') as raw:
    raw.write(json_data)


#question b
def plotting(filename, year, colour=0):
    '''This function plot the data of rainfoall for a specific year.
    It is also ossible to specify a preferred colour for the graph
    '''
    # upload data
    with open(filename,'r')as jsn_data:
        data = json.load(jsn_data)
    
    year = str(year)
    if colour:
        plt.plot(data[year],colour)
    else:
        plt.plot(data[year])
    name = 'plot'+str(year)
    plt.savefig(name)
    plt.close()

# save file with rainfall data of 1988
plotting('python_language.json', 1988)


#question c

def plotting_mean(filename, start_period, end_period):
    ''' This function plot the average of rainfall for a specified period.
    '''

    # upload data
    with open(filename,'r') as jsn_data:
        data = json.load(jsn_data)
    
    # calculating the mean for each year in the period
    mean = [] 
    year = start_period
    while year <= end_period:
        year_str = str(year)
        mean.append(np.mean(data[year_str]))
        year += 1

    # plot and saving
    years = range(start_period,end_period+1)
    plt.plot(years, mean)
    name = 'plot'+str(start_period) +'-'+str(end_period)
    plt.savefig(name)
    plt.close()

plotting_mean('python_language.json', 1988, 2000)


#question d

def correction_factor(val):
    ''' 
    this function applies the correction factor to a single value
    '''

    val = val * 1.2 * np.sqrt(2)
    return val

def function_1(filename, year):
    ''' 
    This fucntion applies the corretion facto to all the value of a specified year
    '''

    # upload data
    with open(filename,'r')as jsn_data:
        data = json.load(jsn_data)

    year = str(year)
    new_value  = []
    for val in data[year]:
        new_value.append(correction_factor(val))
    
    return new_value
        
def function_2(filename, year):
    ''' 
    This fucntion applies the corretion facto to all the value of a specified year.
     In comparison with the function 1 this uses list comprehension which is a more
     elegant and readable way of completing this task. However when the 
     transformation of the data is more complex, or the data structure is more interwined 
     it is more advisable to use a for loop.
    '''
    # upload data
    with open(filename,'r')as jsn_data:
        data = json.load(jsn_data)

    year = str(year)
    new_value = [correction_factor(val) for val in data[year] ]

    return new_value
