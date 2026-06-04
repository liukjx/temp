from transformers import AutoModelForCausalLM
from peft import PrefixTuningConfig, get_peft_model

# 加载预训练模型
model = AutoModelForCausalLM.from_pretrained(r'D:\北京java428\02-code\03-AR模型\gpt2')
print(model)
# prefixconfig
prefix_config = PrefixTuningConfig(task_type='CAUSAL_LM', num_virtual_tokens=6)

# 组合
model = get_peft_model(model=model,peft_config=prefix_config)
print(model)
model.print_trainable_parameters()