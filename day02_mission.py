import random

secret = random.randint(1,10) #random 모듈에서 불러와 1~10 사이의 정수가 임의로 발생
guess = random.randint(1,10)
print(f'secret={secret}  guess={guess}')
if secret - guess > 0 :
    print('too low')
elif secret == guess :
    print('just right')
else :
    print('too high')
