#할인 가격 계산기
price_before_discount = float(input("상품 가격을 입력하여라: "))

discount = int(input("할인율을 입력하여라(0 ~ 100 ) : "))

discount_amount = price_before_discount * discount / 100  #할인된 가격

price_after_discount = price_before_discount - discount_amount  #할인 전 가격 - 할인된 가격

print("최종 할인 급액 : ",price_after_discount)

