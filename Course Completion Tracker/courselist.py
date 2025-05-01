# Course Completion Tracker

courselist = [] #Global variable to store the list of completed courses

def main():
    while True:
        print("Welcome to the Course Completion Tracker!")
        print("1. Add a course")
        print("2. Remove a course")
        print("3. View completed courses")
        print("4. Exit")
        
        choice = input("Please enter your choice (1-4): ")
        
        if choice == '1':
            add_course()
        elif choice == '2':
            remove_courses()
        elif choice == '3':
            view_courses()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    
def add_course():
    course_name = input("Enter the name of the course you completed: ")
    courselist.append(course_name) #Add the course to the list
    print(f"Course '{course_name}' added to the list.")

def remove_courses():
    if not courselist: #Check if the list is empty
        print("No courses to remove.")
        return
    
    print("Completed Courses:")
    for i, course in enumerate(courselist, start=1):
        print(f"{i}. {course}") #Print each course with its index
    
    try:
        index = int(input("Enter the number of the course you want to remove: ")) - 1
        if 0 <= index < len(courselist):
            removed_course = courselist.pop(index) #Remove the course from the list
            print(f"Course '{removed_course}' removed from the list.")
        else:
            print("Invalid number. Please try again.")
    except ValueError:
        print("Please enter a valid integer.")

def view_courses():
    if not courselist: #Check if the list is empty
        print("No courses completed yet.")
    else:
        print("Completed Courses:")
        for course in courselist:
            print(f"- {course}") #Print each course in the list

if __name__ == "__main__":
    main() #Call the main function to start the program