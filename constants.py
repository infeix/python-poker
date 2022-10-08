
EMPTY_TABLE = """
Poker 1.0                                                  
                                                           
                                                           
                                                           
                 [    ]  [    ]  [    ]                    
                /´´´´´´´´´´´```````````\\                   
               /                        \\                  
       [    ] |                          | [    ]          
              |                          |                 
       [    ] |                          | [    ]          
               \                        /                  
                \______________________/                   
                 [    ]  [    ]  [    ]                    
                                                           
                                                           
                                                           
"""

POT_POSITION = (7*60) + 24

TABLE_CARD_POSITIONS = {
        0:(8*60)+20,
        1:(8*60)+24,
        2:(8*60)+28,
        3:(8*60)+32,
        4:(8*60)+36
}

PLAYER_POSITIONS = {
        4:(4*60)+19,
        5:(4*60)+27,
        6:(4*60)+35,
        3:(7*60)+9,
        7:(7*60)+45,
        2:(9*60)+9,
        8:(9*60)+45,
        1:(12*60)+19,
        0:(12*60)+27,
        9:(12*60)+35
}

BET_POSITIONS = {
        4:(5*60)+19,
        5:(5*60)+27,
        6:(5*60)+35,
        3:(7*60)+16,
        7:(7*60)+38,
        2:(9*60)+16,
        8:(9*60)+38,
        1:(11*60)+19,
        0:(11*60)+27,
        9:(11*60)+35
}


DEALER_POSITIONS = {
        4:(4*60)+17,
        5:(4*60)+25,
        6:(4*60)+33,
        3:(7*60)+14,
        7:(7*60)+43,
        2:(9*60)+14,
        8:(9*60)+43,
        1:(12*60)+17,
        0:(12*60)+25,
        9:(12*60)+33
}

PLAYER_CARD_POSITIONS = {
        4:(3*60)+19,
        5:(3*60)+27,
        6:(3*60)+35,
        3:(7*60)+2,
        7:(7*60)+51,
        2:(9*60)+2,
        8:(9*60)+51,
        1:(13*60)+19,
        0:(14*60)+27,
        9:(13*60)+35
}

CARDS = [
        'A+',
        '2+',
        '3+',
        '4+',
        '5+',
        '6+',
        '7+',
        '8+',
        '9+',
        'T+',
        'J+',
        'Q+',
        'K+',
        'A!',
        '2!',
        '3!',
        '4!',
        '5!',
        '6!',
        '7!',
        '8!',
        '9!',
        'T!',
        'J!',
        'Q!',
        'K!',
        'A?',
        '2?',
        '3?',
        '4?',
        '5?',
        '6?',
        '7?',
        '8?',
        '9?',
        'T?',
        'J?',
        'Q?',
        'K?',
        'A>',
        '2>',
        '3>',
        '4>',
        '5>',
        '6>',
        '7>',
        '8>',
        '9>',
        'T>',
        'J>',
        'Q>',
        'K>'
]