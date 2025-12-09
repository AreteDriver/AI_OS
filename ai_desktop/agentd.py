"""
ai_desktop.agentd
Core desktop AI agent.
"""

class DesktopAgent:
    def __init__(self, config=None):
        self.config = config or {}
        self.status = "initialized"

    def start(self):
        self.status = "running"
        print("Agent started.")

    def stop(self):
        self.status = "stopped"
        print("Agent stopped.")
