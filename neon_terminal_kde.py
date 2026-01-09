#!/usr/bin/env python3
import subprocess
import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                            QWidget, QPushButton, QTextEdit, QLabel, QFrame, 
                            QLineEdit, QSplitter)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QFont, QPalette, QColor, QTextCursor

class CommandThread(QThread):
    output = pyqtSignal(str)
    finished = pyqtSignal()
    
    def __init__(self, command):
        super().__init__()
        self.command = command
    
    def run(self):
        try:
            process = subprocess.Popen(
                self.command, 
                shell=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    self.output.emit(output.rstrip())
                    
            # Capture stderr
            stderr = process.stderr.read()
            if stderr:
                self.output.emit(f"Error: {stderr}")
                
        except Exception as e:
            self.output.emit(f"Exception: {str(e)}")
            
        self.finished.emit()

class NeonTerminalKDE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🚀 NEON OS Terminal - KDE Edition")
        self.setGeometry(100, 100, 1000, 700)
        
        # Configuration du thème NEON
        self.setup_neon_theme()
        
        # Historique des commandes
        self.command_history = []
        self.history_index = -1
        
        # Initialiser l'interface
        self.init_ui()
        
    def setup_neon_theme(self):
        """Configurer le thème NEON pour KDE"""
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a2e;
                color: #ffffff;
            }
            QLabel {
                color: #ff00ff;
                font-family: 'Source Code Pro', 'Courier New', monospace;
                font-size: 14px;
                font-weight: bold;
                background-color: transparent;
            }
            QPushButton {
                background-color: #00ffff;
                color: #000000;
                border: 2px solid #ff00ff;
                padding: 8px 16px;
                font-family: 'Source Code Pro', monospace;
                font-weight: bold;
                border-radius: 6px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #ff00ff;
                color: #00ffff;
                border: 2px solid #00ffff;
            }
            QPushButton:pressed {
                background-color: #800080;
            }
            QTextEdit {
                background-color: #0f0f23;
                color: #00ff00;
                border: 2px solid #00ffff;
                font-family: 'Source Code Pro', 'Courier New', monospace;
                font-size: 12px;
                border-radius: 8px;
                padding: 5px;
            }
            QLineEdit {
                background-color: #16213e;
                color: #00ffff;
                border: 2px solid #ff00ff;
                font-family: 'Source Code Pro', 'Courier New', monospace;
                font-size: 12px;
                padding: 8px;
                border-radius: 6px;
            }
            QFrame {
                background-color: #16213e;
                border: 2px solid #00ffff;
                border-radius: 10px;
                padding: 10px;
            }
            QSplitter::handle {
                background-color: #ff00ff;
                width: 2px;
            }
        """)
        
    def init_ui(self):
        """Initialiser l'interface utilisateur"""
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal avec splitter
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Header
        header = QLabel("🚀 NEON OS TERMINAL - KDE PLASMA EDITION")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 18px; color: #00ffff; padding: 10px;")
        main_layout.addWidget(header)
        
        # Info système
        self.realm_label = QLabel("📍 Current Realm: OVERWORLD")
        self.realm_label.setAlignment(Qt.AlignCenter)
        self.realm_label.setStyleSheet("color: #ffff00; font-size: 14px;")
        main_layout.addWidget(self.realm_label)
        
        # Splitter pour terminal et outils
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)
        
        # Zone terminal (gauche)
        terminal_frame = QFrame()
        terminal_layout = QVBoxLayout()
        terminal_frame.setLayout(terminal_layout)
        
        terminal_header = QLabel("💻 TERMINAL OUTPUT")
        terminal_layout.addWidget(terminal_header)
        
        # Terminal output
        self.terminal_output = QTextEdit()
        self.terminal_output.setReadOnly(True)
        self.terminal_output.setPlainText(
            "🏆 TOON ACHIEVEMENT!\n"
            "Successfully entered the Toon Zone!\n\n"
            "🚀 Welcome to NEON OS KDE Terminal!\n\n"
            "Available commands:\n"
            "• help - Show NEON OS help\n"
            "• realms - Explore available realms\n"
            "• tools - Open system tools\n"
            "• cd <realm> - Change current realm\n"
            "• achievement - Show achievements\n"
            "• Any Linux command\n\n"
            "Ready for commands... 🎮"
        )
        terminal_layout.addWidget(self.terminal_output)
        
        # Zone de commande
        command_layout = QHBoxLayout()
        
        self.command_input = QLineEdit()
        self.command_input.setPlaceholderText("Enter command... (use ↑↓ for history)")
        self.command_input.returnPressed.connect(self.execute_command)
        command_layout.addWidget(self.command_input)
        
        execute_btn = QPushButton("🚀 EXECUTE")
        execute_btn.clicked.connect(self.execute_command)
        command_layout.addWidget(execute_btn)
        
        clear_btn = QPushButton("🗑️ CLEAR")
        clear_btn.clicked.connect(self.clear_terminal)
        command_layout.addWidget(clear_btn)
        
        terminal_layout.addLayout(command_layout)
        splitter.addWidget(terminal_frame)
        
        # Zone outils (droite)
        tools_frame = QFrame()
        tools_layout = QVBoxLayout()
        tools_frame.setLayout(tools_layout)
        
        tools_header = QLabel("🔧 QUICK TOOLS")
        tools_layout.addWidget(tools_header)
        
        # Boutons des royaumes
        realms_label = QLabel("🌍 REALMS")
        realms_label.setStyleSheet("color: #ffff00;")
        tools_layout.addWidget(realms_label)
        
        for realm in ["OVERWORLD", "NETHER", "THE_END"]:
            btn = QPushButton(f"🌍 {realm}")
            btn.clicked.connect(lambda checked, r=realm: self.switch_realm(r))
            tools_layout.addWidget(btn)
        
        # Toon Realms
        toon_label = QLabel("🎮 TOON REALMS")
        toon_label.setStyleSheet("color: #00ffff;")
        tools_layout.addWidget(toon_label)
        
        for realm in ["SURVIVAL_V1", "TOON_CITY", "CREATIVE_X"]:
            btn = QPushButton(f"🎮 {realm}")
            btn.clicked.connect(lambda checked, r=realm: self.enter_toon_realm(r))
            tools_layout.addWidget(btn)
        
        # Outils système
        tools_label = QLabel("🔧 SYSTEM TOOLS")
        tools_label.setStyleSheet("color: #ff00ff;")
        tools_layout.addWidget(tools_label)
        
        tools = ["🗑️ Recycle Bin", "📁 Documents", "🌐 Web Browser", "🔧 System Info"]
        for tool in tools:
            btn = QPushButton(tool)
            btn.clicked.connect(lambda checked, t=tool: self.open_tool(t))
            tools_layout.addWidget(btn)
        
        # Achievement
        achievement_btn = QPushButton("🏆 SHOW ACHIEVEMENT")
        achievement_btn.clicked.connect(self.show_achievement)
        achievement_btn.setStyleSheet("background-color: #ffd700; color: #000000;")
        tools_layout.addWidget(achievement_btn)
        
        tools_layout.addStretch()
        splitter.addWidget(tools_frame)
        
        # Configurer les proportions du splitter
        splitter.setSizes([700, 300])
        
        # Timer pour le focus
        self.focus_timer = QTimer()
        self.focus_timer.timeout.connect(self.focus_input)
        self.focus_timer.start(100)
        
    def focus_input(self):
        """Maintenir le focus sur l'input"""
        if not self.command_input.hasFocus():
            self.command_input.setFocus()
            
    def keyPressEvent(self, event):
        """Gérer les touches du clavier pour l'historique"""
        if event.key() == Qt.Key_Up:
            if self.command_history and self.history_index < len(self.command_history) - 1:
                self.history_index += 1
                self.command_input.setText(self.command_history[-(self.history_index + 1)])
        elif event.key() == Qt.Key_Down:
            if self.history_index > 0:
                self.history_index -= 1
                self.command_input.setText(self.command_history[-(self.history_index + 1)])
            elif self.history_index == 0:
                self.history_index = -1
                self.command_input.clear()
        else:
            super().keyPressEvent(event)
            
    def execute_command(self):
        """Exécuter une commande"""
        command = self.command_input.text().strip()
        if not command:
            return
            
        # Ajouter à l'historique
        self.command_history.append(command)
        self.history_index = -1
        
        # Afficher la commande
        self.terminal_output.append(f"\n<span style='color: #00ffff;'>$ {command}</span>")
        
        # Commandes NEON spéciales
        if command.lower() == "help":
            self.show_neon_help()
        elif command.lower() == "realms":
            self.show_realms()
        elif command.lower() == "tools":
            self.show_tools()
        elif command.lower() == "achievement":
            self.show_achievement()
        elif command.lower().startswith("cd "):
            realm = command[3:].upper()
            self.switch_realm(realm)
        else:
            # Exécuter la commande Linux
            self.execute_linux_command(command)
            
        self.command_input.clear()
        
    def execute_linux_command(self, command):
        """Exécuter une commande Linux dans un thread séparé"""
        self.command_thread = CommandThread(command)
        self.command_thread.output.connect(self.append_output)
        self.command_thread.finished.connect(self.command_finished)
        self.command_thread.start()
        
    def append_output(self, text):
        """Ajouter du texte à la sortie du terminal"""
        cursor = self.terminal_output.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(f"{text}\n")
        self.terminal_output.setTextCursor(cursor)
        self.terminal_output.ensureCursorVisible()
        
    def command_finished(self):
        """Appelé quand la commande est terminée"""
        pass
        
    def clear_terminal(self):
        """Effacer le terminal"""
        self.terminal_output.clear()
        self.terminal_output.append("🚀 Terminal cleared. Ready for new commands...")
        
    def show_neon_help(self):
        """Afficher l'aide NEON"""
        help_text = """
🚀 NEON OS COMMANDS:
• help - Show this help
• realms - Show available realms  
• tools - Show system tools
• cd <realm> - Change current realm
• achievement - Show achievements
• clear - Clear terminal

🌍 AVAILABLE REALMS:
• OVERWORLD - Main realm
• NETHER - Dark realm  
• THE_END - Final realm

🎮 TOON REALMS:
• SURVIVAL_V1 - Survival mode
• TOON_CITY - Creative city
• CREATIVE_X - Experimental

Any Linux command will work in this terminal!
"""
        self.append_output(help_text)
        
    def show_realms(self):
        """Afficher les royaumes disponibles"""
        realms_text = """
🌍 OBSIDIAN STORAGE // FILE_BROWSER:
• OVERWORLD - REALM - 🟢 ACCESSIBLE
• NETHER - REALM - 🟢 ACCESSIBLE  
• THE_END - REALM - 🟢 ACCESSIBLE

🎮 TOON REALMS:
• SURVIVAL_V1 - SURVIVAL Mode
• TOON_CITY - CREATIVE Mode
• CREATIVE_X - EXPERIMENTAL Mode
"""
        self.append_output(realms_text)
        
    def show_tools(self):
        """Afficher les outils système"""
        tools_text = """
🔧 SYSTEM TOOLS:
• 🗑️ Recycle Bin - File management
• 📁 Documents - Document viewer
• 🌐 Web Browser - Firefox
• 🔧 System Info - System monitoring
• 📝 Text Editor - Kate/KWrite
• 💻 Terminal - Konsole
"""
        self.append_output(tools_text)
        
    def switch_realm(self, realm):
        """Changer de royaume"""
        self.realm_label.setText(f"📍 Current Realm: {realm}")
        self.append_output(f"\n🌍 Switching to {realm} realm...")
        self.append_output(f"✅ Successfully entered {realm}!")
        
    def enter_toon_realm(self, realm):
        """Entrer dans un Toon Realm"""
        self.append_output(f"\n🎮 Entering Toon Realm: {realm}")
        self.append_output(f"🎯 Loading {realm} environment...")
        self.append_output(f"🎉 Welcome to {realm}!")
        
    def open_tool(self, tool):
        """Ouvrir un outil système"""
        self.append_output(f"\n🔧 Opening {tool}...")
        
        if "Web Browser" in tool:
            subprocess.Popen(["firefox"], shell=False)
        elif "Documents" in tool:
            subprocess.Popen(["dolphin", "/home/neonuser/Documents"], shell=False)
        elif "System Info" in tool:
            subprocess.Popen(["htop"], shell=False)
        else:
            self.append_output(f"📁 {tool} interface would open here")
            
    def show_achievement(self):
        """Afficher un achievement"""
        self.append_output("\n🏆 TOON ACHIEVEMENT!")
        self.append_output("Successfully entered the Toon Zone!")
        self.append_output("🎉 You are now a NEON OS KDE master!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Configuration pour KDE
    app.setApplicationName("NEON OS Terminal")
    app.setApplicationDisplayName("🚀 NEON OS Terminal")
    
    window = NeonTerminalKDE()
    window.show()
    
    sys.exit(app.exec_())
