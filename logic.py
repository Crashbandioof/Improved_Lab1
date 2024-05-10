from PyQt6.QtWidgets import *
from gui import *
import csv

class logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        '''
        The function hides the radio buttons, the vote candidate push button, and the ID widgets
        creates the vote variables for both candidates and sets their value based on what's shown in votedata.csv,
        and maps the buttons functions
        Sets Error label to red text
        '''
        super().__init__()
        self.setupUi(self)

        self.radioButton_John.hide()
        self.radioButton_Jane.hide()
        self.pushButton_vote_candidate.hide()
        self.label_input_ID.hide()
        self.lineEdit_input_ID.hide()

        self.__john_votes: int = 0
        self.__jane_votes: int = 0
        self.__vote_list: list = []
        with open('votedata.csv', 'r') as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            for row in content:
                self.__vote_list.append(row)
            self.__john_votes = int(self.__vote_list[1][1])
            self.__jane_votes = int(self.__vote_list[2][1])

        self.pushButton_vote.clicked.connect(lambda: self.show_vote())
        self.pushButton_exit.clicked.connect(lambda: self.exit())
        self.pushButton_vote_candidate.clicked.connect(lambda: self.vote_candidate())

        self.label_error_message.setStyleSheet("QLabel { color: red; }")

    def show_vote(self) -> None:
        '''
        Reveals the radio buttons and the vote candidate push button
        '''
        self.radioButton_John.show()
        self.radioButton_Jane.show()
        self.pushButton_vote_candidate.show()
        self.label_input_ID.show()
        self.lineEdit_input_ID.show()

    def vote_candidate(self) -> None:
        '''
        Displays an error message if the user input is invalid
        Increases the vote value of the selected candidate by one
        If no candidate is selected, the user is asked to select a candidate
        Submits vote data to votedata.csv
        Clears vote ID form
        '''
        error: str = self.check_errors()
        if error != 'None':
            self.label_error_message.setText(error)
            return
        if self.radioButton_John.isChecked():
            self.__john_votes += 1
        elif self.radioButton_Jane.isChecked():
            self.__jane_votes += 1
        self.radioButton_John.hide()
        self.radioButton_Jane.hide()
        self.pushButton_vote_candidate.hide()
        self.label_error_message.setText('')
        self.label_input_ID.hide()
        self.lineEdit_input_ID.hide()
        file = open('ID_list.txt', 'a')
        file.write(f'{self.lineEdit_input_ID.text()}\n')
        file.close()
        with open('votedata.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            self.__data: list = []
            for row in reader:
                self.__data.append(row)
        self.__data[1][1] = str(self.__john_votes)
        self.__data[2][1] = str(self.__jane_votes)
        with open('votedata.csv', 'w',newline='') as file:
            content = csv.writer(file, delimiter=',')
            content.writerows(self.__data)
        self.lineEdit_input_ID.setText('')

    def exit(self) -> None:
        '''
        Disables all of the buttons
        Displays the vote data to the user
        '''
        self.radioButton_John.hide()
        self.radioButton_Jane.hide()
        self.pushButton_vote_candidate.hide()
        self.pushButton_vote.setEnabled(False)
        self.pushButton_exit.setEnabled(False)


        self.label_voting_results.setText(f'John - {self.__john_votes}, Jane - {self.__jane_votes}, Total - {self.__john_votes + self.__jane_votes}')
    def check_errors(self) -> str:
        '''
        Checks to see if the user ID input is valid
        '''
        try: #checks to see if ID input is an integer
            int_ID = int(self.lineEdit_input_ID.text())
        except:
            return 'ID must only contain numbers'
        with open('ID_list.txt', 'r') as file: #Checks if the user's ID is already in votedata.csv
            for line in file:
                if self.lineEdit_input_ID.text() == line[0:6]:
                    return 'You already voted'
        if len(self.lineEdit_input_ID.text()) != 6:
            return 'Your ID must contain 6 numbers'
        if self.radioButton_John.isChecked() == self.radioButton_Jane.isChecked():
            return 'You must select a candidate'
        return 'None'


