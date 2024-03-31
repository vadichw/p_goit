import asyncio
import websockets


async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
            print('Message received from client: ', message)
            await websocket.send("Message from server: " + message)
        except Exception as e:
            print(e)
            break


async def main():
    async with websockets.serve(handler, "", 8001):  # listen at port 8001
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
