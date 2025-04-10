import numpy as np

# 加载 .npz 文件
file_path = 'data/PEMSD4/train.npz'  # 替换为你的文件路径
data = np.load(file_path)

# 查看文件中包含的数组名称
print("文件中的数组名称:", data.files)

# 遍历并打印每个数组的形状和内容（可选）
for array_name in data.files:
    array = data[array_name]
    print(f"数组名称: {array_name}")
    print(f"形状: {array.shape}")
    print(f"数据类型: {array.dtype}")
    # print(f"前几行数据:\n{array[:5]}")  # 打印前几行数据作为预览
    print("-" * 40)

# 关闭文件
data.close()