import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render가 자동 할당한 포트 사용
    app.run(host='0.0.0.0', port=port)

