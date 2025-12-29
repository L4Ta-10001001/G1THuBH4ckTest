import os
import json
import subprocess
import sys
import time
from datetime import datetime, timedelta

# ==============================================================================
#  GITHUB CONTRIBUTION GRAPH HACK | AUTOMATION TOOL
#  -----------------------------------------------------------------------------
#  Author:      L4Ta-10001001
#  Profile:     https://github.com/L4Ta-10001001
#  Description: Time-travel scripting to manipulate commit history.
#               "Painting pixels with code."
# ==============================================================================

# --- Configuration ---
PATTERN_FILE = "pattern.json"
FILE_PATH = "info.txt"
COMMITS_PER_PIXEL = 5   # Intensity level (5 = Dark Green)

# --- Terminal Colors (Linux/Unix Style) ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# -------------------------------
# System Loading Sequence
# -------------------------------
def loading_animation(task_name="Initializing Core", duration=3):
    print(f"\n{Colors.CYAN}[INFO] {task_name}...{Colors.ENDC}")
    animation = ["■□□□□", "■■□□□", "■■■□□", "■■■■□", "■■■■■"]
    
    end_time = time.time() + duration
    i = 0
    
    while time.time() < end_time:
        sys.stdout.write(f"\r{Colors.GREEN}Loading: {animation[i % len(animation)]}{Colors.ENDC}")
        sys.stdout.flush()
        time.sleep(0.5)
        i += 1
    
    sys.stdout.write(f"\r{Colors.GREEN}[OK] {task_name} Complete.     {Colors.ENDC}\n")

# -------------------------------
# Banner: L4Ta-10001001 Signature
# -------------------------------
def show_start_credit():
    print(Colors.BLUE + r"""
   __ _  _   _____        __ ___  ___  ___  __  ___  ___  __  
  / /| || |_|_   _|__ _  /  / _ \/ _ \/ _ \/  \/ _ \/ _ \/  \ 
 / /_| ||_   _| |/ _ ` | | | (_) | (_) | (_) | | (_) | (_) | | 
/____|_|  |_| |_|\__,_|  |_|\___/ \___/ \___/|_|\___/ \___/|_| 
                                                               
      >> SYSTEM: ONLINE
      >> USER:   L4Ta-10001001
      >> MODE:   HISTORY REWRITE
    """ + Colors.ENDC)
    print(f"{Colors.HEADER}-------------------------------------------------------{Colors.ENDC}")

# -------------------------------
# Banner: Execution Success
# -------------------------------
def show_end_credit():
    print(f"\n{Colors.HEADER}-------------------------------------------------------{Colors.ENDC}")
    print(Colors.GREEN + r"""
      MISSION ACCOMPLISHED.
    """ + Colors.ENDC)
    print(f"{Colors.CYAN}[+] History has been rewritten successfully.")
    print(f"[+] The timeline has been altered.")
    print(f"[+] Check your GitHub profile for updates.{Colors.ENDC}")
    print(f"\n{Colors.BOLD}Code by L4Ta-10001001{Colors.ENDC} | Keep hacking responsibly.")
    print(f"{Colors.HEADER}-------------------------------------------------------{Colors.ENDC}\n")

# -------------------------------
# Git Operations Wrapper
# -------------------------------
def git_commit(message, commit_date):
    # Staging file
    subprocess.run(["git", "add", FILE_PATH], check=True)

    # Environment manipulation for time travel
    env = os.environ.copy()
    date_str = commit_date.strftime("%Y-%m-%dT12:00:00")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    # Executing commit
    subprocess.run(
        [
            "git",
            "commit",
            "--quiet",         # Less noise in terminal
            "--allow-empty",   # Vital for pattern generation
            "-m",
            message,
            "--date",
            date_str
        ],
        env=env,
        check=True
    )
    
    # Log output looks like SysAdmin logs
    print(f"{Colors.GREEN}[EXEC] Commit injected:{Colors.ENDC} {date_str} >> {message}")

def git_push():
    print(f"\n{Colors.WARNING}[NET] Pushing changes to remote repository...{Colors.ENDC}")
    subprocess.run(["git", "push"], check=True)
    print(f"{Colors.GREEN}[NET] Push successful.{Colors.ENDC}")

# -------------------------------
# Core Logic (Pattern Parsing)
# -------------------------------
def load_pattern():
    try:
        with open(PATTERN_FILE, "r") as f:
            print(f"{Colors.CYAN}[IO] Reading pattern file: {PATTERN_FILE}{Colors.ENDC}")
            return json.load(f)
    except FileNotFoundError:
        print(f"{Colors.FAIL}[ERR] Pattern file not found!{Colors.ENDC}")
        sys.exit(1)

def first_sunday(year):
    d = datetime(year, 1, 1)
    while d.weekday() != 6:  # 6 = Sunday
        d += timedelta(days=1)
    return d

def make_commits_from_pattern(year):
    pattern = load_pattern()
    start_date = first_sunday(year)
    
    print(f"{Colors.CYAN}[CALC] Aligning grid to first Sunday of {year}: {start_date.date()}{Colors.ENDC}\n")

    total_commits = 0
    
    for row_idx, row in enumerate(pattern):
        for col_idx, char in enumerate(row):
            if char == " ":
                continue  # Skip empty pixels

            commit_date = start_date + timedelta(
                weeks=col_idx,
                days=row_idx
            )

            # Generate multiple commits for color intensity
            for i in range(1, COMMITS_PER_PIXEL + 1):
                msg = f"L4Ta-10001001 log: {commit_date.date()} pixel entry {i}"
                
                # Update dummy file
                with open(FILE_PATH, "w") as f:
                    f.write(msg)
                
                git_commit(msg, commit_date)
                total_commits += 1

    print(f"\n{Colors.BOLD}[STAT] Total commits generated: {total_commits}{Colors.ENDC}")
    git_push()

# -------------------------------
# Main Execution Entry Point
# -------------------------------
if __name__ == "__main__":
    # Clean screen (Linux/Mac/Win)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    show_start_credit()
    loading_animation("Booting Graph Hack Tools", 2)

    try:
        input_str = input(f"{Colors.BOLD}{Colors.WARNING}👉 Enter target year (YYYY) ➤ {Colors.ENDC}")
        year = int(input_str)
        
        start_time = time.time()
        make_commits_from_pattern(year)
        
        show_end_credit()
        
    except ValueError:
        print(f"{Colors.FAIL}[ERR] Invalid year format. System aborting.{Colors.ENDC}")
    except KeyboardInterrupt:
        print(f"\n{Colors.FAIL}[ERR] User interrupted process.{Colors.ENDC}")
