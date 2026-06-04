
"""'
你需要对用户的反馈进行原因分类。
分类包括：价格过高、售后支持不足、产品使用体验不佳、其他。
回答格式为：分类结果：xx。
用户问题：啄木鸟维修太贵了，师傅服务态度差
"""
import  ollama

while True:
    prompt = input("请输入内容")

    response = ollama.chat(model="qwen2:1.5b",messages=[{"role": "user","content": prompt}])
    print(response.message.content)
