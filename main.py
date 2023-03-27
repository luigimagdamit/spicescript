# line = ["munch", "[]", "like", "munch", "3", "eat_it_for_lunch", "munch", "56", "eat_it_for_lunch"]
file = open("test.mood","r+").read()
inp = "bruh [] like bruh baddie eat_it_for_lunch bruh baddie munch"
# line = ["test", "5", "6", "bite", "like", "test2", "BOYS_A_LIAR", "like", "test", "test2", "bite"]
line = file.split()
bools = ["FEELIN_HOT", "BOYS_A_LIAR", "DUHDUHDUH"]
stack = []
reserved = ["like", "grah", "fun"]
memory = {

}

for i in line:
    if i == "help":
        print("BASICS:\n`IceSpython uses postfix notation because she's in her mood`. \nFUNCTIONS: \n `grah` to print \n `like` for variable assignment \n `eat_it_for_lunch` to push to an array")
    if i in reserved and i == "like":
        a = stack.pop()
        b = stack.pop()
        if a == "[]":
            memory[b] = []
        else:
            memory[b] = a

    elif i == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(int(a) + int(b))
    elif i == "grah":
        print(stack.pop())
    elif i == "eat_it_for_lunch":
        a = stack.pop()
        b = stack.pop()
        memory[b].append(a)
        # memory[b].append(a)
    elif i == "munch":
        a = stack.pop()
        b = stack.pop()
        memory[b].remove(a)
    elif i == "bite":
        a = stack.pop()
        b = stack.pop()

        if a == b:
            print("FEELIN_HOT")
            stack.append("FEELIN_HOT")
        else:
            print("BOYS_A_LIAR")
            stack.append("BOYS_A_LIAR")
    elif i == "ice":
        print(memory)
        print(stack)
    elif i == "a":
        continue
    elif i == "he":
        continue
    elif i not in reserved:
        if i not in memory:
            if i == "\n":
                continue
            elif i.isdigit():
                stack.append(int(i))
            elif (i.isdigit() == False) and type(i) is str:
                stack.append(i)
            
        elif i in memory and isinstance(memory[i], list) == False:
            stack.append(memory[i])
        elif i in memory and isinstance(memory[i], list) == True:
            stack.append(i)

print(memory)