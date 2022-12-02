from stopwatch import Stopwatch
W = Stopwatch(1)
W.start()
S = T = 0
SV = {"X": 1, "Y": 2, "Z": 3}
SD = {
  "A X": 3, "B X": 0, "C X": 6,
  "A Y": 6, "B Y": 3, "C Y": 0,
  "A Z": 0, "B Z": 6, "C Z": 3
  }
TV = {"X": 0, "Y":3, "Z": 6}
TD = {
  "A X": 3, "B X": 1, "C X": 2,
  "A Y": 1, "B Y": 2, "C Y": 3,
  "A Z": 2, "B Z": 3, "C Z": 1
  }
with open("input.txt", "r") as F:
  for L in F:
    S += SV[L[2]] + SD[L[:3]]
    T += TV[L[2]] + TD[L[:3]]
W.stop()
print("First Answer:", S)
print("Second Answer:", T)
print("Time taken:", W)
