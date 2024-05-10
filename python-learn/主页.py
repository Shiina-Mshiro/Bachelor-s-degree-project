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
code_page1 = """
st.title("  ")
st.title("  ")
st.title("  ")
st.title("  ")
st.title("  ")
st.title("  ")
st.title("饱和蒸汽p-t关系模拟仿真实验")
"""

# streamlit run 主页.py   CTRL c

# ------------------------------------------------------------------------------------------------
code_page2 = """
# 标题
st.header("实验仪器")
# 分割线
st.divider()
# 导入图片
from PIL import Image

# 打开图像文件
image = Image.open('2.jpg')
# 使用st.image函数展示图像，调整宽度
st.image(image, caption='仪器', width=400)
# 分割线
st.divider()
#元件
st.subheader("仪器主要元件")
st.text("1、压力表 2、排气阀 3、缓冲器 4、可视玻璃及蒸汽发生器 ")
st.text(" 5、电源开关 6、电功率调节 7、温度计 8、可控数显温度仪")
# 分割线
st.divider()

st.header(" ")
st.header(" ")
st.header(" ")
st.header(" ")
st.header("实验原理及步骤 ")

# 创建一个下拉框，有两个选项
option = st.selectbox(
    '请选择一个选项',
    ('实际实验步骤', '虚拟仿真实验步骤'))

# 根据用户选择的选项，显示不同的文字内容
if option == '实际实验步骤':
    # st.write('实际实验步骤')&nbsp;&nbsp;&nbsp;&nbsp;
    # 分割线
    st.divider()
    #  实验过程
    st.write("（1）熟悉实验装置及使用仪表的工作原理和性能及使用方法。")
    st.write("")
    st.write("（2）将调压旋钮左旋到起始点，然后接通电源。")
    st.write("")
    st.write("（3）调节调压旋钮并缓慢逐渐加大电压至 40v，使温度升高，半小时后，再逐步将输出电压调至")
    st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 200～220V，待蒸汽压力升至第一设定压力值时，将电压降至 20～50V 左右（参考值），由于")
    st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;热惯性，压力将会继续上升，待压力达到设定值时，再适当调整（提高或降低），使工况稳")
    st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;定（压力和温度基本保持不变）。此时，迅速记录下水蒸气的压力和温度。重复上述实验，在")
    st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;0～0.8MPa(表压)范围内，取不少于 6 个压力值，顺序分别进行测试,且实验点应尽量分布均匀。 ")
    st.write("")
    st.write("（4）实验完毕后，将电压旋回零位，并断开电源。 ")
    st.write("")
    st.write("（5）记录室温和大气压力。")
else:
    # 分割线
    st.divider()
    st.text("（1）点击开始按钮后，实验开始，播放实验视频，并显示实验数据（该压力为表压）；")
    st.text("（2）在实验过程中请记录几组实验数据，包括压力和温度值")
    st.text("（3）将你记录的数据填入数据框，每行一组数据，用“英文逗号”分隔 压力p 和 温度t 值；")
    image = Image.open('3.png')
    st.image(image, caption='数据记录示例', width=600)
    st.text("（3）Ctrl+Enter输出图表。（若无法输出，请检查第（3）步是否为英文逗号）")
    st.warning('注意：本仿真实验大气压力采用101.325KPa')


st.text("")
st.text("")
st.text("")
st.text("")

"""
# ------------------------------------------------------------------------------------------------
code_page3 = """


# ------------------------------------------------------------------------------------------------
# 创建开始按钮
start_button = st.button('开始')

# 当点击开始按钮时，运行两个程序
if start_button:
    dongtu = st.empty()
    dongtu.image('01000.gif', width=300)

    def main():
        pressure = st.empty()  # 表压
        temperature = st.empty()
        T = 0
        while T < 41.0:   # 0.001-0.14     6-109
            T += 1
            p = 0.00000283*T*T*T - 0.0000541*T*T + 0.000774*T + 0.0000451  # 表压
            t = (3876.659 / (16.37379 - math.log(p * 1000)) - 229.72)
            pressure.text(f'压力: {round(p - 0.101325, 6)} Mpa')  # round 保留小数
            temperature.text(f'温度: {round(t, 2)} 摄氏度')
            time.sleep(1)

        while T < 87:   # 0.16-1.9      113-209
            T += 1
            p = 0.00000517*T*T*T - 0.000245*T*T + 0.00468*T + 0.000531
            t = (3876.659 / (16.37379 - math.log(p*1000)) - 229.72)
            pressure.text(f'压力: {round(p - 0.101325, 6)} Mpa')
            temperature.text(f'温度: {round(t, 2)} 摄氏度')
            time.sleep(1)

        while T < 189:   # 2.0-22    212-373
            T += 1
            p = -0.00000144 * T * T * T + 0.00156 * T * T - 0.16 * T + 5.07
            t = (5204.082 / (17.65216 - math.log(p * 1000)) - 305.64)
            pressure.text(f'压力: {round(p - 0.101325, 6)} Mpa')
            temperature.text(f'温度: {round(t, 2)} 摄氏度')
            time.sleep(1)
            if T >= 189:
                dongtu.image('010001.png', width=300)
                pressure.text(f'压力: {21.962675} Mpa')
                temperature.text(f'温度: {373.99} 摄氏度')
                st.warning('已达到临界状态！实验停止')

    if __name__ == "__main__":
        main()
# ------------------------------------------------------------------------------------------------

# 创建一个空的数据框
data = pd.DataFrame()

# 创建一个表格，让用户输入数据
user_input = st.text_area("请记录你的数据，每行一组数据，用英文逗号分隔 压力p 和 温度t  值,Ctrl+Enter输出图表")

# 检查用户是否已输入数据
if user_input:
    # 将用户输入的数据转换为数据框
    try:
        # 将用户输入的数据转换为数据框
        data = pd.DataFrame([x.split(',') for x in user_input.split('\\n')], columns=['p', 't']).astype(float)
    except ValueError:
        st.error('数据格式错误，请确保每行数据都是由两个用英文逗号分隔的数字。')
    # 显示数据框
    st.table(data)

    st.write("分别将实验曲线绘制在普通坐标系与双对数坐标系上：")
    # 创建一个折线图
    fig, ax = plt.subplots()
    ax.plot(data['p'], data['t'])

    # 添加数据点标签
    for i in range(len(data['p'])):
        ax.annotate(f"({data['p'][i]}, {data['t'][i]})", (data['p'][i], data['t'][i]))

    ax.set_xlabel('P/Mpa')
    ax.set_ylabel('t/℃')
    ax.set_title('P-t relationship graph')
# -------------------------------------------------------------
    # 显示双对数坐标的折线图
    st.pyplot(fig)

    fig, ax = plt.subplots()
    ax.loglog(data['p'], data['t'])

    # 添加数据点标签
    for i in range(len(data['p'])):
        ax.annotate(f"({data['p'][i]}, {data['t'][i]})", (data['p'][i], data['t'][i]))

    ax.set_xlabel('P/Mpa')
    ax.set_ylabel('t/℃')
    ax.set_title('double logarithmic coordinate')

    # 显示折线图
    st.pyplot(fig)
    st.write("将实验曲线绘制在双对数坐标系上，则基本呈一条直线，故饱和水蒸汽压力和温度的关系式可近似整理成下列经验公式：t=100$\sqrt[4]P$")


# ------------------------------------------------------------------------------------------------

data_df = pd.DataFrame(
            {
                "apps": [
                    "https://www.bilibili.com/video/BV1Sa4y1L78v/?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click",
                ],
            }
        )
# 展示视频链接并可跳转
st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.LinkColumn(
        "视频来源链接",
        help="The top trending Streamlit apps",
        validate="^https://[a-z]+\.streamlit\.app$",
        max_chars=100,
        )
    },
    hide_index=True,
)

"""

# ------------------------------------------------------------------------------------------------
pages = {
    "主页": [code_page1],
    "实验仪器及过程": [code_page2],
    "进行模拟仿真实验": [code_page3],
}
selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))
exec(pages[selected_page][0])
