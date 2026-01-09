#!/usr/bin/env python3
import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon

class NeonOSTray(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        
        # Icône du système tray
        self.setIcon(QIcon.fromTheme("computer"))
        self.setToolTip("NEON OS TOON EDITION")
        
        # Menu contextuel
        menu = QMenu()
        
        # Actions
        terminal_action = QAction("🚀 Open NEON Terminal", self)
        terminal_action.triggered.connect(self.open_terminal)
        menu.addAction(terminal_action)
        
        realms_action = QAction("🌍 Realms Explorer", self)
        realms_action.triggered.connect(self.open_realms)
        menu.addAction(realms_action)
        
        tools_action = QAction("🔧 System Tools", self)
        tools_action.triggered.connect(self.open_tools)
        menu.addAction(tools_action)
        
        menu.addSeparator()
        
        achievement_action = QAction("🏆 Show Achievement", self)
        achievement_action.triggered.connect(self.show_achievement)
        menu.addAction(achievement_action)
        
        menu.addSeparator()
        
        quit_action = QAction("❌ Exit NEON OS", self)
        quit_action.triggered.connect(self.quit)
        menu.addAction(quit_action)
        
        self.setContextMenu(menu)
        
        # Message de bienvenue
        QTimer.singleShot(2000, self.show_welcome)
        
    def show_welcome(self):
        self.showMessage(
            "🚀 NEON OS TOON EDITION",
            "Successfully entered the Toon Zone!",
            QSystemTrayIcon.Information,
            3000
        )
        
    def open_terminal(self):
        subprocess.Popen(["python3", "/app/kde_launcher.py"])
        
    def open_realms(self):
        QMessageBox.information(
            None,
            "🌍 Realms Explorer",
            "Available Realms:\n\n"
            "• OVERWORLD - 🟢 Accessible\n"
            "• NETHER - 🟢 Accessible\n"
            "• THE_END - 🟢 Accessible\n\n"
            "Toon Realms:\n"
            "• SURVIVAL_V1 - Survival Mode\n"
            "• TOON_CITY - Creative Mode\n"
            "• CREATIVE_X - Experimental"
        )
        
    def open_tools(self):
        QMessageBox.information(
            None,
            "🔧 System Tools",
            "Available Tools:\n\n"
            "• 🗑️ Recycle Bin - File management\n"
            "• 📁 Documents - Document viewer\n"
            "• 🔧 System Tools - System utilities\n"
            "• 🌐 Firefox - Web browser\n"
            "• 📝 Nano - Text editor"
        )
        
    def show_achievement(self):
        self.showMessage(
            "🏆 TOON ACHIEVEMENT!",
            "Successfully entered the Toon Zone!",
            QSystemTrayIcon.Information,
            5000
        )
        
    def quit(self):
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    if not QSystemTrayIcon.isSystemTrayAvailable():
        print("❌ System tray is not available")
        sys.exit(1)
        
    tray = NeonOSTray()
    tray.show()
    
    sys.exit(app.exec_())
