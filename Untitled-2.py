print("--- Python Hesap Makinesi ---")
a = int(input("Lütfen bir sayı giriniz: "))
b = int(input("Lütfen bir sayı giriniz: "))
print ("t -topla")
print ("c -çıkar")
print ("x -çarp")
print ("b -böl")
c=input("Lütfen yapmak istediğiniz işlemi giriniz: ")
if (c=="t"):
    d=a+b
    print("Sonuç=",d)
if (c=="c"):
    d=a-b
    print ("Sonuç=",d)
if (c=="x"):
    d=a*b
    print ("Sonuç=",d)
if (c=="b"):
    d=a/b 
    print ("Sonuç=",d)
