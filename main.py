import subprocess
from pathlib import Path
import os
os.system("title Admin Tools")

ROOT = Path(__file__).parent
TOOLS_DIR = ROOT / "Admin Tools" / "tools"

def list_tools():
    tools = {}
    for bat in TOOLS_DIR.glob("*.bat"):
        name = bat.stem.lower()
        tools[name] = bat
    return tools

def run_tool(tool_path):
    subprocess.run(str(tool_path), shell=True)

def main():
    tools = list_tools()

    print("Admin Tools Terminal")
    print("Type 'help' to list commands or 'exit' to quit.\n")

    while True:
        cmd = input("> ").strip().lower()

        if cmd == "exit":
            break

        if cmd == "help":
            print("\nAvailable commands:")
            for name in tools:
                print(f"  {name}")
            print()
            continue

        if cmd in tools:
            run_tool(tools[cmd])
            continue

        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()