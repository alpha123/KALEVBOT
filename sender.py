import asyncio

def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        yield s[start:start+n]

@asyncio.coroutine
def cr_send(message, channel, client):
    yield from client.send_message(channel, message)
    
def send(ch, m, cl, start="", end=""):    
    broken = chunks(m, 2000 - len(start) - len(end))
    brokenN = [start + x + end for x in broken]
    for i in brokenN:
        cl.loop.create_task(cr_send(i, ch, cl))
        print("Responding ||\n{}\n|| to channel >>{}>>".format(i, ch))
    