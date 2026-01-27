#!/bin/bash
# CLImate-Android 快速开始脚本

echo "🐍 CLImate-Android - 快速开始"
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 未找到 Python3，请先安装："
    echo "   pkg install python (Termux)"
    echo "   或"
    echo "   brew install python (macOS)"
    exit 1
fi

echo "✅ Python3: $(python3 --version)"

# 检查依赖
echo ""
echo "📦 检查依赖..."

if ! python3 -c "import anthropic" &> /dev/null; then
    echo "⚠️  未安装 anthropic，正在安装..."
    pip3 install -r requirements.txt
else
    echo "✅ 依赖已安装"
fi

# 检查配置
if [ ! -f ~/.climate-android/config.json ]; then
    echo ""
    echo "⚙️  首次运行，需要配置..."
    python3 agent.py --setup
fi

# 启动
echo ""
echo "🚀 启动 Agent..."
echo ""
python3 agent.py
