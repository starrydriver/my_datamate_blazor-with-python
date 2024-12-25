from flask import Flask
from flask_cors import CORS
from my_pdf import register_routes1
from my_tts import register_routes2
from my_tool import register_routes3
from my_cloudimage import register_routes4

app = Flask(__name__)
CORS(app)  # 允许跨域请求

register_routes1(app)
register_routes2(app)
register_routes3(app)
register_routes4(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # 确保运行在不同的端口
