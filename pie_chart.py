import math
import pygame
import color_manager as cm
import csv_manager as csvm

class Pie():
    def __init__(self, center, radius):
        self._center=center
        self._radius=radius
        self._slice_colors=[]
        self._slice_names=[]
    
    def get_center_x(self):
        return self._center[0]
    
    def get_center_y(self):
        return self._center[1]

class Slice():
    def __init__(self, parent_pie, previous_angle, percentage):
        self._parent_pie=parent_pie
        self._percentage=percentage
        self._is_not_points=self.calc_is_not_points(previous_angle)[0]
        self._angle=self.calc_is_not_points(previous_angle)[1]
            
    def calc_is_not_points(self, previous_angle):
        angle=(self._percentage*360)/100

        center_points=(self._parent_pie.get_center_x(), self._parent_pie.get_center_y())

        points=[(center_points[0], center_points[1])]

        for num in range(int((360-previous_angle)-angle)):
            x = center_points[0]+int(self._parent_pie._radius*math.cos(num*math.pi/180))
            y = center_points[1]+int(self._parent_pie._radius*math.sin(num*math.pi/180))
            points.append((x, y))
        points.append((center_points[0], center_points[1]))
        
        return (points, angle+previous_angle)

def create_pie_graph():
    scale_factor=int(input("Input Scale Factor (whole numbers starting at 1): "))
    pie=Pie((125*scale_factor, 125*scale_factor), 75*scale_factor)
    input_type=input("Use csv file? (Y or N)")
    slices=[]
    surface=pygame.Surface((250*scale_factor, 250*scale_factor), pygame.SRCALPHA)
    if input_type == "Y":
        file_path=input("Input file path: ")
        csv_info=csvm.collect_csv_data(file_path)
        pie._slice_colors=csv_info[0]
        pie._slice_names=csv_info[1]
        for i in range(len(pie._slice_names)):
            if i == 0:
                slices.append(Slice(pie, 0, csv_info[2][i]))
            else:
                slices.append(Slice(pie, slices[-1]._angle, csv_info[2][i]))
    else:
        slice_count=int(input("How many Slices? (whole numbers staring at 1): "))

        for i in range(slice_count):
            print()
            color=cm.str_to_col(input("Input Color (r, g, b): "))
            name=input("Input Slice Name: ")

            is_percentage=input("Percentage or Fraction? (p or f): ")
            if is_percentage == "p":
                percentage=int(input("Input Percentage: "))
            elif is_percentage == "f":
                part=int(input("Input Part (top part of fraction): "))
                whole=int(input("Input Whole (bottom part of fraction): "))
                percentage=(part/whole*100)
            if i == 0:
                slices.append(Slice(pie, 0, percentage))
            else:
                slices.append(Slice(pie, slices[-1]._angle, percentage))
            pie._slice_colors.append(color)
            pie._slice_names.append(name)
    
    pygame.draw.circle(surface, pie._slice_colors[0], pie._center, pie._radius)
    for index, slice in enumerate(slices):
        if len(slice._is_not_points) > 2:
            pygame.draw.polygon(surface, pie._slice_colors[index+1], slice._is_not_points)
    
    return surface