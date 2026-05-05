import time

def query(payload):
    for i in range(3):  # Ye 3 baar khud koshish karega
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            return response.content
        elif response.status_code == 503: # 503 matlab model busy hai
            time.sleep(2) # 2 second intezar karega
            continue
    return response.content
