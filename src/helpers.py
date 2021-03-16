import json
import io
import csv

# Gets the trial data in csv (with header) format.
def get_datafile(participant, datatype):
    contents = {
        "trialdata": {
            "function": lambda p: p.get_trial_data(),
            "headerline": "uniqueid,currenttrial,time,trialData\n"        
        }, 
        "eventdata": {
            "function": lambda p: p.get_event_data(),
            "headerline": "uniqueid,eventtype,interval,value,time\n"        
        }, 
        "questiondata": {
            "function": lambda p: p.get_question_data(),
            "headerline": "uniqueid,questionname,response\n"
        },
        }
    ret = contents[datatype]["headerline"] + contents[datatype]["function"](participant)
    return ret
        