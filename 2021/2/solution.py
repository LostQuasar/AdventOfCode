with open("input.txt","r") as file:
    depth=0
    horizontal=0
    depth2=0
    horizontal2=0
    aim2=0
    for line in file.readlines():
        if line[0] == "u":
            depth-=int(line[-2:-1])
            aim2-=int(line[-2:-1])
        if line[0] == "d":
            depth+=int(line[-2:-1])
            aim2+=int(line[-2:-1])
        if line[0] == "f":
            horizontal+=int(line[-2:-1])
            horizontal2+=int(line[-2:-1])
            depth2+=int(line[-2:-1])*aim2
    print("Part 1 Solution: "+str(depth*horizontal))
    print("Part 2 Solution: "+str(depth2*horizontal2))
