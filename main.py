import sys
from functools import partial

from PyQt5.QtCore import Qt, QObject, QEvent
from PyQt5.QtGui import QIcon

from resource import resources_rc
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget

from mainWindow import Ui_MainWindow


class QQInterface(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.messageVerticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.friendsVerticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.groupChatVerticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.trendsVerticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self._treeWidgets = {
            self.newFriendsPushButtonWidget: [
                self.newFriendsPushButton,
                self.newFriendsWidget],
            self.myDevicePushButtonWidget: [
                self.myDevicePushButton,
                self.myDeviceWidget],
            self.familyPushButtonWidget: [
                self.familyPushButton,
                self.familyWidget],
            self.myFriendPushButtonWidget: [
                self.myFriendPushButton,
                self.myFriendWidget],
            self.createdGroupChatPushButtonWidget: [
                self.createdGroupChatPushButton,
                self.createdGroupChatWidget],
            self.managedGroupChatPushButtonWidget: [
                self.managedGroupChatPushButton,
                self.managedGroupChatWidget],
            self.joinedGroupChatPushButtonWidget: [
                self.joinedGroupChatPushButton,
                self.joinedGroupChatWidget]}
        for key, value in self._treeWidgets.items():
            key.installEventFilter(self)
            value[0].mousePressEvent = key.mousePressEvent
            self.__expand(*value) if value[1] not in (
                self.myFriendWidget, self.joinedGroupChatWidget) else None

        btn_to_page = {
            self.messagePushButton: self.messagePage,
            self.contactsPushButton: self.contactsPage,
            self.spacePushButton: self.spacePage,
            self.friendsPushButton: self.friendsPage,
            self.groupChatPushButton: self.groupChatPage
        }
        for key, value in btn_to_page.items():
            key.clicked.connect(
                partial(value.parent().setCurrentWidget, value))

    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        if a1.type() == QEvent.Type.MouseButtonPress or a1.type(
        ) == QEvent.Type.MouseButtonDblClick and a1.button() == Qt.MouseButton.LeftButton:
            self.__expand(self._treeWidgets[a0][0], self._treeWidgets[a0][1])
        return super().eventFilter(a0, a1)

    @staticmethod
    def __expand(button: QPushButton, widget: QWidget):
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
