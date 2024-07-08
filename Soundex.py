def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def check_condition(present, previous):
    return ((present != '0') + (present != previous))

def soundex_generator(ip_string):
    
    soundex = ip_string[0].upper()
    prev_code = get_soundex_code(soundex)
    for char in ip_string[1:]:
        code = get_soundex_code(char)
        if (check_condition(code, prev_code) > 1):
            soundex += code
            prev_code = code
    return soundex

def generate_soundex(name):
    if not name :
        return ""
        
    res = soundex_generator(name)
    # Pad with zeros
    res += "0000"
    return res[:4]
