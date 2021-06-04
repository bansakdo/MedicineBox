# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from dosing import dosing1
from checkQuantity import measureQuantity, getQuantity
from entrance import slotOpen, slotClose
from showNeopixel import openDoor, closeDoor, showQuantity

app = Flask(__name__)

slotOpenStatus = [False, False, False, False, False, False]


# 약 제공
@app.route('/dosing', methods=['POST'])
def dosingApp():
    data = request.json
    print(data)
    slot = int(data['slot'])
    print(slot)
    result = dosing1(slot)
    if result == "true":
        return "true"
    elif result == "algument_error":
        return "Check slot number!"
    else:
        return "Fail to Dosing!"

    # 약 잔여량


@app.route('/getQuantity', methods=["GET", "POST"])
def getQuantityApp():
    if request.method == "POST":
        if measureQuantity() == "true":
            result = getQuantity()
        else:
            result = "Measure Error"
    else:
        print("asd")
        result = getQuantity()
    return result


# 약 투입구 열기
@app.route('/open/<int:slot_num>', methods=["GET"])
def openSlotApp(slot_num):
    slot = slot_num - 1

    if not slotOpenStatus[slot]:
        resultOpen = slotOpen(slot)
        slotOpenStatus[slot] = True
        openDoor(slot)
        resultClose = slotClose(slot)
        slotOpenStatus[slot] = False
        closeDoor(slot)
        showQuantity()
        if resultOpen == "true" and resultClose == "true":
            return "open success"
        else:
            return "open fail"

    elif slotOpenStatus[slot]:
        resultClose = slotClose(slot)
        slotOpenStatus[slot] = False

        if resultClose == "true":
            return "close success"
        else:
            return "close fail"
    else:
        return "false"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60002, debug=True)
