import time
import BehaviorTreeFBNL
import pydirectinput


roomlist = [[[],[],[],[]],]
roomlist2 = [[[],[],[],[]]]

roomlist[0][0] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/FBNL/room00.png', 0.75, 1, None, [[1277, 600],]],['resources/FBNL/room00a.png', 0.75, 1, None, [[1112, 659],]],]
roomlist[0][1] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/FBNL/room01.png', 0.75, 1, None, [[1013, 555],]],['resources/FBNL/room01a.png', 0.75, 1, None, [[1055, 428],]],]
roomlist[0][2] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/FBNL/room02.png', 0.75, 1, None, [[1062, 534],]],['resources/FBNL/room02a.png', 0.75, 1, None, [[1156, 574],]],]
roomlist[0][3] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],]

roomlist2[0][0] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/FBNL/room00.png', 0.75, 1, None, [[1277, 600],]],['resources/FBNL/room00a.png', 0.75, 1, None, [[1112, 659],]],]
roomlist2[0][1] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/FBNL/room01.png', 0.75, 1, None, [[1013, 555],]],['resources/FBNL/room0a.png', 0.75, 1, None, [[1055, 428],]],]
roomlist2[0][2] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/FBNL/room02.png', 0.75, 1, None, [[1062, 534],]],['resources/FBNL/room02a.png', 0.75, 1, None, [[1156, 574],]],]
roomlist2[0][3] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],]

def 获取玩家当前房间(bossxy,playxy):
    bossroom = (0, 3)
    x,y = (playxy[1]-bossxy[1])//18+bossroom[0],(playxy[0]-bossxy[0])//18+bossroom[1]
    return roomlist[x][y]


def 获取玩家当前房间目标(bossxy,playxy):
    bossroom = (0, 3)
    x,y = (playxy[1]-bossxy[1])//18+bossroom[0],(playxy[0]-bossxy[0])//18+bossroom[1]
    return roomlist[x][y]

def 获取玩家当前房间坐标(bossxy,playxy):
    print('【1】1获取玩家当前房间坐标', bossxy,playxy)
    bossroom = (0, 3)
    x, y = (playxy[1] - bossxy[1]) // 18 + bossroom[0], (playxy[0] - bossxy[0]) // 18 + bossroom[1]
    functions[x][y](x,y)
    return roomlist[x][y]

def 获取玩家当前房间坐标1(bossxy,playxy,FindListNone):
    bossroom = (0, 3)
    x, y = ((playxy[5][0][1]+playxy[4][0][1]) - bossxy[5][0][1]) // 18 + bossroom[0], ((playxy[5][0][0]+playxy[4][0][0]) - bossxy[5][0][0]) // 18 + bossroom[1]
    print('【1】获取玩家当前房间坐标1,',x, y)
    if not FindListNone or (x==3 and y==0):
        functions[x][y](x, y)
    return roomlist[x][y],roomlist2[x][y]

def 获取玩家当前房间坐标2(bossxy,playxy):
    bossroom = (0, 3)
    x, y = ((playxy[5][0][1]+playxy[4][0][1]) - bossxy[5][0][1]) // 18 + bossroom[0], ((playxy[5][0][0]+playxy[4][0][0]) - bossxy[5][0][0]) // 18 + bossroom[1]
    print('【1】2获取玩家当前房间坐标',x, y)
    #functions[x][y](x,y)
    return roomlist[x][y]

def 获取玩家当前房间坐标3(bossxy,playxy):
    bossroom = (0, 3)
    x, y = ((playxy[5][0][1]+playxy[4][0][1]) - bossxy[5][0][1]) // 18 + bossroom[0], ((playxy[5][0][0]+playxy[4][0][0]) - bossxy[5][0][0]) // 18 + bossroom[1]
    print('【1】3获取玩家当前房间坐标',x, y)
    return roomlist2[x][y]

def 获取玩家当前房间坐标4(bossxy,playxy,FindListNone):
    bossroom = (0, 3)
    x, y = ((playxy[5][0][1]+playxy[4][0][1]) - bossxy[5][0][1]) // 18 + bossroom[0], ((playxy[5][0][0]+playxy[4][0][0]) - bossxy[5][0][0]) // 18 + bossroom[1]


def roomfun(x,y):
    print('【3】 roomfun',x,y)
    if x == 0 and y == 0:
        pydirectinput.press("alt")
        time.sleep(1)
        pydirectinput.press("ctrl")
        BehaviorTreeFBNL.AIMoveTo2()
    elif x == 0 and y == 3:
        pydirectinput.press("v")
        BehaviorTreeFBNL.AIMoveTo2()
def roomfun1(x,y):
    print('【3】 roomfun1',x,y)
    BehaviorTreeFBNL.AIMoveTo2()

functions =  [[roomfun,roomfun1,roomfun1,roomfun],]



