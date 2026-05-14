Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "正在推送到 GitHub 仓库..." -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

Set-Location $PSScriptRoot

Write-Host "[1/6] 检查是否已初始化 Git 仓库..." -ForegroundColor Yellow
if (-not (Test-Path ".git")) {
    Write-Host "Git 仓库未初始化，正在初始化..." -ForegroundColor Green
    git init
} else {
    Write-Host "Git 仓库已存在。" -ForegroundColor Green
}
Write-Host ""

Write-Host "[2/6] 添加所有更改..." -ForegroundColor Yellow
git add .
Write-Host ""

Write-Host "[3/6] 提交更改..." -ForegroundColor Yellow
git commit -m "删除广告占位符，保留Google AdSense代码"
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "注意：可能没有新的更改需要提交，或者已存在提交。" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "[4/6] 检查远程仓库配置..." -ForegroundColor Yellow
try {
    $remoteOutput = git remote -v 2>&1
    if ($remoteOutput -match "origin") {
        Write-Host "远程仓库已配置。" -ForegroundColor Green
    } else {
        Write-Host "远程仓库未配置，正在添加..." -ForegroundColor Green
        git remote add origin https://github.com/KNGLOKIKO/skill-hub.git
    }
} catch {
    Write-Host "远程仓库未配置，正在添加..." -ForegroundColor Green
    git remote add origin https://github.com/KNGLOKIKO/skill-hub.git
}
Write-Host ""

Write-Host "[5/6] 检查分支名称..." -ForegroundColor Yellow
git branch -M master
Write-Host ""

Write-Host "[6/6] 推送到 GitHub..." -ForegroundColor Yellow
Write-Host "正在推送到 https://github.com/KNGLOKIKO/skill-hub.git 的 master 分支..." -ForegroundColor Green
Write-Host ""
git push -u origin master

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "操作完成！" -ForegroundColor Cyan
Write-Host "如果推送失败，请检查：" -ForegroundColor Yellow
Write-Host "1. 您是否已登录 GitHub 账户" -ForegroundColor White
Write-Host "2. 您是否有仓库的写入权限" -ForegroundColor White
Write-Host "3. 网络连接是否正常" -ForegroundColor White
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""
Read-Host "按 Enter 键退出"
