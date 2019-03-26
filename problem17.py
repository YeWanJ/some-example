Sin = [0 ,3 ,3 ,5 ,4 ,4 ,3 ,5 ,5 ,4 ,3 ,6 ,6 ,8 ,8 ,7 ,7 ,9 ,8 ,8]
Ten = [0 ,3 ,6 ,6 ,5 ,5 ,5 ,7 ,6 ,6]
Hun = 7
Tho = 8

count = 0
for i in range(1, 1000):
    a = i % 10
    b = i % 100 // 10
    c = i // 100 
    if c != 0 :
        count += Hun + Sin[c]
        if a != 0 or b != 0 :
            count += 3
    if b == 0 or b == 1 :
        count += Sin[b * 10 + a]
    else :
        count += Sin[a] + Ten[b]
count += 3 + Tho

print(count)
    



