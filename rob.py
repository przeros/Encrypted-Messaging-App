from encryptor import Encryptor
from fileHandler import FileHandler
from globals import HOST_IP, RECIPIENT_IP, ROB_PUBLIC_KEY_PATH, ROB_PRIVATE_KEY_PATH, ROB_SERVER_PORT, ROB_CLIENT_PORT
from GUI import GUI


def main():
    encryptor = Encryptor(ROB_PRIVATE_KEY_PATH, ROB_PUBLIC_KEY_PATH)
    encryptor.generateKeys()
    fileHandler = FileHandler()
    gui = GUI(encryptor, fileHandler, HOST_IP, RECIPIENT_IP, ROB_SERVER_PORT, ROB_CLIENT_PORT)
    gui.run()


if __name__ == '__main__':
    main()
