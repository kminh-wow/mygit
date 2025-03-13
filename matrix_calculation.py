import tkinter as tk
from tkinter import messagebox
import numpy as np
import ast

def calculate():
    try:
        A = ast.literal_eval(entry_A.get())
        B = ast.literal_eval(entry_B.get())

        A = np.array(A)
        B = np.array(B)

        operation = operation_var.get()

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
        else:
            messagebox.showerror("오류", "연산 선택택!")
            return

        result_label.config(text=f"결과:\n{result}")

    except Exception as e:
        messagebox.showerror("입력 오류", f"올바른 행렬 형식이 아님님.\n예시: [[1,2],[3,4]]\n\n오류: {e}")

# GUI 구성
root = tk.Tk()
root.title("행렬 계산기")

tk.Label(root, text="행렬 A 입력 (예: [[1,2],[3,4]])").pack()
entry_A = tk.Entry(root, width=40)
entry_A.pack()

tk.Label(root, text="행렬 B 입력 (예: [[5,6],[7,8]])").pack()
entry_B = tk.Entry(root, width=40)
entry_B.pack()

operation_var = tk.StringVar()
tk.Label(root, text="연산 선택").pack()
tk.OptionMenu(root, operation_var, "덧셈", "뺄셈", "곱셈").pack()

tk.Button(root, text="계산하기", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="결과:")
result_label.pack()

root.mainloop()
