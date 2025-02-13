import time
import random
import sys

# ANSI color codes for terminal
RESET = "\033[0m"
COLORS = ["\033[92m", "\033[93m", "\033[94m", "\033[96m", "\033[95m", "\033[91m", "\033[90m"]
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
WHITE = "\033[97m"

# Helper function for random color
def random_color():
    return random.choice(COLORS)

# Functions for various animations
def loading_spinner():
    spinner = ["|", "/", "-", "\\"]
    for _ in range(20):
        for symbol in spinner:
            sys.stdout.write(f"{GREEN}Loading... {symbol}\r")
            sys.stdout.flush()
            time.sleep(0.1)
    print()

def progress_bar_task(task_name="Task in progress"):
    bar_length = 30
    for i in range(1, bar_length + 1):
        percent = int((i / bar_length) * 100)
        bar = "#" * i + "-" * (bar_length - i)
        print(f"{task_name}: [{bar}] {percent}%", end="\r")
        time.sleep(0.1)
    print()

def download_simulation():
    files = ["file1.zip", "file2.tar.gz", "module.bin", "update.pkg", "resource.data"]
    for file in files:
        file_size = random.randint(5, 100)  # Random file size in MB
        downloaded = 0
        print(f"Downloading {file} - {file_size} MB")
        while downloaded < file_size:
            downloaded += random.randint(1, 5)
            progress = min(downloaded, file_size)
            percent = int((progress / file_size) * 100)
            bar = "#" * (percent // 5) + "-" * ((100 - percent) // 5)
            print(f"[{bar}] {percent}% ({progress}/{file_size} MB)", end="\r")
            time.sleep(0.2)
        print(f"{random_color()}Download complete{RESET}\n")

def dot_matrix_effect(width=40):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    for _ in range(5):
        line = "".join(random.choice(characters) for _ in range(width))
        print(f"{GREEN}{line}{RESET}", end="\r")
        time.sleep(0.1)
    print()

def warning_messages():
    warnings = [
        "Warning: Low disk space on drive C:",
        "Warning: High CPU usage detected",
        "Warning: Network latency is high",
        "Warning: Unusual login attempt detected",
        "Warning: System memory is running low",
        "Warning: Application X has stopped responding",
        "Warning: Firewall disabled",
        "Warning: Unrecognized device connected",
        "Warning: Suspicious activity detected",
        "Warning: Outdated driver found"
    ]
    num_warnings = random.randint(1, 2)
    selected_warnings = random.sample(warnings, num_warnings)
    for message in selected_warnings:
        print(f"{YELLOW}{message}{RESET}")
        time.sleep(0.5)

def error_messages():
    errors = [
        "Error: Failed to connect to server",
        "Error: Access denied",
        "Error: File not found",
        "Error: Unknown exception occurred",
        "Error: Unable to retrieve data",
        "Error: Application crashed unexpectedly",
        "Error: Operation timed out",
        "Error: Insufficient permissions",
        "Error: Invalid command syntax",
        "Error: Database connection lost",
        "Error: Disk read failure",
        "Error: Memory overflow",
        "Error: Stack overflow detected"
    ]
    num_errors = random.randint(1, 2)
    selected_errors = random.sample(errors, num_errors)
    for message in selected_errors:
        print(f"{RED}{message}{RESET}")
        time.sleep(0.5)

def success_messages():
    successes = [
        "Success: Backup completed",
        "Success: Data synchronized",
        "Success: User authenticated",
        "Success: Connection established",
        "Success: File uploaded successfully",
        "Success: Configuration updated",
        "Success: Database query executed",
        "Success: Permissions granted",
        "Success: System diagnostics passed",
        "Success: Operation completed successfully"
    ]
    num_successes = random.randint(1, 2)
    selected_successes = random.sample(successes, num_successes)
    for message in selected_successes:
        print(f"{GREEN}{message}{RESET}")
        time.sleep(0.5)

def hacker_typing_effect():
    commands = [
        "Establishing secure connection...",
        "Bypassing firewall...",
        "Uploading payload...",
        "Accessing database...",
        "Retrieving sensitive data...",
        "Executing scripts...",
        "Decrypting security tokens...",
        "Scanning network for vulnerabilities...",
        "Initializing brute-force attack...",
        "Mapping IP addresses...",
        "Injecting malicious code...",
        "Creating backdoor entry...",
        "Exfiltrating data packets...",
        "Compiling exploit modules...",
        "Overriding user permissions...",
        "Spoofing IP address...",
        "Escalating privileges...",
        "Extracting encrypted files...",
        "Disabling security protocols...",
        "Activating remote access tools...",
        "Deploying trojan software...",
        "Encrypting stolen data...",
        "Wiping traces from system logs...",
        "Collecting keystrokes...",
        "Sending encrypted data to external server...",
        "Launching Distributed Denial-of-Service (DDoS) attack...",
        "Establishing proxy connections...",
        "Unpacking malware payload...",
        "Retrieving critical system files...",
        "Masking IP with VPN tunneling...",
        "Generating fake certificates...",
        "Compromising network security...",
        "Removing traces from host machine...",
        "Accessing deep file structure...",
        "Initiating deep scan...",
        "Exploiting zero-day vulnerabilities...",
        "Fetching root access keys...",
        "Injecting SQL payload...",
        "Disabling antivirus software...",
        "Modifying registry entries...",
        "Configuring keylogger...",
        "Encrypting session data...",
        "Launching password-cracking module...",
        "Executing command injection...",
        "Injecting ransomware payload...",
        "Locating sensitive documents...",
        "Exporting database tables...",
        "Obtaining encryption keys...",
        "Modifying network settings...",
        "Gaining control over subnet...",
        "Scanning for open ports...",
        "Seizing control of admin privileges...",
        "Interfering with data packets...",
    ]
    num_commands_to_display = random.randint(2, 8)
    selected_commands = random.sample(commands, k=num_commands_to_display)
    for command in selected_commands:
        sys.stdout.write(f"{GREEN}")
        for char in command:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(random.uniform(0.01, 0.06))
        print(RESET)
        time.sleep(0.3)
    time.sleep(1)

def file_tree_traversal():
    folders = [
        "/home/user/documents", "/home/user/photos", "/home/user/videos",
        "/usr/local/bin", "/etc/nginx", "/var/log", "/opt/software",
        "/home/user/downloads", "/var/www/html", "/etc/apache2", "/home/user/music",
        "/usr/share/fonts", "/opt/tools", "/tmp/cache", "/var/backups",
        "/home/user/projects", "/root/secrets", "/media/user/external_drive",
        "/usr/include", "/lib/systemd/system", "/boot/efi"
    ]

    files = [
        "file1.txt", "image.png", "video.mp4", "data.csv", "config.json", "notes.md",
        "backup.zip", "readme.md", "index.html", "style.css", "script.js", "docker-compose.yml",
        "database.sql", "server.log", "access.log", "license.key", "user_profile.dat",
        "settings.ini", "report.docx", "presentation.pptx", "spreadsheet.xlsx",
        "system_backup.bak", "photo1.jpg", "track1.mp3", "archive.tar.gz",
        "source_code.c", "application.py", "main.go", "module.rs", "config.xml",
        "kernel.img", "disk.img", "error.log", "diagnostics.dmp", "requirements.txt",
        "environment.env", "dependencies.lock", "hashfile.md5", "patch.diff"
    ]

    num_folders_to_scan = random.randint(3, 6)
    selected_folders = random.sample(folders, k=num_folders_to_scan)

    for folder in selected_folders:
        print(f"Scanning {folder}/")
        num_files_in_folder = random.randint(2, 6)
        for _ in range(num_files_in_folder):
            file = random.choice(files)
            print(f"  - {file}")
            time.sleep(0.1)
    print()

def cpu_memory_usage_simulation():
    print(f"{random_color()}Monitoring CPU/Memory usage:{RESET}")
    for _ in range(15):
        cpu_usage = random.randint(0, 100)
        memory_usage = random.randint(0, 100)
        print(f"CPU: {cpu_usage}% | Memory: {memory_usage}%", end="\r")
        time.sleep(0.5)
    print()

def loading_dots_animation():
    print(f"{random_color()}Connecting{RESET}", end="")
    for _ in range(10):
        sys.stdout.write(f".")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{random_color()}Connection established.{RESET}")

def database_query_simulation():
    print(f"{random_color()}Fetching database results...{RESET}")
    time.sleep(1)
    for i in range(1, 3):
        print(f"Record {i}: UserID={random.randint(1000, 9999)} | Status=Active | Balance={random.randint(100, 1000)}")

# List of animations
animations = [
    loading_spinner,
    progress_bar_task,
    download_simulation,
    dot_matrix_effect,
    cpu_memory_usage_simulation,
    loading_dots_animation,
    database_query_simulation,
    warning_messages,
    error_messages,
    success_messages
]

# Run animations in loop
end_time = time.time() + 1620  # 2 minutes
while time.time() < end_time:
    # Run 3-5 random animations
    num_animations = random.randint(3, 5)
    for _ in range(num_animations):
        animation = random.choice(animations)
        animation()
        print()  # Blank line for separation

    # Run file tree traversal
    file_tree_traversal()
    # Run hacker typing effect
    hacker_typing_effect()
    # Short pause before next loop
    time.sleep(1)
