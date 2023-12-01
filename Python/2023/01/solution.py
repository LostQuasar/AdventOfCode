import re
def calibrationSum(file):
  wordnum = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
  p1values = []
  p2values = []
  for line in file:
    p1matches = re.findall(r"(?=("+'|'.join(list(wordnum.values()))+r"))", line)
    p2matches = re.findall(r"(?=("+'|'.join(list(wordnum.values()) + list(wordnum.keys()))+r"))", line)

    for index in [0,-1]: 
      if p2matches[index] in wordnum:
       p2matches[index] = wordnum[p2matches[index]]

    if p1matches != []:
      p1values.append(int(p1matches[0]+p1matches[-1]))
    p2values.append(int(p2matches[0]+p2matches[-1]))
  return sum(p1values), sum(p2values)

with open("test_p1.txt","r") as file:
  ans = calibrationSum(file)
  part1Test = [ans[0], 142]
  if part1Test[0] != part1Test[1]:
    print("Part test 1 should be", part1Test[1], "is", part1Test[0])

with open("test_p2.txt","r") as file:
  ans = calibrationSum(file)
  part2Test = [ans[1], 281]
  if part2Test[0] != part2Test[1]:
    print("Part test 2 should be", part2Test[1], "is", part2Test[0])

with open("input.txt","r") as file:
  ans = calibrationSum(file)
  print("Part 1 Answer:", ans[0])  
  print("Part 2 Answer:", ans[1])
