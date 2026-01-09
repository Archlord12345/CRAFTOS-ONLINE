#!/usr/bin/env python3
import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QTextEdit, QLabel, QFrame
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QPalette, QColor

class CommandThread(QThread):
    output = pyqtSignal(str)
    
    def __init__(self, command):
        super().__init__()
        self.command = command
    
    def run(self):
        try:
            result = subprocess.run(self.command, shell=True, capture_output=True, text=True)
            if result.stdout:
                self.output.emit(result.stdout)
            if result.stderr:
                self.output.emit(f"Error: {result.stderr}")
        except Exception as e:
            self.output.emit(f"Exception: {str(e)}")

class NeonOSKDE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🚀 NEON OS TOON EDITION - KDE Interface")
        self.setGeometry(100, 100, 1200, 800)
        
        # Thème NEON
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a2e;
            }
            QLabel {
                color: #ff00ff;
                font-family: 'Courier New', monospace;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #00ffff;
                color: #000000;
                border: 2px solid #ff00ff;
                padding: 10px;
                font-family: 'Courier New', monospace;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #ff00ff;
                color: #00ffff;
            }
            QTextEdit {
                background-color: #0f0f23;
                color: #00ff00;
                border: 2px solid #00ffff;
                font-family: 'Courier New', monospace;
                font-size: 12px;
            }
            QFrame {
                background-color: #16213e;
                border: 2px solid #00ffff;
                border-radius: 10px;
            }
        """)
        
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Header
        header = QLabel("🚀 NEON OS TOON EDITION - KDE Interface")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)
        
        # Info royaume
        realm_info = QLabel("📍 Current Realm: OVERWORLD")
        realm_info.setAlignment(Qt.AlignCenter)
        realm_info.setStyleSheet("color: #ffff00;")
        main_layout.addWidget(realm_info)
        
        # Zone des royaumes
        realms_frame = QFrame()
        realms_layout = QHBoxLayout()
        realms_frame.setLayout(realms_layout)
        
        # Boutons des royaumes
        realms = ["OVERWORLD", "NETHER", "THE_END"]
        for realm in realms:
            btn = QPushButton(f"🌍 {realm}")
            btn.clicked.connect(lambda checked, r=realm: self.switch_realm(r))
            realms_layout.addWidget(btn)
        
        main_layout.addWidget(realms_frame)
        
        # Zone Toon Realms
        toon_frame = QFrame()
        toon_layout = QHBoxLayout()
        toon_frame.setLayout(toon_layout)
        
        toon_realms = ["SURVIVAL_V1", "TOON_CITY", "CREATIVE_X"]
        for realm in toon_realms:
            btn = QPushButton(f"🎮 {realm}")
            btn.clicked.connect(lambda checked, r=realm: self.enter_toon_realm(r))
            toon_layout.addWidget(btn)
        
        main_layout.addWidget(toon_frame)
        
        # Zone terminal
        terminal_frame = QFrame()
        terminal_layout = QVBoxLayout()
        terminal_frame.setLayout(terminal_layout)
        
        terminal_label = QLabel("💻 TERMINAL")
        terminal_layout.addWidget(terminal_label)
        
        # Terminal output
        self.terminal = QTextEdit()
        self.terminal.setPlainText("🏆 TOON ACHIEVEMENT!\nSuccessfully entered the Toon Zone.\n\nWelcome to NEON OS KDE Interface!\n\nAvailable commands:\n- help: Show help\n- realms: Show realms\n- tools: Show system tools\n- Any Linux command\n\nType your command below:")
        self.terminal.setReadOnly(True)
        terminal_layout.addWidget(self.terminal)
        
        # Zone de commande
        command_layout = QHBoxLayout()
        
        self.command_input = QTextEdit()
        self.command_input.setMaximumHeight(40)
        self.command_input.setPlaceholderText("Enter Linux command...")
        command_layout.addWidget(self.command_input)
        
        execute_btn = QPushButton("🚀 EXECUTE")
        execute_btn.clicked.connect(self.execute_command)
        command_layout.addWidget(execute_btn)
        
        terminal_layout.addLayout(command_layout)
        main_layout.addWidget(terminal_frame)
        
        # Zone outils système
        tools_frame = QFrame()
        tools_layout = QHBoxLayout()
        tools_frame.setLayout(tools_layout)
        
        tools = ["🗑️ Recycle Bin", "📁 Documents", "🔧 System Tools"]
        for tool in tools:
            btn = QPushButton(tool)
            btn.clicked.connect(lambda checked, t=tool: self.open_tool(t))
            tools_layout.addWidget(btn)
        
        main_layout.addWidget(tools_frame)
        
        # Achievement
        achievement_btn = QPushButton("🏆 SHOW ACHIEVEMENT")
        achievement_btn.clicked.connect(self.show_achievement)
        main_layout.addWidget(achievement_btn)
        
    def switch_realm(self, realm):
        self.terminal.append(f"\n🌍 Switching to {realm} realm...")
        self.terminal.append(f"✅ Successfully entered {realm}!")
        
    def enter_toon_realm(self, realm):
        self.terminal.append(f"\n🎮 Entering Toon Realm: {realm}")
        self.terminal.append(f"🎯 Loading {realm} environment...")
        
    def execute_command(self):
        command = self.command_input.toPlainText().strip()
        if not command:
            return
            
        self.terminal.append(f"\n$ {command}")
        
        # Exécuter la commande dans un thread séparé
        self.command_thread = CommandThread(command)
        self.command_thread.output.connect(self.append_output)
        self.command_thread.start()
        
        self.command_input.clear()
        
    def append_output(self, output):
        self.terminal.append(output)
        
    def open_tool(self, tool):
        self.terminal.append(f"\n🔧 Opening {tool}...")
        if "Documents" in tool:
            self.terminal.append("📁 /home/neonuser/Documents contents:")
            self.command_thread = CommandThread("ls -la /home/neonuser/Documents")
            self.command_thread.output.connect(self.append_output)
            self.command_thread.start()
        elif "System Tools" in tool:
            self.terminal.append("🔧 System Tools available:")
            self.terminal.append("- htop: Process monitor")
            self.terminal.append("- nano: Text editor")
            self.terminal.append("- firefox: Web browser")
        else:
            self.terminal.append("🗑️ Recycle Bin opened")
            
    def show_achievement(self):
        self.terminal.append("\n🏆 TOON ACHIEVEMENT!")
        self.terminal.append("Successfully entered the Toon Zone.")
        self.terminal.append("🎉 You are now a NEON OS master!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NeonOSKDE()
    window.show()
    sys.exit(app.exec_())
