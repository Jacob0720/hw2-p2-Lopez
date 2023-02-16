inputFile = input()
inFile = open(inputFile)
id_dict = {}


def process_input_file(inputFile):
    for line in inFile:
        line.rstrip()
        line_list = line.split()
        student_ID = line_list[0]
        student_name = line_list[1]
        student_major = line_list[2]
        student_courses = line_list[3]
        student_GPA = line_list[4]
    return line_list


def create_id_dict(line_list):
    id_dict[line_list[0]] = (line_list[2], line_list[4])
    return id_dict


print(id_dict)