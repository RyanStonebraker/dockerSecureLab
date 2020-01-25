import requests

pwd = ""
while True:
    command = input("$ ").replace("'", "\\'")
    change_dir = f"cd {pwd};" if pwd else ""
    command_pwd = f"bash -c '{change_dir}{command};pwd;'".replace("'", "\\'")
    url = f"http://localhost:8090/execute?import os\\nprint(os.popen('{command_pwd}').read())"
    
    output = requests.get(url).text
    print(output[:output.rfind("\n/")+1], end="")

    if "cd" in command:
        pwd = output[output.rfind("\n/")+1:].strip()