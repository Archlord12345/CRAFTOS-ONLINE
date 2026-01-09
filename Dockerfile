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
COPY web_app.py /neon-os/

# Expose port for Render
EXPOSE 8000

# Start the web application
CMD ["python3", "web_app.py"]
