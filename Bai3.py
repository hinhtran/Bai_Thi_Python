s = input("Nhập câu của bạn: ")
d={"D":0, "L":0}
for c in s:
 if c.isdigit():
    d["D"]+=1
 elif c.isalpha():
    d["L"]+=1
 else:
    pass
print ("Số chữ cái là:", d["L"])
print ("Số chữ số là:", d["D"])
