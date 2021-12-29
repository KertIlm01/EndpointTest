import requests
import json
import re
import time
import calendar

calculate1_results = {"totalRepayableAmount":202052.04,"monthlyPayment":2886.45,"apr":11.4}
calculate2_results = {"totalRepayableAmount":11032.47,"monthlyPayment":919.38,"apr":38.46}

def init():
    global logFileName
    global startTime
    startTime = str(calendar.timegm(time.gmtime()))
    print("Start time: ",startTime)
    logFileName = "logFile_"+startTime+".log"
    print(logFileName)

def log(text):
    logFile = open(logFileName,"a")
    logFile.write("\n"+str(text))
    logFile.close()



def verifyResults(result,desiredResult):
    desiredjson = json.dumps(desiredResult,separators=(',', ':'))
    if result == str(desiredjson):
        log("Test : PASS")
        print("Pass")
    else:
        log("FAIL : \n"+ "Result not matching\n"+ "desired result:\n"+str(desiredjson)+"Actual result:\n"+str(result) )
        print("desired: ")
        print(str(desiredjson))
        print("Actual result")
        print(str(result))
    

def calculate(length,amount,interest,desiredResults):
    URL = "https://ansokan.bigbank.se/api/v1/loan/calculate"
    parameters = {"maturity":length,"productType":"LOANSE02","amount":amount,"interestRate":interest,"monthlyPaymentDay":27,"administrationFee":40,"conclusionFee":695,"currency":"SEK"}
    response =  requests.post(URL,json = parameters)
    log("calculation response:\n"+response.text)
    verifyResults(response.text,desiredResults)
    return response.text



def testCalculation(length,amount,interest,desiredResults):
    log("running test with parameters: \nlength: "+str(length)+"\namount: "+ str(amount)+ "\ninterest: "+str(interest))
    results = calculate(length,amount,interest,desiredResults)

    



init()
log("\n\nStart running test calculate1")
testCalculation(70,150000,10,calculate1_results) #period in months, amount, interest rate
log("\n\nStart running test calculate1")
testCalculation(12,10000,10,calculate2_results)