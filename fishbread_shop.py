#주문, 관리자, 종료 3가지 각각 기능 만들기
#input()을 통해 3가지 중 한가지를 입력받아서 작동
#딕셔너리는 어떤 스토리 기반으로 데이터를 구성할때 많이 쓰인다.

stock = { #key값을 이용해서 Value를 찾을 수 있다. {ket:Value구조}
    "팥붕어빵" : 10,
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 5
    }


sales = {
    "팥붕어빵" : 0,
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
    }



def order_bread():
    while True:
        bread_type = input("주문할 붕어빵을 선택해주세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) : , 뒤로가길 원하시면 뒤로가기를 입력해주세요.")
        if bread_type == "뒤로가기":
            break
        if bread_type in stock: #in을 쓸때는 value값이 아니라 키값으로 비교한다.
            bread_count = int(input("주문하실 붕어빵의 수량을 입력해주세요: "))
            if  stock[bread_type] >= bread_count:            
            #창고에 있는 빵의 가수가 니가 주문한 개수보다 많은지 확인해볼깨
                stock[bread_type] -= bread_count
            #stock[bread_type] = stock[bread_type] - bread_count
            #i = i + 1 => i += 1
            #딕셔너리의 키값을 넣으면 딕셔너리의 벨류가 나온다.
                sales[bread_type] += bread_count
                print(f"{bread_type} {bread_count}개가 판매되었습니다.")
                break
            else:
                print(f"재고가 부족합니다. 현재 {stock[bread_type]}개만 주문 가능합니다.")
        else:
            print("없는 메뉴 입니다. 다시 주문해주세요!!!")
    


while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료):")
    #입력받은 값에 따라 밑으로 내려가면서 반응한다.
    #맞는 값이 나오면 그 줄의 함수를 호출해서 위로 올라간다.
    if mode == "종료":
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()        