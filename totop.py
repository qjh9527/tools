import win32gui
import keyboard
import win32con
import atexit


class totop:
    flag = False
    hw = ''
    top_windows = {}

    def force_focus(self, hwnd):
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOOWNERZORDER | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
        print("置顶", hwnd, win32gui.GetWindowText(hwnd))

    def cancel_focus(self, hwnd):
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                              win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
        print("取消置顶", hwnd, win32gui.GetWindowText(hwnd))

    def handler(self, op, hwnd):
        op(hwnd)

    def get_key(self):
        def fun():
            if win32gui.GetForegroundWindow() != '':
                hd = win32gui.GetForegroundWindow()
                h_name = win32gui.GetWindowText(hd)

                if hd not in self.top_windows:
                    # 未置顶
                    self.handler(self.force_focus, hd)
                    self.top_windows[hd] = h_name

                else:
                    # 已置顶
                    self.handler(self.cancel_focus, win32gui.GetForegroundWindow())
                    self.top_windows.pop(hd)

            print(list(self.top_windows.values()))

        keyboard.add_hotkey('alt+t', fun)

        while True:
            keyboard.wait()


if __name__ == '__main__':
    zd = totop()
    zd.get_key()
