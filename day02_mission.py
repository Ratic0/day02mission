import random

small_num = random.randint(0,1) #random 모듈에서 불러와 0~1 사이의 정수가 임의로 발생
green_num = random.randint(0,1)

small = bool(small_num) #1이 TRUE
green = bool(green_num)

print(f'small : {small} | green : {green}')

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange

if small == True and green == True :
    print(G+'이건 완두콩이야!'+W)
elif small == True and green == False :
    print(R+'이건 체리야!'+W)
elif small == False and green == True :
    print(G+'이건 수박이야!'+W)
elif small == False and green == False :
    print(O+'이건 호박이야!'+W)

