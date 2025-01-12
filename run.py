from app import create_app

app = create_app()  # 创建 Flask 应用

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # 运行 Flask 应用
