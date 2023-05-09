import sys

from PyQt5.QtCore import pyqtSlot, Qt, QObject, QEvent
from PyQt5.QtGui import QIcon

from resource import resources_rc
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QButtonGroup, QAbstractButton

from mainWindow import Ui_MainWindow


class QQInterface(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.friendsVerticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.groupChatVerticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        # self.newFriendsWidget.setVisible(False)
        # self.myDeviceWidget.setVisible(False)
        # self.familyWidget.setVisible(False)
        # self.myFriendWidget.setVisible(False)
        # self.createdGroupChatWidget.setVisible(False)
        # self.managedGroupChatWidget.setVisible(False)
        # self.joinedGroupChatWidget.setVisible(False)

        self._the_form_corresponding_to_the_button = {
            self.newFriendsPushButtonWidget: [self.newFriendsPushButton, self.newFriendsWidget],
            self.myDevicePushButtonWidget: [self.myDevicePushButton, self.myDeviceWidget],
            self.familyPushButtonWidget: [self.familyPushButton, self.familyWidget],
            self.myFriendPushButtonWidget: [self.myFriendPushButton, self.myFriendWidget],
            self.createdGroupChatPushButtonWidget: [self.createdGroupChatPushButton, self.createdGroupChatWidget],
            self.managedGroupChatPushButtonWidget: [self.managedGroupChatPushButton, self.managedGroupChatWidget],
            self.joinedGroupChatPushButtonWidget: [self.joinedGroupChatPushButton, self.joinedGroupChatWidget]
        }
        for key, value in self._the_form_corresponding_to_the_button.items():
            key.installEventFilter(self)
            # value[0].clicked.connect(lambda: self.__expand(value[0], value[1]))
            value[1].setVisible(False)

        # self.buttonGroup = QButtonGroup()
        # self.buttonGroup.setExclusive(False)
        # self.buttonGroup.addButton(self.newFriendsPushButton)
        # self.buttonGroup.addButton(self.myDevicePushButton)
        # self.buttonGroup.addButton(self.familyPushButton)
        # self.buttonGroup.addButton(self.myFriendPushButton)
        # self.buttonGroup.addButton(self.createdGroupChatPushButton)
        # self.buttonGroup.addButton(self.managedGroupChatPushButton)
        # self.buttonGroup.addButton(self.joinedGroupChatPushButton)
        # self.buttonGroup.buttonToggled.connect(lambda button, checked: self.__expand(
        #     button, self._the_form_corresponding_to_the_button[button], checked))
        # self.myFriendPushButton.setChecked(True)
        # self.joinedGroupChatPushButton.setChecked(True)

        self.messagePushButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(
                self.messagePage))
        self.contactsPushButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(
                self.contactsPage))
        self.spacePushButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(
                self.spacePage))
        self.friendsPushButton.clicked.connect(
            lambda: self.stackedWidget_2.setCurrentWidget(
                self.friendsPage))
        self.groupChatPushButton.clicked.connect(
            lambda: self.stackedWidget_2.setCurrentWidget(
                self.groupChatPage))

    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        if a1.type() == QEvent.Type.MouseButtonPress or a1.type() == QEvent.Type.MouseButtonDblClick and a1.button() == Qt.MouseButton.LeftButton:
            self.__expand(self._the_form_corresponding_to_the_button[a0][0], self._the_form_corresponding_to_the_button[a0][1])
        return super().eventFilter(a0, a1)

    def __expand(self, button: QPushButton, widget: QWidget):
        if widget.isHidden():
            button.setIcon(QIcon(":/icon/icon/箭头下.svg"))
            widget.show()
        else:
            button.setIcon(QIcon(":/icon/icon/箭头右.svg"))
            widget.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QQInterface()
    w.show()
    sys.exit(app.exec())
