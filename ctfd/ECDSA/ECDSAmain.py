import os
import random
from typing import Generator, Optional

# install pycryptodome from pypi to get Crypto
import Cryptodome.Hash.SHA256
import Cryptodome.PublicKey.ECC
import Cryptodome.Signature.DSS
import trio

HOST = "ctf.afnom.net"
PORT = 1337
FLAG = "AFNOM{}"


# Credit to Nathaniel J. Smith for this class (CC0 licensed)
class LineReader:
    def __init__(self, stream: trio.SocketStream, max_line_length: int = 16384) -> None:
        self.stream = stream
        self._line_generator = self.generate_lines(max_line_length)

    @staticmethod
    def generate_lines(max_line_length: int) -> Generator[Optional[bytes], bytes, None]:
        buf = bytearray()
        find_start = 0
        while True:
            newline_idx = buf.find(b"\n", find_start)
            if newline_idx < 0:
                if len(buf) > max_line_length:
                    raise RuntimeError("line too long")
                find_start = len(buf)
                more_data = yield None
            else:
                line = buf[:newline_idx]
                del buf[: newline_idx + 1]
                find_start = 0
                more_data = yield line

            if more_data is not None:
                buf += bytes(more_data)

    async def readline(self) -> bytes:
        line = next(self._line_generator)
        while line is None:
            more_data = await self.stream.receive_some(1024)
            if not more_data:
                raise RuntimeError("client hung up")
            line = self._line_generator.send(more_data)
        return line


async def main() -> None:
    await trio.serve_tcp(process_connection, host=HOST, port=PORT)


async def process_connection(stream: trio.SocketStream) -> None:
    curve = "P-256"
    mode = "fips-186-3"
    local_random = random.Random()
    local_random.seed(os.urandom(128))
    key = Crypto.PublicKey.ECC.generate(curve=curve)
    ecdsa = Crypto.Signature.DSS.new(key, mode, randfunc=local_random.randbytes)
    reader = LineReader(stream)
    try:
        await stream.send_all(b"Welcome to the ECDSA crypto toolbox!")
        await main_menu(stream, reader, local_random, ecdsa)
    except Exception:
        pass
    finally:
        await stream.aclose()


async def main_menu(
    stream: trio.SocketStream,
    reader: LineReader,
    local_random: random.Random,
    ecdsa: Cryptodome.Signature.DSS.FipsEcDsaSigScheme,
) -> None:
    client_message_signed = False
    while True:
        await stream.send_all(
            b"\nMenu:\n1. Generate random number\n2. Sign data\n3. Debug menu\n4. Quit\n"
        )
        result = (await reader.readline()).decode()
        if result == "1":
            await stream.send_all(str(local_random.getrandbits(32)).encode() + b"\n")
        elif result == "2":
            if not client_message_signed:
                client_message_signed = True
                await stream.send_all(b"Send message to sign\n")
                to_sign = await reader.readline()
                signature = ecdsa.sign(Crypto.Hash.SHA256.new(to_sign))
                await stream.send_all(
                    b"Your signature is: " + signature.hex().encode() + b"\n"
                )
            else:
                await stream.send_all(
                    b"You've already had something signed. Calculating those signatures is expensive you know!\n"
                )
        elif result == "3":
            message = os.urandom(128)
            await stream.send_all(
                b"Sign the following to verify credentials: "
                + message.hex().encode()
                + b"\n"
            )
            signature = await reader.readline()
            try:
                ecdsa.verify(
                    Crypto.Hash.SHA256.new(message),
                    bytes.fromhex(signature.decode()),
                )
            except ValueError:
                await stream.send_all(b"Incorrect signature\n")
            else:
                await stream.send_all(b"Verification successful!\n")
                await debug_menu(stream, reader)

        elif result == "4":
            await stream.send_all(b"Bye!\n")
            await stream.send_eof()
            break
        else:
            await stream.send_all(b"Unknown option\n")
            await stream.send_eof()
            raise RuntimeError("unknown option at main menu")


async def debug_menu(stream: trio.SocketStream, reader: LineReader) -> None:
    while True:
        await stream.send_all(
            b"\nDebug menu:\n1. Retrieve local\n2. Retrieve global\n3. Return\n"
        )
        result = (await reader.readline()).decode()
        if result == "1":
            await stream.send_all(b"Enter local name\n")
            name = await reader.readline()
            await stream.send_all(str(locals().get(name.decode())).encode() + b"\n")
        elif result == "2":
            await stream.send_all(b"Enter global name\n")
            name = await reader.readline()
            await stream.send_all(str(globals().get(name.decode())).encode() + b"\n")
        elif result == "3":
            return
        else:
            await stream.send_all(b"Unknown option\n")
            await stream.send_eof()
            raise RuntimeError("unknown option at debug menu")


if __name__ == "__main__":
    trio.run(main)
