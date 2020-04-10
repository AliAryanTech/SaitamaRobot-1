import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

import tg_bot.modules.fun_strings as fun_strings
from tg_bot import dispatcher, OWNER_ID
from tg_bot.modules.disable import DisableAbleCommandHandler

from tg_bot.modules.helper_funcs.chat_status import is_user_admin
from tg_bot.modules.helper_funcs.extraction import extract_user


@run_async
def runs(bot: Bot, update: Update):
    update.effective_message.reply_text(random.choice(fun_strings.RUN_STRINGS))


@run_async
def slap(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    user = update.effective_user

    reply_text = message.reply_to_message.reply_text if message.reply_to_message else message.reply_text

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.SLAP_SAITAMA_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(chat.id, message.from_user.id, until_date=mutetime, can_send_messages=False)
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    temp = random.choice(fun_strings.SLAP_TEMPLATES)
    item = random.choice(fun_strings.ITEMS)
    hit = random.choice(fun_strings.HIT)
    throw = random.choice(fun_strings.THROW)

    reply = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)

    reply_text(reply, parse_mode=ParseMode.HTML)
    
    


@run_async
def shrug(bot: Bot, update: Update):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(r"¯\_(ツ)_/¯")
    
    
@run_async
def insult(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    user = update.effective_user
    user_id = extract_user(message, args)
    if user_id == OWNER_ID:
        message.reply_text("Listen here you little sh*t. I will not Insult my Owner")
        return
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.INSULT_STRINGS))
    
@run_async
def table(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.TABLE))


__help__ = """
 - /runs: reply a random string from an array of replies.
 - /insult: Reply to a text with /insult for insults.
 - /slap: slap a user, or get slapped if not a reply.
 - /shrug : get shrug XD.
 - /table : get flip/unflip :v.
"""

RUNS_HANDLER = DisableAbleCommandHandler("runs", runs)
INSULT_HANDLER = DisableAbleCommandHandler("insult", insult, pass_args=True)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap, pass_args=True)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug)
TABLE_HANDLER = DisableAbleCommandHandler("table", table)

dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)
dispatcher.add_handler(INSULT_HANDLER)

__mod_name__ = "Fun"
__command_list__ = ["runs", "slap", "insult", "shrug", "table"]
__handlers__ = [RUNS_HANDLER, SLAP_HANDLER, SHRUG_HANDLER, INSULT_HANDLER, TABLE_HANDLER]
