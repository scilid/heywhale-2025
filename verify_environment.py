#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
环境验证脚本
"""

import sys
import os
from pathlib import Path

def check_python_path():
    """检查Python路径"""
    print("🔍 检查Python解释器...")
    print(f"当前Python路径: {sys.executable}")
    print(f"Python版本: {sys.version}")
    
    # 检查是否在虚拟环境中
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ 正在使用虚拟环境")
    else:
        print("⚠️  未检测到虚拟环境")
    
    return True

def check_installed_packages():
    """检查已安装的包"""
    print("\n📦 检查已安装的包...")
    
    required_packages = [
        'numpy', 'pandas', 'sklearn', 'matplotlib', 
        'seaborn', 'plotly', 'xgboost', 'jupyter'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - 未安装")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  缺少包: {', '.join(missing_packages)}")
        print("请运行: pip install " + " ".join(missing_packages))
        return False
    else:
        print("\n✅ 所有必需的包都已安装")
        return True

def check_vscode_config():
    """检查VS Code配置"""
    print("\n⚙️  检查VS Code配置...")
    
    vscode_dir = Path(".vscode")
    settings_file = vscode_dir / "settings.json"
    
    if settings_file.exists():
        print("✅ VS Code配置文件存在")
        return True
    else:
        print("❌ VS Code配置文件不存在")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("环境验证")
    print("=" * 50)
    
    # 检查Python路径
    check_python_path()
    
    # 检查已安装的包
    packages_ok = check_installed_packages()
    
    # 检查VS Code配置
    vscode_ok = check_vscode_config()
    
    print("\n" + "=" * 50)
    if packages_ok and vscode_ok:
        print("✅ 环境验证通过！")
        print("\n📋 下一步:")
        print("1. 在VS Code中选择Python解释器")
        print("2. 运行Jupyter: ./start_jupyter.sh")
        print("3. 开始您的机器学习项目！")
    else:
        print("❌ 环境验证失败！")
        print("请检查上述问题并重新配置。")
    print("=" * 50)

if __name__ == "__main__":
    main() 