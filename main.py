import pygame
import pie_chart as pc

graph_type_options=["pie"]

print("\n--- Graph Studio ---\n")
print("Welcome to Graph Studio!")
print("Available Graph Type Options:\n")
for option in graph_type_options:
    print(option)
print("\nMake sure to use hex numbers for your colors when using CSV Files!")
graph_type=input("\nGraph Type: ")

while graph_type not in graph_type_options:
    graph_type=input("\nGraph Type: ")

if graph_type == "pie":
    output_surface=pc.create_pie_graph()

pygame.image.save(output_surface, "file.jpg")