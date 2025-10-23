from flask import Flask

app = Flask(__name__)

@app.route('/')
def mostrar_primos():
    primos = []
    for n in range(1, 21):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                primos.append(n)
    return f"Números primos del 1 al 20: {primos}"

if __name__ == '__main__':
    app.run(debug=True)
