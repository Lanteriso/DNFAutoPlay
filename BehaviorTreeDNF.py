import time

import myfunction
import MiniMap
import pydirectinput
import threading

presslist = {'up':False,'down':False,'left':False,'right':False}

global_variable = None

def RunBehaviorTree(player, monster):
    global global_variable
    global_variable = player
    while 1:
        运行状态(player)

def 运行状态(player):
    #print(player.状态)
    if player.状态 == "默认":
        player.状态 = "副本中"
    elif player.状态 == "副本中":
            GetTarget(player)
    elif player.状态 == "移动中":
        if 完成移动(player):
            释放按键()
            player.状态 = "副本中"
    elif player.状态 == "战斗中":
        if not 战斗进行中(player):
            player.状态 = "移动中"
    elif player.状态 == "结算中":
        if not 结算进行中(player):
            player.状态 = "默认"





def GetTarget(player):
    FindImg1 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapPlayer.PNG', 0.7, 1, None, [[0, 0],]],['resources/destroyedcastleofdead/MiniMapPlayer1.PNG', 0.7, 1, None, [[0, 0],]], ['resources/destroyedcastleofdead/MiniMapPlayer2.PNG', 0.7, 1, None, [[18, 0],]], ])
    FindImg3 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapNone.PNG', 0.7, 1, None, [[25, 200],]], ])
    FindImg4 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapBoss.PNG', 0.7, 1, None, [[25, 200],]], ])
    FindImg5 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/zctz.PNG', 0.7, 1, None, [[36, 13],]],])
    if FindImg3 and FindImg4 and FindImg1:
        player.currentroomlist = MiniMap.获取玩家当前房间坐标2(FindImg4, FindImg1)
        player.状态 = "移动中"
    elif FindImg4:
        if FindImg4 and FindImg1:
            player.currentroomlist = MiniMap.获取玩家当前房间坐标2(FindImg4, FindImg1)
        player.状态 = "战斗中"
    elif FindImg5:
        player.状态 = "结算中"
    else:
        释放按键() # 找不到目标，通常在通关之后

def 完成移动(player):
    FindImg3 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapNone.PNG', 0.7, 1, None, [[25, 200], 'right']], ])
    if not FindImg3:return True
    FindImg1 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/0.PNG', 0.6, 1.62, None, [[70, player.身高], 'right']],['resources/destroyedcastleofdead/0r.PNG', 0.6, 1.62, None, [[1, 280], 'right']],['resources/destroyedcastleofdead/0l.PNG', 0.6, 1.62, None, [[70, 280], 'right']], ])
    FindImg2 = myfunction.试验查找指定图片([0, 0, 1920, 1080], player.currentroomlist)

    if FindImg1 and FindImg2:
        AIMoveTo(FindImg1,FindImg2,(0,0))
    else:# 找不到图片时移动结束，距离小时移动完成
        return True

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

        return True

def AIMoveTo2():
    TargetLocation = (1280//2,740)
    while 1:
        PlayLocation = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/0.PNG', 0.6, 1.62, None, [[70, 260], 'right']],['resources/destroyedcastleofdead/0r.PNG', 0.6, 1.62, None, [[1, 280], 'right']],['resources/destroyedcastleofdead/0l.PNG', 0.6, 1.62, None, [[70, 280], 'right']], ])
        if PlayLocation:
            x = TargetLocation[0] - (PlayLocation[5][0][0] + PlayLocation[4][0][0])
            y = TargetLocation[1] - (PlayLocation[5][0][1] + PlayLocation[4][0][1])
            print('【2】移动',x,y)
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
                释放按键()
                ppp = "right" if x > 0 else "left"

                skills = global_variable.use_random_available_skill((0, 0))
                if skills:
                    pydirectinput.press(ppp)
                    pydirectinput.press(skills.name)
                    time.sleep(skills.press_time)
                    释放按键()
                return True

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

    FindImg1 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapPlayer.PNG', 0.7, 1, None, [[0, 0],]],['resources/destroyedcastleofdead/MiniMapPlayer1.PNG', 0.7, 1, None, [[0, 0],]], ['resources/destroyedcastleofdead/MiniMapPlayer2.PNG', 0.7, 1, None, [[18, 0],]], ])
    FindImg2 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapBoss.PNG', 0.7, 1, None, [[25, 200], 'right']], ])
    # FindImg3 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapNone.PNG', 0.7, 1, None, [[25, 200], 'right']], ])
    if FindImg1 and FindImg2:

        print('room',FindImg2[5][0], FindImg1[5][0],player.状态)
        return MiniMap.获取玩家当前房间(FindImg2[5][0], FindImg1[5][0])



def 战斗进行中(player):

    FindImg2 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapBoss.PNG', 0.7, 1, None, [[25, 200], 'right']], ])
    FindImg3 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapNone.PNG', 0.7, 1, None, [[25, 200], 'right']], ])
    FindImg4 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapPlayer.PNG', 0.7, 1, None, [[0, 0],]],['resources/destroyedcastleofdead/MiniMapPlayer1.PNG', 0.7, 1, None, [[0, 0],]], ['resources/destroyedcastleofdead/MiniMapPlayer2.PNG', 0.7, 1, None, [[18, 0],]], ])
    if FindImg3 or not FindImg2:return False    # 可进入下一个房间，战斗结束
    FindImg5 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/0.PNG', 0.6, 1.62, None, [[70, player.身高], 'right']],['resources/destroyedcastleofdead/0r.PNG', 0.6, 1.62, None, [[1, 280], 'right']],['resources/destroyedcastleofdead/0l.PNG', 0.6, 1.62, None, [[70, 280], 'right']], ])
    FindImg6 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/1.PNG', 0.6, 1.62, None, [[70, 1], 'right']], ['resources/destroyedcastleofdead/2.PNG', 0.7, 1.62, None, [[70, 1], 'right']],['resources/destroyedcastleofdead/sstl.PNG', 0.7, 1, None, [[43, 130], 'right']],['resources/destroyedcastleofdead/hbrwg.PNG', 0.7, 1, None, [[53, 280], 'right']],['resources/destroyedcastleofdead/3.PNG', 0.7, 1, None, [[72, 1], 'right']],])
    if FindImg5 and FindImg6:
        攻击目标(player,FindImg5,FindImg6,(250,0))
    else:
        释放按键()
        因找不到敌人而移动2(player)
    return True


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
        AIMoveTo(PlayLocation,TargetLocation,(250,0))



def 因找不到敌人而移动(player):
    FindImg1 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapPlayer.PNG', 0.7, 1, None, [[0, 0],]],['resources/destroyedcastleofdead/MiniMapPlayer1.PNG', 0.7, 1, None, [[0, 0],]], ['resources/destroyedcastleofdead/MiniMapPlayer2.PNG', 0.7, 1, None, [[18, 0],]], ])
    FindImg3 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/MiniMapBoss.PNG', 0.7, 1, None, [[25, 200], 'right']], ])
    if FindImg3 and FindImg1:
        player.currentroomlist = GetCurrentRoom(player)
        if player.currentroomlist:
            FindImg1 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/0.PNG', 0.6, 1.62, None, [[70, player.身高], 'right']],['resources/destroyedcastleofdead/0r.PNG', 0.6, 1.62, None, [[1, 280], 'right']],['resources/destroyedcastleofdead/0l.PNG', 0.6, 1.62, None, [[70, 280], 'right']], ])
            FindImg2 = myfunction.试验查找指定图片([0, 0, 1920, 1080], player.currentroomlist)
            if FindImg1 and FindImg2:
                AIMoveTo(FindImg1,FindImg2,(0,0))

def 因找不到敌人而移动2(player):
    if player.currentroomlist:
        FindImg1 = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/destroyedcastleofdead/0.PNG', 0.6, 1.62, None, [[70, player.身高], 'right']],['resources/destroyedcastleofdead/0r.PNG', 0.6, 1.62, None, [[1, 280], 'right']],['resources/destroyedcastleofdead/0l.PNG', 0.6, 1.62, None, [[70, 280], 'right']], ])
        FindImg2 = myfunction.试验查找指定图片([0, 0, 1920, 1080], player.currentroomlist)
        if FindImg1 and FindImg2:
            AIMoveTo(FindImg1,FindImg2,(0,0))

def 结算进行中(player):

    player.resetCD()
    pydirectinput.press('esc')
    pydirectinput.press('Insert')
    time.sleep(3)
    pydirectinput.press('Delete')
    time.sleep(5)
    return False