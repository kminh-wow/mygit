class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def power(self, a, b):
        return a ** b  

# 계산기 실행 함수
def run_calculator():
    calc = Calculator()
    
    print("\n=== 연속 계산 지원 계산기 ===")
    print("사용법: 숫자 연산자 숫자 ... 연속 입력 (예: 5 + 3 * 2)")
    print("계산을 종료하려면 'exit' 입력, 결과를 확인하려면 '=' 입력")

    while True:
        user_input = input("\n계산식을 입력하세요: ")

        if user_input.lower() == "exit":
            print("계산기를 종료합니다.")
            break

        try:
            tokens = user_input.split()  # 입력을 공백 기준으로 분할
            if len(tokens) < 3:
                print("잘못된 입력입니다. 최소한 '숫자 연산자 숫자' 형식이어야 합니다.")
                continue
            
            result = float(tokens[0])  # 첫 번째 숫자
            
            i = 1
            while i < len(tokens) - 1:
                op = tokens[i]
                num = float(tokens[i + 1])

                if op == "+":
                    result = calc.add(result, num)
                elif op == "-":
                    result = calc.subtract(result, num)
                elif op == "*":
                    result = calc.multiply(result, num)
                elif op == "/":
                    result = calc.divide(result, num)
                elif op == "**":
                    result = calc.power(result, num)
                elif op == "=":
                    break
                else:
                    print(f"지원하지 않는 연산자: {op}")
                    break

                i += 2  # 다음 연산자로 이동
            
            print(f"결과: {result}")

        except ValueError:
            print("잘못된 입력입니다. 숫자와 연산자를 올바르게 입력하세요.")
        except Exception as e:
            print(f"오류 발생: {e}")

# 실행
run_calculator()