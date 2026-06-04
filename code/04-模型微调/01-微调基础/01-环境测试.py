# 1. 导入必要的库
import torch

# 2. 检查PyTorch和CUDA
print(f"PyTorch版本: {torch.__version__}")
print(f"CUDA是否可用: {torch.cuda.is_available()}")

# 如果CUDA可用，进一步检查信息
if torch.cuda.is_available():
    print(f"当前GPU设备: {torch.cuda.get_device_name(0)}")
    print(f"CUDA版本: {torch.version.cuda}")