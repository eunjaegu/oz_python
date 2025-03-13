# balance : 통장에 들어있는 기본 금액을 담는 변수
# 1.입금, 2.출금, 3.영수증 보기, 4.종료 => 글자를 입력 받을지(입금, 출금...) / 숫자를 입력받을지(1, 2, 3... )
# 숫자로 원하는 기능을 입력할 수 있게 만들어주세요 그리고 사용자가 입력한 기능은 num 변수에 담아주세요
# deposit_amount: 
# withdraw_amount:
# 영수증 기능에는 사용되는 데이터타입은 list => [["입금", 5000, 8000],["출금", 3000, 5000], ["출금", 2000, 3000]]

#영수증 기능 구현을 위한 빈 리스트 선언
receipts = []

balance = 3000 
# datetime.hour < 12 데이터 출금 시간 정할수있음
while True :
    type_num = int(input("기능의 번호를 입력해주세요.(1.입금, 2.출금, 3.영수증 보기, 4.종료) : "))

    # 입금
    if type_num == 1:
        deposit_amount = input("입금할 금액을 입력해주세요. : ") # "123123123".isdigit => True
        if deposit_amount.isdigit() and int(deposit_amount) > 0: #첫번째 조건 문자가 입력된건 아닌지 확인 / 0 보다 큰 금액을 입력했는지 
            balance += int(deposit_amount) # balance = balance + int(deposit_amount)
            print(f'{deposit_amount}원 입금 완료, 현재 잔액 {balance}원')
            # 영수증에 데이터 넣기 (입금, 입금잔액, 현재잔액)
            # 튜플로 사용 : 값이 변하지 않음 
            receipts.append(("입금", deposit_amount, balance))
        else:
            print("다시 입력해주세요.")
    # 출금
    if type_num == 2:
        withdraw_amount = input("출금할 금액을 입력해주세요 : ")
        if withdraw_amount.isdigit() and int(deposit_amount) >0:
            withdraw_amount = min(balance, int(withdraw_amount))
            balance -= withdraw_amount

            # 영수증에 데이터 넣기 (출금, 입금잔액, 현재잔액)
            # 튜플로 사용 : 값이 변하지 않음 
            receipts.append(("출금", withdraw_amount, balance))
        else:
            print("다시 입력해주세요.")
        print(f"{withdraw_amount}원 출금 완료, 현재 잔액 {balance}원'")
    #
    if type_num == 3:
                # 리스트의 값이 있을 때와 없을 때 달랐으면 한다.
        # 값이 있을 때 출력 결과가 출금 : 3000원 | 잔액 : 5000원과 같이 나왔으면 합니다.
        #   ""
        if receipts:
            print("===영수증===")
            for i in receipts:
                print(f"{i[0]} : {i[1]}원 | {i[2]}원")
        else :
            print("영수증 내역이 없습니다.")
        break
    if type_num == "4":
        print("서비스를 종료합니다.")
        break
