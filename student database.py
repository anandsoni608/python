n=int(input("Enter number of student:-"))
i=0
students={}

for i in range(1,n+1):
    print("Student"+" ",i)
    students[i]={"Name":input("Enter name:-"),"Roll no.":int(input("Enter roll no.:-")),"Sub1":int(input("Enter marks of sub1:-")),"Sub2":int(input("Enter marks of sub2:-")),"Sub3":int(input("Enter marks of sub3:-"))}
    students[i]['Totalmarks']=students[i].get("Sub1")+students[i].get("Sub2")+students[i].get("Sub3")
    students[i]['Average']=students[i].get("Totalmakrs")/3

print("The database is:-",students)

check=int(input("Enter roll no. to check details:-"))

i=0
for i in range(1,n+1):
    if check==students.get("Roll no."):
        print("Student detail is:-",students[i])
        break;

print("Do you want to update any data")
print("1.Yes \n 2.No")
ch=int(input("Enter your choice:-"))

if ch==1:
    up=int(input("Enter roll no. of student:-"))
    j=int(input("Which data you want to update:- "))
    print("1.Name")
    print("2.Roll no.")
    print("3.Sub1")
    print("4.Sub2")
    print("5.Sub3")

    if j==1:
        print("Enter updated name:-")
        students[up].get("Name")=input()
    elif j==2:
        print("Enter updated Roll no.:-")
        students[up].get("Roll no.")=int(input())
    elif j==3:
        print("Enter updated marks of Sub1:-")
        students[up].get("Sub1")=int(input())
    elif j==4:
        print("Enter updated marks of Sub2:-")
        students[up].get("Sub2")=int(input())
    elif j==5:
        print("Enter updated marks of Sub3:-")
        students[up].get("Roll no.")=int(input())

#r=int(input("checking 1st rank :-"))

        

    
