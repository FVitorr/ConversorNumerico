import telebot
import convert as c
import os

#Chave da Api
KEY_API = ""
bot = telebot.TeleBot(KEY_API) #Iniciar bot

print("Bot Active")

@bot.message_handler(commands=["help"])
def set(mensagem):
    msg = '''❓Bot de Conversão de Numeros:
    -> Decimal - Binario:
            Sucessivas divisoes por 2,  até que o número a dividir seja um 1. 
            Quando se atinge o 1, devem ordenar-se os números que restam (restos) 
            do último ao primeiro. Esse será o número binário que procura.
    -> Decimal - Octal:
            Sucessivas divisoes por 8,  até que o número a dividir, não seja divisivel por 8. 
            Ordenar-se os números que restam (restos) do último ao primeiro. 
            Esse será o número Octal que procura.
    -> Decimal - Hexadecimal:
            Sucessivas divisoes por 16,  até que o número a dividir, não seja divisivel por 16. 
            Ordenar-se os números que restam (restos) do último ao primeiro. 
            Esse será o número Hexadecimal que procura.
            Lembrando que: 10 - A ; 11 - B ; 12 - C ; 13 - D ; 14 - E ; 15 - F 
    '''
    bot.reply_to(mensagem,msg)

def verificar(mensagem):
    print(mensagem.chat.id)
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """ -- Conversor Numerico --
    Informe Numero (base)
    Ex: 120(10) """
    try:
        num = mensagem.text
        msg = c.opInit(num=num)
        bot.reply_to(mensagem,msg)
    except:
        bot.reply_to(mensagem, texto)# marca a mensagem e envia


bot.polling() #loop Infinito do bot
