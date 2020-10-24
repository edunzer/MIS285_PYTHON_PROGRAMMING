## SENTENCE CAPITALIZER

def capitalize ():
    user_input = input('Enter a sentence/sentences please:')
    sentences = user_input.split('.')
    for sentence in sentences:
        print (sentence.strip().capitalize()+". ",end='')


capitalize()
