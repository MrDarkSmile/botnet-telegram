import os
try:
  from pyrogram import Client , filters
  import pyromod.listen
except:
  os.system("python3 -m pip install pip --upgrade")
  os.system("pip install pyrogram pyromod")
  os.system("clear")
  from pyrogram import Client , filters
  import pyromod.listen
import subprocess
import time
app = Client(
  "my_account",
  bot_token = "",
  api_id=,
  api_hash=""
  )




@app.on_message(filters.command("help","/"))
async def helper(cli,msg):
  text = """
**DarkSmile Bot**
------------------------
/show 
for show the online bots
برای نمایش ربات های آنلاین
------------------------
/ping
for show speed of bots
برای نمایش سرعت ربات ها
------------------------
/run command
جهت اجرای دستورات خط فرمان ، به جای command دستور دلخواه را بزارید
------------------------
/run
جهت اجرای دستورات خط فرمان ، جهت اجرا ابتدا /run را بزنید سپس در پیام بعدی دستوارت را وارا کنید
------------------------
/file name
بجای name نام فایل دلخواه و در پیام بعدی ، محتویات مورد نظر جهت سیو را وارد کنید
**Developer : **@MrDarkSmileBot
  """
  await msg.reply(text)


@app.on_message(filters.command("show","/"))
async def check(cli,msg):
  await msg.reply("bot is on")



@app.on_message(filters.command("ping","/"))
async def ping(cli,msg):
  me = await msg.reply("ok")
  t1 = time.time()
  await me.edit("loading...")
  t2 = time.time()
  t3 = int(round(t2-t1,3)*1000)
  text = f"ping is {t3}ms"
  await me.edit(text)




@app.on_message(filters.command("run","/"))
async def run(cli,msg):
  try:
    command = str(msg.text).replace("/run ","")
    result = subprocess.check_output(command,shell=True).decode()
  except:
    command = await cli.ask(msg.chat.id,"**enter command to run**")
    result = subprocess.check_output(command.text,shell=True).decode()
  if len(result) > 0:
    await msg.reply("**Result : **\n"+result)
  else:
    await msg.reply("ok")




@app.on_message(filters.command("file","/"))
async def file(cli,msg):
  name = str(msg.text).replace("/file ","")
  print(name)
  t = f"**OK , Now Send Your Code To Save in {name}**"
  code = await cli.ask(msg.chat.id,t)
  with open(name,"w+") as f:
    f.write(code.text)
  await msg.reply("ok file was save")


app.run()