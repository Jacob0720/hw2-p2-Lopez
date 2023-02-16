inputFile = input()
inFile = open(inputFile)
id_dict = {}
class_roster = []
course_set = set()


def process_input_file(inFile):
    student_info = []

    for line in inFile:
        line.rstrip()
        line_list = line.split(',')
        student_info.append(line_list)
    return student_info


def create_id_dict(student_info):
    for student in student_info:
        id_dict[student_info[0]] = (student_info[2], float(student_info[3]))
    return id_dict


def create_class_roster(student_info, subject, course_number):
    for student in student_info:
        class_roster.append((student[0], student[4], student[5], float(student[6])))
    return class_roster


def create_course_set(student_info, subject):
    for student in student_info:
        course_set.add(student[1])
    return course_set


def output_sorted_students(student_info, id_dict):
    for student in student_info:
        student_id = student[0]
        student_name = student[4] + ' ' + student[5]
        major = id_dict[student_id][0]
        gpa = id_dict[student_id][1]
        print(f'{student_name} ({student_id}) - {major}, {gpa:.2f}')

    
