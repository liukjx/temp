from transformers import AutoModelForCausalLM
from peft import LoraConfig, get_peft_model

# 加载预训练模型
model = AutoModelForCausalLM.from_pretrained(r'D:\北京java428\02-code\03-AR模型\gpt2')
print(model)
# lora
lora_config = LoraConfig(
    task_type='CAUSAL_LM',
    r=8,
    lora_alpha=16,
    target_modules=['c_attn','c_proj','c_fc'],
    lora_dropout=0.1
)
# 组合
model = get_peft_model(model=model,peft_config=lora_config)
print(model)
model.print_trainable_parameters()