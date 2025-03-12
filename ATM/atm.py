# balance : 통장에 들어있는 기본 금액을 담는 변수
# 1.입금, 2.출금, 3.영수증 보기, 4.종료
# 숫자로 원하는 기능을 입력할 수 있게 만들기, 사용자가 입력한 기능은 num 변수에 담기

balance = 3000 

while True:
    type_num = int(input("기능의 번호를 입력해주세요.(1.입금, 2.출금, 3.영수증 보기, 4.종료) : "))

    if type_num == 1:
        deposit_amount = input("입금할 금액을 입력해주세요. : ")
        if deposit_amount != "" and deposit_amount > 0

        print("입금 완료")
    elif type_num == 2:
        print("출금 완료")
    elif type_num == 3:
        print("영수증 보기")
    elif type_num == 4:
        print("종료")
        break
    else:
        print("다시 입력하세요.")