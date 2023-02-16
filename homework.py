def narcissistic( value ):
    total = 0
    for num in str(value):
        total += int(num)**len(str(value))
    return total == value
    
print(narcissistic(371))

def solution(number):
    count = 0
    sum = 0
    while count < number:
        if count % 3 == 0 and count% 5 == 0:
            sum += count

        elif count % 3 == 0:
            sum += count

        elif count % 5 == 0:
            sum += count
        count += 1
    return sum

print(solution(15))

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    my_list = []
    while a <= b:
        i=0
        digit_list = []
        for num in str(a):
            digit_list.append(num)
        total = 0
        for i in range(len(digit_list)):
            total += int(digit_list[i])**(i+1)
            i+=1
        if total == int(a):
            my_list.append(total)
        a += 1
    return my_list

print(sum_dig_pow(1,100))
