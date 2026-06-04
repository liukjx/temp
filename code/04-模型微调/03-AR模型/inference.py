from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("/gemini/code/weights/qwen2-7b-sft-lora-merged", trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    "/gemini/code/weights/qwen2-7b-sft-lora-merged",
    device_map="auto",
    trust_remote_code=True
).eval()

response, history = model.chat(tokenizer,
                               "请提取以下内容中的摘要信息,提高学习效率的三个技巧：\n\n1. 使用番茄工作法，每25分钟专注后休息5分钟\n2. 建立思维导图整理知识框架\n3. 睡前复习重点内容加强记忆",
                               history=None)
print(response)
