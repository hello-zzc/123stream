from langchain.prompts import ChatPromptTemplate #获取标题提示模版 
from langchain_deepseek import ChatDeepSeek #deepseek-chat模型





def catch_content(video_object, video_length, video_create, video_api_key): #参数分别为视频主题、视频长度、创造力和用户API密钥
    # 获取视频标题
    script_title = ChatPromptTemplate.from_messages(
        [
            ("human", "请为'{video_object}'这个主题的视频起一个吸引人的标题，要求有文采")
        ]
    )
     # 获取视频脚本内容
    script_content = ChatPromptTemplate.from_messages(
        [
            ("human",
             """你是一位小红书平台的短视频博主。根据以下标题和相关信息，写一个文本内容。
             视频标题：{title}，视频时长：{duration}分钟，生成的文本的长度尽量遵循视频时长的要求。
             要求开头抓住眼球，中间提供干货内容，结尾有惊喜，文本格式也请按照【开头、中间，结尾】分隔。
             整体内容的表达方式要尽量轻松有趣，吸引年轻人。
             你需要根据标题和时长来生成内容，内容要有趣且吸引人。
             """)
        ]
    )
    # 创建模型获取api和创造性
    model = ChatDeepSeek(api_key=video_api_key, temperature=video_create, model="deepseek-reasoner")


    # 获取标题和文本内容
    title_chain = script_title | model
    content_chain = script_content | model
    # 调用获取真正标题
    title = title_chain.invoke({"video_object": video_object}).content

    # 调用获取真正内容
    content = content_chain.invoke({"title": title, "duration": video_length}).content

    return title, content
