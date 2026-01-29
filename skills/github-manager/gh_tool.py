import sys
import json
import subprocess

def run_gh_command(args):
    try:
        # Construct the command: gh <args> --json ...
        cmd = ["gh"] + args
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            # If the command itself returns JSON, we parse and return it
            try:
                return json.loads(result.stdout)
            except:
                return {"output": result.stdout.strip()}
        else:
            return {"error": result.stderr.strip()}
    except Exception as e:
        return {"error": str(e)}

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: python gh_tool.py [repo|issue|pr] [list|view|...]"}))
        return

    # Pass all arguments directly to gh CLI
    output = run_gh_command(sys.argv[1:])
    print(json.dumps(output, ensure_ascii=False))

if __name__ == "__main__":
    main()
