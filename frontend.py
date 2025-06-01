import streamlit as st #前端库
from backend import catch_content

st.title("📹 视频文本生成器")

with st.sidebar: #侧边栏
    deepseek_api_key = st.text_input("请输入Deepseek API密钥：", type="password")
    st.markdown("[获取Deepseek API密钥](https://platform.deepseek.com/api_keys)")

aim = st.text_input("✨ 请输入视频的主题")
video_length = st.number_input("⏱️ 请输入视频的时长（单位：分钟）", min_value=0.1, step=0.1)
creativity = st.slider("✨ 请输入视频脚本的创造力（数字小说明更严谨，数字大说明更多样）", min_value=0.0,
                       max_value=1.0, value=0.3, step=0.1) #必须都为小数
submit = st.button("生成文本")
# 检查输入
if submit and not deepseek_api_key:
    st.info("请输入你的Deepseeek API密钥")
    st.stop() #检查API密钥是否输入,若输入则不在执行后续代码
if submit and not aim:
    st.info("请输入视频的主题")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("视频长度需要大于或等于0.1")
    st.stop()
if submit:
    # 加载效果
    with st.spinner("AI正在思考中，请稍等..."): #只要以下代码未运行完，这st.spinner就会一直显示
        title, content = catch_content(aim, video_length, creativity, deepseek_api_key)
    st.success("视频文本已生成！")
    st.subheader("❤️‍🔥 标题：")
    st.write(title)
    st.subheader("⭐ 视频文本：")
    st.write(content)

