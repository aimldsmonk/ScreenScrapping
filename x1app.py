from flask import Flask,request,jsonify,render_template

app = Flask(__name__)

# Route
#  "/" - Home page.
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/operation",methods=['POST'])
def math_operation():
    if(request.method == 'POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        
        result = 0
        if operation == "add":
            result = num1+num2
        elif operation == "multiply":
            result = num1*num2
        elif operation == "divide":
            result = num1/num2
        else:
            result = num1-num2

    return render_template('results.html',result=result)  


@app.route("/demo",methods=['POST'])
def demo_operation():
    if(request.method == 'POST'):
        operation=request.json['operation'] 
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        
        result = 0
        if operation == "add":
            result = num1+num2
        elif operation == "multiply":
            result = num1*num2
        elif operation == "division":
            result = num1/num2
        else:
            result = num1-num2

        return jsonify("the operation is {} and the result is {}".format(operation,result))  

@app.route("/aboutus")
def aboutus():
    return "We are iNeuron" 

# entry point is main
# 0.0.0.0 
# flask runs default on 5000

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)