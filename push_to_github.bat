@echo off
chcp 65001 > nul
echo =========================================
echo 正在推送到 GitHub 仓库...
echo =========================================
echo.

cd /d "%~dp0"

echo [1/6] 检查是否已初始化 Git 仓库...
if not exist ".git" (
    echo Git 仓库未初始化，正在初始化...
    git init
) else (
    echo Git 仓库已存在。
)
echo.

echo [2/6] 添加所有更改...
git add .
echo.

echo [3/6] 提交更改...
git commit -m "删除广告占位符，保留Google AdSense代码"
if errorlevel 1 (
    echo.
    echo 注意：可能没有新的更改需要提交，或者已存在提交。
)
echo.

echo [4/6] 检查远程仓库配置...
git remote -v > nul 2>&1
if errorlevel 1 (
    echo 远程仓库未配置，正在添加...
    git remote add origin https://github.com/KNGLOKIKO/skill-hub.git
) else (
    echo 远程仓库已配置。
)
echo.

echo [5/6] 检查分支名称...
git branch -M master
echo.

echo [6/6] 推送到 GitHub...
echo 正在推送到 https://github.com/KNGLOKIKO/skill-hub.git 的 master 分支...
echo.
git push -u origin master

echo.
echo =========================================
echo 操作完成！
echo 如果推送失败，请检查：
echo 1. 您是否已登录 GitHub 账户
echo 2. 您是否有仓库的写入权限
echo 3. 网络连接是否正常
echo =========================================
echo.
pause
