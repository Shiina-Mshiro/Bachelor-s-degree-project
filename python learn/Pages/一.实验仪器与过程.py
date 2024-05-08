import streamlit as st



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
    image = Image.open('数据记录示例.png')
    st.image(image, caption='数据记录示例', width=600)
    st.text("（3）Ctrl+Enter输出图表。（若无法输出，请检查第（3）步是否为英文逗号）")
    st.warning('注意：本仿真实验大气压力采用101.325KPa')


st.text("")
st.text("")
st.text("")
st.text("")
