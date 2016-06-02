# Code For America Challenge
# Joel Shooster
# This program will calculate the number of violations in each category.
# It will include the earliest and latest violation date for each category.

def build_violation_data(fileName):
  violation_data = {}
  try:
    violations = open(fileName, "r")
    for line in violations:
      line = line.strip("\n")
      line = line.split(",")
      case = line[0]
      violation_data[case] = line[1:]
    violations.close()
    return violation_data
  except (IOError, ValueError):
    print "File not found"
violation_book = build_violation_data("Violations-2012.csv")

types= {}
dates= []
#Finding the most common violation type
for x in violation_book.values():
  category = x[1]
  date = x[2]
  if category not in types:
    types[category] = 1
    dates.append(date)
  else:
    types[category] += 1
    dates.append(date)

maximum = max(types, key=types.get)
dates.sort()

earliest = dates[0].split(" ")[0]
latest = dates[-2].split(" ")[0]

print maximum, "has the most violations:", types[maximum]
print "The earliest offense occured on {}.\nThe most recent offense occured on {}".format(earliest, latest)
