import asyncio


async def echo_server():
    print('Serving on localhost:8000')
    await asyncio.start_server(handle_connection,
                               'localhost', 8000)


async def handle_connection(reader, writer):
    print('New connection...')

    while True:
        data = await reader.read(8192)

        if not data:
            break

        print('Sending {:.10}... back'.format(repr(data)))
        writer.write(data)


loop = asyncio.new_event_loop()
loop.run_until_complete(echo_server())
try:
    loop.run_forever()
finally:
    loop.close()