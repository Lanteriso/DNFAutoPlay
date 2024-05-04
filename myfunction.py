import pyautogui
import time
import random
import math
import cv2
import numpy
def click_on_position(pairs1,pairs2):
    pyautogui.moveTo(pairs2[0][0]+pairs1[0][0] + random.randint(-10, 10), pairs2[0][1]+pairs1[0][1] + random.randint(-10, 10), duration=random.uniform(0.2, 0.3))
    time.sleep(random.uniform(1.0, 2.0))
    pyautogui.click(button = pairs1[1])

def 点击某点(pairs1,pairs2):  # ['resources/DailyEntrustment/czbc.png', 0.7, myfunction.仅移动, [[40, 10], 'left',[-10, 10]]
    pyautogui.moveTo(pairs2[0][0]+pairs1[0][0] + random.randint(-10, 10), pairs2[0][1]+pairs1[0][1] + random.randint(-10, 10), duration=random.uniform(0.2, 0.3))
    time.sleep(random.uniform(1.0, 2.0))
    pyautogui.click(button = pairs1[1])

def 移动并攻击(pairs1,pairs2):
    d = 和目标的距离(960, 540, pairs2[0][0] + pairs1[0][0], pairs2[0][1] + pairs1[0][1])
    print(f'移动并攻击{pairs1, pairs2} {d}')
    xy = (pairs2[0][0]+pairs1[0][0] + random.randint(-10, 10), pairs2[0][1]+pairs1[0][1] + random.randint(-10, 10))
    pyautogui.moveTo((xy[0]+960)//2, (xy[1]+540)//2, duration=random.uniform(0.2, 0.3))
    if d > 450: # 距离太于450就移动
        pyautogui.click(button=pairs1[1])
    return d < 450 # 距离小于450就返回True,就叫攻击

def press_key(pairs1,pairs2):
    # 模拟按下 'e' 键
    pyautogui.keyDown(pairs1[0])
    # 保持按下状态3秒钟
    time.sleep(pairs1[1])
    # 模拟释放 'e' 键
    pyautogui.keyUp(pairs1[0])

def calculate_point_b(o,a, distance):
    # 计算从原点 O 到点 A 的向量
    dx = a[0]-o[0]
    dy = a[1]-o[1]

    # 单位化向量
    vector_length = math.sqrt(dx ** 2 + dy ** 2)
    unit_dx = dx / vector_length
    unit_dy = dy / vector_length

    # 计算延伸向量
    extension_vector = (unit_dx * distance, unit_dy * distance)

    # 计算点 B 的坐标
    b = (a[0] + extension_vector[0], a[1] + extension_vector[1])

    return b

def 小地图点击某点(pairs1,pairs2):
    print(f'小地图点击某点{pairs1, pairs2}')
    xy = calculate_point_b((960, 540), (960 + (pairs2[0][0] + pairs1[0][0] - 147), 540 + (pairs2[0][1] + pairs1[0][1] - 128)), pairs1[1])
    pyautogui.moveTo(xy[0],min(xy[1], 900), duration=random.uniform(0.2, 0.3))
    pyautogui.click(button='right')

def 小地图移动攻击某点(pairs1,pairs2):
    d = 和目标的距离(147, 128, pairs2[0][0] + pairs1[0][0], pairs2[0][1] + pairs1[0][1])
    print(f'小地图移动攻击某点{pairs1, pairs2,d}')
    xy = calculate_point_b((960, 540), (960 + (pairs2[0][0] + pairs1[0][0] - 147), 540 + (pairs2[0][1] + pairs1[0][1] - 128)), pairs1[1])
    pyautogui.moveTo(xy[0],min(xy[1], 900), duration=random.uniform(0.2, 0.3))
    if d > 60:
        pyautogui.click(button='right')
    return d < 60

def 试验查找指定图片(Screenxy,templatepath):# 屏幕范围，白名单
    # 在很多血条模板中找，找到一张就返回True,相当于or，返回的是单个坐标,都没找到返回空数组
    imgbase = GetAnImageOfTheScreen(Screenxy[0],Screenxy[1],Screenxy[2],Screenxy[3])
    for i in templatepath:
        outTarget = 试验全屏TheImageTemplateMatches(imgbase, i)
        if outTarget:
            return i+outTarget
    return []

def 重复查找指定图片(Screenxy,templatepath,timeout,Interval):# 屏幕范围，白名单,超时时间，间隔
    # 在很多血条模板中找，找到一张就返回True,相当于or，返回的是单个坐标,都没找到返回空数组
    current_timestamp = time.time()
    imgbase = GetAnImageOfTheScreen(Screenxy[0],Screenxy[1],Screenxy[2],Screenxy[3])
    while time.time() - current_timestamp < timeout:
        for i in templatepath:
            outTarget = 试验全屏TheImageTemplateMatches(imgbase, i)
            if outTarget:
                return i+outTarget
        time.sleep(Interval)
    return []

def GetAnImageOfTheScreen(ScreenX1,ScreenY1,ScreenX2,ScreenY2):
    Screen_img = pyautogui.screenshot(region=(ScreenX1,ScreenY1,ScreenX2,ScreenY2))
    Screen_img = cv2.cvtColor(numpy.array(Screen_img), 0)
    Screen_img = cv2.cvtColor(Screen_img, cv2.COLOR_BGR2GRAY)
    return Screen_img

def 试验全屏TheImageTemplateMatches(img1, templatelist, ):
    # #['resources/demo/068.png', 0.7, 按下某键, [参数1]，[参数2]] = templatelist
    # 读取大图像
    base_img = img1
    # 读取模板图像
    template_img = cv2.imread(templatelist[0], 0)
    template_img = cv2.resize(template_img, None, fx=templatelist[2], fy=templatelist[2], interpolation=cv2.INTER_LINEAR)
    # 如果图像是四通道或更多通道，需要转换为三通道
    if len(base_img.shape) >= 3:
        if base_img.shape[2] > 3:
            base_img = cv2.cvtColor(base_img, cv2.COLOR_BGRA2BGR)
    if len(template_img.shape) >= 3:
        if template_img.shape[2] > 3:
            template_img = cv2.cvtColor(template_img, cv2.COLOR_BGRA2BGR)
    # 确保模板图像不是空的
    if template_img is None:
        print("模板图像未找到，请检查路径")
        return False

    # 获取模板图像的大小
    template_size = template_img.shape[::-1]

    # 使用cv2.TM_CCOEFF_NORMED进行归一化相关匹配
    result = cv2.matchTemplate(base_img, template_img, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #  print(max_val,templatelist[1])
    if max_val > templatelist[1]:

        return [[max_loc,template_size,max_val]]  # 找到图片
    else:
        return [] # 没找到图片

def 和目标的距离(x1,y1,x2,y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    time.sleep(5)
    FindImg = 试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/0.png', 0.7, 1.62, None, [[25, 200], 'right']], ])
    FindImg = 试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/1.PNG', 0.7, 1.62, None, [[25, 200], 'right']], ])
    FindImg = 试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/2.PNG', 0.7, 1.62, None, [[25, 200], 'right']], ])
    FindImg = 试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/3.png', 0.7, 1, None, [[25, 200], 'right']], ])
    FindImg = 试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapPlayer.PNG', 0.7, 1.54, None, [[25, 200], 'right']], ])
    FindImg = 试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapBoss.PNG', 0.7, 1.54, None, [[25, 200], 'right']], ])
    FindImg = 试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapBoss1.png', 0.7, 1, None, [[25, 200], 'right']], ])
    FindImg = 试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapNone.PNG', 0.7, 1.54, None, [[25, 200], 'right']], ])
    FindImg = 试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/door1up.png', 0.7, 1, None, [[25, 200], 'right']], ])
    print(FindImg)
    FindImg = 试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/door0up.png', 0.7, 1, None, [[25, 200], 'right']], ])
    print(FindImg)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
