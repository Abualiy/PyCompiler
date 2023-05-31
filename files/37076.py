x = int(input())
y = int(input())

sum = x + y
sub = x - y

opr = input()

if opr == "sub":
    print("The operation is {}".format(opr))
    print()
    print("The result is {}".format(sub))
if opr == "sum":
    print("The operation is {}".format(opr))
    print()
    print("The result is {}".format(sum))