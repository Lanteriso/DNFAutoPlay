import Character
import time
import BehaviorTreeDNF2
import BehaviorTreeFBNL
import sys

def 自动副本开始(player, monster):
    BehaviorTreeDNF2.RunBehaviorTree(player, monster)

def 风暴逆鳞开始(player, monster):
    BehaviorTreeFBNL.RunBehaviorTree(player, monster)

def print_hi():
    # choice = input("a打怪:")
    choice = sys.argv[1]
    if choice == 'a':
        choice = "自动地牢"
        player = Character.Player("英雄", 500, 10, sys.argv[2])
        monster = Character.Monster("哥布林", 300, 5)
        print(f"{choice} 模式 进入游戏")
        time.sleep(3)  # 切到游戏里
        自动副本开始(player, monster)
    elif choice == 'b':
        choice = "风暴逆鳞"
        player = Character.Player("英雄", 500, 10, sys.argv[2])
        monster = Character.Monster("哥布林", 300, 5)
        print(f"{choice} 模式 进入游戏")
        time.sleep(3)  # 切到游戏里
        风暴逆鳞开始(player, monster)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# python main.py a 驱魔师
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
