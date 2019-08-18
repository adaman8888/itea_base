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
    def create_database_from_file(self, database_file):
        with open(database_file) as file:
            members = []  # list for members of university
            for line in file:  # read each line
                member = []  # list for each member
                member_list = line.split()  # split each line by space and add to temporary list
                for element in member_list:
                    member.append(element.split('=')[1])  # split each element of temporary list by '=' and add second part to member list
                members.append(member)  # add member list to list of members
        database = []
        for member in members:
            if member[0] == 'Student':
                student = Student(member[1], member[2], member[3], member[4], member[5], member[6])
                database.append(student)
            elif member[0] == 'Lecturer':
                lecturer = Lecturer(member[1], member[2], member[3], member[4], member[5], member[6])
                database.append(lecturer)
        return database

    def print_database(self, database):
        for member in database:
            print('{}: {} {}, birth year: {}, salary: {} UAH, faculty: {}, '
                  .format(member.__class__.__name__, member.first_name, member.last_name,
                          member.birth_year, member.salary, member.faculty), end='')
            if member.__class__.__name__ == 'Student':
                print('course: {}'.format(member.course))
            elif member.__class__.__name__ == 'Lecturer':
                print('experience: {} years'.format(member.experience))

    def sort_by_faculty(self, database):
        sorted_database = sorted(database, key=lambda member: member.faculty)
        return sorted_database
