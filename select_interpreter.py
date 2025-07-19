#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VS Code Python解释器选择助手
"""

import os
import sys
import json
from pathlib import Path

def find_virtual_environments():
    """查找可用的虚拟环境"""
    workspace = Path.cwd()
    venv_paths = []
    
    # 查找常见的虚拟环境目录
    possible_venv_dirs = [
        workspace / "ml_env",
        workspace / "venv",
        workspace / "env",
        workspace / ".venv",
        workspace / "envs" / "ml_env",
    ]
    
    for venv_dir in possible_venv_dirs:
        if venv_dir.exists():
            python_path = venv_dir / "bin" / "python"
            if python_path.exists():
                venv_paths.append(str(python_path))
    
    return venv_paths

def create_vscode_config():
    """创建VS Code配置"""
    venv_paths = find_virtual_environments()
    
    if not venv_paths:
        print("❌ 未找到虚拟环境")
        return False
    
    # 选择第一个找到的虚拟环境
    selected_path = venv_paths[0]
    
    # 创建.vscode目录
    vscode_dir = Path(".vscode")
    vscode_dir.mkdir(exist_ok=True)
    
    # 创建settings.json
    settings = {
        "python.defaultInterpreterPath": selected_path,
        "python.terminal.activateEnvironment": True,
        "python.terminal.activateEnvInCurrentTerminal": True,
        "jupyter.interpreter.autoStartServer": True,
        "python.linting.enabled": True,
        "python.linting.pylintEnabled": False,
        "python.linting.flake8Enabled": True,
        "python.formatting.provider": "black",
        "python.sortImports.args": ["--profile", "black"],
        "editor.formatOnSave": True,
        "python.analysis.autoImportCompletions": True
    }
    
    settings_file = vscode_dir / "settings.json"
    with open(settings_file, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=4, ensure_ascii=False)
    
    print(f"✅ VS Code配置已创建")
    print(f"📁 配置文件: {settings_file}")
    print(f"🐍 Python解释器: {selected_path}")
    print("\n📋 使用说明:")
    print("1. 重启VS Code")
    print("2. 按 Ctrl+Shift+P 打开命令面板")
    print("3. 输入 'Python: Select Interpreter'")
    print("4. 选择我们的虚拟环境")
    
    return True

def main():
    """主函数"""
    print("🔍 查找虚拟环境...")
    
    if create_vscode_config():
        print("\n✅ 配置完成！")
    else:
        print("\n❌ 配置失败！")

if __name__ == "__main__":
    main() 