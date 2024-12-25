from flask import  request, jsonify
import pyttsx3
import os
def register_routes2(app):
    @app.route('/api/TTS', methods=['POST'])
    def tts():
        data = request.json
        text = data.get('text', '')
        if text:
            # 使用pyttsx3生成音频文件
            engine = pyttsx3.init()
            blazor_file = os.path.abspath(os.path.dirname(os.getcwd()))+'\BlazorDisplay\BlazorDisplay\wwwroot'
            audio_file = blazor_file+'\output.mp3'
            engine.save_to_file(text, audio_file)
            engine.runAndWait()
            # 返回音频文件的URL
            return jsonify(audio_file), 200
        else:
            return jsonify({"error": "No text provided"}), 400

