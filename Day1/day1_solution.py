count = 0
with open("input.txt","r") as file:
    measurements = file.readlines()
    measurements = [int(val) for val in measurements]
    previous_answer = 0
    for index in range(len(measurements)):
        if index>2:
            first_sum = measurements[index-3] + measurements[index-2] + measurements[index-1]
            second_sum = measurements[index-2] + measurements[index-1] + measurements[index]
            if second_sum > first_sum:
                count+=1
print(count)
