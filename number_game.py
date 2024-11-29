from random import randint #random 함수중 randint 메소드호출
import sys    #sys 함수호출
def game_play():   # game_play 함수선언
    answer = randint(1,10) #1부터 10사이의 랜덤숫자
    while True: #while 반복문
        print("1과 10 사이의 숫자를 하나 정했습니다.\n 이 숫자는 무엇일까요?") 
        try:
            input_number = int(input("숫자를 입력해주세요: "))  #사용자 숫자 입력
            print(f"예상 숫자: {input_number} ")
            if input_number not in range(1,11,1): #사용자 숫자가 1부터 11사이의 정수인지 판단후 아니면 다시 while문 반복
                print('유효한 값이 아닙니다. 1부터 10사이의 정수를 입력해주세요')
                continue
            elif input_number == answer: #정답이면 정답입니다
                print("정답입니다.")
            elif input_number > answer: #정답보다 크면 너무큽니다. while문 초기로 반복
                print("너무 큽니다. 다시 입력하세요.")
                continue
            elif input_number < answer: #정답보다 작으면 너무작습니다. while문 초기로반복
                print("너무 작습니다. 다시 입력하세요.")
                continue
        except ValueError: #유효하지 않은 값 입력 방지
                print('유효한 값이 아닙니다. 1부터 10사이의 정수를 입력해주세요')
                continue
        replay = input("게임을 다시 하시겠습니까? (y/n): ") #게임을 다시할지 끌지 선택
        if replay == 'y':#다시하면 정답값을 새로뽑고 while문 다시시작
            answer = randint(1,10)
            continue
        elif replay == 'n':#아니면 파이썬 종료
            sys.exit("게임을 종료합니다. 즐거우셨나요? 또 만나요!")
game_play()
