def cylinder_volume(height, radius):
    pi =3.14159
    return height*pi*radius

print(cylinder_volume(10,3))

#----------------------------------------------------------------
# Population Density Function
# Write a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values.
def population_density(population, land_area):
    return population/land_area



# readable_timedelta
'''Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. For example, calling the function and printing the result like this:'''
def readable_timedelta(days):
    weeks = days//7
    remainder = days % 7
    return f'{weeks} week(s) and {remainder} day(s).'
print(readable_timedelta(10))
print(readable_timedelta(7))
print(readable_timedelta(5))

#-----------------------------------------------------------
# Make a function that counts a word in a document
sentence = 'Lorem ipsum dolor sit amet, Lorem consectetur adip proident et partur Lorem Lorem Lorem'

def word_count(document, search_term):
    words=document.split()
    count = 0
    for word in words:
        if word == search_term:
            count +=1
    return count

print(word_count(sentence, 'Lorem')) # 5


#================================================================
# Lambda expressions

double = lambda x: x*2
print(double(23)) # 46

# Multiple arguments
multiply = lambda x,y:x*y
print(multiply(10,15)) # 150


# --------------------------------------------------------------

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)  # [57.0, 58.2, 50.6, 27.2]

# -----------------------------------------------------
# Filter
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)  # ['Chicago', 'Denver', 'Boston']


# -----------------------------------------------------

avgs = lambda numb_list: sum(numb_list) / len(numb_list)

lamb_averages = list(map(avgs, numbers))
print(lamb_averages)  # [57.0, 58.2, 50.6, 27.2]

# --------------------------------------------------
averagesLX = list(map(lambda x:sum(x) / len(x), numbers))
print(averagesLX) # [57.0, 58.2, 50.6, 27.2]

# --------------------------------------------------

short = lambda name: len(name) < 10

short_cities_lambda = list(filter(short, cities))
print(short_cities_lambda)  # ['Chicago', 'Denver', 'Boston']

# ---------------------------------------------------
short_citiesLX = list(filter(lambda x: len(x) < 10, cities))
print(short_citiesLX) # ['Chicago', 'Denver', 'Boston']




