import csv 
from random import sample, shuffle, choice
from itertools import accumulate

numbers = [('one', 1), ('two',2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)] #list of pairs (number as text, number as symbol)
colors = [('orange', '#FF5F0F'), ('green', '#20C100'), ('blue', '#009BE8'), ('purple', '#C900F2')] #list of pairs (color as text, color as hex)

features = ['case', 'color', 'identity']

def permute_pairs(input_set):
    return [(i, j) for i in input_set for j in input_set if i != j]

n = 16 #number of experimental subjects to exhaust stimuli pool

#list of conditions (feature1 + feature2)
conditions = []
for i in range(n):
    batch = permute_pairs(features)*2
    shuffle(batch)
    conditions += batch
    
#generating a table 
with open('stimuli_pool.csv', 'w', newline='') as feature_table:
    writer = csv.DictWriter(feature_table, ['stimulus_id', 'text', 'identity', 'identity_wrong', 'color', 'color_wrong', 'color_hex', 'case', 'case_wrong', 'feature_1', 'feature_2'])
    writer.writeheader()
    for i, condition in enumerate(conditions):
        def case_randomize(text): 
            return eval(choice(['(text.upper(), "UPPERCASE", "lowercase")', '(text, "UPPERCASE", "lowercase")']))
        color, color_wrong = sample(colors, 2)
        number, number_wrong = sample(numbers, 2)
        text = case_randomize(number[0])
        writer.writerow({'stimulus_id': str(i).zfill(3), 
                         'text': text[0], 
                         'identity': number[1],
                         'identity_wrong': number_wrong[1],
                         'color': color[0],
                         'color_wrong': color_wrong[0], 
                         'color_hex': color[1], 
                         'case': text[1], 
                         'case_wrong': text[2],
                        'feature_1': condition[0],
                        'feature_2': condition[1]
                         }) 