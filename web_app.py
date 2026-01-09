from flask import Flask, render_template_string, request, jsonify
import subprocess
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>NEON OS TOON EDITION</title>
    <style>
        body { background: #1a1a2e; color: #eee; font-family: monospace; margin: 0; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .header { text-align: center; color: #ff00ff; font-size: 2em; margin-bottom: 20px; }
        .terminal { background: #0f0f23; border: 2px solid #00ffff; padding: 20px; border-radius: 10px; }
        .output { background: #000; color: #00ff00; padding: 10px; margin: 10px 0; border-radius: 5px; min-height: 200px; white-space: pre-wrap; font-family: monospace; }
        .input-group { display: flex; margin: 10px 0; }
        input { flex: 1; background: #222; color: #fff; border: 1px solid #00ffff; padding: 10px; font-family: monospace; }
        button { background: #00ffff; color: #000; border: none; padding: 10px 20px; cursor: pointer; font-family: monospace; }
        button:hover { background: #00cccc; }
        .realm-info { color: #ffff00; margin: 10px 0; }
        .command-line { color: #00ffff; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">🚀 NEON OS TOON EDITION 🚀</div>
        <div class="realm-info">Current Realm: OVERWORLD</div>
        <div class="terminal">
            <div class="output" id="output">Welcome to NEON OS TOON EDITION!
Successfully entered the Toon Zone.

Available Realms:
- OVERWORLD
- NETHER  
- THE_END

Toon Realms:
- SURVIVAL_V1
- TOON_CITY
- CREATIVE_X

Type Linux commands below or try: help, realms, tools, achievement</div>
            <div class="input-group">
                <input type="text" id="command" placeholder="Enter command..." autofocus>
                <button onclick="executeCommand()">Execute</button>
            </div>
        </div>
    </div>
    <script>
        const output = document.getElementById("output");
        const input = document.getElementById("command");
        
        input.addEventListener("keypress", function(e) {
            if (e.key === "Enter") {
                executeCommand();
            }
        });
        
        function executeCommand() {
            const cmd = input.value.trim();
            if (!cmd) return;
            
            output.innerHTML += "\\n<span class=\\"command-line\\">$ " + cmd + "</span>\\n";
            
            fetch("/execute", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({command: cmd})
            })
            .then(response => response.json())
            .then(data => {
                output.innerHTML += data.output + "\\n";
                output.scrollTop = output.scrollHeight;
            })
            .catch(error => {
                output.innerHTML += "Error: " + error + "\\n";
                output.scrollTop = output.scrollHeight;
            });
            
            input.value = "";
            input.focus();
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/execute", methods=["POST"])
def execute_command():
    data = request.get_json()
    command = data.get("command", "")
    
    try:
        if command.lower() in ["exit", "quit"]:
            return jsonify({"output": "Goodbye from NEON OS!"})
        elif command.lower() == "help":
            help_text = """NEON OS Commands:
help - Show this help
realms - Show available realms
tools - Show system tools
achievement - Show achievement
cd <realm> - Change realm
exit/quit - Exit

Any Linux command will work in this terminal!"""
            return jsonify({"output": help_text})
        elif command.lower() == "realms":
            realms_text = """OBSIDIAN STORAGE // FILE_BROWSER:
OVERWORLD - REALM - 🟢 ACCESSIBLE
NETHER - REALM - 🟢 ACCESSIBLE  
THE_END - REALM - 🟢 ACCESSIBLE

TOON REALMS:
SURVIVAL_V1 - SURVIVAL
TOON_CITY - CREATIVE
CREATIVE_X - CREATIVE"""
            return jsonify({"output": realms_text})
        elif command.lower() == "tools":
            tools_text = """SYSTEM TOOLS:
🗑️  Recycle Bin
📁 Documents
🔧 System Tools"""
            return jsonify({"output": tools_text})
        elif command.lower() == "achievement":
            return jsonify({"output": "🏆 TOON ACHIEVEMENT!\nSuccessfully entered the Toon Zone."})
        else:
            # Execute Linux command
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
            output = result.stdout or result.stderr or "Command executed"
            return jsonify({"output": output})
    except Exception as e:
        return jsonify({"output": f"Error: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting NEON OS web interface on port {port}")
    app.run(host="0.0.0.0", port=port, debug=True)
