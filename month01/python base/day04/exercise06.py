# 练习6：在控制台中录入学生成绩，计算最高分，最低分，
#   请输入学生总数：
#   请输入第1个学生成绩：
#   ...
score_list = list()
stu_count = int(input("Please input count:"))
for item in range(stu_count):
    score_list.append(int(input("Please input score of No.%d"%(item+1))))
max_score = max(score_list)
min_score = min(score_list)
total_score = sum(score_list)
print("max score is %d" % (max_score))
print("min score is %d" % (min_score))
print("total score is %d" % (total_score))