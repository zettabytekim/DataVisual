import pygal
from die import Die

die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequncies = []
for value  in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequncies.append(frequency)
    
hist = pygal.Bar()
hist.title = "Result of rollong one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequncies)
hist.render_to_file('./DataVisual/01/die_visual.svg')