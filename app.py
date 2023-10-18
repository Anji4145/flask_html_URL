from flask import Flask,render_template



FAI = Flask(__name__)


@FAI.route('/wish/<name>')
def wish(name):
    return f'hi! {name} how are u '

@FAI.route('/first')
def first():
    return render_template('first.html',name='anji')


@FAI.route('/second')
def second():
    return  render_template('second.html')


if __name__=='__main__':
    FAI.run(debug=True)