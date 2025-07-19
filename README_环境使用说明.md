# 机器学习环境使用说明

## 环境概述

已成功创建Python 3.13虚拟环境，包含以下机器学习包：

- **NumPy**: 2.3.1 - 数值计算库
- **Pandas**: 2.3.1 - 数据分析库
- **Scikit-learn**: 1.7.1 - 机器学习库
- **Matplotlib**: 3.10.3 - 绘图库
- **Seaborn**: 0.13.2 - 统计可视化库
- **Plotly**: 6.2.0 - 交互式绘图库
- **XGBoost**: 3.0.2 - 梯度提升库
- **Jupyter**: 1.1.1 - 交互式开发环境

## 使用方法

### 1. 激活虚拟环境

```bash
source ml_env/bin/activate
```

激活后，命令行提示符会显示 `(ml_env)` 前缀。

### 2. VS Code配置（推荐）

VS Code已经自动配置好了虚拟环境。如果需要在VS Code中使用：

1. **重启VS Code**
2. **按 `Ctrl+Shift+P` 打开命令面板**
3. **输入 `Python: Select Interpreter`**
4. **选择 `/workspace/ml_env/bin/python`**

或者直接使用工作区文件：
- 双击 `ml_workspace.code-workspace` 文件
- VS Code会自动使用正确的Python解释器

### 2. 启动Jupyter Notebook

方法一：使用启动脚本（推荐）
```bash
./start_jupyter.sh
```

方法二：手动启动
```bash
source ml_env/bin/activate
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

或者启动Jupyter Lab：

```bash
source ml_env/bin/activate
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

### 3. 在Jupyter中选择内核

启动Jupyter后，在新建notebook时选择 "Python (ML Environment)" 内核。

### 4. 退出虚拟环境

```bash
deactivate
```

## 验证环境

运行测试脚本验证环境是否正常：

```bash
source ml_env/bin/activate
python test_environment.py
```

## 常用命令

### 查看已安装的包
```bash
pip list
```

### 安装新包
```bash
pip install package_name
```

### 升级包
```bash
pip install --upgrade package_name
```

## 项目文件

- `ml_env/` - 虚拟环境目录
- `requirements.txt` - 依赖包列表
- `test_environment.py` - 环境测试脚本
- `setup_env.sh` - 环境设置脚本
- `start_jupyter.sh` - Jupyter启动脚本
- `ml_workspace.code-workspace` - VS Code工作区配置
- `.vscode/settings.json` - VS Code设置文件
- `select_interpreter.py` - VS Code解释器配置脚本

## 注意事项

1. 每次使用前都需要激活虚拟环境
2. 在Jupyter中工作时，确保选择了正确的内核
3. 如需添加新包，请在激活环境后使用pip安装

## 故障排除

### Jupyter内核问题

如果遇到 "Running cells with 'Python 3.13.3' requires the ipykernel package" 错误：

1. 确保虚拟环境已激活：
   ```bash
   source ml_env/bin/activate
   ```

2. 重新安装ipykernel：
   ```bash
   pip install ipykernel
   ```

3. 重新注册内核：
   ```bash
   python -m ipykernel install --user --name=ml_env --display-name="Python (ML Environment)"
   ```

4. 在Jupyter中选择正确的内核："Python (ML Environment)"

### 其他常见问题

1. 确保虚拟环境已激活
2. 检查Python版本：`python --version`
3. 重新安装包：`pip install -r requirements.txt`
4. 重新创建环境：删除`ml_env/`目录，重新运行`setup_env.sh`
5. 检查Jupyter内核：`jupyter kernelspec list` 