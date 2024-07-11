[參考網址](https://flask.palletsprojects.com/en/3.0.x/)

[參考網址](https://jinja.palletsprojects.com/en/3.1.x/templates/)

[參考網址](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

{%  %} statements(敘述,不會傳出值)

{{  }} expression(運算式,傳出一變數)

{#  #} 註解

{% block block_name%}
{% endblock %}

```
{%block left_content%}
striptags 移除所有標籤
title 將開頭第一個 設為大寫
{{left | striptags | title}}
{%endblock%}
```

```
@app.route("/")
def index():
    content="daily news around Taiwan and present the perspectives of Taiwan and Asia."
    return render_template("index.html.jinja",left=content)


將上述 left 傳入 下面
{%block left_content%}
{{left | striptags | title}}
{%endblock%}   


| 後面都要+filter
```

```
{#註解 for展示#}

{%for item  in['list','of','objects'] %}
<li>{{item}}</li>
{%endfor%}
```