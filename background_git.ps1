# Background Git 操作脚本
# 使用方法: .\background_git.ps1 [命令]

param(
    [Parameter(Mandatory=$true)]
    [string]$GitCommand
)

# 获取当前目录
$CurrentDir = Get-Location

# 创建后台作业
$Job = Start-Job -ScriptBlock {
    param($Command, $WorkingDir)
    Set-Location $WorkingDir
    Invoke-Expression $Command
} -ArgumentList $GitCommand, $CurrentDir.Path

Write-Host "后台作业已启动，作业ID: $($Job.Id)"
Write-Host "使用 'Get-Job' 查看作业状态"
Write-Host "使用 'Receive-Job -Id $($Job.Id)' 查看结果"
Write-Host "使用 'Remove-Job -Id $($Job.Id)' 清理作业"

return $Job 