class student:

  def__init__(self,name,roll_number,cgpa):
  self.name=Name
  self.roll_number=roll_number
  self.cgpa=cgpa

def sort_students(student_list):
  #sort the list of students in descending order of CGPA
  sorted_students=sorted(students_list,key=lambda student.student.cgpa,reverse=true)
 # Syntax - lambda arg:exp
  return sorted_students

#example usage:
students=[
  student("hari","A123",7.8),
  student("srikanth","A124",8.9),
  student("saumya","A125",9.1),
  student("mahidhar","A126",9.9),
]

sorted_students=sort_students(students)

#print the sorted list of students
for student in sorted_students:
  print("name:{},roll number:{},CGPA:{}".format(student.name,student.roll_number,student.cgpa))