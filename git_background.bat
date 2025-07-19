@echo off
REM Background Git 操作批处理文件
REM 使用方法: git_background.bat [git命令]

if "%1"=="" (
    echo 使用方法: git_background.bat [git命令]
    echo 例如: git_background.bat status
    echo 例如: git_background.bat pull
    exit /b 1
)

echo 正在后台执行: git %*
start /b cmd /c "git %* > git_output.txt 2>&1"

echo 后台作业已启动
echo 结果将保存到 git_output.txt 文件中
echo 使用 'type git_output.txt' 查看结果 