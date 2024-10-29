import pyautogui
import pyperclip
import time

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        # 读取文件的每一行，并去除空白符，每行是一个image_path
        image_paths = [line.strip() for line in file.readlines()]
    return image_paths

def automate_input(image_path, date, hour, minute):
    time.sleep(2)  # 等待页面加载
    pyautogui.click(x=768, y=94, duration=1)
    pyautogui.hotkey('shift')  # 轉英文
    pyautogui.write(image_path)  # 输入链接
    pyautogui.press('enter')  # time.sleep(2)  # 等待页面加载
    time.sleep(15)  # 等待页面加载
    pyautogui.press('tab')  # 按回车键
    pyautogui.hotkey('space')
    pyautogui.hotkey('up')
    pyautogui.hotkey('space')
    pyautogui.hotkey('esc')
    time.sleep(2)  # 等待页面加载
    pyautogui.hotkey('tab')
    time.sleep(2)  # 等待页面加载
    pyautogui.press('down',40,0.002)
    pyautogui.click(x=808, y=587, duration=3)
    time.sleep(2)  # 等待页面加载
    pyautogui.hotkey('tab')
    time.sleep(5)  # 等待页面加载
    #fb
    pyautogui.press('backspace',5,0.002)
    pyautogui.write(date)  # date enter
    time.sleep(2)  # 等待页面加载
    pyautogui.hotkey('tab')
    time.sleep(2)  # 等待页面加载
    pyautogui.write(hour)  # hours enter
    pyautogui.hotkey('tab')
    time.sleep(1)  # 等待页面加载
    pyautogui.write(minute)  # hours enter
    pyautogui.hotkey('tab')
    time.sleep(1)  # 等待页面加载
    #end fb
    #ig
    pyautogui.press('backspace',5,0.002)
    pyautogui.write(date)  # date enter
    time.sleep(2)  # 等待页面加载
    pyautogui.hotkey('tab')
    time.sleep(1)  # 等待页面加载
    pyautogui.write(hour)  # hours enter
    pyautogui.hotkey('tab')
    time.sleep(1)  # 等待页面加载
    pyautogui.write(minute)  # hours enter
    time.sleep(1)  # 等待页面加载
    #end ig
    time.sleep(2)  # 等11-02
    pyautogui.press('tab',7)
    pyautogui.press('enter')  # 按回车键 send
    time.sleep(5)  # 等待页面加载
    pyautogui.press('enter')  # 按回车键 send

def export_report(data, report_file):
    with open(report_file, 'w') as file:
        for entry in data:
            file.write("圖片路徑: {}\n".format(entry[1]))
            file.write("日期: {}\n".format(entry[0]))
            file.write("\n")
    print("處理完!所有資料匯出到 {}".format(report_file))


def main():
    file_path = 'inputp.txt'  # 输入文件路径
    report_file = 'report.txt'  # 报告文件路径

    hour = '18'  # 确保这是正确的小时值
    minute = '30' # 确保这是正确的分钟值

    dates = ["11-18", "11-22"]
    image_paths = read_input_file(file_path)

    # 确保日期列表和图片路径列表长度相同
    assert len(dates) == len(image_paths), "日期列表和图片路径列表长度不匹配"

    # 创建数据列表，每个日期对应一个图片路径
    data = list(zip(dates, image_paths))

    for date, image_path in data:
        automate_input(image_path, date, hour, minute)

    export_report(data, report_file)


if __name__ == "__main__":
    main()
