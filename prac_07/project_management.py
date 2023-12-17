import datetime
from prac_07.project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
class_projects = []
project_dictionary = {}


def main():
    with open("projects.txt", "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()
        extract_data(data)
    choice = get_choice()
    while choice != "Q":
        if choice == "L":
            try:
                filename = input("Filename: ")
                input_file = open(f"{filename}.txt", "r")
                in_file = input_file.readlines()
                extract_data(in_file)
                input_file.close()
            except FileNotFoundError:
                print("Error no file of such name found")
        elif choice == "S":
            filename = input("Filename: ")
            output_file = open(f"{filename}.txt", "w")
            print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=output_file)
            for project in class_projects:
                print(
                    f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                    file=output_file)
            output_file.close()
        elif choice == "D":
            class_projects.sort()
            print("Incomplete Project: ")
            for project in class_projects:
                if not project.is_completed():
                    print(project)
            print("Completed Projects: ")
            for project in class_projects:
                if project.is_completed():
                    print(project)
        elif choice == "F":
            date_string = str(validate_date())
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            sorted_filtered_projects = []
            sort_project_by_date(date, sorted_filtered_projects)
            for project in sorted_filtered_projects:
                print(project)
            restore_datetime()
        elif choice == "A":
            print("Let's add a new project")
            name = input("Name: ")
            start_date = validate_date()
            priority = validate_priority("Priority: ")
            cost_estimate = validate_cost_estimate()
            completion_percentage = validate_percentage("Percent Complete: ")
            class_projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "U":
            for i, project in enumerate(class_projects, 0):
                print(
                    f"{i} {project.name}, start:{project.start_date}, priority {project.priority}, estimate: ${project.cost_estimate}, completion: {project.completion_percentage}% ")
                project_dictionary[i] = project
            project_choice = validate_project_choice()
            print(project_dictionary[project_choice])
            new_percentage = validate_percentage("New Percentage: ")
            new_priority = validate_priority("New Priority: ")
            update_project(new_percentage, new_priority, project_choice)
        else:
            print("Invalid Choice")
        choice = get_choice()
    autosave()
    print("Thank you for using custom-built project management software.")


def restore_datetime():
    for project in class_projects:
        project.start_date = project.start_date.strftime("%d/%m/%Y")


def update_project(new_percentage, new_priority, project_choice):
    class_projects[project_choice] = Project(class_projects[project_choice].name,
                                             class_projects[project_choice].start_date, int(new_priority),
                                             float(class_projects[project_choice].cost_estimate),
                                             int(new_percentage))


def sort_project_by_date(date, sorted_filtered_projects):
    filtered_projects = []
    filtered_dates = []
    final_sorted_filtered_dates = []
    filter_projects(date, filtered_projects)
    filter_dates(filtered_dates, filtered_projects)
    sorted_filtered_dates = [date for date in sorted(filtered_dates)]
    remove_duplicated_dates(final_sorted_filtered_dates, sorted_filtered_dates)
    for date in final_sorted_filtered_dates:
        for project in filtered_projects:
            if date == project.start_date:
                sorted_filtered_projects.append(project)


def remove_duplicated_dates(final_sorted_filtered_dates, sorted_filtered_dates):
    for date in sorted_filtered_dates:
        if date not in final_sorted_filtered_dates:
            final_sorted_filtered_dates.append(date)


def filter_dates(filtered_dates, filtered_projects):
    for project in filtered_projects:
        filtered_dates.append(project.start_date)


def filter_projects(date, filtered_projects):
    for project in class_projects:
        project.start_date = datetime.datetime.strptime(str(project.start_date), "%d/%m/%Y").date()
        if project.start_date > date:
            filtered_projects.append(project)


def validate_project_choice():
    try:
        project_choice = int(input("Project choice: "))
    except ValueError:
        print("Invalid Choice")
        project_choice = int(input("Project choice: "))
    while project_choice not in project_dictionary:
        print("Invalid Choice")
        project_choice = int(input("Project choice: "))
    return project_choice


def validate_date():
    data = input("Start date (dd/mm/yy): ")
    while len(data) < 8 or len(data) > 10 or data.count("/") != 2:
        print("Invalid input")
        data = input("Start date (dd/mm/yy): ")
    return data


def validate_cost_estimate():
    try:
        data = float(input("Cost estimate: $"))
    except ValueError:
        print("Invalid input")
        data = float(input("Cost estimate: $"))
    return data


def validate_priority(prompt):
    try:
        data = int(input(prompt))
    except ValueError:
        print("Invalid input")
        data = int(input(prompt))
    while data < 0 or data > 10:
        print("Invalid input")
        data = int(input(prompt))
    return data


def validate_percentage(prompt):
    try:
        data = int(input(prompt))
    except ValueError:
        print("Invalid input")
        data = int(input(prompt))
    while data < 0 or data > 100:
        print("Invalid input")
        data = int(input(prompt))
    return data


def autosave():
    output_file = open("projects.txt", "w")
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=output_file)
    for project in class_projects:
        print(
            f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
            file=output_file)
    output_file.close()


def get_choice():
    print(MENU, end="\n")
    choice = input(">>>").upper()
    return choice


def extract_data(data):
    projects = []
    for line in data[1:]:
        items = line.strip().split("\t")
        projects.append(items)
    for project in projects:
        class_projects.append(Project(project[0], project[1], int(project[2]), float(project[3]), int(project[4])))


main()