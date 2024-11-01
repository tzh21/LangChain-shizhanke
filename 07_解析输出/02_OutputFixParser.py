""" 
本文件是【输出解析：用OutputParser生成鲜花推荐列表】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388070987826364450
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
# 导入所需要的库和模块
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

# 使用Pydantic创建一个数据格式，表示花
class Flower(BaseModel):
    name: str = Field(description="name of a flower")
    colors: List[str] = Field(description="the colors of this flower")


# 定义一个用于获取某种花的颜色列表的查询
flower_query = "Generate the charaters for a random flower."

# 定义一个格式不正确的输出
misformatted = "{'name': '康乃馨', 'colors': ['粉红色','白色','红色','紫色','黄色']}"

# 创建一个用于解析输出的Pydantic解析器，此处希望解析为Flower格式
parser = PydanticOutputParser(pydantic_object=Flower)
# 使用Pydantic解析器解析不正确的输出
# parser.parse(misformatted) # 这行代码会出错

# 从langchain库导入所需的模块
from langchain.output_parsers import OutputFixingParser
from langchain_openai import ChatOpenAI

# 设置OpenAI API密钥
import os

# os.environ["OPENAI_API_KEY"] = 'Your OpenAI API Key'

# 使用OutputFixingParser创建一个新的解析器，该解析器能够纠正格式不正确的输出
new_parser = OutputFixingParser.from_llm(
    parser=parser,
    llm=ChatOpenAI(
        model=os.environ.get("LLM_MODELEND"),
    ),
)

# 使用新的解析器解析不正确的输出
result = new_parser.parse(misformatted)  # 错误被自动修正
print(result)  # 打印解析后的输出结果
