class UniversityMember(object):
    """Main class for people in the university"""
    def __init__(self, first_name, last_name, birth_year, salary, faculty):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.salary = salary
        self.faculty = faculty


class Student(UniversityMember):
    """Class for the students of the university"""
    def __init__(self, first_name, last_name, birth_year, salary, faculty, course):
        UniversityMember.__init__(self, first_name, last_name, birth_year, salary, faculty)
        self.course = course


class Lecturer(UniversityMember):
    """Class for the lecturers of the university"""
    def __init__(self, first_name, last_name, birth_year, salary, faculty, experience):
        UniversityMember.__init__(self, first_name, last_name, birth_year, salary, faculty)
        self.experience = experience


class Controller(object):
    """Class that controls university members database"""
    # Function takes file as argument and reads it. Then splits each line by spaces and '=',
    # creates student or lecturer object for each line with values from this line,
    # and returns list of objects
    def create_database_from_file(self, database_file):
        with open(database_file) as file:
            database = []  # create list for members of university
            for line in file:  # read each line of file
                member = []  # create list for each member properties (name, faculty etc)
                temp_list = line.split()  # split each line by space and add to temporary list
                for element in temp_list:                  # split each element of temporary list by '='
                    member.append(element.split('=')[1])   # and add second part to member list
                if member[0] == 'Student':  # if member is student, create student object
                    student = Student(member[1], member[2], member[3], member[4], member[5], member[6])
                    database.append(student)    # add created student object to final list
                elif member[0] == 'Lecturer': # if member is lecturer, create lecturer object
                    lecturer = Lecturer(member[1], member[2], member[3], member[4], member[5], member[6])
                    database.append(lecturer) # add created lecturer object to final list
        return database

    # Function takes list of objects as argument and prints all properties of each object
    def print_database(self, database):
        for member in database: # for each member object in database list print common properties
            print('{}: {} {}, birth year: {}, salary: {} UAH, faculty: {}, '
                  .format(member.__class__.__name__, member.first_name, member.last_name,
                          member.birth_year, member.salary, member.faculty), end='')
            if member.__class__.__name__ == 'Student':      # for students print course
                print('course: {}'.format(member.course))
            elif member.__class__.__name__ == 'Lecturer':   # for lecturers print experience
                print('experience: {} years'.format(member.experience))

    # Function takes ist of objects as argument and sorts it by value of property 'faculty'
    def sort_by_faculty(self, database):
        # Create new list. For each member of database take value of 'faculty' and sort
        # database by this value
        sorted_database = sorted(database, key=lambda member: member.faculty)
        return sorted_database
