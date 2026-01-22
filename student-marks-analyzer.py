def marks_analyzer():
    print("="*30)
    print("STUDENT MARKS ANALYZER!")
    print("="*30)

    student_marks = {}
    
    nums_students = int(input("Please enter the number of students: "))
    
    for i in range(nums_students):
        print(f"---Student {i+1}")
        name = input("Please enter the name of the student: ")
        marks = float(input("Please enter marks: "))
        student_marks[name] = marks
        
    total = sum(student_marks.values())
    average = total/ len(student_marks)
    highest_score = max(student_marks.values())
    top_scorer = max(student_marks, key=lambda name: student_marks[name])
    
    print("=="*30)

    print("DETAILS OF ALL STUDENTS:")
    for name, marks in student_marks.items():
        print(f"    {name}: {marks}")
    print("=="*30)
    
    print("=="*30)
    
    print(f"Total Marks : {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {highest_score}")
    print(f"Top Scorer: {top_scorer} with {highest_score} marks.")
    print("=="*30)


if __name__ == "__main__":
    marks_analyzer()