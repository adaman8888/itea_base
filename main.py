import university


def main():
    controller = university.Controller()
    database = controller.create_database_from_file('database.txt')
    controller.print_database(database)


if __name__ == "__main__":
    main()
