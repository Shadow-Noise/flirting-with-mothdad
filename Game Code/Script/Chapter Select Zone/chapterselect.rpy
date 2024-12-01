init python:
    def seenLabel(xlabel=""):
        return gameVersion == 3 or renpy.seen_label(xlabel)

label redo_identity_loop:
    menu:
        extend ""
        "Take me to {b}Chapter Select.{/b}":
            jump chapter_select_label

        "Send me to the Fights!":
            jump battle_select_label

        "I want to change some gameplay things.":
            voice atticus_mixingthingsup
            menu:
                extend ""
                "I want to change my dice":
                    voice atticus_dicechoice
                    Atticus "Alright then, which one?{nw}"
                    $displaymenu = True

                    call dice_choice_menu from _call_dice_choice_menu

                    python:
                        displaymenu = True
                        diceBot.setDieType(persistent.dieSettings)
                        pc_karma = diceBot.maxKarma
                    voice atticus_chuckle
                    Atticus "Wanna test them out?{nw}"
                    menu:
                        extend ""

                        "Sure!":
                            call dice_roll(rMod=0, rDiff=7, rDesc="Test Roll") from _call_dice_roll_1
                            $pc_karma = diceBot.maxKarma
                        "No thanks.":
                            pass


                    $Atticus_State["eye"] = 6
                    $displaymenu = True
                    voice atticus_anythingelsea
                    Atticus "Anything else?{nw}"
                    jump redo_identity_loop
                "I want to change the game's difficulty.":
                    voice atticus_diffchoice
                    Atticus "Alright, what kind of heat are you looking for?"

                    call diff_choice_menu from _call_diff_choice_menu

                    voice atticus_anythingelsea
                    Atticus "Anything else?{nw}"
                    jump redo_identity_loop
                "I want to redo my stats!":
                    call stats_redo_questions from _call_stats_redo_questions
                    $displaymenu = True
                    $Atticus_State["eye"] = 6
                    voice atticus_anythingelsea
                    Atticus "Anything else?{nw}"
                    jump redo_identity_loop

        "I want to change some personal things.":
            voice atticus_mixingthingsup
            menu:
                extend ""
                "I want to change my style.":
                    $Atticus_State["armR"] = 1
                    $Atticus_State["eye"] = 5
                    voice atticus_chuckle

                    Atticus "Nothin' wrong with swapping your style!\n\n .,What would you like to change?{nw}"
                    $Atticus_State["armR"] = 1
                    $Atticus_State["eye"] = 0
                    show robyn:
                        matrixcolor TintMatrix("#b6f0fc")
                        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                        xcenter 1.3
                        ease 1.0 xcenter 0.85
                    show atticus:
                        ease 0.5 xcenter 0.2
                    call id_Loop from _call_id_Loop_1
                    show robyn:
                        ease 1.0 xcenter 1.5
                    show atticus:
                        ease 0.5 xcenter 0.5
                    $Atticus_State["armR"] = 0
                    voice atticus_anythingelsea
                    Atticus "Lookin' slick kiddo. \n\n What else do you need?"
                    jump redo_identity_loop
                "I want to change my name.":
                    voice atticus_reminded
                    $Atticus_State["eye"] = 0
                    $displaymenu = False
                    python:
                        PCname = renpy.input("First Name",length=10)
                        persistent.RobynName[0] = PCname = PCname.strip()
                    play sfx select3
                    python:
                        PClastname = renpy.input("Last Name",length=10)
                        persistent.RobynName[1] = PClastname = PClastname.strip()
                    play sfx select3

                    python:
                        if not PCname:
                            persistent.RobynName[0] = PCname = "Robyn"
                        if not PClastname:
                            persistent.RobynName[1] = PClastname = "Hart"

                        save_name = "[PCname] [PClastname]"

                    Atticus "[PCname] [PClastname] huh? \n\n Consider it done."

                    $displaymenu = True
                    Atticus "How would you like to be addressed?{nw}"
                    menu:
                        extend ""
                        "He/Him":
                            python:
                                persistent.RobynPronouns = 0
                                PCthey = "he"
                                PCthem = "him"
                                PCtheir = "his"
                                PCtheirs = "his"
                                PCThey = "He"
                                PCThem = "Him"
                                PCTheir = "His"
                                PCTheirs = "His"
                        "She/Her":
                            python:
                                persistent.RobynPronouns = 1
                                PCthey = "she"
                                PCthem = "her"
                                PCtheir = "her"
                                PCtheirs = "hers"
                                PCThey = "She"
                                PCThem = "Her"
                                PCTheir = "Her"
                                PCTheirs = "Hers"
                        "They/Them":
                            python:
                                persistent.RobynPronouns = 2
                                PCthey = "they"
                                PCthem = "them"
                                PCtheir = "their"
                                PCtheirs = "theirs"
                                PCThey = "They"
                                PCThem = "Them"
                                PCTheir = "Their"
                                PCTheirs = "Theirs"
                    Atticus "I'll keep that in mind."

                    $displaymenu = True
                    voice atticus_anythingelseb
                    Atticus "Anything else?"
                    $Atticus_State["eye"] = 0
                    $Atticus_State["armR"] = 0
                    jump redo_identity_loop
                "I want to change my voice.":
                    Atticus "Alright then, which one?{nw}"

                    menu:
                        extend ""

                        "Voice A":
                            $robynvoice = persistent.pcvoice = 1
                        "Voice B":
                            $robynvoice = persistent.pcvoice = 2

                    $Atticus_State["eye"] = 6
                    play voice2 [RobynSays("Generic","Excited"),audio.atticus_anythingelsea]
                    Atticus "Anything else?{nw}"
                    jump redo_identity_loop

        "I'd like to go to the testing zone" if gameVersion == 3:
            jump test_zone_select_label

        "I wanna flirt.":
            $displaymenu = False
            $Atticus_State["eye"] = 4

            $xStr = renpy.random.choice(["Ehm..","Go ahead.","Uh.","Shoot your shot kid.","You're kidding. Right?","Don't give me that look.","Don't tell Atlas about this..."])
            Atticus "[xStr]"

            $Atticus_State["eye"] = 3

            voice atticus_hmmd
            Atticus "{sc=6}...{/sc}"

            $Atticus_State["eye"] = 5
            show atticus:
                blur 0
                ease 0.2 yoffset -20
                ease 0.2 yoffset 0

            $xStr = renpy.random.choice(["Come a little closer, I won't bite... Unless you want me to..",
                "Alone on a late night? Don't worry, I'll be there soon..",
                "If you let me, I'll carry you off into the night..",
                "Well aren't you a cute little thing?",
                "Are you a lamp? Because I would crash into a window and die for you..",
                "Wanna touch my antennae?",
                "Who up moffing they man?",
                "None of this is canon. What do I mean? Nothing, Nothing.."])

            voice atticus_chuckle
            Atticus "[xStr]"
            $Atticus_State["eye"] = 6

            voice atticus_anythingelsea
            Atticus "Anything else?{nw}"
            jump redo_identity_loop

    return

label diff_choice_menu:
    menu:
        extend ""

        "Human (Easy)":
            Atticus "Ah easy. This mode lowers the damage you and your allies take in battles as well as slightly making rolls easier."
            $gameDiff = persistent.gD = 1

        "Cryptid (Default)":
            Atticus "I see. Going with the intended difficulty."
            $gameDiff = persistent.gD = 2

        "Ghoul (Hard)":
            Atticus "So you're looking for a challenge. Ghoul essentially raises the damage/healing everyone takes. It's more explosive, but designed to be faster for those looking for low turn counts in battles."
            $gameDiff = persistent.gD = 3

        "Demon (Extra Hard)":
            Atticus "Oh you're a masochist. On top of raising all damage/healing values, this difficulty raises all roll difficulties as well."
            $gameDiff = persistent.gD = 4
    return

label dice_choice_menu:
    menu:
        extend ""

        "Ol' Reliable" if persistent.unlockedDice[0] or gameVersion >= 2:
            $persistent.dieSettings = 1
            $displaymenu = False
            Atticus "Ah right, ol reliable. Even if it's a little basic, the base die are nothing if not reliable."
        "Die Hard Purist" if persistent.unlockedDice[1] or gameVersion >= 2:
            $persistent.dieSettings = 2
            $displaymenu = False
            Atticus "Good choice. Die Hard Purist is the kind of dice you go for if you want to mostly forego the karma system. With only one karma, you'll have to rely more on luck."

            Atticus "Good thing it's more weighted to higher numbers."
        "Lemon Squeezy" if persistent.unlockedDice[2] or gameVersion >= 2:
            $persistent.dieSettings = 3
            $displaymenu = False
            Atticus "Lemon Squeezy. This one's definitely more suited if you're not looking for much of a challenge. Even if you fail your rerolls, you still get a point of karma back."
        "Jackalope's Fate" if persistent.unlockedDice[3] or gameVersion >= 2:
            $persistent.dieSettings = 4
            $displaymenu = False
            Atticus "You like a bit of chaos don't you? Jackalope's Fate is either a complete success or failure. No numbers, just success or fail on the flip of a coin."
        "Snake Eye Sam" if persistent.unlockedDice[4] or gameVersion >= 2:
            $persistent.dieSettings = 5
            $displaymenu = False
            Atticus "Snake Eye Sam's a weird one. it always fails the first roll, and then rolls at least an 8 on each subsequent reroll. This one's knee deep in karma management."

        "More" if True in persistent.unlockedDice[5:] or gameVersion >= 2:
            $displaymenu = True
            menu:
                extend ""

                "Full Moon Duet" if persistent.unlockedDice[5] or gameVersion >= 2:
                    $persistent.dieSettings = 6
                    $displaymenu = False
                    Atticus "Full Moon Duet is a fun one. Instead of 2d6, it's a d4 and a d8!"
                    Atticus "..."
                    Atticus "It's mostly aestetic difference. This set is just more likely to get something more towards the middle."
                "Even Stevens" if persistent.unlockedDice[6] or gameVersion >= 2:
                    $persistent.dieSettings = 7
                "Prime Party" if persistent.unlockedDice[7] or gameVersion >= 2:
                    $persistent.dieSettings = 8
                "3 Lizards In a Trenchcoat" if persistent.unlockedDice[8] or gameVersion >= 2:
                    $persistent.dieSettings = 9
                "Mothman's Hoard" if persistent.unlockedDice[9] or gameVersion >= 2:
                    $persistent.dieSettings = 10
                "New Jersey Greataxe" if persistent.unlockedDice[10] or gameVersion >= 2:
                    $persistent.dieSettings = 11

    python:
        diceBot.setDieType(persistent.dieSettings)
        pc_karma = diceBot.maxKarma
    return

label dice_choice_menu_alt:
    menu:
        extend ""

        "Ol' Reliable" if persistent.unlockedDice[0] or gameVersion >= 2:
            $persistent.dieSettings = 1
            $displaymenu = False
            Narrator "Ol' reliable are the standard dice. 3 karma with both dice being 1-6."
        "Die Hard Purist" if persistent.unlockedDice[1] or gameVersion >= 2:
            $persistent.dieSettings = 2
            $displaymenu = False
            Narrator "Die Hard purist is a set of dice characterized by having high rolls but only 1 karma. If you fail on a reroll though, you still get that karma back."

        "Lemon Squeezy" if persistent.unlockedDice[2] or gameVersion >= 2:
            $persistent.dieSettings = 3
            $displaymenu = False
            Narrator "Lemon Squeezy is an easier die with 6 karma, higher rolls, and the ability to get karma back even on failed rolls. It's easily the best dice in the game all for the sake of making the game easier if you so choose."

        "Jackalope's Fate" if persistent.unlockedDice[3] or gameVersion >= 2:
            $persistent.dieSettings = 4
            $displaymenu = False
            Narrator "Jackalope's fate has 2 outcomes, complete success or complete failure. It's a split 50/50 set for those who like chaos, 2 max karma, and karma returned on failed rerolls."
        "Snake Eye Sam" if persistent.unlockedDice[4] or gameVersion >= 2:
            $persistent.dieSettings = 5
            $displaymenu = False
            Narrator "Snake Eye Sam always rolls snake eyes on the first roll, but on rerolls it never rolls below an 8. With a staggering 8 max karma, this set is focused on managing karma and failing tactically."

        "More" if True in persistent.unlockedDice[5:] or gameVersion >= 2:
            $displaymenu = True
            menu:
                extend ""

                "Full Moon Duet" if persistent.unlockedDice[5] or gameVersion >= 2:
                    $persistent.dieSettings = 6
                    $displaymenu = False
                    Atticus "Full Moon Duet is a fun one. Instead of 2d6, it's a d4 and a d8!"
                    Atticus "..."
                    Atticus "It's mostly aestetic difference. This set is just more likely to get something more towards the middle."
                "Even Stevens" if persistent.unlockedDice[6] or gameVersion >= 2:
                    $persistent.dieSettings = 7
                "Prime Party" if persistent.unlockedDice[7] or gameVersion >= 2:
                    $persistent.dieSettings = 8
                "3 Lizards In a Trenchcoat" if persistent.unlockedDice[8] or gameVersion >= 2:
                    $persistent.dieSettings = 9
                "Mothman's Hoard" if persistent.unlockedDice[9] or gameVersion >= 2:
                    $persistent.dieSettings = 10
                "New Jersey Greataxe" if persistent.unlockedDice[10] or gameVersion >= 2:
                    $persistent.dieSettings = 11

    python:
        diceBot.setDieType(persistent.dieSettings)
        pc_karma = diceBot.maxKarma
    return

label chapter_select_label:
    $displaymenu = True
    voice atticus_chselect
    Atticus "Where are you going?{nw}"

    menu:
        extend ""
        "The VERY beginning":
            Atticus "Sure. Let me just forget everything about you."
            call choose_identity from _call_choose_identity_1
            jump Ch0_Intro
        "Chapter 0":
            jump Ch0_SectionSelect_Label

        "Chapter 1" if seenLabel("Ch1_Start"):
            jump Ch1_SectionSelect_Label

        "Chapter 2" if seenLabel("Ch2_DreamHouse_Intro"):
            jump Ch2_SectionSelect_Label

        "Hangouts" if checkUnlock("MM",1) or gameVersion == 3:
            jump Hangouts_select_label


    return

#Chapter 0
label Ch0_SectionSelect_Label:
    menu:
        extend ""
        "Play Normally":
            jump Ch0_Intro
        "Elkhorn Radio" if seenLabel("atTheStation"):
            jump atTheStation
        "Elkhorn Radio (Inside the Station & Investigation)" if seenLabel("exploreStation"):
            jump exploreStation
        "Madhouse's Show" if seenLabel("RadioShow"):
            jump RadioShow
        "Madlas Tutorial" if seenLabel("fightbuildup"):
            python:
                displaymenu = False
                PC_Stats = RobynUnit()
                PC_Stats.updateStats()
                PC_Stats.resetSelf()

                PC_Stats.SetAttackMoves(['Bash', 'Cheer', 'Focus', 'Heart Out'], 'FIGHT_01_MM_ROBYN_')

                playerUnits = []
                playerUnits.append(PC_Stats)

            jump fightbuildup
        "Post-Madhouse Bash & Ghost Zone" if seenLabel("MM_fightAftermath"):
            $displaymenu = False
            jump MM_fightAftermath
        "After the Ghost Zone & Driving Home" if seenLabel("leavingElkhornRadio_ch0"):
            $displaymenu = False
            jump leavingElkhornRadio_ch0


#Side Story / B Plot
label Hangouts_select_label:
    menu:
        extend ""
        "Madhouse #1" if checkUnlock("MM",1):
            jump MM_Hangout1

        "Madhouse #2" if checkUnlock("MM",2):
            jump Madhouse_Hangout2

        "August #1" if checkUnlock("Gus",1):
            jump August_Hangout1

#Test Zones
label test_zone_select_label:
    menu:
        extend ""
        "Jos' Test Zone":
            $displaymenu = False
            ##TESTING FOR JOS COMMENT IF NEEDED
            jump FIGHT_00_DUNGEON_MAESTRO
        "Dom's Test Zone":
            $displaymenu = False
            #In scripts\testingzone.rpy
            jump testZone
        "Zakirin's Test Zaone":
            $displaymenu = False
            #In scripts/biscuitTown.rpy
            jump biscuittown

#Battles
label battle_select_label:
    if gameVersion < 2:
        Atticus "Here you can fight optional or powered up versions of bosses throughout the game. On top of that, certain patrons can even fight Bosses that're still being developed!"

    voice atticus_diffchoiceb
    Atticus "So, which battle shall we try?{nw}"

    menu:
        extend ""
        "Madhouse" if seenLabel("FIGHT_01_MADHOUSE"):
            voice atticus_goodchoice
            call FIGHT_01_MADHOUSE from _call_FIGHT_01_MADHOUSE

        "Mr. Walker" if seenLabel("FIGHT_05_MISTWALKER"):
            voice atticus_goodchoice
            call FIGHT_05_MISTWALKER from _call_FIGHT_05_MISTWALKER_1

        "Jamie" if seenLabel("FIGHT_06_JAMIE"):
            voice atticus_goodchoice
            call FIGHT_06_JAMIE from _call_FIGHT_06_JAMIE

        "Dream Guard" if gameVersion >= 1:
            voice atticus_goodchoice
            call FIGHT_04_DREAMOZ from _call_FIGHT_04_DREAMOZ

        "Dream Eater" if gameVersion >= 1:
            voice atticus_goodchoice
            call FIGHT_02_LEX from _call_FIGHT_02_LEX

        "EX Battles" if seenLabel("FIGHT_01_MADHOUSE"):
            menu:
                extend ""

                "Gladhouse":
                    voice atticus_goodchoice
                    call FIGHT_01B_MADHOUSE from _call_FIGHT_01B_MADHOUSE

                "Madlas EX":
                    voice atticus_goodchoice
                    call FIGHT_00B_MADLAS from _call_FIGHT_00B_MADLAS

                "Book Babes" if gameVersion >= 1:
                    voice atticus_goodchoice
                    Atticus "This fight is going to be scrapped into an EX Battle and replaced with a new fight as an FYI but enjoy!"

                    call FIGHT_03_LIB from _call_FIGHT_03_LIB
                    
                "Mistwalker EX" if seenLabel("FIGHT_05_MISTWALKER"):
                    voice atticus_goodchoice
                    call FIGHT_05B_MISTWALKER from _call_FIGHT_05B_MISTWALKER

                "Jamie EX" if seenLabel("FIGHT_06_JAMIE"):
                    call FIGHT_06B_JAMIE from _call_FIGHT_06B_JAMIE

                "Robo-Atlas" if seenLabel("FIGHT_06_JAMIE"):
                    voice atticus_goodchoice
                    call FIGHT_03_RBA from _call_FIGHT_03_RBA


    $HideBars()
    jump start
