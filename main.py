from Menu import *
from Order import *
from Sales import *
from datetime import datetime

if __name__ == '__main__':
    menu=Menu()
    order=Order()
    sales=Sales()
    now = datetime.now()
    y = now.time()
    k=now.strftime('%H:%M')
#작업선택 안내
#x가 아닌동안
#m:메뉴목록 보여주기
#o : 주문입력
#   메뉴번호 입력
#   메뉴번호가 0이 아닌동안 반복
#   수량
#   새메뉴번호 입력
#   주문내역 보여주고, 모바일 번호 입력대기
#   모바일 번호가 -1이면, 주문취소
#   그렇지 않으면 매출에 추가
#   s:매출목록&매출총액 보여주기
    sch=input('작업을 선택하시오 [m:메뉴목록, o:주문입력, s:매출조회, u:메뉴관리, x:프로그램종료]\n')
    while sch!='x':
        order = Order()
        if sch=='u':
            sch_2=input("작업을 선택하시오[C:신규메뉴추가, U: 기존메뉴수정, D: 기존메뉴삭제, X: 메뉴관리종료]\n")
            while sch_2!='X':
                if sch_2=='C':
                    menu.display()
                    name=input('추가할 메뉴이름:')
                    price=input('가격:')
                    menu.addnew(name, price)
                    menu.display()
                elif sch_2=='U':
                    menu.display()
                    ndx=int(input('수정할 메뉴 번호: '))
                    name=input('메뉴 이름: ')
                    price=input('가격: ')
                    menu.update(ndx, name, price)
                    menu.display()
                elif sch_2=='D':
                    menu.display()
                    ndx=int(input('삭제할 메뉴 번호: '))
                    menu.delete(ndx)
                    menu.display()
                sch_2 = input("작업을 선택하시오[C:신규메뉴추가, U: 기존메뉴수정, D: 기존메뉴삭제, X: 메뉴관리종료]\n")
        if sch=='m':
            menu.display()
        sch = input('작업을 선택하시오 [m:메뉴목록, o:주문입력, s:매출조회, u:메뉴관리, x:프로그램종료]\n')
        if sch=='o':
            sch_1=int(input('메뉴번호 를 입력해 주세요\n'))
            while sch_1!=0:
                qty=int(input('메뉴 수량을 입력해 주세요\n'))
                order.add(sch_1, qty, menu.price[sch_1-1])
                menu.display()
                sch_1 = int(input('메뉴번호 를 입력해 주세요\n'))

            else:
                for i in range(len(order.menu_no)):
                    print(menu.name[order.menu_no[i]], order.qty[i], '잔', order.price[i], '원')
            mobile=input('모바일 번호를 입력해 주세요\n')
            if mobile=='-1':
                order.cancel()
                print('주문이 취소 되었습니다.')
            else:
                sales.add(mobile, sum(order.price), k)
            sch = input('작업을 선택하시오 [m:메뉴목록, o:주문입력, s:매출조회, x:프로그램종료]\n')
        if sch == 's':
            sales.sum()


