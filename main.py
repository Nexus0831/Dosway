import converter
from flask import Flask, request, render_template, send_file

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('first.html')


@app.route('/itemName', methods=['POST'])
def item_name():
    count = int(request.form['column'])
    # ToDo: 配列に変換
    column_count = [i+1 for i in range(count)]
    return render_template('second.html', column_count=column_count)


@app.route('/elementName', methods=['POSt'])
def element_name():
    names = request.form.getlist('key-names[]')
    return render_template('third.html', names=names);


@app.route('/download', methods=['POST'])
def download():
    title = request.form['title']
    text = request.form['text']
    converter.convert.create_csv(title, text, app.root_path)
    converter.convert.create_tsv(title, text, app.root_path)
    converter.convert.create_json(title, app.root_path)
    converter.convert.create_yaml(title, app.root_path)
    converter.convert.create_zip(title, app.root_path)

    download_file_name = app.root_path + '/download/' + title + '.zip'
    download_file = title + '.zip'

    return send_file(download_file_name, as_attachment=True, attachment_filename=download_file, mimetype='application/zip')


if __name__ == '__main__':
    app.run()
