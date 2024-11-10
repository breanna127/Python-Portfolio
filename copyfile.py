filename = input("Enter the input file name: ")
outfile = input("Enter the output file name: ")

try:
    with open(filename, 'r') as f, open(outfile, 'w') as w:
        for line in f:
            w.write(line)
except FileNotFoundError:
    print(filename + " does not exist!")