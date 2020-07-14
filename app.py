import asyncio

import websockets as websockets


class Application(object):
    def Start(self):
        async def echo(websocket, path):
            async for message in websocket:
                #отправляем назад строку в верхнем регистре
                await websocket.send(message.upper())

        asyncio.get_event_loop().run_until_complete(
            websockets.serve(echo, '', 8765))
        asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    app = Application()
    app.Start()