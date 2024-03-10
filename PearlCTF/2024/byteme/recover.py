from hashlib import md5
import time

def crackme():
    print()
    print('Welcome Warrior! You have made it till here')
    print('This is where best of the best have fallen prey to the fate')
    print()

    print('It is written that only the true Thalor can get The sword of Eldoria')
    print('Do you have what it takes to be Thalor?')
    print('Prove your mettle by bringing the sword out of the castle')
    print()

    print('Go on! unlock the castle with XEKLEIDOMA spell')
    print()

    spell = input('> ')
    print()

    if len(spell.strip()) != 12 or md5(spell.strip().encode()).hexdigest() != '9ce86143889d80b01586f8a819d20f0c':
        print('You are not THE ONE')
        print('True Thalor is a master of sorcery')
        print('Ground beneath you opens up and you fall into the depths of hell')
        exit()
    else:
        print('The door is opened!')
        print('You surely mastered sorcery')
        print()

    time.sleep(3)
    return spell


def solveme():
    print("As you walk in, you see a spectral figure Elyrian, the Guardian of Souls")
    print("He speaks to you in a voice that echoes through the chamber")
    print()
    print('"Brave warrior, before you lies the next trial on your path. Answer my riddle, and prove your worthiness to continue your quest."')
    print('\n"I am a word of ten, with numbers and letters blend,\nUnravel me, and secrets I\'ll send.\nThough cryptic in sight, I hold the code tight,\nUnlock my mystery with wit and might."\n')

    answer = input("> ")
    print()

    answer = list(map(ord, list(answer.strip())))

    assert len(answer) == 10

    if (answer[6] + answer[7] + answer[8] - answer[5] == 190 and
        answer[6] + answer[5] + answer[5] - answer[2] == 202 and
        answer[9] + answer[3] + answer[2] + answer[5] == 433 and
        answer[7] + answer[0] - answer[0] + answer[3] == 237 and
        answer[1] - answer[9] - answer[5] + answer[4] == -50 and
        answer[2] - answer[3] + answer[5] - answer[0] == -6 and
        answer[8] - answer[7] - answer[6] + answer[5] == -88 and
        answer[0] + answer[8] - answer[5] - answer[3] == -117 and
        answer[5] - answer[6] - answer[0] - answer[5] == 385 and
        answer[5] - answer[4] + answer[5] - answer[9] == 63 and
        answer[5] - answer[3] + answer[6] - answer[0] == -6 and
        answer[8] + answer[3] + answer[7] - answer[6] == 167 and
        answer[6] - answer[5] - answer[0] - answer[5] == -126 and
        answer[2] - answer[3] - answer[0] + answer[5] == -199):
        print("You have proven your `wit and might`")
        print("Elyrian, the Guardian of Souls, bows to you")
        print("You have unlocked the next chamber")
    else:
        print("You are not worthy")
        print("Your soul has been cursed")
        print("You will seek your own death in a fortnight")
        exit()


def breakme():
    sword = sword.split('\n')
    for line in sword:
        print(line)
        time.sleep(0.1)

    print()
    print("There it is! The sword of Eldoria")
    print("Break its shackles and show that you are the Thalor")
    print()

    chain = input("> ")

    best = [117, 84, 87, 108, 59, 85, 66, 71, 71, 30, 16]
    mod = list()

    plier = 69

    for i in range(len(chain)):
        mod.append(plier ^ ord(chain[i]))
        plier = ord(chain[i])

    if mod == best:
        print("Oh! True Thalor, you have broken the shackles")
        print("You are the chosen one")
        print("I kneel before you")
        print("Go on! Take the sword and fulfill your destiny")
        print()
        time.sleep(2)
        return chain
    else:
        print("You are not worthy")
        print("The fate has you in its grip")
        print("You will be forgotten in the sands of time")
        exit()

if __name__ == '__main__':
    spell = crackme()
    answer = solveme()
    chain = breakme()

    print('Thalor has risen!')
    print('The prophecy has been fulfilled')
    print()
    print('#######################################')
    print('##                                  ##')
    print('## {}{}{} ##'.format(spell, answer, chain))
    print('##                                  ##')
    print('#######################################')