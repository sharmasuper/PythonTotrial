import requests
# response = requests.get("https://www.geeksforgeeks.org/shutil-module-in-python/")
# print(response.text)
# this method we get html page
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title":"foo",
    "body":"bar",
    "userId":1
}
headers =  {
    'Content-type' :'application/json;charset=UTF-8',

}
response = requests.post(url,headers = headers,json=data)
print(response.text)