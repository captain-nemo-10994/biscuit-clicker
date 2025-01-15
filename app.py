from flask import Flask, render_template, request

app = Flask(__name__)

click_power = 1
auto_click = 0

def get_biscuits():
    return int(request.json.get("biscuits"))

def get_click_cost_val():
    return int(request.json.get("clickCostVal"))

def get_auto_cost_val():
    return int(request.json.get("autoCostVal"))

@app.route("/increment", methods=["POST"])
def increment():
    global click_power
    biscuits = get_biscuits()
    biscuits = biscuits + click_power
    return {"answer": biscuits}

@app.route("/oneUp", methods=["POST"])
def oneUp():
    global click_power
    biscuits = get_biscuits()
    clickCostVal = get_click_cost_val()
    if biscuits >= clickCostVal:
        click_power = click_power + 1
        return {"biscuits": biscuits-clickCostVal, "clickCostVal":clickCostVal+(click_power*click_power)}
    else:
        return{"biscuits":biscuits, "clickCostVal":clickCostVal}

@app.route("/buyAutoClick", methods=["POST"])
def buyAutoClick():
    global auto_click
    biscuits = get_biscuits()
    autoCostVal = get_auto_cost_val()
    if biscuits >= autoCostVal:
        auto_click = auto_click + 1
        return {"biscuits": biscuits-autoCostVal, "autoCostVal":autoCostVal+(auto_click*auto_click)}
    else:
        return {"biscuits":biscuits, "autoCostVal":autoCostVal}

@app.route("/autoClick", methods=["POST"])
def autoClick():
    global auto_click
    biscuits = get_biscuits()
    biscuits = biscuits + auto_click
    return {"biscuits":biscuits}

@app.route("/")
def hello_world():
    return render_template("index.html")
