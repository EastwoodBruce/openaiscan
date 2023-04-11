import os
import sys
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def askChatGPT(prompt):
    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

if len(sys.argv) < 2:
    print("用法: python3 openaiscan.py <文件名>")
    sys.exit()

# 获取文件名和内容
filename = sys.argv[1]
with open(filename, 'r') as f:
    file_content = f.read()

# 首先提示 ChatGPT 扮演一个代码审计专家
intro_prompt = "现在你扮演一个代码审计专家,分析向你传输的代码是否存在漏洞并标出危害等级"
intro_response = askChatGPT(intro_prompt)
print(intro_response)

# 将文件内容分成较小的部分
max_length = 2048
parts = [file_content[i:i+max_length] for i in range(0, len(file_content), max_length)]

# 逐个部分向 ChatGPT 传递文件内容并获取回应
for idx, part in enumerate(parts):
    print(f"部分 {idx+1}：")
    code_audit_prompt = f"请审计以下 PHP 代码：\n{part}"
    code_audit_response = askChatGPT(code_audit_prompt)
    print(code_audit_response)
    print("\n" + "=" * 80 + "\n")
