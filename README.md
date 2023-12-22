# 如何使用 curl 命令或者 requests 库发送 HTTP 请求进行测试

## 简介

本文简单快速地介绍使用 curl 命令来发送 HTTP 请求进行测试的方法，以及对应的 Flask 或者 FastAPI 项目的对应写法．

## 项目启动

启动 Flask 项目可以使用：

```bash
gunicorn --bind 0.0.0.0:8080 app_flask:app
```

启动 FastAPI 可以使用：

```bash
uvicorn --host 0.0.0.0 --port 8080 app_fastapi:app
```

FastAPI 有提供 OSA，可以直接浏览器访问 http://localhost:8080/docs 查看这个服务提供的接口，并进行测试．

## 测试命令

### 使用 curl

```bash
curl --get --data-urlencode "text=你好" http://localhost:8080/api/translate_v1
curl --json '{"text": "你好"}' http://localhost:8080/api/translate_v2
```

### 使用 requests 库

```python
import json
import requests

url1 = "http://localhost:8080/api/translate_v1"
response1 = requests.get(url1, params={"text": "你好"})
print(response1.json())

url2 = "http://localhost:8080/api/translate_v2"
response2 = requests.post(url2, json={"text": "你好"})
print(response2.json())

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}
response3 = requests.post(url2, data=json.dumps({"text": "你好"}), headers=headers)
print(response3.json())
```
