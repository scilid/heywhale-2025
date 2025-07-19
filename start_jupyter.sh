#!/bin/bash

echo "启动机器学习环境..."

# 激活虚拟环境
source ml_env/bin/activate

# 检查内核
echo "检查Jupyter内核..."
jupyter kernelspec list

# 启动Jupyter Notebook
echo "启动Jupyter Notebook..."
echo "请在浏览器中访问: http://localhost:8888"
echo "使用token登录，token会显示在下方"
echo ""
echo "按 Ctrl+C 停止服务器"
echo ""

jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root 