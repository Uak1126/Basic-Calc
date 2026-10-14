def toplama(a,b):
    if (c=="t"):
        return a+b

def cıkarma(a,b):
    if (c=="c"):
        return a-b

def bolme(a,b):
    if (c=="b"):
        return a/b
    if b==0:
        return ("Sıfıra bölünemez!")

def çarpma(a,b):
    if (c=="x"):
        return a*b

a = int(input("Lütfen bir sayı giriniz: "))
b = int(input("Lütfen bir sayı giriniz: "))
print ("t -topla")
print ("c -çıkar")
print ("x -çarp")
print ("b -böl")
c=input("Lütfen yapmak istediğiniz işlemi giriniz: ")