#input variable a dan b
a=input("Masukkan variable a:")
b=input("Masukkan variable b:")

#print variable a dan b
print("Variable a=",a)
print("Variable b=",b)

#print hasil operasi dari variable dengan string format
print("Hasil penggabungan {0}&{1}=%s".format(a,b)%(a+b))

#konversi nilai variable
a=int(a)
b=int(b)
print("Hasil penjumlahan {0}+{1}=%d".format(a,b)%(a+b))
print("Hasil pembagian {0}/{1}=%d".format(a,b)%(a/b))
print("Sisa pembagian {0}/{1}=%d".format(a,b)%(a%b))
