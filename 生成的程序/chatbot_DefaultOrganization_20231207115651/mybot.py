from wechaty import Wechaty
class MyBot(Wechaty):
    async def on_message(self, message):
        if message.text() == 'ding':
            await message.say('dong')
    async def start(self):
        await super().start()