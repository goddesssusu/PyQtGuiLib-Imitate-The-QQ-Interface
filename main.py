# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 10:42
# @Author  : 讨厌自己
# @Email   : 507194368@qq.com
# @File    : main.py
# @Software: PyCharm
import sys
from functools import partial

from PyQtGuiLib.header import (
    Qt,
    QObject,
    QEvent,
    QIcon,
    QApplication,
    QPushButton,
    QWidget,
    QStyledItemDelegate
)

from resource import resources_rc
from pyqt_frameless_window import FramelessMainWindow

from mainWindow import Ui_MainWindow


class QQInterface(FramelessMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        FramelessMainWindow.mousePressEvent = lambda *args: None

        self.setupUi(self)
        self.messageVerticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.friendsVerticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.groupChatVerticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.trendsVerticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.comboBox.setItemDelegate(QStyledItemDelegate())

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
            value[0].setAttribute(
                Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
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
            self.__expand(*self._treeWidgets[a0])
            return True

        return super().eventFilter(a0, a1)

    @staticmethod
    def __expand(button: QPushButton, widget: QWidget):
        if widget.isHidden():
            button.setIcon(QIcon(":/icon/icon/箭头下.svg"))
            widget.show()
        else:
            button.setIcon(QIcon(":/icon/icon/箭头右.svg"))
            widget.hide()

    def mouseMoveEvent(self, e):
        super().mouseMoveEvent(e)
        self._move()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QQInterface()
    w.show()
    sys.exit(app.exec())
