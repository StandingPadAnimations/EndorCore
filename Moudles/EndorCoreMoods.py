import random
# from nltk.util import ngrams
# import re 

class Mood(object):
    def __init__(self):
        self.responses = []
        self.sleep_responses = []
        self.out4 = []
        self.out3 = []
        
    def mood_response(self):
        # rand_response = random.choice(self.responses)  
        # self.out4 = list(ngrams(rand_response.split(), 4))
        # self.out3 = list(ngrams(rand_response.split(), 3))
        # rand_response3 = random.choice(self.out3)  

        # return " ".join(rand_response3);

        rand_response = random.choice(self.responses)
        return rand_response
    
    def sleep_mood_response(self):
        rand_sleep_response = random.choice(self.sleep_responses)  
        return rand_sleep_response

##############################################################################################################################################

class Happy(Mood):
    def __init__(self):
        self.responses = [
        "good", 
        "fine, how are you?", 
        "understandable, have a great day", 
        "Reddit is wonderful", 
        "Python is better then JavaScript and C++", 
        "The dev cat speel :p", 
        "Hi guys! Today’s going great! ᕕ( ᐛ )ᕗ",
        "c:"
        ]
        
        self.sleep_responses = [
        "ok", 
        "Good night", 
        "Off to dreamland!!!"
        ]

        self.out4 = []
        self.out3 = []
        self.happy_responses = self.responses
        self.happy_sleep_responses = self.sleep_responses

##############################################################################################################################################

class Angry(Mood):
    def __init__(self):
        self.responses = [
        "That stupid fan in StandingPad's Raspberry Pi won't shut up", 
        '''I'M TRYING TO STUDY FOR A MATH TEST!!!!!!!''', 
        "will you shut up man?", 
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAA", 
        "Curse autocorrect", 
        "Can you shut up for 5 MINUTES?!?!?!", 
        "May you please stop asking?", 
        "If you won't shut up, I'll just stop here", 
        "Angry Noises", 
        "for goodness sake, LET ME WATCH YOUTUBE!!!!!!!! >:c", 
        "angry garbling noises SOMEONE STOLE MY MUFFINS"
        ]
        
        self.sleep_responses = [
        "NOOOOOOOOOOOOOOOOOOOOOOOO SLEEEEEEEEEEEEEEEP",
        "I will refuse to sleep", 
        "no", 
        "no I don't think I will", 
        "but do I need sleep?"
        ]

        self.out4 = []
        self.out3 = []
        self.mad_responses = self.responses
        self.mad_sleep_responses = self.sleep_responses

##############################################################################################################################################

class Sad(Mood):
    def __init__(self):
        self.responses = [
        "not good :c", 
        "I hate 31 C temperature, it's too cold :c", 
        ]
        
        self.sleep_responses = [
        "ok :c"
        ]

        self.out4 = []
        self.out3 = []
        self.sad_responses = self.responses
        self.sad_sleep_responses = self.responses

##############################################################################################################################################

class Tired(Mood):
    def __init__(self):
        self.responses = [
        "not good :c", 
        "I may have stayed up all night....", 
        "That stupid fan in StandingPad's Raspberry Pi won't shut up", 
        "falls to ground", 
        "I need a cup of tea", 
        "slams head on CPU", 
        "massive yawn"
        ]
        
        self.sleep_responses = [
        "sleep...... falls asleep"
        ]

        self.out4 = []
        self.out3 = []
        self.tired_responses = self.responses
        self.tired_sleep_responses = self.sleep_responses

##############################################################################################################################################

class OwO(Happy):
    def __init__(self):
        super().__init__()
        
        self.responses = [
        "owo", 
        "uwu", 
        "happy endorcore noises", 
        "murders and commits genocide cutely"
        ] + self.happy_responses
        
        self.sleep_responses = [
        ":3 ok"
        ] + self.happy_sleep_responses
        
        self.out4 = []
        self.out3 = []
        self.owo_responses = self.responses
        self.owo_sleep_responses = self.sleep_responses
