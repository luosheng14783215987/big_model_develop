# 测试浮点表达式
# print(f'{1.23456789:.2f}')
# print(f'{1.23456789:10.2f}') # 右对齐

import os
# 仅检查是否已配置，避免在终端打印密钥内容
print("DASHSCOPE_API_KEY configured:", bool(os.getenv("DASHSCOPE_API_KEY")))
print("OPENAI_API_KEY configured:", bool(os.getenv("OPENAI_API_KEY")))

# import sys
# print(sys.executable)