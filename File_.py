# Write initial content
with open("Practice.txt", "w") as f:
    f.write("Hi.Everyone.\nWe are learning file I/O\n")
    f.write("using Java\nI like Programming in Java")


word = "learning"

def found():
    with open("Practice.txt", "r") as f:
        data = f.read()
        if word in data:
            print("Found!!")
        else:
            print("Not Found!")


def check_word_inLine():
    word = "learning"
    line_no = 1
    
    with open("Practice.txt", "r") as f:
        for line in f:
            if word in line:
                print("Found at line:", line_no)
                return
            line_no += 1
    
    print("Not Found")
    return -1


# Replace Java with Python and save to file
with open("Practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")

with open("Practice.txt", "w") as f:
    f.write(new_data)

print(new_data)


# Function calls
found()
check_word_inLine()