import json
import socket
from pathlib import Path
import subprocess

while 1:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(("0.0.0.0", 5000))
        print("显示端正在等待 JSON 文件...", flush=True)
        data, _ = sock.recvfrom(4096)

    message = json.loads(data.decode("utf-8"))
    Path(__file__).with_name("received.json").write_bytes(data)
    print("收到：", message)

    if message.get("code") == "1112" and message.get("target_ip") == "127.0.0.1":
        subprocess.Popen(["notepad.exe"])
        #the line above used for whitebox testing
