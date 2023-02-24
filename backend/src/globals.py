betbot_process = None
betbot_state = "not running"

def update_process(val):
    global betbot_process
    betbot_process = val

def update_state(val):
    global betbot_state
    betbot_state = val 