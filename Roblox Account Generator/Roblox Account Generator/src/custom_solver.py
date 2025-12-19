from util import Util
from time import sleep
from curl_cffi import requests

config = Util.get_config()

SOLVER_KEY = config["solverKey"]

def get_token(roblox_session: requests.Session, blob, proxy):
    session = requests.Session()

    challengeInfo = {
        "publicKey": "A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F",
        "site": "https://www.roblox.com/",
        "surl": "https://arkoselabs.roblox.com",
        "capiMode": "inline",
        "styleTheme": "default",
        "languageEnabled": False,
        "jsfEnabled": False,
        "extraData": {
            "blob": blob
        },
        "ancestorOrigins": ["https://www.roblox.com"],
        "treeIndex": [0],
        "treeStructure": "[[]]",
        "locationHref":  "https://www.roblox.com/arkose/iframe",
        "documentReferrer": "https://www.roblox.com/CreateAccount"
    }

    browserInfo = {
        'Sec-Ch-Ua': roblox_session.headers["sec-ch-ua"],
        'User-Agent': roblox_session.headers["user-agent"],
        'Mobile': False
    }

    payload = {
        "key": SOLVER_KEY,
        "challengeInfo": challengeInfo,
        "browserInfo": browserInfo,
        "proxy": proxy
    }

    response = session.post("https://rosolve.pro/createTask", json=payload, timeout=120).json()

    task_id = response.get("taskId")

    if task_id == None:
        raise ValueError(f"Failed to get taskId, reason: {response["error"]}")
    
    counter = 0

    while counter < 60:
        sleep(1)

        payload = {
            "key": SOLVER_KEY,
            "taskId": task_id
        }

        solution = session.post("https://rosolve.pro/taskResult", json=payload).json()

        if solution["status"] == "completed":
            return solution["result"]["solution"]
        
        elif solution["status"] == "failed":
            return None
        
        counter += 1

    return None