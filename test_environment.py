#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试机器学习环境
"""

import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import plotly
import plotly.express as px
import plotly.graph_objects as go

def test_environment():
    """测试所有机器学习包是否正常工作"""
    print("=" * 50)
    print("机器学习环境测试")
    print("=" * 50)
    
    # 测试NumPy
    print("✓ NumPy版本:", np.__version__)
    arr = np.array([1, 2, 3, 4, 5])
    print("✓ NumPy数组:", arr)
    
    # 测试Pandas
    print("✓ Pandas版本:", pd.__version__)
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': ['a', 'b', 'c', 'd', 'e']
    })
    print("✓ Pandas DataFrame:")
    print(df)
    
    # 测试Scikit-learn
    import sklearn
    print("✓ Scikit-learn版本:", sklearn.__version__)
    
    # 测试Matplotlib
    print("✓ Matplotlib版本:", matplotlib.__version__)
    
    # 测试Seaborn
    print("✓ Seaborn版本:", sns.__version__)
    
    # 测试Plotly
    print("✓ Plotly版本:", plotly.__version__)
    
    # 简单机器学习示例
    print("\n" + "=" * 30)
    print("机器学习示例")
    print("=" * 30)
    
    # 加载iris数据集
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    
    # 分割数据
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 训练模型
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    
    # 预测
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"✓ 逻辑回归模型准确率: {accuracy:.4f}")
    
    print("\n" + "=" * 50)
    print("✓ 所有测试通过！环境设置成功！")
    print("=" * 50)
    
    return True

if __name__ == "__main__":
    try:
        test_environment()
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        sys.exit(1) 