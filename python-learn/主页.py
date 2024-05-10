# import streamlit as st
# st.title("  ")
# st.title("  ")
# st.title("  ")
# st.title("  ")
# st.title("  ")
# st.title("  ")
# st.title("饱和蒸汽p-t关系虚拟仿真实验")


# # streamlit run 主页.py   CTRL c




import streamlit as st
import pandas as pd
import math
import time
import matplotlib.pyplot as plt
# ------------------------------------------------------------------------------------------------


# streamlit run 主页.py   CTRL c

# 导入图片
from PIL import Image

# 打开图像文件
image = Image.open('python-learn/010001.png')
# 使用st.image函数展示图像，调整宽度
st.image(image, caption='仪器', width=400)
# 分割线

