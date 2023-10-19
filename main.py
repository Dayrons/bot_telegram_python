import telebot
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import re
load_dotenv()


bot  = telebot.TeleBot(os.getenv('TOKEN_TELEGRAM'))

@bot.message_handler(commands=["help", "start"])
def  calculator(message):
 
    response =  requests.get('https://www.bcv.org.ve/')
    page_parse = BeautifulSoup(response.content, "html.parser")
    
    result = page_parse.find("div", id="dolar")
    
    tasa = int(result.find("strong").text) 
   
    bot.reply_to(message,"Hola como estas?")



@bot.message_handler(func=lambda message:True,regexp="dolar")
def mensjae(message):
    
    
    regex = re.findall("\d", message.text)

    valor = ""
    for i in regex:
        valor+=str(i)

    response =  requests.get('https://www.bcv.org.ve/')
    page_parse = BeautifulSoup(response.content, "html.parser")
    
    result = page_parse.find("div", id="dolar")
    
    result  = result.find("strong").text.replace(",",".")
    
    tasa = float(result)
     
    monto = int(valor)
    
    result = monto / tasa
    bot.reply_to(message,f"Resultado :{round(result, 2)}")
    

@bot.message_handler(func=lambda message:True,regexp="Bolivares")
def mensjae(message):
    
    
    regex = re.findall("\d", message.text)

    valor = ""
    for i in regex:
        valor+=str(i)

    response =  requests.get('https://www.bcv.org.ve/')
    page_parse = BeautifulSoup(response.content, "html.parser")
    
    result = page_parse.find("div", id="dolar")
    
    result  = result.find("strong").text.replace(",",".")
    
    tasa = float(result)
     
    monto = int(valor)
    
    result = monto * tasa
    bot.reply_to(message,f"Resultado :{round(result, 2)}")

    
    
    
bot.polling()