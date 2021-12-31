import shutil
#################### FINDING MODE ####################
#controller code for finding the max/spike/mode   
def process_spike(lines_in_file):
    max_line_index, max_height = find_spike(lines_in_file)
    coordinates = find_coordinates(lines_in_file[max_line_index])
    return coordinates, max_height

#code to find index of line corresponding to the bar with highest frequency
#this bar is the bar with the greatest height
def find_spike(lines_in_file):
    max_line_index = 0
    max_height = 0
    for i, line in enumerate(lines_in_file):
        if "g-rect-container" in line and "height" in lines_in_file[i+1]: #only focus on those lines that define rectangles
            dimensions = lines_in_file[i+1].split() #return a list of dimensions: height, width
            height_specifications = dimensions[2] 
            height = float(height_specifications[8:-1])
            if height > max_height:
                max_height = height
                max_line_index = i
    return max_line_index, max_height 

#utility function for process_spike
#This gets the x-coordinate of the tallest bar
def find_coordinates(line):
    split_line = line.split("translate")
    extracted_coordinates = split_line[1]
    extracted_coordinates = extracted_coordinates[:-3]
    return extracted_coordinates

#Function to get the coordinates of the highlighting circle
def circle_details(coordinates,max_height):
    width,starting_coord,gap = bar_details()
    circle_radius = ((width + gap) * 3 + gap)/2.0
    x_coord = float(coordinates[1:-3]) + circle_radius - gap
    y_coord = max_height
    circle = "" + str(x_coord) + "," + str(y_coord) + "," + str(circle_radius) +"\n"
    return circle

#################### FINDING MORE/LESS THAN ####################
#controller code for finding more than
def process_more(number):
    coordinate_string = "(" + str(find_bar_coord(number)) + ", 0)"
    return coordinate_string

#controller code for finding less than
def process_less(number):
    starting_coord = 1.742808798646362
    start_coord = "(" + str(starting_coord) + ", 0)"
    end_coord = "(" + str(find_bar_coord(number)) + ", 0)"
    return start_coord,end_coord

#utility functions for process_more and process_less
def find_bar_coord(number):
    number = number / 50 - 1
    width,starting_coord,gap = bar_details()
    coordinate = float(number) * (width + gap) + starting_coord 
    return coordinate

def rectangle_details(front_coord, end_coord):
    width = end_coord - front_coord
    height = 486
    rectangle = "" + str(width) + "," + str(height) + "," + str(front_coord) + "," + str(height) + "\n"
    return rectangle

#################### OTHER UTILITY FUNCTIONS ####################
#utility function to find the number being referenced
def find_impt_number(phrase):
    valid_number = False
    wordList = phrase.split()
    wordList_length = len(wordList)
    number = 0

    if "calories" in wordList:
        for i in range(wordList_length):
            if wordList[i] == "calories":
                number = int(wordList[i-1])
                valid_number = True
    else:
        string_num = ""
        for i in range(wordList_length):
            if wordList[i].isdigit():
                string_num = string_num + wordList[i]
        
        if string_num != "":
            number = int(string_num)
            valid_number = True
                
    return number, valid_number

#utility function to return bar details
def bar_details():
    width = 15.685279187817258 
    starting_coord = 1.742808798646362
    gap = 19.17089678510998  - width - starting_coord
    return width,starting_coord,gap

#utility function to write the coordinates to coordinates.txt
def write_to_coord_file(string_towrite):
    coordinate_file = open("visualization/coordinates.txt", "a")
    coordinate_file.write(string_towrite)
    coordinate_file.close()
    print("Written to file: " + string_towrite)
    return

def main():
    #Read the SRT file 
    srtFile = open('prototype/output.txt')
    phrases_in_file = srtFile.readlines()
    
    # #take in a string, convert to lowercase
    # phrase = str(input("Input a phrase: "))
    # phrase = phrase.lower()
    # number = 0

    #open the SVG file and read it line by line
    svgFile = open('system/testchipotle.svg')
    lines_in_file = svgFile.readlines()

    for phrase in phrases_in_file:
        #for testing & file-writing purposes
        string_towrite = ""
        coordinates = ""

        is_valid_number = False;

        #case 1: Finding the peak of the graph
        if (("spike" in phrase) or ("max" in phrase) or ("mode" in phrase)):
            number, is_valid_number = find_impt_number(phrase)
            if is_valid_number:
                coordinates,max_height = process_spike(lines_in_file)
                circle_coordinates = circle_details(coordinates, max_height)
                #writing to txt file
                # string_towrite = "Spike at " + str(number) +": Coordinates are " + coordinates + "\n"
                string_towrite = phrase 
                string_towrite = string_towrite + "circle: " + circle_coordinates
                write_to_coord_file(string_towrite)
            
        #Case 2: More than 
        elif "more" in phrase:
            number, is_valid_number = find_impt_number(phrase)
            end_coord = "(1033, 0)"
            if (is_valid_number):
                coordinates = process_more(number)
                rectangle_coordinates = rectangle_details(float(coordinates[1:-4]), float(end_coord[1:-4]))
                #writing to txt file
                # string_towrite = "More than " + str(number) +": Coordinates are " + coordinates + "\n"
                string_towrite = phrase 
                string_towrite = string_towrite + "rectangle: " + rectangle_coordinates
                write_to_coord_file(string_towrite)

        #Case 3: less than
        elif "fewer" in phrase:
            number, is_valid_number  = find_impt_number(phrase)
            if (is_valid_number):
                start_coord, end_coord = process_less(number)
                rectangle_coordinates = rectangle_details(float(start_coord[1:-4]), float(end_coord[1:-4]))
                # string_towrite = "Less than " + str(number) + ": Coordinates are " + start_coord + " to " + end_coord + "\n"
                string_towrite = phrase
                string_towrite = string_towrite  + "rectangle: " + rectangle_coordinates
                write_to_coord_file(string_towrite)

    shutil.copy('prototype/output.srt', 'visualization')
        #code to end the program
        # if phrase == "end":
        #     print("Bye bye!\n")
        #     svgFile.close()
        # else:
        #     if not is_valid_number:
        #         print("Invalid number!\n")

            # main()

main()