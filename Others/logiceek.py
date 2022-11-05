import telegram.ext
import pandas_datareader as web
import matplotlib.pyplot as plt

TOKEN = '5452102958:AAG6RKUAnjOCSOIRPCyIL5YK3AolqRcjiPk'

def start(update, context):
    update.message.reply_text("Hello! Welcome To Logiceek!")

def help(update, context):
    update.message.reply_text("""
    The following commands are available:

    /start -> Welcome Message
    /help -> This Message
    /content -> Information About Logiceek
    /contact -> Information About Contact

    """)

def content(update, context):
    update.message.reply_text("We are a group of people who loves logic!")


def contact(update, context):
    update.message.reply_text("You can contact Shuilian through Channel Logiceek!")

def stock(update, context):
    ticker = context.args[0]
    data = web.DataReader(ticker,'yahoo')
    bmw = web.DataReader("BMW.DE","yahoo")
    bmw['Close'].plot()
    plt.show()
    price = data.iloc[-1]['Close']
    update.message.reply_text(f"the close price of {ticker} is {price:.2f}$!")
    price = data.iloc[-1]['Open']
    update.message.reply_text(f"the open price of {ticker} is {price:.2f}$!")
    


def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}")

updater = telegram.ext.Updater(TOKEN,use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start",start))
disp.add_handler(telegram.ext.CommandHandler("help",help))
disp.add_handler(telegram.ext.CommandHandler("content",content))
disp.add_handler(telegram.ext.CommandHandler("contact",contact))
disp.add_handler(telegram.ext.CommandHandler("stock",stock))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text,handle_message))



updater.start_polling()
updater.idle()