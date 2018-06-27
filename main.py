import converter
from flask import Flask, request, render_template, send_file

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('first.html')


@app.route('/keyNames', methods=['POST'])
def key_names():
    count = int(request.form['column'])
    column_count = [i+1 for i in range(count)]

    return render_template('second.html', column_count=column_count)


@app.route('/itemNames', methods=['POSt'])
def item_names():
    names = request.form.getlist('key-names[]')

    return render_template('third.html', names=names)


@app.route('/download', methods=['POST'])
def download():
    file_name = request.form['title']
    text = request.form['text']
    base_dir = app.root_path + '/download/'

    converter.convert.remove_files(base_dir)
    converter.convert.create_csv(file_name, text, base_dir)
    converter.convert.create_tsv(file_name, text, base_dir)
    converter.convert.create_json(file_name, base_dir)
    converter.convert.create_yaml(file_name, base_dir)
    converter.convert.create_xml(file_name, base_dir)
    converter.convert.create_zip(file_name, base_dir)

    download_file_name = base_dir + file_name + '.zip'
    download_file = file_name + '.zip'

    send_file(download_file_name, as_attachment=True, attachment_filename=download_file, mimetype='application/zip')

    return render_template('first.html')


if __name__ == '__main__':
    app.run()
