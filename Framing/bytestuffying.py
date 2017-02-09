from math import ceil
def bytestuffing():
    pass

def split(text,size):
    check = list()
    start = 0
    for i in range(ceil(len(text)/size)):
        check.append(text[start:start+size])
        start += size
    return check

def main():
    data = input("Enter the data: ")
    flag = input("Enter the flag: ")
    esc = input("Enter the escape sequence: ")
    size = input("Enter the size of frame")

    spilt_text = split(data,int(size))
    print(spilt_text)
if __name__ == '__main__':
    main()
