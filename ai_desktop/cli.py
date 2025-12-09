"""
ai_desktop.cli
Basic CLI interface for the desktop agent.
"""
import argparse
from ai_desktop.agentd import DesktopAgent

def main():
    parser = argparse.ArgumentParser(description="Arete AI Desktop Agent CLI")
    parser.add_argument('--start', action='store_true', help="Start the desktop agent")
    parser.add_argument('--stop', action='store_true', help="Stop the desktop agent")
    args = parser.parse_args()

    agent = DesktopAgent()
    if args.start:
        agent.start()
    elif args.stop:
        agent.stop()
    else:
        print("No action provided. Use --start or --stop.")

if __name__ == "__main__":
    main()
