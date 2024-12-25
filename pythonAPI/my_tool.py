from flask import  request, jsonify
import os
import random
def register_routes3(app):
    @app.route('/api/Tool1', methods=['POST'])
    def rename_files():
        data = request.json
        folder_path = data['folderPath']
        string_a = data['stringA']
        number_b = data['numberB']
        number_c = data['numberC']
        print(folder_path)
        try:
            files = os.listdir(folder_path)
            for file in files:
                file_extension = os.path.splitext(file)[1]
                new_file_name = f"{string_a}{number_b}{file_extension}"
                if number_b < number_c:
                    number_b += 1
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_file_name))
            return jsonify({"message": "重命名成功"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route('/api/Tool2', methods=['POST'])
    def generate_numbers():
        data = request.json
        if not data:
            return jsonify({"error": "请求数据不能为空"}), 200#断点断点
        number_type = data['numberType']
        quantity = data['quantity']
        min_value = data['minValue']
        max_value = data['maxValue']
        sort_order = data['sortOrder']
        # 检查必需字段是否存在
        print(number_type, quantity, min_value, max_value, sort_order)
        if number_type is None or quantity is None or min_value is None or max_value is None or sort_order is None:
            return jsonify({"error": "所有字段都是必需的"}), 400
        try:
            quantity = int(quantity)
            min_value = float(min_value)
            max_value = float(max_value)
        except (ValueError, TypeError):
            return jsonify({"error": "数量、最小值和最大值必须是有效的数字"}), 400
        # 检查数量是否有效
        if quantity <= 0:
            return jsonify({"error": "生成数量必须大于0"}), 400
        if min_value >= max_value:
            return jsonify({"error": "最小值必须小于最大值"}), 400
        # 生成随机数
        if number_type == 'integer':
            numbers = [random.randint(int(min_value), int(max_value)) for _ in range(quantity)]
        elif number_type == 'float':
            numbers = [random.uniform(min_value, max_value) for _ in range(quantity)]
        else:
            return jsonify({"error": "无效的数字类型"}), 400
        # 根据排序方式排序
        if sort_order == 'asc':
            numbers.sort()
        elif sort_order == 'desc':
            numbers.sort(reverse=True)
        return jsonify(numbers), 200
