[參考網址](https://getbootstrap.com/)

[參考網址](https://pypi.org/project/gunicorn/)

[參考網址](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application)


> ## flask gunicorn
    gunicorn 只能在liunx環境

    flask gunicorn 都是wsgi
    
    flask 是開發版
    
    gunicorn 是正式發布版

    1 flask 要在虛擬環境執行
    2 conda install --yes
    --file requirements.txt
    3 flask --app main run
    4 flask --app main run --debug
    5 gunicorn --work=2 py名:app
    6 將html多.jinja
    7 jinja語法
    ```
    <link href="{{url_for('static',filename='style/bootstrap.min.css')}}" rel="stylesheet">
    <script src="{{url_for('static',filename='js/bootstrap.min.js')}}"></script>
    ```
