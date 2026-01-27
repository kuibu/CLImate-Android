#!/bin/bash
# CLImate-Android Quick Start Script

echo "🐍 CLImate-Android - Quick Start"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found, please install:"
    echo "   pkg install python (Termux)"
    echo "   or"
    echo "   brew install python (macOS)"
    exit 1
fi

echo "✅ Python3: $(python3 --version)"

# Check dependencies
echo ""
echo "📦 Checking dependencies..."

if ! python3 -c "import anthropic" &> /dev/null; then
    echo "⚠️  anthropic not installed, installing..."
    pip3 install -r requirements.txt
else
    echo "✅ Dependencies installed"
fi

# Check configuration
if [ ! -f ~/.climate-android/config.json ]; then
    echo ""
    echo "⚙️  First run, configuration needed..."
    python3 agent.py --setup
fi

# Launch
echo ""
echo "🚀 Starting Agent..."
echo ""
python3 agent.py
