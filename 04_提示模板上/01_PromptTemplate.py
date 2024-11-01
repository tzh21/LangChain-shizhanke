"""
本文件是【提示工程（上）：用少样本FewShotTemplate和ExampleSelector创建应景文案】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388069971579895818
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""

from langchain import PromptTemplate

template = """\
你是业务咨询顾问。
你给一个销售{product}的电商公司，起一个好的名字？
"""
prompt = PromptTemplate.from_template(template)

print(prompt.format(product="鲜花"))

prompt = PromptTemplate(
    input_variables=["product", "market"],
    template="你是业务咨询顾问。对于一个面向{market}市场的，专注于销售{product}的公司，你会推荐哪个名字？",
)
print(prompt.format(product="鲜花", market="高端"))
