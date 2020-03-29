#경과 시간 출력하기

number = int(input("경과 시간(초)를 위력하시오 : "))

days, r = divmod(number, 86400)
hours, r = divmod(r, 3600)
minutes, seconds = divmod(r, 60)

print(days,"일",hours,"시간",minutes, "분", seconds, " 초")