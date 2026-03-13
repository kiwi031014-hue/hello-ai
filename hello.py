import random

# 1부터 100 사이의 임의의 숫자를 생성합니다.
secret_number = random.randint(1, 100)
attempts = 0

print("1부터 100 사이의 숫자를 맞춰보세요!")

while True:
    guess = int(input("숫자를 입력하세요: "))
    attempts += 1

    if guess < secret_number:
        print("더 큰 숫자입니다! (UP)")
    elif guess > secret_number:
        print("더 작은 숫자입니다! (DOWN)")
    else:
        print(f"정답입니다! {attempts}번 만에 맞추셨네요.")
        break