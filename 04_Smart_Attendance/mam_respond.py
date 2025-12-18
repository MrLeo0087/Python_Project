import random
def mam_respond_present():
        present_responses = [
        "Thank you",
        "Okay",
        "Good",
        "Alright",
        "Fine",
        "Done",
        "Perfect",
        "Yes",
        "Great",
        "Thanks",
        "Hmm",
        "Okay done"]

        respond = random.choice(present_responses)
        return respond

def mam_respond_absent():
    absent_responses = [
    "Okay",
    "Marked absent",
    "Not present",
    "Hmm",
    "Got it",
    "Absent",
    "Alright",
    "Noted",
    "Fine",
    ]
    respond = random.choice(absent_responses)
    return respond
 
        
