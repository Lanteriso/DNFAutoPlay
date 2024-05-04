import time
import BehaviorTreeDNF2
import pydirectinput

海伯伦 = [[0,4,5,"boss"],
         [0,3,0,0],
         [0,2,0,0],
         [1,0,0,0],]

roomlist = [[[],[],[],[]],
            [[],[],[],[]],
            [[],[],[],[]],
            [[],[],[],[]]
            ]
roomlist2 = [[[],[],[],[]],
            [[],[],[],[]],
            [[],[],[],[]],
            [[],[],[],[]]
            ]
roomlist[3][0] = [['resources/destroyedcastleofdead/door0c.png', 0.75, 1, None, [[1000, 350], 'right']],['resources/destroyedcastleofdead/door0b.png', 0.75, 1, None, [[385, 430], 'right']],['resources/destroyedcastleofdead/door0a.png', 0.75, 1, None, [[391, 249], 'right']],]
roomlist[2][0] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door1b.png', 0.75, 1, None, [[443, 446], 'right']],['resources/destroyedcastleofdead/door1a.png', 0.75, 1, None, [[750, 750], 'right']],]
roomlist[2][1] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door2b.png', 0.75, 1, None, [[-537, 418], 'right']],['resources/destroyedcastleofdead/door2a.png', 0.75, 1, None, [[102, 507], 'right']],]
roomlist[1][1] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door3a.png', 0.75, 1, None, [[90, 490], 'right']],]
roomlist[0][1] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door4a.png', 0.75, 1, None, [[658, 453], 'right']],['resources/destroyedcastleofdead/door4b.png', 0.75, 1, None, [[680, 603], 'right']],]
roomlist[0][2] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door5a.png', 0.75, 1, None, [[800, 375], 'right']],['resources/destroyedcastleofdead/door5b.png', 0.75, 1, None, [[543, 463], 'right']],]
roomlist[0][3] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],]
roomlist[1][2] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door12a.png', 0.75, 1, None, [[-93, 470], 'right']],['resources/destroyedcastleofdead/door12b.png', 0.75, 1, None, [[373,178], 'right']],]
roomlist[1][0] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door10a.png', 0.75, 1, None, [[1033,395], 'right']],]
roomlist[0][0] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door00a.png', 0.75, 1, None, [[958,458], 'right']],]
roomlist[2][2] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door22a.png', 0.75, 1, None, [[-1070,605], 'right']],['resources/destroyedcastleofdead/door22b.png', 0.75, 1, None, [[-417,549], 'right']],]

roomlist2[3][0] = [['resources/destroyedcastleofdead/door0c.png', 0.75, 1, None, [[1000, 550], 'right']],['resources/destroyedcastleofdead/door0b.png', 0.75, 1, None, [[385, 630], 'right']],['resources/destroyedcastleofdead/door0a.png', 0.75, 1, None, [[391, 449], 'right']],]
roomlist2[2][0] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door1b.png', 0.75, 1, None, [[443, 646], 'right']],['resources/destroyedcastleofdead/door1a.png', 0.75, 1, None, [[750, 1050], 'right']],]
roomlist2[2][1] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door2b.png', 0.75, 1, None, [[-537, 618],]],['resources/destroyedcastleofdead/door2a.png', 0.75, 1, None, [[102, 707],]],]
roomlist2[1][1] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door3a.png', 0.75, 1, None, [[90, 690], 'right']],]
roomlist2[0][1] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door4a.png', 0.75, 1, None, [[658, 653], 'right']],['resources/destroyedcastleofdead/door4b.png', 0.75, 1, None, [[680, 803], 'right']],]
roomlist2[0][2] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door5a.png', 0.75, 1, None, [[800, 375], 'right']],['resources/destroyedcastleofdead/door5b.png', 0.75, 1, None, [[543, 463], 'right']],]
roomlist2[0][3] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],]
roomlist2[1][2] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door12a.png', 0.75, 1, None, [[-93, 470], 'right']],['resources/destroyedcastleofdead/door12b.png', 0.75, 1, None, [[373,378], 'right']],]
roomlist2[1][0] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door10a.png', 0.75, 1, None, [[1033,395], 'right']],]
roomlist2[0][0] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door00a.png', 0.75, 1, None, [[958,658], 'right']],]
roomlist2[2][2] = [['resources/destroyedcastleofdead/rmb.png', 0.75, 1, None, [[22, 21],]],['resources/destroyedcastleofdead/door22a.png', 0.75, 1, None, [[-1070,805], 'right']],['resources/destroyedcastleofdead/door22b.png', 0.75, 1, None, [[-417,549], 'right']],]


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

def 获取玩家当前房间坐标2(bossxy,playxy):
    bossroom = (0, 3)
    x, y = ((playxy[5][0][1]+playxy[4][0][1]) - bossxy[5][0][1]) // 18 + bossroom[0], ((playxy[5][0][0]+playxy[4][0][0]) - bossxy[5][0][0]) // 18 + bossroom[1]
    print('【1】2获取玩家当前房间坐标',x, y)
    functions[x][y](x,y)
    return roomlist[x][y]

def 获取玩家当前房间坐标3(bossxy,playxy):
    bossroom = (0, 3)
    x, y = ((playxy[5][0][1]+playxy[4][0][1]) - bossxy[5][0][1]) // 18 + bossroom[0], ((playxy[5][0][0]+playxy[4][0][0]) - bossxy[5][0][0]) // 18 + bossroom[1]
    print('【1】3获取玩家当前房间坐标',x, y)
    return roomlist2[x][y]

def 获取玩家当前房间坐标3(bossxy,playxy):
    bossroom = (0, 3)
    x, y = ((playxy[5][0][1]+playxy[4][0][1]) - bossxy[5][0][1]) // 18 + bossroom[0], ((playxy[5][0][0]+playxy[4][0][0]) - bossxy[5][0][0]) // 18 + bossroom[1]
    print('【1】3获取玩家当前房间坐标',x, y)
    return roomlist2[x][y]

def roomfun(x,y):
    print('【3】 roomfun',x,y)
    if x == 3 and y == 0:
        pydirectinput.press("alt")
        time.sleep(1)
        pydirectinput.press("ctrl")
    elif x == 0 and y == 3:
        pydirectinput.press("v")
        BehaviorTreeDNF2.AIMoveTo2()
def roomfun1(x,y):
    print('【3】 roomfun1',x,y)
    BehaviorTreeDNF2.AIMoveTo2()

functions =  [[roomfun1,roomfun1,roomfun1,roomfun],
                [roomfun1,roomfun1,roomfun1,roomfun1],
                [roomfun1,roomfun1,roomfun1,roomfun1],
                [roomfun,roomfun1,roomfun1,roomfun1]
                ]



