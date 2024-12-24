from flask import Flask, render_template, request
from oscopilot import FridayAgent, ToolManager
from oscopilot import FridayExecutor, FridayPlanner, FridayRetriever
from oscopilot.utils import setup_config, setup_pre_run

app = Flask(__name__)

# 存储用户输入和输出的列表
chat_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history

    if request.method == "POST":
        user_input = request.form["user_input"]  # 获取用户输入

        # 将用户输入作为 query 传入 FridayAgent
        result = run_friday_agent(user_input)

        # 保存输入和输出到聊天记录
        chat_history.append({"input": user_input, "output": result})

    return render_template("index.html", chat_history=chat_history)

def run_friday_agent(user_query):
    """
    将用户输入传递给 FridayAgent 并返回结果
    """
    # 配置 FridayAgent 参数
    args = setup_config()
    args.query = user_query  # 设置 query 为用户输入

    # 初始化任务
    task = setup_pre_run(args)

    # 初始化并运行 FridayAgent
    agent = FridayAgent(
        FridayPlanner, FridayRetriever, FridayExecutor, ToolManager, config=args
    )
    # result = agent.run(task=task)  # 运行任务并获取结果
    agent.run(task=task)

    # return result  # 返回结果
    return 'The operation has been successfully completed. \nPlease check the database or folder </home/hjh/nlp/os/OS-Copilot/ppt_making/result>'

if __name__ == "__main__":
    app.run(debug=True)
