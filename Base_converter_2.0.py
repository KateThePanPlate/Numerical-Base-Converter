#possible bases are based on the length of this string, with values of symbols based on their position within this string
#add and modify to your own content
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def convBaseFromDecim(num, base):
    #converts an integer from base ten to given integer base
    values, sign = [], ""
    E = num
    try:
        if abs(base) < 2 or abs(base) > len(digits): # base check
            raise ValueError("invalid base")
    except:
        error = "invalid base"
        return error

    if int(num) < 0 and base > 0: num *= -1; sign = "-" # handle negatives

    while num:
        num, d = divmod(int(num), base)
        if d < 0: num += 1; d -= base # handle negative base conversion
        values.append(d)

    values.reverse()
    if str(E) == "0":
        converted = 0
    else:
        converted = sign + "".join(digits[i] for i in values)
    return converted
def convBaseToDecim(num, base):
    #Converts an integer from a given integer base to base ten
    # initializing substring
    A = 1
    # create a result list
    result1 = []
    result2 = []
    B = 0
    for i in range(0, len(num), A):
        #convert to int, after the slicing process
        result1.append(num[i : i + A])
    if str(result1[0])=="-":
        isnegative=1
        result1.remove("-")
    else:
        isnegative=0

    print(result1)
    result1.reverse()
    for i in range(0, len(result1), A):
        #Convert from base
        for x in range(0, len(digits), A):
            if result1[i]==digits[x]:
                D=x
                result2.append(D*(base**i))
    for i in range(0, len(result2), A):
        #combines digits
        B = B + int(result2[i])
    B = (B*((isnegative*2)-1))*-1
    return B
def convBaseToBase(num, base1, base2):
    base1 = int(base1)
    base2 = int(base2)
    num = str(num)
    if base1 == 1:
        C = len(str(num))
    else:
        C = convBaseToDecim(num, base1)
    if base2 == 1:
        return ("1"*int(C))
    else:
        finale = convBaseFromDecim(C, base2)
        return finale
#warnings and information
print("Currently running Kate's Base Converter version 1.0.2")
print("")
print("Acceptable bases can be any integer from "+str(len(digits)*-1)+" to "+str(len(digits))+" except for bases -1 and 0\nThese are the acceptable symbols to use as numbers: "+digits+"\nNumbers for conversion must be integers.\nDon't use ,\n")
while True:
    while True:
        try:
            #taking input
            base1 = int(input("What is the starting base? "))
            base2 = int(input("What is the target base? "))
            num = input("What is the number to be converted? ")
            break
        except ValueError:
            print("Sorry, please input integers.")
    #giving answer
    print(convBaseToBase(num, base1, base2))