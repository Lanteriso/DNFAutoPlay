import time

import myfunction
import MiniMap
import pydirectinput
import threading
import 我的装饰器
import random

presslist = {'up':False,'down':False,'left':False,'right':False}
FindList = {'MiniMapBoss':None,'MiniMapPlayer':None,'MiniMapNone':None}
global_variable_player = None
playernameplate = []

start_time = time.time()  # 记录开始时间
end_time = time.time()   # 记录结束时间
last_time = time.time()  # 记录每次

def RunBehaviorTree(player, monster):
    global global_variable_player
    global_variable_player = player
    setplayernameplate(player)
    while 1:
        Tick(player)

def setplayernameplate(player):
    global playernameplate
    playernameplate = [['resources/destroyedcastleofdead/0.PNG', 0.6, 1.62, None, [[70, player.身高], 'right']],
                       ['resources/destroyedcastleofdead/0r.PNG', 0.6, 1.62, None, [[1, player.身高], 'right']],
                       ['resources/destroyedcastleofdead/0l.PNG', 0.6, 1.62, None, [[70, player.身高], 'right']],
                        ['resources/destroyedcastleofdead/0ll.PNG', 0.6, 1.62, None, [[70, player.身高], 'right']],
                        ['resources/destroyedcastleofdead/0rr.PNG', 0.6, 1.62, None, [[1, player.身高], 'right']],
                       ]

def Tick(player):
    #print(player.状态)
    if player.状态 == "默认":
        GetTarget(player)
    elif player.状态 == "副本中":
        GetTargetInDungeon(player)
    elif player.状态 == "可进入下一个房间":
        if 可进入下一个房间(player):
            player.状态 = "默认"
    elif player.状态 == "战斗进行中":
        if 战斗进行中(player):
            player.状态 = "副本中"
    elif player.状态 == "结算中":
        if 结算进行中(player):
            player.状态 = "默认"

# @我的装饰器.log_decorator
def GetPlayerRoom(player):
    FindImg = myfunction.试验查找指定图片([1180, 30, 100, 100], [['resources/destroyedcastleofdead/MiniMapBoss.PNG', 0.7, 1, None, [[25, 200], ]], ])
    FindImg1 = myfunction.试验查找指定图片([1180, 30, 100, 100], [['resources/destroyedcastleofdead/MiniMapPlayer.PNG', 0.7, 1, None, [[25, 200], 'right']], ])
    if FindImg and FindImg1:
        return MiniMap.获取玩家当前房间坐标(FindImg[5][0], FindImg1[5][0])

def GetTarget(player):
    print('【0】 GetTarget')
    FindListNone = myfunction.试验查找指定图片([1180, 30, 100, 100], [['resources/destroyedcastleofdead/MiniMapNone.PNG', 0.7, 1, None, [[0, 0], 'right']], ])
    FindList['MiniMapBoss'] = myfunction.试验查找指定图片([1180, 30, 100, 100], [['resources/destroyedcastleofdead/MiniMapBoss.PNG', 0.7, 1, None, [[25, 200], ]], ])
    FindImg5 = myfunction.试验查找指定图片([0, 0, 1280, 960], [['resources/destroyedcastleofdead/zctz.PNG', 0.7, 1, None, [[36, 13], ]], ])
    FindList['MiniMapPlayer'] = myfunction.试验查找指定图片([1180, 30, 100, 100], [['resources/destroyedcastleofdead/MiniMapPlayer.PNG', 0.7, 1, None, [[0, 0], ]],['resources/destroyedcastleofdead/MiniMapPlayer1.PNG', 0.7, 1, None, [[0, 0], ]],['resources/destroyedcastleofdead/MiniMapPlayer2.PNG', 0.7, 1, None, [[18, 0], ]], ])
    if FindList['MiniMapBoss'] and FindList['MiniMapPlayer']:
        player.currentroomlist,player.currentroomlist2 = MiniMap.获取玩家当前房间坐标1(FindList['MiniMapBoss'], FindList['MiniMapPlayer'],FindListNone)
        player.状态 = "副本中"
        player.isend = 0
    elif FindImg5:
        player.状态 = "结算中"

def GetTargetInDungeon(player):
    FindList['MiniMapNone'] = myfunction.试验查找指定图片([1180, 30, 100, 100], [['resources/destroyedcastleofdead/MiniMapNone.PNG', 0.7, 1, None, [[0, 0], 'right']], ])
    FindList['MiniMapPlayer'] = myfunction.试验查找指定图片([1180, 30, 100, 100], [['resources/destroyedcastleofdead/MiniMapPlayer.PNG', 0.7, 1, None, [[0, 0],]],['resources/destroyedcastleofdead/MiniMapPlayer1.PNG', 0.7, 1, None, [[0, 0],]], ['resources/destroyedcastleofdead/MiniMapPlayer2.PNG', 0.7, 1, None, [[18, 0],]], ])
    FindImg5 = myfunction.试验查找指定图片([0, 0, 1280, 960],[['resources/destroyedcastleofdead/zctz.PNG', 0.7, 1, None, [[36, 13], ]], ])
    if FindList['MiniMapNone'] and FindList['MiniMapPlayer'] and FindList['MiniMapBoss']:
        player.状态 = "可进入下一个房间"
        player.isend = 0
    elif FindList['MiniMapBoss'] and FindList['MiniMapPlayer'] and FindList['MiniMapBoss']:
        player.状态 = "战斗进行中"
        player.isend = 0
    elif FindImg5:
        player.状态 = "结算中"

def 副本中(player):
    GetTargetInDungeon(player)



def 可进入下一个房间(player):
    while 1:
        print('可进入下一个房间')
        FindList['MiniMapNone'] = myfunction.试验查找指定图片([1180, 30, 100, 100], [['resources/destroyedcastleofdead/MiniMapNone.PNG', 0.7, 1, None, [[0, 0], 'right']], ])
        if not FindList['MiniMapNone']:return True
        FindImg1 = myfunction.试验查找指定图片([0, 0, 1280, 960], playernameplate)
        FindImg2 = myfunction.试验查找指定图片([0, 0, 1280, 960], player.currentroomlist)

        if FindImg1 and FindImg2:
            print('可进入下一个房间2')
            if AIMoveTo(FindImg1,FindImg2,(0,0)):
                print("重置2？？？？？")
                global_variable_player.状态 = '默认'
                return False
        else: # 进太快了，一次进了两个房间
            global_variable_player.状态 = '默认'
            print("重置？？？？？")
            return False



def AIMoveTo(PlayLocation,TargetLocation,offset):
    x = (TargetLocation[5][0][0] + TargetLocation[4][0][0]) - (PlayLocation[5][0][0] + PlayLocation[4][0][0])
    y = (TargetLocation[5][0][1] + TargetLocation[4][0][1]) - (PlayLocation[5][0][1] + PlayLocation[4][0][1])
    if x > 0:
        x -= offset[1]
    else:
        x += offset[1]



    print('【3】',x,y,TargetLocation[0])

    if x > 0:
        presskey('right','left',x)
        if x < 90:
            Unpresskey('right')
    else:
        presskey('left','right',x)
        if x > -90:
            Unpresskey('left')
    if y > 0:
        presskey('down','up',0)
        if y < 90:
            Unpresskey('down')
    else:
        presskey('up','down',0)
        if y > -90:
            Unpresskey('up')

    if abs(x) < 90 and abs(y) < 90:
        print('移动完成1')
        return True

def AIMoveTo2():
    TargetLocation = (1280//2,740)
    while 1:
        PlayLocation = myfunction.试验查找指定图片([0, 0, 1280, 960], playernameplate)
        if PlayLocation:
            x = TargetLocation[0] - (PlayLocation[5][0][0] + PlayLocation[4][0][0])
            y = TargetLocation[1] - (PlayLocation[5][0][1] + PlayLocation[4][0][1])
            print('【4】移动',x,y)

            if abs(x) < 90 and abs(y) < 90:
                print('移动完成2')
                释放按键()
                ppp = "right" if x > 0 else "left"

                skills = global_variable_player.use_random_available_skill((0, 0))
                if skills:
                    print('【5】技能', skills.name)
                    pydirectinput.press(ppp)
                    pydirectinput.press(skills.name)
                    time.sleep(skills.press_time)
                return True

            if x > 0:
                presskey('right','left',x)
                if x < 90:
                    Unpresskey('right')
            else:
                presskey('left','right',x)
                if x > -90:
                    Unpresskey('left')
            if y > 0:
                presskey('down','up',0)
                if y < 90:
                    Unpresskey('down')
            else:
                presskey('up','down',0)
                if y > -90:
                    Unpresskey('up')


def AIMoveTo3(PlayLocation,TargetLocation,offset):
    x = (TargetLocation[5][0][0] + TargetLocation[4][0][0]) - (PlayLocation[5][0][0] + PlayLocation[4][0][0])
    y = (TargetLocation[5][0][1] + TargetLocation[4][0][1]) - (PlayLocation[5][0][1] + PlayLocation[4][0][1])
    if x > 0:
        x -= offset[1]
    else:
        x += offset[1]

    if abs(x) < 90 and abs(y) < 90:
        print('移动完成1')
        return True

    print('【3】',x,y,TargetLocation[0])

    if x > 0:
        presskey('right','left',x)
        if x < 90:
            Unpresskey('right')
    else:
        presskey('left','right',x)
        if x > -90:
            Unpresskey('left')
    if y > 0:
        presskey('down','up',0)
        if y < 90:
            Unpresskey('down')
    else:
        presskey('up','down',0)
        if y > -90:
            Unpresskey('up')
def presskey(dkey,ukey,x):
    if not presslist[dkey]:
        if presslist[ukey]:
            Unpresskey(ukey)
        if dkey == 'left' or dkey == 'right' and abs(x) > 500:
            pydirectinput.press(dkey)
        presslist[dkey] = True
        pydirectinput.keyDown(dkey)



def Unpresskey(key):
    if presslist[key]:
        pydirectinput.keyUp(key)
        presslist[key] = False

def 释放按键():
    for k,v in presslist.items():
        if v:
            Unpresskey(k)


def GetCurrentRoom(player):

    FindImg1 = myfunction.试验查找指定图片([1180, 30, 100, 100], [['resources/destroyedcastleofdead/MiniMapPlayer.PNG', 0.7, 1, None, [[25, 200], 'right']], ])
    FindImg2 = myfunction.试验查找指定图片([1180, 30, 100, 100], [['resources/destroyedcastleofdead/MiniMapBoss.PNG', 0.7, 1, None, [[25, 200], 'right']], ])
    # FindImg3 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapNone.PNG', 0.7, 1, None, [[25, 200], 'right']], ])

    if FindImg1 and FindImg2:
        print('room',FindImg2[5][0], FindImg1[5][0],player.状态)
        return MiniMap.获取玩家当前房间目标(FindImg2[5][0], FindImg1[5][0])



def 战斗进行中(player):
    while 1:
        print('战斗进行中')
        FindList['MiniMapNone'] = myfunction.试验查找指定图片([1180, 30, 100, 100], [['resources/destroyedcastleofdead/MiniMapNone.PNG', 0.7, 1, None, [[0, 0], 'right']], ])
        FindList['MiniMapBoss'] = myfunction.试验查找指定图片([1180, 30, 100, 100], [['resources/destroyedcastleofdead/MiniMapBoss.PNG', 0.7, 1, None, [[25, 200], ]], ])
        if FindList['MiniMapNone'] or not FindList['MiniMapBoss']:return True   # 可进入下一个房间，或没看到小地图BOSS 战斗结束
        FindImg5 = myfunction.试验查找指定图片([0, 0, 1280, 960], playernameplate)
        FindImg6 = myfunction.试验查找指定图片([0, 0, 1280, 960], [['resources/destroyedcastleofdead/1.PNG', 0.6, 1.62, None, [[70, 1], 'right']], ['resources/destroyedcastleofdead/1l.PNG', 0.7, 1.62, None, [[70, 1], 'right']],['resources/destroyedcastleofdead/1r.PNG', 0.7, 1.62, None, [[1, 1], 'right']],['resources/destroyedcastleofdead/2.PNG', 0.7, 1.62, None, [[70, 1], 'right']],['resources/destroyedcastleofdead/2l.PNG', 0.7, 1.62, None, [[70, 1], 'right']],['resources/destroyedcastleofdead/2r.PNG', 0.7, 1.62, None, [[1, 1], 'right']],['resources/destroyedcastleofdead/sstl.PNG', 0.7, 1, None, [[43, 130], 'right']],['resources/destroyedcastleofdead/hbrwg.PNG', 0.7, 1, None, [[53, 280], 'right']],['resources/destroyedcastleofdead/3.PNG', 0.7, 1, None, [[72, 1], 'right']],])
        if FindImg5 and FindImg6:
            攻击目标(player,FindImg5,FindImg6,(250,0))
        else:
            释放按键()
            因找不到敌人而移动(player)



def 攻击目标(player,PlayLocation,TargetLocation,offset):
    x = (TargetLocation[5][0][0] + TargetLocation[4][0][0]) - (PlayLocation[5][0][0] + PlayLocation[4][0][0])
    y = (TargetLocation[5][0][1] + TargetLocation[4][0][1]) - (PlayLocation[5][0][1] + PlayLocation[4][0][1])
    ppp = "right" if x > 0 else "left"
    if x > 0:
        x -= offset[0]
    else:
        x += offset[0]
    skills = player.use_random_available_skill((x,y))
    if skills:
        pydirectinput.press(ppp)
        pydirectinput.press(skills.name)
        time.sleep(skills.press_time)
        释放按键()
    else:
        AIMoveTo3(PlayLocation,TargetLocation,(250,0))


def 因找不到敌人而移动(player):

    FindImg1 = myfunction.试验查找指定图片([0, 0, 1280, 960], playernameplate)
    FindImg2 = myfunction.试验查找指定图片([0, 0, 1280, 960], player.currentroomlist2)
    if FindImg1 and FindImg2:
        AIMoveTo3(FindImg1,FindImg2,(0,0))
        攻击目标(player, FindImg1, FindImg2, (250, 0))

def printtime():
    global last_time
    end_time = time.time()  # 记录结束时间
    print(f"时间：{end_time - last_time}秒,{(end_time - start_time)/60}分")
    last_time = end_time

def 结算进行中(player):
    print('结算进行中',player.isend)
    if player.isend > 10:
        player.isend = 0
    if player.isend < 1:

        printtime()

        player.isend += 1
        player.resetCD()

        pydirectinput.press('Insert')
        time.sleep(3)
        if random.random() < 0.25:
            pydirectinput.press('a')
            time.sleep(0.5)
            pydirectinput.press('space')
            time.sleep(0.5)
            pydirectinput.press('left')
            time.sleep(0.5)
            pydirectinput.press('space')
            time.sleep(0.5)
        pydirectinput.press('esc')
        pydirectinput.press('Delete')
        time.sleep(5)
        return True

    player.isend += 1
    pydirectinput.press('x')
    time.sleep(1)