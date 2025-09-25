import random
#Create a Function that generates a list of students with random names and writes them to grades.txt
#Use A Small Set of sample names and assign each a random grade between 1-100
#Over the file each time it's called

def save_grades(students,grades):
    
    with open('grades.txt','w') as file:
        for student, grade in zip(students,grades):
         file.write(f'{student},{grade}\n')



def load_grades():

    student_grades = {'Alice':100,'Bob':90,'Joe':60,'Dinnerbone':70}
    
    try:
        
        with open('grades.txt', 'r') as file: #opens it in read only
            
            for line in file:
                student, grade = line.strip().split(',')
        
    except FileNotFoundError:
        print('ERROR: No grades are found')
        
    return student,grade


def Initalize_grades():
    
    
        student_grades = load_grades()
        grades = [random.randint(1,100) for _ in students] #creates student variable based on names on list
        save_grades(students,grades)
        print('Grades Intialized')
   


    

#Create a function that reads grades.txt and displays all student names and grades in the console
#if the file doesnt exist or is empty, display a message indicating that no grades are found

def display_grades():

    students = load_grades()
    if not students:
        print('No grades found')
        return

    print('Current Grades')
    for student, grade in zip(students,grades):
        print(f'{student}:{grade}')
    
    
#Develop a function that allows user to add a new student and grade.
#Prompt user for students name and grade and append this info to grades.txt
def add_grade():

    new_student = input('Enter new student:')
    
    try:
        
        new_grade = int(input('Enter new grade:'))
        if 0 <= new_grade <= 100:
            with open('grades.txt', 'a') as file: 
                file.write(f'name: {new_student},{grade}\n')
                print('New Student and Grade added.')
        else:
            print('grade must be between 0 and 100')

            
    except ValueError:
        print('ERROR: Enter a positive number')
    except FileNotFoundError:
        print('ERROR: file does not exist')


#Write a function to update specific grade
#Read and store all the students and thier grades from grades.txt
#Sort the list of students alphabetically and display them as a numbered menu
#Allow the User to select a student by number and input a new grade
#Update the grade for the selected student in the oringal list and overwrite grades.txt with the updated list



def update_grade():

    students, grades = load_grades()
    if not students:
            print('No grades found to update')
            return
        
    print('\nSelect a student to update:')
       
    for index, (student,grade) in enumerate(students):
            print(f'{index}. {student}: {grade}')
        
        
    try:

            student_index = int(input('Enter the number of student you want to update:'))
            
            if 1 <= student_index < len(students): #if student_index is more than zero and less than the length of the list containing the students
                updated_grade = int(input(f'Enter new grade (0-100): '))
                if 1 <= updated_grade <= 100:
                    grades[choice - 1] = new_grade
                    
                    with open('grades.txt','w') as file:
                        for student, grade in zip(students,grades):
                           file.write(f'name: {student},{grade}\n')
            
                    print(f'Grade Updated for {students[choice - 1]}')

                else:
                    print('Grade must be 0 and 100')

            else:
                print('Invaild selection.')

    except ValueError:
        print('ERROR: Enter vaild number')


#Create a function to sort and display grades in descending order without modifiying the order in grades.txt
#read student names and grades into a list
#sort the list by grade in descending order
#Display sorted grades


def sort_grade():

        students, grades = load_grades()
        if not students:
            print('No grades to sort')
            return


        combined = list(zip(students, grades))
        students.sort(key = lambda x:x[1], reverse = True) #sorts grades by descending order
        
    
        print('\nGrades in descending order:')
        for student, grade in combined:
            print(f'{name} - Grade: {grade}')
 
     
    
        
        

#create a function that reads the grades from grades.txt identifies the highest and lowest grades and displays them
def high_low_grades():

    students, grades = load_grades()
    if not students:
            print('No grades to found')
            return

    
    max_grade = max(grades)
    min_grade = min(grades)

    max_students = students[grades.values(max_grade)]
    min_students = students[grades.values(min_grade)]

    print(f'Highest Grade:{max_student} with {max_grade}')
    print(f'Lowest Grade:{min_student} with {min_grade}')
      
    
def display_menu():
    
    while True:
        print("\nMenu:")
        print("1. Initalize grades")
        print("2. view grades")
        print("3. add grades")
        print("4. update grade")
        print("5. sort grades")
        print("6. highest/lowest grade")
        print("99.Exit")
        choice = input("Choose an option (1-6 or 99 to exit): ")
        if choice == "1":
           Initalize_grades()
        elif choice == '2':
           display_grades()
        elif choice == "3":
            add_grade()
        elif choice == "4":
            update_grade()
        elif choice == "5":
            sort_grade()
        elif choice == "6":
            high_low_grades()
        elif choice == "99":
            print('exiting..')
            break
        else:
            print('must pick a number between 1-6 or 99')

def main():

    display_menu()

main()
