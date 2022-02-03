# discordbotgui
Show the channels and messages that the bot can see in the gui.
このコードを利用してBotが見れるチャンネルやメッセージを表示します
このコードを使用する際は別ファイルでdiscord botのclientを起動して
viewbotgui.start_up()関数をon_ready内で実行してください。
プロセスを分けないとBotが反応しなくなります
例

import viewbotgui
intent=discord.Intents.all()
discord.member=True
client = commands.Bot(command_prefix='!',intents=intent)

@client.event
async def on_ready():
   viewbotgui.start_up(client)

client.run("Your Token")
