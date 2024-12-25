import os
from flask import  request, jsonify
import jieba
import wordcloud

blazor_file = os.path.abspath(os.path.dirname(os.getcwd())) + '\BlazorDisplay\BlazorDisplay\wwwroot'
def register_routes4(app):
    @app.route('/api/cloudimage', methods=['POST'])
    def get_cloudimage():
        data = request.json
        text = data.get('text', '')
        if text:
            ls = jieba.lcut(text)  # 生成分词列表
            str_text = ' '.join(ls)  # 连接成字符串
            sw = ["的", "是", "了","吗" ,"被","而","再"]  # 去掉不需要显示的词
            wc = wordcloud.WordCloud(font_path="deyihei.ttf",
                                     width=1000,
                                     height=700,
                                     background_color='white',
                                     max_words=100, stopwords=sw)
            wc.generate(str_text)  # 加载词云文本
            output_path = os.path.join(blazor_file, "my_cloud.png")
            wc.to_file(output_path)  # 保存词云文件
            return jsonify({"message": "词云生成成功", "file_path": output_path}), 200


