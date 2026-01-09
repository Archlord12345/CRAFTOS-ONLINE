#!/bin/bash

# NEON OS Welcome Script
echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                    NEON OS TOON EDITION                      ║"
echo "║                 Linux Container Environment                   ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Display system info
echo "🖥️  SYSTEM INFORMATION:"
echo "   Kernel: $(uname -r)"
echo "   Container: $(hostname)"
echo "   User: $(whoami)"
echo "   Date: $(date)"
echo ""

# Show achievement
echo "🏆 TOON ACHIEVEMENT!"
echo "   Successfully entered the Toon Zone."
echo ""

# Start the main NEON OS interface
python3 neon_os.py
