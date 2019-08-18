import university


def main():
    controller = university.Controller()    # Create controller object
    database = controller.create_database_from_file('database.txt')     # Process the file and add data to database
    print('========================= University database =========================')
    controller.print_database(database)     # print the database
    sorted_database = controller.sort_by_faculty(database)  # sort the database by faculty
    print()
    print('================ University database sorted by faculty ================')
    controller.print_database(sorted_database)  # print the sorted database


if __name__ == "__main__":
    main()
