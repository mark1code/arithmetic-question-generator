import random

def getSmaller(num):
    y = 9999
    while num < y:
        y = random.randint(100, 1000)
    return y

while True:
    try:
        num_q = int(input("\nEnter number of questions:\n\n"))
        break
    except ValueError:
        print("\nnot a good number\n")


op = []
valid_op = {"+","-","x","/"}
while not op:
    op_input = input("\nEnter which types of questions you want: + - x /\n\n")
    for char in op_input:
        if char in valid_op:
            op.append(char)
             
print(f"\nGenerating {num_q} questions with {" ".join(list(set(op)))} sign...\n")

for i in range(num_q):
    sign = random.choice(op)
    if sign == "+":
        print(f"{random.randint(100,2000)} {sign} {random.randint(100,1000)} = ")
    elif sign == "-":
        x = random.randint(100,2000)
        print(f"{x} {sign} {getSmaller(x)} =")
    elif sign == "x":
        print(f"{random.randint(10, 99)} {sign} {random.randint(10,100)} = ")
    else:
        divisor = random.randint(3,12)
        quotient = random.randint(13,999)
        dividend = divisor * quotient
        print(f"{dividend} {sign} {divisor} = ")
