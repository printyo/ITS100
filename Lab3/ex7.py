from random import *

n1 = str(randint(8,9))
n2 = str(randint(6,7))
n3 = str(randint(4,5))
n4 = str(randint(2,3))
n5 = str(randint(0,1))

otp = n1+n2+n3+n4+n5
print("Your OTP is %s. This password will be expired within 5 minutes."%otp)