import sys, detectEnglish
"""
#straymarcs.net 
LETTERS=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
list={}
while 1:    #<<while loop
    mode = raw_input("Select a mode: ('e' to encrypt, 'd' to decrypt, 'h' to hack, 'q' to quit):  ") #raw_input is a cin with a label
    if mode=="q":
        break
    message = raw_input('What is your message? ')   #<< all variables generic based off of what the input is
    
    if (mode=="e" or mode=="d"): 
        while True:
                    try:
                            key = int(raw_input("Enter a key(must be an interger): "))
                    except valueError:
                            print("your key must be an interger.")
                            continue 
                    else:
                            break
        translated = ''
        for symbol in message: # for each in java instantiates symbol
            if  symbol in LETTERS:
                num=LETTERS.find(symbol)    #int of symbol in letters
                if  mode== 'e':
                    num= num+key
                elif mode == 'd': # else if
                    num= num - key

                if num >= len(LETTERS): # len(arr) = length of arr
                    num = num-len(LETTERS)
                elif num<0:
                    num = num +len(LETTERS)
                translated = translated + LETTERS[num]  # variable[] = treat as array                    else:
            else:
                translated = translated + symbol
        print       #CRLF
        print translated #  prints translated... do i need ()?
    elif (mode == "h"):
        for key in range(len(LETTERS)):
            # It is important to set translated to the blank string so that the
            # previous iteration's value for translated is cleared.
            translated = ''
            # run the encryption/decryption code on each symbol in the message
            for symbol in message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol) # get the number of the symbol
                    num = num - key
                    # handle the wrap-around if num is 26 or larger or less than 0
                    if num < 0:
                        num = num + len(LETTERS)

                    # add number's symbol at the end of translated
                    translated = translated + LETTERS[num]

                else:
                    # just add the symbol without encrypting/decrypting
                    translated = translated + symbol

            # display the current key being tested, along with its decryption
            print('Key #%s: %s' % (key, translated))
            if detectEnglish.isEnglish(translated):
                # Check with user to see if the decrypted key has been found.
                print("***")
                print('Possible encryption hack:')
                list[translated]=key
                print('Key %s: %s' % (key, translated))
                print("***")
    else:
        print "You have selected an improper option"
    print "\n"
        
    print "possible keys:"
    for n in list :
        print "Key:%s  Message: %s" %(list[n], n) 
    print "\n*****************************************************************\n"
"""


def cc_encrypt():
    LETTERS=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

    message= raw_input("Enter message to encrypt:")  #<< all variables generic based off of what the input is
    key = raw_input("Enter key")
    translated = ''
    for symbol in message: # for each in java instantiates symbol
        if  symbol in LETTERS:
            num=LETTERS.find(symbol)+key    #int of symbol in letters
            if num >= len(LETTERS): # len(arr) = length of arr                    
                num = num-len(LETTERS)
            elif num<0:
                num = num +len(LETTERS)
                translated = translated + LETTERS[num]  # variable[] = treat as array                    else:
            else:
                translated = translated + symbol
    print       #CRLF
    print translated


def cc_decrypt():
    #straymarcs.net 
    LETTERS=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    
    message= raw_input("Enter message to decrypt:") 
    key = raw_input("Enter key")       
    translated = ''
    for symbol in message: # for each in java instantiates symbol
        if  symbol in LETTERS:
            num=LETTERS.find(symbol)-key    #int of symbol in letters
            if num >= len(LETTERS): # len(arr) = length of arr
                num = num-len(LETTERS)
            elif num<0:
                num = num +len(LETTERS)
                translated = translated + LETTERS[num]  # variable[] = treat as array                    else:
            else:
                translated = translated + symbol
        print       #CRLF
        print translated #  prints translated... do i need ()?

def cc_hack():
    LETTERS=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    list={}
    message= raw_input("Enter message to hack:")

    for key in range(len(LETTERS)):
# It is important to set translated to the blank string so that the
# previous iteration's value for translated is cleared.
        translated = ''
# run the encryption/decryption code on each symbol in the message
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol) # get the number of the symbol
                num = num - key
# handle the wrap-around if num is 26 or larger or less than 0
                if num < 0:
                    num = num + len(LETTERS)
# add number's symbol at the end of translated
                    translated = translated + LETTERS[num]
                else:
# just add the symbol without encrypting/decrypting
                    translated = translated + symbol
# display the current key being tested, along with its decryption
    print('Key #%s: %s' % (key, translated))
    if detectEnglish.isEnglish(translated):
# Check with user to see if the decrypted key has been found.
        print("***")
        print('Possible encryption hack:')
        list[translated]=key
        print('Key %s: %s' % (key, translated))
        print("***")
        
    print "possible keys:"
    for n in list :
        print "Key:%s  Message: %s" %(list[n], n) 
    print "\n*****************************************************************\n"









