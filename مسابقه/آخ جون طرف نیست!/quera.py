n1 = int(input())
days1 = input().split()

n2 = int(input())
days2 = input().split()

n3 = int(input())
days3 = input().split()

week = ["shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"]
 
for i in (days1 + days2 + days3):
    if i in week:
        week.remove(i)
        
print(len(week))