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
    def __init__(self, course):
        self.course = course


class Lecturer(UniversityMember):
    """Class for the lecturers of the university"""
    def __init__(self, experience):
        self.experience = experience


class Controller(object):
    """Class that controls university members database"""
    def print_database(self, database):
        print(database)

    def sort_by_faculty(self, database):
        return sorted(database)
