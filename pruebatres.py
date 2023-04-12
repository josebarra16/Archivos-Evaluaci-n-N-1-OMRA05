aclNum = int(input("Cual es el número de la IPV4 ACL? "))
if aclNum >= 1 and aclNum <= 99:
 print("Esta es una ACL IPv4 estándar.")
elif aclNum >=100 and aclNum <= 199:
 print("Esta es una ACL IPv4 extendida")
else:
 print("Esta ACL IPv4 no es ni extendida ni estandar .")
