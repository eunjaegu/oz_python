# balance : 통장에 들어있는 기본 금액을 담는 변수
# 1.입금, 2.출금, 3.영수증 보기, 4.종료
# 숫자로 원하는 기능을 입력할 수 있게 만들기, 사용자가 입력한 기능은 num 변수에 담기

balance = 3000 

while True:
    type_num = int(input("기능의 번호를 입력해주세요.(1.입금, 2.출금, 3.영수증 보기, 4.종료) : "))

    if type_num == 1:
        deposit_amount = input("입금할 금액을 입력해주세요. : ")
        if deposit_amount.isdigit() and int(deposit_amount) > 0:
            balance += int(deposit_amount)
            print(f'{deposit_amount}원 입금 완료, 현재 잔액 {balance}원')
        else:
            print("다시 입력해주세요.")
    elif type_num == 2:
        withdraw_amount = input("출금할 금액을 입력해주세요 : ")
        if withdraw_amount.isdigit() and int(deposit_amount) >0:
            withdraw_amount = min(balance, int(withdraw_amount))
            balance -= withdraw_amount
        else:
            print("다시 입력해주세요.")
        print(f"{withdraw_amount}원 출금 완료, 현재 잔액 {balance}원'")
    elif type_num == 3:
        print("영수증 보기")
    elif type_num == 4:
        print("종료")
        break
    else:
        print("다시 입력하세요.")