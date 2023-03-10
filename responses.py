import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'ayoko na suko na ako'
    elif p_message == 'mami':
        return 'crissy'
    elif p_message == "roll a dice":
        random_num = random.randint(1,7)
        return random_num
    
    return 'Hindi ko alam ano sinasabi mo'