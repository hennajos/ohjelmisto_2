from flask import Flask

app=Flask(__name__)

@app.route('/summa/<luku1>/<luku2>')
def summa(luku1, luku2):
    summa=float(luku1) + float(luku2)

    vastaus={
        'luku1' : luku1,
        'luku2' : luku2,
        'luku3' : summa
    }
    return vastaus

@app.route('/alkuluku/<int:luku>')
def onko_alkuluku(luku):
    on_alkuluku=True

    if luku < 2:
        on_alkuluku=False

    for jakaja in range(2, luku):

        if luku % jakaja == 0:
            on_alkuluku=False
            break

    vastaus={
        'Number' : luku,
        'isPrime' : on_alkuluku
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)