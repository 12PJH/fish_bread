#주문, 관리자, 종료 3가지 각각 기능 만들기
#input()을 통해 3가지 중 한가지를 입력받아서 작동


while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료):")
    #입력받은 값에 따라 밑으로 내려가면서 반응한다.
    if mode == "종료":
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()