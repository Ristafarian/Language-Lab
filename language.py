from PyQt6.QtWidgets import *
from gui import *
import csv
import os


class Language(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Class initialization.
        """
        super().__init__()
        self.setupUi(self)
        self.reset()

        self.radio_spanish.toggled.connect(lambda: self.label_image.setPixmap(QtGui.QPixmap("langimages/spanish.jpg")))
        self.radio_french.toggled.connect(lambda: self.label_image.setPixmap(QtGui.QPixmap("langimages/french.jpg")))
        self.radio_korean.toggled.connect(lambda: self.label_image.setPixmap(QtGui.QPixmap("langimages/korean.png")))
        self.radio_japanese.toggled.connect(lambda: self.label_image.setPixmap(QtGui.
                                                                               QPixmap("langimages/japanese.png")))
        self.radio_other.toggled.connect(lambda: self.label_image.setPixmap(QtGui.QPixmap("langimages/main.png")))

        self.button_select.clicked.connect(lambda: self.select())
        self.button_enter.clicked.connect(lambda: self.enter())
        self.button_reset.clicked.connect(lambda: self.reset())

    def select(self) -> None:
        """
        Select language and open up dictionary entry options.
        """
        try:
            if self.radio_spanish.isChecked():
                pass
            elif self.radio_french.isChecked():
                pass
            elif self.radio_korean.isChecked():
                pass
            elif self.radio_japanese.isChecked():
                pass
            elif self.radio_other.isChecked():
                pass
            else:
                raise
            self.button_select.hide()
            self.label_select.hide()
            self.button_reset.show()
            self.button_enter.show()
            self.label_vocab.show()
            self.input_vocab.show()
            self.label_translation.show()
            self.input_translation.show()
            self.groupPOS.show()
            self.radio_noun.show()
            self.radio_pronoun.show()
            self.radio_adjective.show()
            self.radio_verb.show()
            self.radio_adverb.show()
            self.radio_preposition.show()
            self.radio_conjunction.show()
            self.radio_interjection.show()
            self.radio_determiner.show()
        except:
            self.label_select.setStyleSheet('color: red; font-weight: bold; background-color: rgb(255, 255, 127)')

    def enter(self) -> None:
        """
        Enter vocab-related data into language-specific dictionary.
        """
        try:
            if self.radio_spanish.isChecked():
                self.spanish()
            elif self.radio_french.isChecked():
                self.french()
            elif self.radio_korean.isChecked():
                self.korean()
            elif self.radio_japanese.isChecked():
                self.japanese()
            elif self.radio_other.isChecked():
                self.other()
            else:
                pass
        except:
            pass

    def reset(self) -> None:
        """
        Reset to language selection/initial configuration.
        """
        self.uncheck()
        self.label_image.setPixmap(QtGui.QPixmap("langimages/main.png"))
        self.input_other.clear()
        self.button_select.show()
        self.label_select.show()
        self.label_select.setStyleSheet('color: black; font-weight: regular; background-color: rgb(170, 85, 255)')
        self.button_reset.hide()
        self.button_enter.hide()
        self.label_enter.clear()
        self.label_vocab.hide()
        self.input_vocab.hide()
        self.label_translation.hide()
        self.input_translation.hide()
        self.groupPOS.hide()
        self.radio_noun.hide()
        self.radio_pronoun.hide()
        self.radio_adjective.hide()
        self.radio_verb.hide()
        self.radio_adverb.hide()
        self.radio_preposition.hide()
        self.radio_conjunction.hide()
        self.radio_interjection.hide()
        self.radio_determiner.hide()

    def part_of_speech(self) -> str:
        """
        Return string for part of speech (POS) based on radio button selection.
        Return 'Not Specified' if no button is selected; this is useful if unsure of POS.
        :return: String representing selected POS, or Not Specified if none selected.
        """
        if self.radio_noun.isChecked():
            return 'Noun'
        elif self.radio_pronoun.isChecked():
            return 'Pronoun'
        elif self.radio_adjective.isChecked():
            return 'Adjective'
        elif self.radio_verb.isChecked():
            return 'Verb'
        elif self.radio_adverb.isChecked():
            return 'Adverb'
        elif self.radio_preposition.isChecked():
            return 'Preposition'
        elif self.radio_conjunction.isChecked():
            return 'Conjunction'
        elif self.radio_interjection.isChecked():
            return 'Interjection'
        elif self.radio_determiner.isChecked():
            return 'Determiner'
        else:
            return 'Not Specified'

    def uncheck(self) -> None:
        """
        De-select all radio buttons.
        """
        self.radio_spanish.setAutoExclusive(False)
        self.radio_spanish.setChecked(False)
        self.radio_spanish.setAutoExclusive(True)
        self.radio_french.setAutoExclusive(False)
        self.radio_french.setChecked(False)
        self.radio_french.setAutoExclusive(True)
        self.radio_korean.setAutoExclusive(False)
        self.radio_korean.setChecked(False)
        self.radio_korean.setAutoExclusive(True)
        self.radio_japanese.setAutoExclusive(False)
        self.radio_japanese.setChecked(False)
        self.radio_japanese.setAutoExclusive(True)
        self.radio_other.setAutoExclusive(False)
        self.radio_other.setChecked(False)
        self.radio_other.setAutoExclusive(True)

        self.radio_noun.setAutoExclusive(False)
        self.radio_noun.setChecked(False)
        self.radio_noun.setAutoExclusive(True)
        self.radio_pronoun.setAutoExclusive(False)
        self.radio_pronoun.setChecked(False)
        self.radio_pronoun.setAutoExclusive(True)
        self.radio_adjective.setAutoExclusive(False)
        self.radio_adjective.setChecked(False)
        self.radio_adjective.setAutoExclusive(True)
        self.radio_verb.setAutoExclusive(False)
        self.radio_verb.setChecked(False)
        self.radio_verb.setAutoExclusive(True)
        self.radio_adverb.setAutoExclusive(False)
        self.radio_adverb.setChecked(False)
        self.radio_adverb.setAutoExclusive(True)
        self.radio_preposition.setAutoExclusive(False)
        self.radio_preposition.setChecked(False)
        self.radio_preposition.setAutoExclusive(True)
        self.radio_conjunction.setAutoExclusive(False)
        self.radio_conjunction.setChecked(False)
        self.radio_conjunction.setAutoExclusive(True)
        self.radio_interjection.setAutoExclusive(False)
        self.radio_interjection.setChecked(False)
        self.radio_interjection.setAutoExclusive(True)
        self.radio_determiner.setAutoExclusive(False)
        self.radio_determiner.setChecked(False)
        self.radio_determiner.setAutoExclusive(True)

    def spanish(self) -> None:
        """
        1st: Check for, then set up, Spanish directory/dictionary if they don't exist.
        2nd: Enter new vocab into dictionary.
        """
        directory = 'Spanish'
        path = './Spanish/Spanish Dictionary.csv'

        if os.path.exists(directory):
            pass
        else:
            os.makedirs('Spanish')

        if os.path.exists(path):
            pass
        else:
            with open('Spanish/Spanish Dictionary.csv', 'a', newline='')as data:
                content = csv.writer(data)
                content.writerow(['Vocab', 'Translation', 'P.O.S.'])

        try:
            self.label_enter.clear()

            if self.input_vocab.text() == '':
                raise
            else:
                pass

            if self.input_translation.text() == '':
                raise
            else:
                pass

            vocab = self.input_vocab.text()
            translation = self.input_translation.text()
            pos = self.part_of_speech()
            dict_entry = [vocab, translation, pos]

            with open('Spanish/Spanish Dictionary.csv', 'a', newline='')as data:
                content = csv.writer(data)
                content.writerow(dict_entry)

        except:
            self.label_enter.setText('Please enter vocab and translation')
            self.label_enter.setStyleSheet('color: black;')

    def french(self) -> None:
        """
        1st: Check for, then set up, French directory/dictionary if they don't exist.
        2nd: Enter new vocab into dictionary.
        """
        directory = 'French'
        path = './French/French Dictionary.csv'

        if os.path.exists(directory):
            pass
        else:
            os.makedirs('French')

        if os.path.exists(path):
            pass
        else:
            with open('French/French Dictionary.csv', 'a', newline='') as data:
                content = csv.writer(data)
                content.writerow(['Vocab', 'Translation', 'P.O.S.'])

        try:
            self.label_enter.clear()

            if self.input_vocab.text() == '':
                raise
            else:
                pass

            if self.input_translation.text() == '':
                raise
            else:
                pass

            vocab = self.input_vocab.text()
            translation = self.input_translation.text()
            pos = self.part_of_speech()
            dict_entry = [vocab, translation, pos]

            with open('French/French Dictionary.csv', 'a', newline='')as data:
                content = csv.writer(data)
                content.writerow(dict_entry)

        except:
            self.label_enter.setText('Please enter vocab and translation')
            self.label_enter.setStyleSheet('color: black;')

    def korean(self) -> None:
        """
        1st: Check for, then set up, Korean directory/dictionary if they don't exist.
        2nd: Enter new vocab into dictionary.
        """
        directory = 'Korean'
        path = './Korean/Korean Dictionary.csv'

        if os.path.exists(directory):
            pass
        else:
            os.makedirs('Korean')

        if os.path.exists(path):
            pass
        else:
            with open('Korean/Korean Dictionary.csv', 'a', newline='') as data:
                content = csv.writer(data)
                content.writerow(['Vocab', 'Translation', 'P.O.S.'])
        try:
            self.label_enter.clear()

            if self.input_vocab.text() == '':
                raise
            else:
                pass

            if self.input_translation.text() == '':
                raise
            else:
                pass

            vocab = self.input_vocab.text()
            translation = self.input_translation.text()
            pos = self.part_of_speech()
            dict_entry = [vocab, translation, pos]

            with open('Korean/Korean Dictionary.csv', 'a', newline='') as data:
                content = csv.writer(data)
                content.writerow(dict_entry)

        except:
            self.label_enter.setText('Please enter vocab and translation')
            self.label_enter.setStyleSheet('color: black;')

    def japanese(self) -> None:
        """
        1st: Check for, then set up, Japanese directory/dictionary if they don't exist.
        2nd: Enter new vocab into dictionary.
        """
        directory = 'Japanese'
        path = './Japanese/Japanese Dictionary.csv'

        if os.path.exists(directory):
            pass
        else:
            os.makedirs('Japanese')

        if os.path.exists(path):
            pass
        else:
            with open('Japanese/Japanese Dictionary.csv', 'a', newline='') as data:
                content = csv.writer(data)
                content.writerow(['Vocab', 'Translation', 'P.O.S.'])
        try:
            self.label_enter.clear()

            if self.input_vocab.text() == '':
                raise
            else:
                pass

            if self.input_translation.text() == '':
                raise
            else:
                pass

            vocab = self.input_vocab.text()
            translation = self.input_translation.text()
            pos = self.part_of_speech()
            dict_entry = [vocab, translation, pos]

            with open('Japanese/Japanese Dictionary.csv', 'a', newline='')as data:
                content = csv.writer(data)
                content.writerow(dict_entry)

        except:
            self.label_enter.setText('Please enter vocab and translation')
            self.label_enter.setStyleSheet('color: black;')

    def other(self) -> None:
        """
        1a: Check for, then set up, other language directory/dictionary if they don't exist.
        1b: Directory and Language will be based on user input.
        2nd: Enter new vocab into dictionary.
        """
        try:
            directory = self.input_other.text()
            path = f'./{directory}/{directory} Dictionary.csv'

            if os.path.exists(directory):
                pass
            else:
                os.makedirs(f'{directory}')

            if os.path.exists(path):
                pass
            else:
                with open(f'{directory}/{directory} Dictionary.csv', 'a', newline='') as data:
                    content = csv.writer(data)
                    content.writerow(['Vocab', 'Translation', 'P.O.S.'])

            try:
                self.label_enter.clear()
                language = self.input_other.text()

                if self.input_vocab.text() == '':
                    raise
                else:
                    pass

                if self.input_translation.text() == '':
                    raise
                else:
                    pass

                vocab = self.input_vocab.text()
                translation = self.input_translation.text()
                pos = self.part_of_speech()
                dict_entry = [vocab, translation, pos]

                with open(f'{language}/{language} Dictionary.csv', 'a', newline='') as data:
                    content = csv.writer(data)
                    content.writerow(dict_entry)

            except:
                self.label_enter.setText('Please enter vocab and translation')
                self.label_enter.setStyleSheet('color: black;')

        except:
            self.label_enter.setText('Please enter a language name.')
            self.label_enter.setStyleSheet('color: navy;')

