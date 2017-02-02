def crc(msg, div, code):
    """
        To generate please enter the msg,div,and code to be appended
        To check please enter the msg without appended code . divisor and extracted code
    """
    # Append the code to the message. If no code is given, default to '000'
    msg = msg + code

    # Convert msg and div into list form for easier handling
    msg = list(msg)
    div = list(div)

    # Loop over every message bit (minus the appended code)
    for i in range(len(msg)-len(code)):
        # If that messsage bit is 1, perform modulo 2 multiplication
        if msg[i] == '1':
            for j in range(len(div)):
                # Perform modulo 2 multiplication on each index of the divisor
                msg[i+j] = str((int(msg[i+j])+int(div[j]))%2)

    # Output the last error-checking code portion of the message generated
    print(msg)
    return ''.join(msg[-len(code):])

if __name__ == '__main__':

    def main():
        case = input("Enter what you want to do: \n i) Send(s) \n ii) Recieve(r) \n Please Input you choice: ")
        div = input("Enter the divisor in binary: ")
        msg = input("Enter the msg in binary: ")
        if case == 's':
            code = '0'
            for i in range(len(div) -2):
                code += '0'
            code = crc(msg, div,code)
            print('Output code:', code)
            print("Message to be send",m1sg+code)
        elif case == 'r':
            code = msg[-(len(div) - 1):]
            msg = msg[0: -(len(div) -1)]
            if not int(crc(msg, div, code)):
                print("No error detected")
            else:
                print("Error Detected")
    main()