import university


def main():
    controller = university.Controller()
    database = controller.create_database_from_file('database.txt')
    print('========================= University database =========================')
    controller.print_database(database)
    sorted_database = controller.sort_by_faculty(database)
    print()
    print('================ University database sorted by faculty ================')
    controller.print_database(sorted_database)


if __name__ == "__main__":
    main()
