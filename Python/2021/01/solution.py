count = 0
with open("input.txt","r") as file:
  measurements = file.readlines()
  measurements = [int(val) for val in measurements]
  for index in range(len(measurements)):
    if index>2:
      firstSum = measurements[index-3] + measurements[index-2] + measurements[index-1]
      secondSum = measurements[index-2] + measurements[index-1] + measurements[index]
      if secondSum > firstSum:
        count+=1
print(count)
