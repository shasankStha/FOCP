import sys

count = len(sys.argv)
if count == 1:
    print("No argument provided")
else:
    total = 0
    while count > 1:
        count -= 1
        total += float(sys.argv[count])
    av= total / len(sys.argv[1:])

    print("Total is", total)
    print("Average is", av)
