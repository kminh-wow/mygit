import tkinter as tk
from tkinter import messagebox
import numpy as np
import ast
from fractions import Fraction

def parse_matrix(input_str):
    """ 입력 문자열을 2차원 리스트로 변환 (간단한 형식 지원) """
    try:
        # 리스트 자동 보정정
        if not input_str.startswith('['):
            input_str = f"[{input_str}]"
        matrix = ast.literal_eval(input_str)  # 문자열을 리스트로 변환
        return np.array([[Fraction(str(x)) for x in row] for row in matrix])  # 요소를 분수로 변환
    except Exception as e:
        raise ValueError(f"잘못된 행렬 형식! (예: [1,1],[1,1])\n오류: {e}")

def parse_scalar(input_str):
    """ 입력값이 단순한 숫자 또는 분수라면 Fraction으로 변환 """
    try:
        return Fraction(input_str)
    except Exception as e:
        raise ValueError(f"잘못된 상수 입력! (예: 3 또는 1/2)\n오류: {e}")

def format_result(matrix):
    """ 행렬 결과를 보기 쉽게 문자열로 변환 (Fraction을 1/2 형태로 표시) """
    return np.array2string(np.vectorize(str)(matrix), separator=", ")

def calculate():
    try:
        A = parse_matrix(entry_A.get())  # A를 행렬로 변환
        operation = operation_var.get()  # 선택한 연산

        if operation in ["곱셈", "덧셈", "뺄셈"]:
            B = parse_matrix(entry_B.get())  # B를 행렬로 변환
        elif operation == "상수배":
            scalar = parse_scalar(entry_B.get())  # 상수를 Fraction으로 변환

        if operation == "곱셈":
            if A.shape[1] != B.shape[0]:
                messagebox.showerror("오류", "행렬 A의 열 수와 B의 행 수가 같아야 곱셈이 가능!")
                return
            result = A @ B  
        elif operation == "덧셈":
            if A.shape != B.shape:
                messagebox.showerror("오류", "덧셈을 위해서는 두 행렬의 크기가 같아야 함!")
                return
            result = A + B
        elif operation == "뺄셈":
            if A.shape != B.shape:
                messagebox.showerror("오류", "뺄셈을 위해서는 두 행렬의 크기가 같아야 함!")
                return
            result = A - B
        elif operation == "역행렬":
            if A.shape[0] != A.shape[1]:
                messagebox.showerror("오류", "역행렬을 구하려면 정사각 행렬이어야 함!")
                return
            try:
                result = np.linalg.inv(A).astype(Fraction)  # 역행렬을 Fraction으로 변환
            except np.linalg.LinAlgError:
                messagebox.showerror("오류", "이 행렬은 역행렬이 존재하지 않음!")
                return
        elif operation == "상수배":
            result = scalar * A  # 상수배 연산 수행
        else:
            messagebox.showerror("오류", "연산 선택!")
            return

        result_label.config(text=f"결과:\n{format_result(result)}")  # 결과를 보기 쉽게 출력

    except Exception as e:
        messagebox.showerror("입력 오류", str(e))

# GUI 구성
root = tk.Tk()
root.title("행렬 계산기 (분수 지원)")

tk.Label(root, text="행렬 A 입력 (예: [1,1],[1,1] 또는 [1/2,1],[3,4])").pack()
entry_A = tk.Entry(root, width=40)
entry_A.pack()

tk.Label(root, text="행렬 B 또는 상수 입력 (예: [5,6],[7,8] 또는 3 또는 1/2)").pack()
entry_B = tk.Entry(root, width=40)
entry_B.pack()

operation_var = tk.StringVar()
tk.Label(root, text="연산 선택").pack()

operations_frame = tk.Frame(root)
operations_frame.pack()
operations = ["덧셈", "뺄셈", "곱셈", "역행렬", "상수배"]
for op in operations:
    tk.Radiobutton(operations_frame, text=op, variable=operation_var, value=op).pack(side=tk.LEFT)

tk.Button(root, text="계산하기", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="결과:")
result_label.pack()

root.mainloop()
