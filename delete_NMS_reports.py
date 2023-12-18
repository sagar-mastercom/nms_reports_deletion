import requests

token =""

def get_nms_reports(pattern,token):
    try:
        api_url=""
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }
        if params is None:
            params = {}
        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 200:
            print("NMS Reports:")
            print(response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print("An error Occured: {e}")


def Authentication(username,password):
    login_url ="https://192.168.4.7/api/v2/authentication/signin?nmsLogin=false"
    try:
        headers = {
            'Content-Type': 'application/json',
        }
        params = {"name": "admin",  "password": "SevOne#123"}
        response = requests.get(login_url, headers=headers, params=params)
        if response.status_code == 200:
            print("Token:")
            print(response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print("An error Occured: {e}")

if __name__ == "__main__":
        
    if token != "":
        get_nms_reports(token=token)