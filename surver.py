from flask import Flask


app = Flask(__name__)


topics = [
    {'id' : 1, 'title' : '입력', 'body' : 'html is ...'},
    {'id' : 2, 'title' : '저장', 'body' : 'css is ...'},
    {'id' : 3, 'title' : '불러오기', 'body' : 'javascript is ...'}
    # 쓰기 기능을 구현하면 껐다키면 초기화 > 데이터베이스에 저장하면 해결 (여기 코드는 데이터베이스 코드 읽어오는 코드)
]

@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a><h1>
            <ol>
                {liTags}
            </ol>
            <h2>Wlecome</h2>
            Hello, web
        </body>
    </html>
    '''

@app.route('/create/')
def create():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a><h1>
            <ol>
                {liTags}
            </ol>
            <h2>Wlecome</h2>
            Hello, web
        </body>
    </html>
    '''

@app.route('/read/<id>/')
def read(id):
    return 'read' +id 

app.run(debug=True)

# 플라스크는 기본적으로 5000번 포트에서 리스닝을 한다
# 만약 5천번에서 먼저 실행된 서버가 있다면 실행을 거부할 수 있다
# 이런 경우 실행 중인 서버를 끄고 다시 실행하거나 포트를 변경한다
# app.run(port=5001)  <-- 포트 변경

# 웹을 만든 뒤 코드에 변경사항을 주게 되면 웹은 이전 코드를 반영하여 돌아가고 있어서
# 변경이 되지 않는다 crtl + C 해서 끄고 다시 실행해야한다
# app.run(debug=True) 이렇게 하면 디버깅 모드로 플라스크 실행
# 디버깅 모드는 편의를 위한 것이기에 실제 서비스에서는 디버깅 ㄴㄴ


# 플라스크
# 사용자의 요청을 동적으로 생성하고 그것에 응답한다

# 라우팅
# 주소와 페이지를 연결해 주는 것 (라우터)
