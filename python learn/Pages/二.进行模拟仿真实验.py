import streamlit as st
import pandas as pd
import math
import time
import matplotlib.pyplot as plt
import markdown

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
    #data = pd.DataFrame([x.split(',') for x in user_input.split('\n')], columns=['p', 't']).astype(float)
    try:
        # 将用户输入的数据转换为数据框
        data = pd.DataFrame([x.split(',') for x in user_input.split('\n')], columns=['p', 't']).astype(float)
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

# ------------------------------------------------------------------------------------------------
# 0.1,99
# 0.2,120
# 0.3,133
# 0.4,143
# 0.5,151
# 0.6,158
# 0.7,164
# 0.8,170