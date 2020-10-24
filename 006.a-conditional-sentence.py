# 조건문

# 기본 문법
if True:
    print("code1")
    print("code2")
print("code3")
print('---------------------')

# 조건문의 활용
input = 11
real = 11
if real == input:
    print("Hello!")
print('---------------------')

# else
input = 11
real = 11
if real == input:
    print("Hello!")
else:
    print("Who are you?")
print('---------------------')

# else if
input = 33
real_bogi = 11
real_skyler = "ab"
if real_bogi == input:
  print("Hello!, bogi")
elif real_skyler == input:
  print("Hello!, skyler")
else:
  print("Who are you?")