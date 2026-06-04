import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import gc

def clear_gpu_memory():
    """清理GPU内存"""
    gc.collect()
    torch.cuda.empty_cache()
def print_gpu_usage(description):
    """打印当前GPU使用情况"""
    if torch.cuda.is_available():
        allocated = torch.cuda.memory_allocated() / 1024 ** 3  # 转换为GB
        reserved = torch.cuda.memory_reserved() / 1024 ** 3  # 转换为GB
        print(f"{description}:")
        print(f"  已分配显存: {allocated:.2f} GB")
        print(f"  已保留显存: {reserved:.2f} GB")
        print("-" * 50)
    else:
        print("CUDA不可用")


def test_fp16_model():
    """测试FP16模型的显存使用"""
    print("=== 测试 FP16 模型 ===")
    clear_gpu_memory()
    print_gpu_usage("初始状态")

    # 记录加载前的显存
    start_allocated = torch.cuda.memory_allocated() / 1024 ** 3

    model = AutoModelForCausalLM.from_pretrained(
        "/gemini/pretrain/Qwen2-7b-instruct",
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True
    )
    tokenizer = AutoTokenizer.from_pretrained("/gemini/pretrain/Qwen2-7b-instruct", trust_remote_code=True)

    print_gpu_usage("模型加载后")

    # 记录推理前的显存
    pre_inference_memory = torch.cuda.memory_allocated() / 1024 ** 3

    # 进行推理测试
    messages = [{"role": "user", "content": "你好，请介绍一下你自己。"}]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True
        )

    print_gpu_usage("推理过程中")

    # 计算模型本身占用的显存（近似值）
    model_memory = pre_inference_memory - start_allocated
    print(f"模型参数大致占用: {model_memory:.2f} GB")

    del model, tokenizer, inputs, outputs
    clear_gpu_memory()


def test_4bit_model():
    """测试量化模型的显存使用"""
    print("\n=== 测试 4-bit 量化模型 ===")
    clear_gpu_memory()
    print_gpu_usage("初始状态")

    # 记录加载前的显存
    start_allocated = torch.cuda.memory_allocated() / 1024 ** 3

    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )

    model = AutoModelForCausalLM.from_pretrained(
        "/gemini/pretrain/Qwen2-7b-instruct",
        quantization_config=quantization_config,
        device_map="auto",
        trust_remote_code=True
    )
    tokenizer = AutoTokenizer.from_pretrained("/gemini/pretrain/Qwen2-7b-instruct", trust_remote_code=True)

    print_gpu_usage("模型加载后")

    # 记录推理前的显存
    pre_inference_memory = torch.cuda.memory_allocated() / 1024 ** 3

    # 进行推理测试
    messages = [{"role": "user", "content": "你好，请介绍一下你自己。"}]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True
        )

    print_gpu_usage("推理过程中")

    # 计算模型本身占用的显存（近似值）
    model_memory = pre_inference_memory - start_allocated
    print(f"模型参数大致占用: {model_memory:.2f} GB")

    del model, tokenizer, inputs, outputs
    clear_gpu_memory()

def test_8bit_model():
    """测试量化模型的显存使用"""
    print("\n=== 测试 8-bit 量化模型 ===")
    clear_gpu_memory()
    print_gpu_usage("初始状态")

    # 记录加载前的显存
    start_allocated = torch.cuda.memory_allocated() / 1024 ** 3

    quantization_config= BitsAndBytesConfig(
        load_in_8bit=True,  # 启用8-bit量化
        llm_int8_enable_fp32_cpu_offload=True,  # 允许CPU卸载
        llm_int8_threshold=6.0,  # 异常值阈值
    )

    model = AutoModelForCausalLM.from_pretrained(
        "/gemini/pretrain/Qwen2-7b-instruct",
        quantization_config=quantization_config,
        device_map="auto",
        trust_remote_code=True
    )
    tokenizer = AutoTokenizer.from_pretrained("/gemini/pretrain/Qwen2-7b-instruct", trust_remote_code=True)

    print_gpu_usage("模型加载后")

    # 记录推理前的显存
    pre_inference_memory = torch.cuda.memory_allocated() / 1024 ** 3

    # 进行推理测试
    messages = [{"role": "user", "content": "你好，请介绍一下你自己。"}]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True
        )

    print_gpu_usage("推理过程中")

    # 计算模型本身占用的显存（近似值）
    model_memory = pre_inference_memory - start_allocated
    print(f"模型参数大致占用: {model_memory:.2f} GB")

    del model, tokenizer, inputs, outputs
    clear_gpu_memory()

# 运行测试
if __name__ == "__main__":
    print("选择要运行的测试:")
    print("1 - FP16模型")
    print("2 - 8-bit量化模型")
    print("3 - 4-bit量化模型")

    choice = input("请输入选择 (1/2/3): ").strip()

    if choice == "1":
        test_fp16_model()
    elif choice == "2":
        test_8bit_model()
    elif choice == "3":
        test_4bit_model()
    else:
        print("无效选择")