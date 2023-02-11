from flask import Flask,request,jsonify,render_template

bill = Flask(__name__)

# Route
#  "/" - Home page.
@bill.route("/")
def hello_world():
    return render_template("billinvoice.html")

@bill.route("/operation",methods=['POST'])
def math_operation():
    
    print (request.method)
    if(request.method == 'POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        num3=int(request.form['num3'])
        num4=int(request.form['num4'])
        num5=int(request.form['num5'])

        result = 0
        aftdiscounts = 0
        result = num1+num2+num3+num4+num5
        if result <=1000:
            aftdiscounts = result*.90
        elif result <=2000:
            aftdiscounts = result*.80
        elif result >2000:
            aftdiscounts = result*.70    
        else: 
            aftdiscounts = result*1

        pass_value = {
           "operation" : "add",
            "item1" :num1,
            "item2" :num2,
            "item3" :num3,
            "item4" :num4,
            "item5" :num2,
            "total" :result,
            "after discounts": aftdiscounts
        }
    return render_template('billpay.html',result=pass_value)  


@bill.route("/demo",methods=['POST'])
def demo_operation():
    
    if(request.method == 'POST'):
        operation=request.json['operation'] 
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        num3=int(request.json['num3'])
        num4=int(request.json['num4'])
        num5=int(request.json['num5'])

        result = 0
        aftdiscounts = 0
        result = num1+num2+num3+num4+num5
        if result <=1000:
            aftdiscounts = result*.90
        elif result <=2000:
            aftdiscounts = result*.80
        elif result >2000:
            aftdiscounts = result*.70    
        else: 
            aftdiscounts = result*1

        return jsonify("the operation is {} for a total of {} post the discount is {}".format(operation,result,aftdiscounts))  

@bill.route("/aboutus")
def aboutus():
    return "We are iNeuron - Praveen" 

# entry point is main
# 0.0.0.0 
# flask runs default on 5000

if __name__ == '__main__':
    bill.run(host='0.0.0.0', port=5002)