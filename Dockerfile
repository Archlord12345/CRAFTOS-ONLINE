FROM ubuntu:22.04

# Avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install basic packages and dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    ncurses-utils \
    figlet \
    lolcat \
    curl \
    wget \
    nano \
    vim \
    htop \
    tree \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies for the interface
RUN pip3 install rich colorama

# Create the NEON OS directory structure
RUN mkdir -p /neon-os/{realms,storage,system_tools}

# Create the main OS script
COPY neon_os.py /neon-os/
COPY welcome.sh /neon-os/

# Make scripts executable
RUN chmod +x /neon-os/neon_os.py /neon-os/welcome.sh

# Set working directory
WORKDIR /neon-os

# Create entrypoint script
RUN echo '#!/bin/bash\n./welcome.sh' > /neon-os/entrypoint.sh && chmod +x /neon-os/entrypoint.sh

ENTRYPOINT ["/neon-os/entrypoint.sh"]
