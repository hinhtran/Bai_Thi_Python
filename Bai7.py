def SoNguyen(n):
    i = 2;
    lst = [];

    while (n > 1):
        if (n % i == 0):
            n = int(n / i);
            lst.append(i);
        else:
            i = i + 1;

    if (len(lst) == 0):
        lst.append(n);
    return lst;
 
n = int(input("Nhập số nguyên dương n = "));

lst = SoNguyen(n);
size = len(lst);
s1 = "";
for i in range(0, size - 1):
    s1 = s1 + str(lst[i]) + " * ";
s1 = s1 + str(lst[size-1]);
