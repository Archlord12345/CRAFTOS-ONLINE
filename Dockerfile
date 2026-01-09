FROM ubuntu:22.04

# Avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install basic packages and dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    ncurses-bin \
    curl \
    wget \
    nano \
    vim \
    htop \
    tree \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies for the interface
RUN pip3 install rich colorama flask

# Create the NEON OS directory structure
RUN mkdir -p /neon-os/{realms,storage,system_tools}

# Create the main OS script
COPY neon_os.py /neon-os/
COPY welcome.sh /neon-os/

# Make scripts executable
RUN chmod +x /neon-os/neon_os.py /neon-os/welcome.sh

# Set working directory
WORKDIR /neon-os

# Create a web interface for Render
RUN echo 'from flask import Flask, render_template_string, request, jsonify\nimport subprocess\nimport os\n\napp = Flask(__name__)\n\nHTML_TEMPLATE = """\n<!DOCTYPE html>\n<html>\n<head>\n    <title>NEON OS TOON EDITION</title>\n    <style>\n        body { background: #1a1a2e; color: #eee; font-family: monospace; margin: 0; }\n        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }\n        .header { text-align: center; color: #ff00ff; font-size: 2em; margin-bottom: 20px; }\n        .terminal { background: #0f0f23; border: 2px solid #00ffff; padding: 20px; border-radius: 10px; }\n        .output { background: #000; color: #00ff00; padding: 10px; margin: 10px 0; border-radius: 5px; min-height: 200px; }\n        .input-group { display: flex; margin: 10px 0; }\n        input { flex: 1; background: #222; color: #fff; border: 1px solid #00ffff; padding: 10px; }\n        button { background: #00ffff; color: #000; border: none; padding: 10px 20px; cursor: pointer; }\n        button:hover { background: #00cccc; }\n        .realm-info { color: #ffff00; margin: 10px 0; }\n    </style>\n</head>\n<body>\n    <div class="container">\n        <div class="header">🚀 NEON OS TOON EDITION 🚀</div>\n        <div class="realm-info">Current Realm: OVERWORLD</div>\n        <div class="terminal">\n            <div class="output" id="output">Welcome to NEON OS TOON EDITION!\nSuccessfully entered the Toon Zone.\n\nAvailable Realms:\n- OVERWORLD\n- NETHER  \n- THE_END\n\nToon Realms:\n- SURVIVAL_V1\n- TOON_CITY\n- CREATIVE_X\n\nType Linux commands below or try: help, realms, tools, achievement</div>\n            <div class="input-group">\n                <input type="text" id="command" placeholder="Enter command..." autofocus>\n                <button onclick="executeCommand()">Execute</button>\n            </div>\n        </div>\n    </div>\n    <script>\n        const output = document.getElementById("output");\n        const input = document.getElementById("command");\n        \n        input.addEventListener("keypress", function(e) {\n            if (e.key === "Enter") {\n                executeCommand();\n            }\n        });\n        \n        function executeCommand() {\n            const cmd = input.value.trim();\n            if (!cmd) return;\n            \n            output.innerHTML += "\\n$ " + cmd + "\\n";\n            \n            fetch("/execute", {\n                method: "POST",\n                headers: {"Content-Type": "application/json"},\n                body: JSON.stringify({command: cmd})\n            })\n            .then(response => response.json())\n            .then(data => {\n                output.innerHTML += data.output + "\\n";\n                output.scrollTop = output.scrollHeight;\n            })\n            .catch(error => {\n                output.innerHTML += "Error: " + error + "\\n";\n            });\n            \n            input.value = "";\n        }\n    </script>\n</body>\n</html>\n"""\n\n@app.route("/")\ndef index():\n    return render_template_string(HTML_TEMPLATE)\n\n@app.route("/execute", methods=["POST"])\ndef execute_command():\n    data = request.get_json()\n    command = data.get("command", "")\n    \n    try:\n        if command.lower() in ["exit", "quit"]:\n            return jsonify({"output": "Goodbye from NEON OS!"})\n        elif command.lower() == "help":\n            help_text = """NEON OS Commands:\nhelp - Show this help\nrealms - Show available realms\ntools - Show system tools\nachievement - Show achievement\ncd <realm> - Change realm\nexit/quit - Exit\n\nAny Linux command will work in this terminal!"""\n            return jsonify({"output": help_text})\n        elif command.lower() == "realms":\n            realms_text = """OBSIDIAN STORAGE // FILE_BROWSER:\nOVERWORLD - REALM - 🟢 ACCESSIBLE\nNETHER - REALM - 🟢 ACCESSIBLE  \nTHE_END - REALM - 🟢 ACCESSIBLE\n\nTOON REALMS:\nSURVIVAL_V1 - SURVIVAL\nTOON_CITY - CREATIVE\nCREATIVE_X - CREATIVE"""\n            return jsonify({"output": realms_text})\n        elif command.lower() == "tools":\n            tools_text = """SYSTEM TOOLS:\n🗑️  Recycle Bin\n📁 Documents\n🔧 System Tools"""\n            return jsonify({"output": tools_text})\n        elif command.lower() == "achievement":\n            return jsonify({"output": "🏆 TOON ACHIEVEMENT!\\nSuccessfully entered the Toon Zone."})\n        else:\n            # Execute Linux command\n            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)\n            output = result.stdout or result.stderr or "Command executed"\n            return jsonify({"output": output})\n    except Exception as e:\n        return jsonify({"output": f"Error: {str(e)}"})\n\nif __name__ == "__main__":\n    port = int(os.environ.get("PORT", 8000))\n    app.run(host="0.0.0.0", port=port)' > /neon-os/web_app.py

# Expose port for Render
EXPOSE 8000

# Start the web application
CMD ["python3", "web_app.py"]
