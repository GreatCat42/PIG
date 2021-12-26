from Tk2050 import *

stroke('')

fill('#000000')

rect(0,0,400,400)

fill('#00aa00')

line(0,200,400,200)

fill('#00ff00')

with open('./log.txt') as log_doc:
    log_content=log_doc.read()
    log_arr=log_content.split('\n')

    index=0

    while index < 2000:
        line(index/5,200-int(log_arr[index]), index/5+1, 200-int(log_arr[index]))
        index+=5

def draw():
    pass

loop()
