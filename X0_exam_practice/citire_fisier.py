

def read_file(filename):
    '''
    File descriptor

    fd = open(filename, "r")

    fd.close
    '''
    fd =open(filename, "r")
    data = []
    line = fd.readline()
    while len(line):
        for i in range (len(line)):
            if line[i] == "-":
                data.append(" ")
            elif line[i] == "x":
                data.append("X")
            elif line[i] == "o":
                data.append("O")
        line = fd.readline()

    fd.close()
    return data


def print_to_file(filename, data):
    fd = open(filename, "w")
    # for i in range(6):
    #     line = data[i]
    #     fd.write(line)
    for i in range(6):
        for j in range(6):
            if data[i][j] == " ":
                symb = "-"
            elif data[i][j] == "X":
                symb = "x"
            elif data[i][j] == "O":
                symb = "o"
            fd.write(symb)
        fd.write("\n")

print(read_file("other_input.txt"))