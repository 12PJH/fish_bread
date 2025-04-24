#주문, 관리자, 종료 3가지 각각 기능 만들기
#input()을 통해 3가지 중 한가지를 입력받아서 작동
#딕셔너리는 어떤 스토리 기반으로 데이터를 구성할때 많이 쓰인다.

#붕어빵 메인 화면
from fishbread_model import BreadShop

shop = BreadShop()

while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료):")
    #입력받은 값에 따라 밑으로 내려가면서 반응한다.
    #맞는 값이 나오면 그 줄의 함수를 호출해서 위로 올라간다.
    if mode == "종료":
        shop.total_price()
        print("시스템을 종료합니다.")
        break
    elif mode == "주문":
        shop.order_bread()
    elif mode == "관리자":
        shop.admin_mode()