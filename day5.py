student_heights = [180, 124, 165, 173, 189, 169, 146]
# no_o = len(student_heights)
total_height = 0
cnt =0
for i in student_heights:
    total_height = total_height + i
    cnt = cnt + 1
avg_height = total_height/cnt
print(avg_height)

