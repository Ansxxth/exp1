std_ne=input("enter name ")
stdt_Rno=int(input("enter rollno"))
std_C=input("enter class ")
Mk_Pyt=int(input("py"))
Mk_Ja=int(input("ja"))
Mk_DS=int(input("ds"))
Mk_HTML=int(input("ht"))
Mk_CSS=int(input("cs"))
total=(Mk_Pyt+Mk_Ja+Mk_DS+Mk_HTML+Mk_CSS)
print(total)
avg=(total/500)*100

print(avg)
if avg >=90:
    print("A+ Grade")
    print("Very Good")
elif avg >=80:
    print("A Grade")
    print("Good")
elif avg >=70:
    print("B+ Grade")
    print("Average")
elif avg >=60:
    print("B Grade")
    print("Below Average")
else:
    print("U Grade")
    print("RA")
