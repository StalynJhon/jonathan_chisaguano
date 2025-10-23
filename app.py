from flask import Flask

app = Flask(__name__)

@app.route('/')
def mostrar_primos():
    primos = [2, 3, 5, 7, 11, 13, 17, 19]
    return f"Números primos del 1 al 20: {primos}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)
