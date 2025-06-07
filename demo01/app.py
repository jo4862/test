from flask import Flask, render_template, request, send_file
from drlin import drlin
import random
import io
import os
x = 1
app = Flask(__name__)
app.config['DECODE_FOLDER'] = 'decode'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制16MB
os.makedirs(app.config['DECODE_FOLDER'], exist_ok=True)
app.config['DEFILTER_FOLDER'] = 'defilter'
os.makedirs(app.config['DEFILTER_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decode', methods=['GET', 'POST'])
def decode_image():
    if request.method == 'POST':
        # 检查是否有文件上传
        if 'file' not in request.files:
            return render_template('decode.html', error='没有选择文件')

        file = request.files['file']

        # 验证文件
        if file.filename == '':
            return render_template('decode.html', error='未选择文件')

        if not allowed_file(file.filename):
            return render_template('decode.html', error='仅支持PNG/JPG/JPEG/GIF格式')

        try:
            x = int(request.form['number'])
            # 保存原始文件
            original_path0 = os.path.join(app.config['DECODE_FOLDER'], file.filename)
            file.save(original_path0)

            # 图片处理流程
            random.seed(x)
            processed_img = drlin.decode(original_path0)

            # 转换为字节流
            img_byte_arr0 = io.BytesIO()
            processed_img.save(img_byte_arr0, format='PNG')
            img_byte_arr0.seek(0)

            # 返回处理后的图片
            os.remove(original_path0)
            return send_file(img_byte_arr0, mimetype='image/png')

        except Exception as e:
            return render_template('decode.html', error=f'处理失败: {str(e)}')

    return render_template('decode.html')

@app.route('/defilter', methods=['GET', 'POST'])
def defilter_image():
    if request.method == 'POST':
        # 检查是否有文件上传
        if 'file' not in request.files:
            return render_template('defilter.html', error='没有选择文件')

        file = request.files['file']

        # 验证文件
        if file.filename == '':
            return render_template('defilter.html', error='未选择文件')

        if not allowed_file(file.filename):
            return render_template('defilter.html', error='仅支持PNG/JPG/JPEG/GIF格式')

        try:
            # 从表单字段获取字符串并转为数字
            x = int(request.form['number'])
            # 保存原始文件
            original_path1 = os.path.join(app.config['DEFILTER_FOLDER'], file.filename)
            file.save(original_path1)

            # 图片处理流程
            random.seed(x)
            processed_img = drlin.defilter(original_path1)

            # 转换为字节流
            img_byte_arr1 = io.BytesIO()
            processed_img.save(img_byte_arr1, format='PNG')
            img_byte_arr1.seek(0)

            # 返回处理后的图片
            os.remove(original_path1)
            return send_file(img_byte_arr1, mimetype='image/png')

        except Exception as e:
            return render_template('defilter.html', error=f'处理失败: {str(e)}')

    return render_template('defilter.html')

if __name__ == '__main__':
    app.run(port = 8001)