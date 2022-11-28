from stopwatch import Stopwatch
s = Stopwatch(3)
s.start()
with open("input.txt","r") as file:
  exp = [int(x) for x in file.readlines()]

found = False
for num in exp:
  for num2 in exp:
    if num == num2:
      break
    if num + num2 == 2020:
      print("Answer:", num * num2)
      found = True
  if found:
    break
s.stop()
print("Time taken:", s)