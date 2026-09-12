#inp = 32
#out = Thirty four

number = int(input("Enter a number: "))
ntw = {1:'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',\
       7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',\
       12: 'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', \
       16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30: 'thirty', 40: 'fourty', 50:'fifty', \
       60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

#ntw --> number to words

#1 to 20
if number <= 20:
    print(ntw[number])

#21 to 99
elif 21 <= number <= 99:
    ones = number % 10
    tens = (number // 10) * 10

    if ones == 0:
        print(ntw[tens])
    else:
        print(f"{ntw[tens]} {ntw[ones]}")

#100 to 999
elif 100 <= number <= 999:
    hundreds = number // 100
    rest =number % 100

    if rest == 0:
        print(f" {ntw[hundreds]} hundred")
    else:
        if rest <= 20:
            print(f"{ntw[hundreds]} hundred {ntw[rest]}")
        else:
            ones = rest % 10
            tens = (rest // 10) * 10

            if ones == 0:
                print(f"{ntw[hundreds]} hundred {ntw[tens]}")
            else:
                print(f"{ntw[hundreds]} hundred {ntw[tens]} {ntw[ones]}")

#1000 to 9999
elif 1000 <= number <= 9999:
    thousands = number // 1000
    rest = number % 1000

    if rest == 0:
        print(f" {ntw[thousands]} thousand")
    else:
        hundreds = rest // 100
        last = rest % 100

        if hundreds == 0:
            if last <= 20:
                print(f"{ntw[thousands]} thousand {ntw[last]}")
            else:
                ones = last % 10
                tens = (last // 10) * 10

                if ones == 0:
                    print(f" {ntw[thousands]} thousand {ntw[tens]}")
                else:
                    print(f" {ntw[thousands]} thousand {ntw[tens]} {ntw[ones]} ")
        else:
            if last == 0:
                print(f" {ntw[thousands]} thousand {ntw[hundreds]} hundred ")
            else:
                if last <= 20:
                    print(f"{ntw[thousands]} thousand {ntw[hundreds]} hundred {ntw[last]} ")
                else:
                    tens = (last // 10) * 10
                    ones = last % 10

                    if ones == 0:
                        print(f" {ntw[thousands]} thousand {ntw[hundreds]} hundred {ntw[tens]} ")
                    else:
                        print(f" {ntw[thousands]} thousand {ntw[hundreds]} hundred {ntw[tens]} \
{ntw[ones]} ")

# 10000 to 99999
elif 10000 <= number <= 99999:
    tenthousand = number // 10000
    rest = number % 10000

    if rest == 0:
        print(f" {ntw[tenthousand]} tenthousand")

