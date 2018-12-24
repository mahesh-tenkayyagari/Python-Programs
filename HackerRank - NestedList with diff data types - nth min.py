"""
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format
The first line contains an integer, N , the number of students. 
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

Constraints
2<=N<=5
There will always be one or more students having the second lowest grade.
"""



def myFunc(elem):
    return elem[1]

def nthmax(arr,n):
    i=0    
    while i<n:
        x=p.index(min(arr,key=myFunc))
        #print(x)
        arr=arr[0:x]
        #print(arr)
        i=i+1
        #print("iteration"+str(i) +"completed")
    return arr


if __name__ == '__main__':
    p=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l=[name,score]
        p.append(l)
    n=1
    p.sort(reverse=True,key=myFunc)
    p=nthmax(p,n)
    x=p.index(min(p,key=myFunc))
    nthmax_names=list()
    for i in range(x,len(p)):
        y=len(p[i])
        #print(y)
        for j in range(0,1):
            nthmax_names.append(p[i][j])
    nthmax_names.sort()
    for i in range(len(nthmax_names)):
        print(nthmax_names[i])
    


