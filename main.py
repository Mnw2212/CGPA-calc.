# CGPA calculator.
# parameters. credits vs grade
#database


# Grade to score convesion

S,A,B,C,D,E,F=10,9,8,7,6,5,4

#check for previous CGPA

print 'enter the previous gpa and credits taken'

gpa=input()
cre=input()

#facility to enter subject vs grade


avg=0
grade=[]
subject=[]
print 'enter the number of subjects'
sub=input()

print ' input the subject <enter> grade '

for i in range(sub):
    x=raw_input()
    subject.append(x)
    y=input()
    grade.append(y)

print grade
print subject

p=cre*gpa

avg=(sum(grade)+p)/(len(subject)+cre)

print avg
