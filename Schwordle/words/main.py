answers = []
f = open("words.txt", "r", encoding="utf8")
for line in f:
  answers.append(line.rstrip("\n"))
print(answers)
f.close()
f = open("words.txt", "r")
of = open("a_list.txt", "w")
for each in answers:
  of.write("\"")
  of.write(each)
  of.write("\"")
  if each != answers[-1]:
    of.write(",")
    of.write(" ")
of.close()