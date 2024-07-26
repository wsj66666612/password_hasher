import hashlib
import base64
import tkinter as tk
from tkinter import messagebox
import pyperclip

FIXED_SALT = b"your_fixed_salt_here_black_hack_fack_mom_bitch_pussy_dick_sugar_daddy"  # 你可以使用任何固定的盐值

def hash_password(password: str, length: int = 16, iterations: int = 5000000) -> str:
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), FIXED_SALT, iterations)
    hash_b64 = base64.urlsafe_b64encode(dk).decode()
    hash_substr = hash_b64[:length]
    
    # 确保结果包含大写字母、小写字母、数字和符号
    has_upper = any(c.isupper() for c in hash_substr)
    has_lower = any(c.islower() for c in hash_substr)
    has_digit = any(c.isdigit() for c in hash_substr)
    has_symbol = any(not c.isalnum() for c in hash_substr)
    
    if not (has_upper and has_lower and has_digit and has_symbol):
        return hash_password(hash_substr, length)

    return hash_substr

def generate_and_copy():
    password = entry.get()
    if not password:
        messagebox.showerror("输入错误", "请输入一个密码")
        return
    encrypted_password = hash_password(password)
    result_label.config(text=encrypted_password)
    pyperclip.copy(encrypted_password)
    messagebox.showinfo("复制成功", "加密后的密码已复制到剪贴板")

# 创建Tkinter窗口
root = tk.Tk()
root.title("密码加密工具")

# 创建并放置标签、输入框和按钮
tk.Label(root, text="输入密码：").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="生成并复制", command=generate_and_copy)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# 添加“防伪”标签
authentic_label = tk.Label(root, text="阿钧网络工作室出品", fg="red")
authentic_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# 运行Tkinter主循环
root.mainloop()
