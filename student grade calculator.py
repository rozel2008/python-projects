name = input("ENTER STUDENT NAME")
marks = int(input("ENTER MARKS OUT OF 100"))
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
      grade = "D"
else:
    grade = "F(Fail)"

print("\n---- Result ----")
print("name:", name)
print("marks:", marks)
print("grade:", grade)
