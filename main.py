from flask import Flask, request, Response

app = Flask(__name__)

# HTML-форма для ввода номера телефона и кода
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Сбор данных</title>
</head>
<body>
    <h2>Введите номер телефона</h2>
    <form action="/submit_phone" method="POST">
        <label for="phone">Номер телефона:</label>
        <input type="tel" id="phone" name="phone" required>
        <button type="submit">Отправить номер</button>
    </form>
    <h2>Введите код</h2>
    <form action="/submit_code" method="POST">
        <label for="code">Код:</label>
        <input type="text" id="code" name="code" required>
        <button type="submit">Отправить код</button>
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return HTML_FORM

@app.route('/submit_phone', methods=['POST'])
def submit_phone():
    phone = request.form.get('phone')
    if not phone:
        return Response("Номер телефона не указан", status=400)
    
    # Выводим в терминал
    print(f"Получен НОМЕР ТЕЛЕФОНА: {phone}")
    
    # Сохраняем в файл
    try:
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(f"PHONE: {phone}\n")
        return "Номер телефона успешно сохранён!"
    except Exception as e:
        print(f"Ошибка при сохранении номера: {str(e)}")
        return Response(f"Ошибка при сохранении номера: {str(e)}", status=500)

@app.route('/submit_code', methods=['POST'])
def submit_code():
    code = request.form.get('code')
    if not code:
        return Response("Код не указан", status=400)
    
    # Выводим в терминал
    print(f"Получен КОД: {code}")
    
    # Сохраняем в файл
    try:
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(f"CODE: {code}\n")
        return "Код успешно сохранён!"
    except Exception as e:
        print(f"Ошибка при сохранении кода: {str(e)}")
        return Response(f"Ошибка при сохранении кода: {str(e)}", status=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
