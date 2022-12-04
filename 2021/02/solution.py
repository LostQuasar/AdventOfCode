with open("input.txt","r") as file:
  depth=0
  horizontal=0
  depth2=0
  horizontal2=0
  aim=0
  for line in file.readlines():
    match line[0]:
      case "u":
        depth-=int(line[-2:-1])
        aim-=int(line[-2:-1])
      case "d":
        depth+=int(line[-2:-1])
        aim+=int(line[-2:-1])
      case "f":
        horizontal+=int(line[-2:-1])
        horizontal2+=int(line[-2:-1])
        depth2+=int(line[-2:-1])*aim
  print("Part 1 Solution:", depth*horizontal)
  print("Part 2 Solution:", depth2*horizontal2)
