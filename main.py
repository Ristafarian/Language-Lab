from language import *

def main():
    application = QApplication([])
    window = Language()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()