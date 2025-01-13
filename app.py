from flask import Flask, render_template, request

app = Flask(__name__)

click_power = 1
auto_click = 0

@app.route("/increment", methods=["POST"])
def increment():
    global click_power
    biscuits = request.json.get("biscuits")
    biscuits = int(biscuits)

    print("Old number: " + str(biscuits))

    biscuits = biscuits + click_power

    print("New number: " + str(biscuits))

    return {"answer": biscuits}

@app.route("/oneUp", methods=["POST"])
def oneUp():
    global click_power
    biscuits = request.json.get("biscuits")
    biscuits = int(biscuits)

    clickCostVal = request.json.get("clickCostVal")
    clickCostVal = int(clickCostVal)

    if biscuits >= clickCostVal:
        click_power = click_power + 1
        return {"biscuits": biscuits-clickCostVal, "clickCostVal":clickCostVal+(click_power*click_power)}
    else:
        print("Not enough biscuits")
        return{"biscuits":biscuits, "clickCostVal":clickCostVal}

@app.route("/buyAutoClick", methods=["POST"])
def buyAutoClick():
    global auto_click
    biscuits = request.json.get("biscuits")
    biscuits = int(biscuits)

    autoCostVal = request.json.get("autoCostVal")
    autoCostVal = int(autoCostVal)

    if biscuits >= autoCostVal:
        auto_click = auto_click + 1
        return {"biscuits": biscuits-autoCostVal, "autoCostVal":autoCostVal+(auto_click*auto_click)}
    else:
        print("Not enough biscuits")
        return {"biscuits":biscuits, "autoCostVal":autoCostVal}

@app.route("/autoClick", methods=["POST"])
def autoClick():
    global auto_click
    biscuits = request.json.get("biscuits")
    biscuits = int(biscuits)

    biscuits = biscuits + auto_click
    return {"biscuits":biscuits}

@app.route("/")
def hello_world():

    return render_template("index.html")
