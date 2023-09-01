from PIL import Image
import numpy as np
import json

# 打开灰度图像
image_path = "map.png"
image = Image.open(image_path).convert("L")

# 将图像转换为NumPy数组
gray_values = np.array(image)

# 获取图像宽度和高度
image_width, image_height = image.size

# 定义高度范围
min_height = 0
max_height = 10

# 定义 x 和 y 的范围
min_x = 0.000001
max_x = 0.999999
min_y = 0.000001
max_y = 0.999999

# 生成每个位置的高度信息
height_data = []

for y in range(image_height):
    for x in range(image_width):
        gray_value = gray_values[y, x]
        height = min_height + (gray_value / 255) * (max_height - min_height)

        # 映射 x 和 y 到指定范围
        mapped_x = min_x + (x / (image_width - 1)) * (max_x - min_x)
        mapped_y = min_y + (y / (image_height - 1)) * (max_y - min_y)

        # 格式化 x 和 y 的值为字符串，保留小数点后 6 位
        formatted_x = "{:.6f}".format(mapped_x)
        formatted_y = "{:.6f}".format(mapped_y)

        height_info = {"x": formatted_x, "y": formatted_y, "high": height}
        height_data.append(height_info)

# 将高度数据存储到JSON文件
with open("map.json", "w") as json_file:
    json.dump(height_data, json_file, indent=2)  # 使用 indent 使 JSON 文件更易读



