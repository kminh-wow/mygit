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
        return a ** b  # 제곱 연산

# 계산기 실행 함수
def run_calculator():
    calc = Calculator()
    result = None  # 초기값
    
    print("\n=== 단계별 계산기 ===")
    print("첫 숫자를 입력한 후, 연산자와 숫자를 하나씩 입력하세요.")
    print("예: '5' 입력 후, '+ 3' 입력 → 8 출력")
    print("'=' 입력 시 현재 결과 표시, 'exit' 입력 시 종료")

    while True:
        if result is None:  # 첫 번째 숫자 입력
            try:
                result = float(input("\n첫 번째 숫자를 입력하세요: "))
            except ValueError:
                print("숫자를 올바르게 입력하세요.")
                continue
        else:  # 연산자와 숫자를 계속 입력
            user_input = input("연산자와 숫자를 입력하세요: ").strip()

            if user_input.lower() == "exit":
                print("계산기를 종료합니다.")
                print(result)
                break
            elif user_input == "=":
                print(f"현재 결과: {result}")
                continue

            try:
                op, num = user_input.split()
                num = float(num)

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
                else:
                    print("지원하지 않는 연산자입니다. 다시 입력하세요.")
                    continue

                print(f"결과: {result}")

            except ValueError:
                print("올바른 형식으로 입력하세요. (예: + 3, * 2, 연산자와 숫자 공백 필수)")
            except Exception as e:
                print(f"오류 발생: {e}")

# 실행
run_calculator()
