import http.server
import os
import socketserver

# 定义服务器的主机和端口
host = 'localhost'
port = 8000

# 切换到网页文件所在的目录
web_dir = './'  # 将此处替换为你的网页文件所在的目录
os.chdir(web_dir)

# 创建简单的 HTTP 服务器
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer((host, port), Handler)

# 在控制台输出服务器信息
print(f"Serving web files at http://{host}:{port}/")

# 启动服务器
httpd.serve_forever()
