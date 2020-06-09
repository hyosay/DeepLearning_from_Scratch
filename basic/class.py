class Unit:  #Unit class를 작성
    def __init__(self, name, power):  #이름과 전투력을 정의
        self.name = name
        self.power = power

    def attack(self):      #공격을 하는 함수
        print(self.name, "이(가) 공격을 수행합니다. [전투력 :", self.power, "]")


unit = Unit("전효성", 285)
unit.attack()


class Monster(Unit):  # Unit을 상속
    def __init__(self, name, power, type):  #이름,전투력, 종류를 정의
        self.name = name
        self.power = power
        self.type = type

    def show_info(self):
        print("몬스터 이름 :", self.name, "/ 몬스터 종류 :", self.type)


monster = Monster(" 슬라임", 10, "초급 ")
monster.attack()

