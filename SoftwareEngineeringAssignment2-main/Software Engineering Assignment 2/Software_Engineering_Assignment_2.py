import csv

# Format I used here (do feel free to tweak) ModuleName, ModID, Students[StudentIDs], ModuleGrades[ModGrades]
# Similarly as above students are in numerical order with their grades :
# eg. Visual Data has an ID of 10 and has registered:
ModuleList = []
  
#Student Data
StudentList = [] #An empty list for where all the students will be placed into.

#The student class, here is where a student object can be created apon making a new student they will be added to the list automatically.
class Student: 
    def __init__(self, name, studentID, modules, modgrades):
        #The individual attributes for the students: Name, Student ID, Modules attending and Modual grades
        self.name = name 
        self.studentID = studentID 
        self.modules = modules #modules can be done using a list
        self.modgrades = modgrades #modgrades should also be using a list in the same order as in modules for simplicity
        
        #Appends the newly created student into the "StudentList" list
        StudentList.append({'StudentName': name,  'studentID': studentID, 'registeredModulsID': modules, 'myGrades': modgrades})
        print(f"Student: {name} ID: {studentID} Added!")

#Module class for making a new Module.
class Module:
    def __init__(self, ModuleName, ModID, registeredStudentsID, moduleGrades):
        # The individual attributes for the module: Name, module ID, registered Student ID and module grades
        self.ModuleName = ModuleName
        self.ModID = ModID
        self.registeredStudentsID = registeredStudentsID
        self.moduleGrades = moduleGrades

        # Appends the newly created student into the "StudentList" list
        ModuleList.append({'ModuleName': ModuleName, 'ModID': ModID, 'registeredStudentsID': registeredStudentsID, 'moduleGrades': moduleGrades})
        print(f"Module: {ModuleName} ID: {ModID} Added!")

#Function for reading a CSV File to add the data    
def studentAddFromDatabase(fileName):
    
    with open(fileName) as csvFile:
        reader = csv.DictReader(csvFile) #This here will read the CSV File provided as a Dictonary
        
        for row in reader:
            #Due to how the CSV file is formatted the Registered Modules and student grades are in a single cell.
            #So to extract those numbers we need to use Split(", ") to pull each of the numbers out.
            SplitRegMod = row['Registered Modules'].split(", ")
            SplitStuGrade = row['Student Grades'].split(", ")
            
            #Here are all the storage variables for use in the Class at the End.
            fileStudName = row['Student Name'] #Extracts the Student name from the file.
            fileStudID = int(row['Student ID']) #Extracts the Student ID.
            RegModList = [] #An empty list to store the registered modules for the student.
            StuGradList = [] #An empty list to store the student's grades.
            
            for num in SplitRegMod:
                RegModList.append(int(num)) #this appends each of the extracted values into the temporary list and casts them to int.
                    
            for num in SplitStuGrade:
                StuGradList.append(int(num)) #Same as for SplitRegMod
            
            newStudent = Student(fileStudName, fileStudID, RegModList, StuGradList)
        print("=-=-=-=-=-=-=")
 
def moduleAddFromDatabase(fileName):
    #this function is functinally similar to what happens within studentAddFromDatabase but instead for modules
    with open(fileName) as csvFile:
        reader = csv.DictReader(csvFile)
        
        for row in reader:
            
            SplitRegStu = row['Registered Students'].split(", ")
            SplitModGrade = row['Module Grades'].split(", ")
            
            fileModName = row['Module Name']
            fileModID = int(row['Module ID'])
            RegStuList = []
            ModGradList = []
            
            for num in SplitRegStu:
                RegStuList.append(int(num))
                    
            for num in SplitModGrade:
                ModGradList.append(int(num))
            
            newModule = Module(fileModName, fileModID, RegStuList, ModGradList)
        print("=-=-=-=-=-=-=")

#Function that Takes Student ID As input, Prints all modules student is part of, and grades.
def module_finder():
    studId = input("\nModule Finder: Input student's ID (type 'exit' to exit): ") #This variable takes User input asking for the desired Student ID.
    GradeIter = 0 #This variable is for use in iterating through the Grades.
    
    if (studId != "exit"): #If you type "Exit" you will close the function.
        print("==========")
        for S in StudentList: #This loop cycles through the list of registered students.
            if (S['studentID'] != int(studId)): #If the Student ID Isn't the desired Student ID It will Skip this iteration.
                continue
            else: #If it is the desired ID then execute the following.
                #Print the student name.
                print(f"Student Name: {S['StudentName']}")
                
                #Getting the module Names and grades are alil more complex.
                for Stu, Mod in S.items(): #Loop through the dictonary of the Student's records to find their Modules.
                    if (Stu != 'registeredModulsID'): #If it isnt the Modules key. Skip.
                        continue
                    else: #If it is Modules
                        for modules in Mod: #Loop through the modules.
                            for M in ModuleList: 
                                if(M['ModID'] != modules): #If the Student isnt registered for this module ID then Skip.
                                    continue
                                else: #If the Module IS one the Student is registered.
                                    print(f"Module Name: {M['ModuleName']}") #Print module name.
                                    print(f"Module Grade: {S['myGrades'][GradeIter]}/100\n") #print Module Grade.
                                    GradeIter += 1
                                
                        break

                break
        # Calls itself in order for you to continue looking up students until you type "Exit"
        print("==========")
        module_finder()
    
#Function that finds students in a module
def student_finder():
    ModuleID = input("Student Finder: Input module ID (type 'exit' to exit) ")
    GradeIter = 0
    
    if (ModuleID != "exit"):
        print("==========")
        for M in ModuleList:
            if (M['ModID'] != int(ModuleID)):
                continue
            else:
                print(f"Module name: {M['ModuleName']} ")
                
                for Mod, Stu in M.items():
                    if (Mod != 'registeredStudentsID'):
                        continue
                    else:
                        for students in Stu:
                            for S in StudentList:
                                if (S['studentID'] != students):
                                    #print(f"Student: {S['StudentId']} : {students}")
                                    continue
                                else:
                                    print(f"Student Name: {S['StudentName']}") #Print module name.
                                    print(f"Student Grade: {M['moduleGrades'][GradeIter]}/100\n") #print Module Grade.
                                    GradeIter += 1   
        #Function calls itself to enable multiple searches (recursion)
        print("==========")
        student_finder()
    

#Function that prints Students andn their average grades.
def student_adverage():
    print("=-=-=-=-=")
    print("Student Averages: ")
    # Inital Loop to go though entrys
    for S in StudentList:
        for Stu, Key in S.items():
            if (Stu != 'myGrades'): #if the key isnt 'myGrades' skip the iteration.
                continue
            else:
                #We set it to 0 here so that each loop the variables reset for the next student.
                ScoreTotal = 0 #Container variable for addign the grades together.
                NoOfModules = 0 #container variable for counting the modules.
                
                for G in Key: 
                    #for each grade a Student has add it to ScoreTotal and increase the modules by one.
                    ScoreTotal += G
                    NoOfModules += 1
                
                # Print the adverage of each student, using round() to round them to 2 decimal palces.
                print(f"Student: {S['StudentName']}, Adv: {round(ScoreTotal/NoOfModules, 2)}")
    print("=-=-=-=-=")

#Function that Takes Modules and modules adverages.
def module_adverage():
    # Inital Loop to go though entrys
    print("=-=-=-=-=")
    print("Module Averages: ")
    for M in ModuleList:
        for Mod, Key in M.items():
            if (Mod != 'moduleGrades'): #if the key isnt 'myGrades' skip the iteration.
                continue
            else:
                #We set it to 0 here so that each loop the variables reset for the next student.
                ScoreTotal = 0 #Container variable for addign the grades together.
                NoOfModules = 0 #container variable for counting the modules.
                
                for G in Key: 
                    #for each grade a Student has add it to ScoreTotal and increase the modules by one.
                    ScoreTotal += G
                    NoOfModules += 1
                
                # Print the adverage of each student, using round() to round them to 2 decimal palces.
                print(f"Module: {M['ModuleName']},  Adv: {round(ScoreTotal/NoOfModules, 2)}")
    print("=-=-=-=-=")
     
# Initial Calling for adding the students to the database
# Students database
studentfile = 'List of Students.csv'
studentAddFromDatabase(studentfile)

# Module database
modulefile = 'List of Modules.csv'
moduleAddFromDatabase(modulefile)

# Initial execution of Module_Finder. (comment this out if you dont need it.)
module_finder()

# Initial execution of Student_adverage. (comment this out if you dont need it.)
student_adverage()

# Initial execution of Student_finder. (comment this out if you dont need it.)
student_finder()

# Execution of Module_adverage. (comment this out if you dont need it.)
module_adverage()

