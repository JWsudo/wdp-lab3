counter = 0
last_number = 2

while counter<10:
    is_prime = True
    for i in range(2, int(last_number ** 0.5) +1):
        if (last_number % i ==0):
            is_prime = False
            break
    if (is_prime):
        print(last_number, end="")
        if(counter <9):
            print(",", end="")
        counter +=1
    last_number +=1

