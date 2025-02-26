class Fourcal:
    def setdata(self, first, second):   #매서드의 매개변수
        self.first = first              #매서드의 수행문
        self.second = second            # //
    def add(self):
         result = self.first + self.second
         return result
    def mul(self):
         result = self.first * self.second
         return result
    def sub(self):
         result = self.first - self.second
         return result
    def div(self):
         result = self.first / self.second
         return result

a = Fourcal()   #a 객체를 통해 setdata 매서드 호출
a.setdata(4,2)  # 이 떄 self는 a, first는 4, second는 2 
                # 해석은 self.first = 4, self.second = 2이므로 다시 a.first = 4, a.second = 2
#print(a.first,a.second)
                #클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적이다.


class MoreFourcal(Fourcal): #클래스 상속
    def pow(self):
        result = self.first ** self.second
        return result
    
class SafeFourCal(Fourcal): #매서드 오버라이딩
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

#############################################################
#계산기만들어보자 !
