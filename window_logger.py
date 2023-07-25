import win32gui, time, win32process


def get_foreground():
    return win32gui.GetForegroundWindow()


last_window = 0
while True:
    current_window = get_foreground()
    if current_window != last_window:
        process_id = win32process.GetWindowThreadProcessId(current_window)
        window_title = win32gui.GetWindowText(current_window)
        print(f"{current_window} = {window_title}")
        print(f"Process ID: {process_id}\n")
        last_window = current_window
    if current_window == last_window:
        pass

    time.sleep(0.001)
