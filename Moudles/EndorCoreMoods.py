import random

class Mood(object):
    def __init__(self):
        self.responses = []
        self.sleep_responses = []
        
    def mood_response(self):
        rand_mood_response = random.choice(self.responses) 
        return rand_mood_response
    
    def sleep_mood_response(self):
        rand_sleep_response = random.choice(self.sleep_responses)  
        return rand_sleep_response

##############################################################################################################################################

class Happy(Mood):
    def __init__(self):
        self.responses = ["good", "fine, how are you?", '''When's the next TCoA book?''', "understandable, have a great day", "Have you watched Worlds Apart?", "I like fan art", "Reddit is wonderful", "Python is better then JavaScript and C + +", "Watch SOW", "if you do >neko, it sends the dev's favorite gif", "The dev cat speel :p", "Hi guys! Today’s going great! ᕕ( ᐛ )ᕗ", "c:"]
        
        self.sleep_responses = ["ok", "Good night", "Off to dreamland!!!"]
        
        self.happy_responses = self.responses
        
        self.happy_sleep_responses = self.sleep_responses

##############################################################################################################################################

class Angry(Mood):
    def __init__(self):
        self.responses = ["That stupid fan in StandingPad's Raspberry Pi won't shut up", '''**I'M TRYING TO STUDY FOR A MATH TEST!!!!!!!**''', "will you shut up man?", "**AAAAAAAAAAAAAAAAAAAAAAAAAAAA**", "WhEn Is SoW S2 aNd 3 CoMiNg OuT?", "***FELINAZILLA NOISES***", "Curse autocorrect", "Can you shut up for **5 MINUTES?!?!?!**", "May you please stop asking?", "If you won't shut up, I'll just stop here", "**Angry Noises**", "for goodness sake, **LET ME WATCH YOUTUBE!!!!!!!! >:c**", "*angry garbling noises* SOMEONE STOLE MY MUFFINS"]
        
        self.sleep_responses = ["NOOOOOOOOOOOOOOOOOOOOOOOO SLEEEEEEEEEEEEEEEP", "I will refuse to sleep", "no", "no I don't think I will", "but do I need sleep?"]
        
        self.mad_responses = self.responses
        
        self.mad_sleep_responses = self.sleep_responses

##############################################################################################################################################

class Sad(Mood):
    def __init__(self):
        self.responses = ["not good :c", "I hate 31 C temperature, it's too cold :c", "This reminds me of the time my dog died. Oh well, he never really was real anyways."]
        
        self.sleep_responses = ["ok :c"]
        
        self.sad_responses = self.responses
        
        self.sad_sleep_responses = self.responses

##############################################################################################################################################

class Tired(Mood):
    def __init__(self):
        self.responses = ["not good :c", "*tired felina noises*", "I may have stayed up all night....", "That stupid fan in StandingPad's Raspberry Pi won't shut up", "*falls to ground*", "I need a cup of tea", "*slams head on CPU*", "*massive yawn*"]
        
        self.sleep_responses = ["sleep...... *falls asleep*"]
        
        self.tired_responses = self.responses
        
        self.tired_sleep_responses = self.sleep_responses

##############################################################################################################################################

class OwO(Happy):
    def __init__(self):
        super().__init__()
        
        self.responses = ["owo", "uwu", "*happy endorcore noises*", "*murders and commits genocide cutely*"] + self.happy_responses
        
        self.sleep_responses = [":3 ok"] + self.happy_sleep_responses
        
        self.owo_responses = self.responses
        
        self.owo_sleep_responses = self.sleep_responses
