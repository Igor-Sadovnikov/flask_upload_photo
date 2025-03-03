from flask import Flask, url_for, request
import os
app = Flask(__name__)

@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    filename = 'image.jpg'
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h2 align="center">Для участия в миссии</h2>
                            <form class="photo_form" method="post" enctype="multipart/form-data">
                                <div>Приложите фотографию</div>
                               <div class="form-group">
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <img src="/static/img/{filename}" alt="Здесь будет отображена загруженная картинка">
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        UPLOAD_FOLDER = 'static/img'
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        if f:
            # Сохраните файл
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
            f.save(file_path)
            filename = f.filename
        return f'''<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h2 align="center">Для участия в миссии</h2>
                            <form class="photo_form" method="post" enctype="multipart/form-data">
                                <div>Приложите фотографию</div>
                               <div class="form-group">
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <img src="/static/img/{filename}" alt="Здесь будет отображена загруженная картинка">
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')