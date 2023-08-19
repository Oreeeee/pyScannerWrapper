import time, random, sys


def main():
    while True:
        sys.stdout.write("Discovered open port 80/tcp on 127.0.0.1\n")
        sys.stdout.flush()
        time.sleep(random.random())


if __name__ == "__main__":
    main()
