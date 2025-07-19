#!/bin/bash

# 创建Python虚拟环境
echo "正在创建Python虚拟环境..."
python3 -m venv ml_env

# 激活虚拟环境
echo "正在激活虚拟环境..."
source ml_env/bin/activate

# 升级pip
echo "正在升级pip..."
pip install --upgrade pip

# 安装所需的包
echo "正在安装机器学习包..."
pip install -r requirements.txt

# 安装Jupyter内核
echo "正在安装Jupyter内核..."
python -m ipykernel install --user --name=ml_env --display-name="Python (ML Environment)"

echo "虚拟环境设置完成！"
echo "使用方法："
echo "1. 激活环境：source ml_env/bin/activate"
echo "2. 启动Jupyter：jupyter notebook"
echo "3. 退出环境：deactivate" 