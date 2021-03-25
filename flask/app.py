# import the Flask class from the flask module
from flask import Flask, render_template


"""
# Minimum reproductible example

# Two questions:

1. Should we call function outside route functions? so that we have them available 
mumtiple route function?
If no, what is the other better solution?

2. How to user the same arguments without repeting them?
(i. e passing same argument to multile function --> render_template())
"""
app = Flask(__name__)



def dotest():
    one = 'one'
    print('one')
    return one


def dotest2():
    two = 'two'
    print('two')
    return two


def dotest3():
    three = 'three'
    print('three')
    return three


one = str(dotest())
two = dotest2()
three = dotest3()

args=dict(one=one, two=two, three=three)
print(args)

@app.route('/')
def home():
    print('foo')
    return render_template('welcome.html', 
    one=one, 
    two=two, 
    three=three)  




@app.route('/test_one')
def welcome():
    print('bar')
    return render_template('test_one.html', 
    one=one, 
    two=two, 
    three=three)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)