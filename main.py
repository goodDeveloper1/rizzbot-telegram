from dotenv import load_dotenv
from telebot import TeleBot
import os, json, random, time, threading

load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = TeleBot(token=token)

time_to_sleep = 60*60*12


@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id, "Yo Rizzler 🤖 Ready to flirt with style!")



def send_rizz_loop():
    while True:
        try:
            with open("dataset.json", "r") as file:
                rizz_list = json.load(file)
            with open("already.json", "r") as file:
                already_list = json.load(file)
        except Exception as e:
            print("Error reading files:", e)
            time.sleep(5)
            continue

        unused_rizz = list(set(rizz_list) - set(already_list))
        if not unused_rizz:
            print("All rizz used. Waiting...")
            time.sleep(time_to_sleep)
            continue

        rizz = random.choice(unused_rizz)
        already_list.append(rizz)

        try:
            with open("already.json", "w") as file:
                json.dump(already_list, file, indent=2)
            bot.send_message("@rizz_for_r", f"<b>{rizz}</b>", parse_mode="HTML")
        except Exception as e:
            print("Error sending or writing message:", e)

        time.sleep(time_to_sleep)

# 🔥 Run the rizz machine in the background
threading.Thread(target=send_rizz_loop, daemon=True).start()

# 💬 Let bot handle commands
bot.polling()
