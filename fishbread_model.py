class BreadShop:
        #초기화 과정
        def __init__(self):
            self.stock = {"팥붕어빵" : 10, "슈크림붕어빵" : 8, "초코붕어빵" : 5}
            self.sales = {"팥붕어빵" : 0, "슈크림붕어빵" : 0, "초코붕어빵" : 0}
            self.price = {"팥붕어빵" : 1000, "슈크림붕어빵" : 1200, "초코붕어빵" : 1500}
            
        #붕어빵 주문 기능
        def order_bread(self):
            while True:
                bread_type = input("주문할 붕어빵을 선택해주세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) : , 뒤로가길 원하시면 뒤로가기를 입력해주세요.")
                if bread_type == "뒤로가기":
                    break
                if bread_type in self.stock:  #in을 쓸때는 value값이 아니라 키값으로 비교한다.
                    bread_count = int(input("주문하실 붕어빵의 수량을 입력해주세요: "))
                    if  self.stock[bread_type] >= bread_count:            
                    #창고에 있는 빵의 가수가 니가 주문한 개수보다 많은지 확인해볼깨
                        self.stock[bread_type] -= bread_count
                    #stock[bread_type] = stock[bread_type] - bread_count
                    #i = i + 1 => i += 1
                    #딕셔너리의 키값을 넣으면 딕셔너리의 벨류가 나온다.
                        self.sales[bread_type] += bread_count
                        print(f"주문해주셔서 감사합니다.")
                        print(f"{bread_type}의 재고가 현재{self.stock[bread_type]}개 입니다.")
                        break
                    else:
                        print(f"재고가 부족합니다. 현재 {self.stock[bread_type]}개만 주문 가능합니다.")
                else:
                    print("없는 메뉴 입니다. 다시 주문해주세요!!!")
            

    #붕어빵 admin 기능
        def admin_mode(self):
            while True:
                bread_type = input("추가하고자 하는 맛을 입력하세요, 추가가 끝이시면 종료를 입력해주세요.:")
                if bread_type in self.stock:
                    bread_count = int(input("추가하실 개수를 입력하세요:"))
                    self.stock[bread_type] += bread_count
                    print(f"{bread_type}의 재고가{bread_count}개 추가 되어, 현재{self.stock[bread_type]}개 입니다.")
                elif bread_type == "종료":
                    break
                else:
                    print("없는 종류입니다. 다시 입력해주세요 :")


    #붕어빵 가격 계산 기능
        def total_price(self):
            #고급반 total_sales = sum(sales [key] * price [key] for key in sales) #items 매우 많이 중요
            #딕셔너리를 for문에 넣으면 하나씩 데이터를 가져오는데 이 데이터는 key값을 가져온다.
            total = 0
            for key in self.sales:
                total += (self.sales[key] * self.price[key])
            print(f"오늘의 총 매출액은 {total}원 입니다.")
