import csv
import pygame

def do_string_division(string):
    for index, char in enumerate(string):
        if char == '/':
            division_index=index
    base=int(string[:division_index])
    whole=int(string[division_index+1:])
    return (base/whole*100)


def collect_csv_data(file_path):
    colors=[]
    names=[]
    percentages=[]
    with open(file_path) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            colors.append(pygame.Color(row[0]))
            names.append(row[1])
            if '%' in row[2]:
                percentages.append(int(row[2][:len(row[2])-1]))
            else:
                percentages.append(do_string_division(row[2]))
    print(colors)
    print(names)
    print(percentages)
    return colors, names, percentages