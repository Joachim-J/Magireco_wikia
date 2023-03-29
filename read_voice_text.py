from json import loads


def read_lines_json():
    with open("jsons/charaCard.json", "r", encoding="utf-8-sig") as f:
        info_dict = loads(f.read())
    overview = []
    for entry in info_dict:
        try:
            lis = info_dict[entry]["charaMessageList"]
        except KeyError:
            print(f"NO VOICELINES FOUND FOR ID={entry}")
            continue
        lines = [int(entry)]
        for line in lis:
            lines.append(line["message"])
        overview.append(lines)
    return overview


def mats_sender(voice_list):
    overview = {}
    for line in voice_list:
        text = """{{Quotes
|id = """ + str(line[0]) + """
| Japanese Self introduction = 
| NA Self introduction = 
| Self introduction = 
| Japanese Strengthening complete = 
| NA Strengthening complete = 
| Strengthening complete = 
| Japanese Strengthening max = 
| NA Strengthening max = 
| Strengthening max = 
| Japanese Episode lvl up = 
| NA Episode lvl up = 
| Episode lvl up = 
| Japanese Magical release 1 = 
| NA Magical release 1 = 
| Magical release 1 = 
| Japanese Magical release 2 = 
| NA Magical release 2 = 
| Magical release 2 = 
| Japanese Magical release 3 = 
| NA Magical release 3 = 
| Magical release 3 = 
| Japanese Magia lvl up = 
| NA Magia lvl up = 
| Magia lvl up = 
| Japanese Awaken 1 = 
| NA Awaken 1 = 
| Awaken 1 = 
| Japanese Awaken 2 = 
| NA Awaken 2 = 
| Awaken 2 = 
| Japanese Awaken 3 = 
| NA Awaken 3 = 
| Awaken 3 = 
| Japanese Unused 2 = 
| NA Unused 2 = 
| Unused 2 = 
| Japanese First login of the day = 
| NA First login of the day = 
| First login of the day = 
| Japanese Morning = 
| NA Morning = 
| Morning = 
| Japanese Noon = 
| NA Noon = 
| Noon = 
| Japanese Evening = 
| NA Evening = 
| Evening = 
| Japanese Night = 
| NA Night = 
| Night = 
| Japanese Other times = 
| NA Other times = 
| Other times = 
| Japanese AP full = 
| NA AP full = 
| AP full = 
| Japanese BP full = 
| NA BP full = 
| BP full = 
| Japanese Unused 3 = 
| NA Unused 3 = 
| Unused 3 = 
| Japanese Tap 1 = 
| NA Tap 1 = 
| Tap 1 = 
| Japanese Tap 2 = 
| NA Tap 2 = 
| Tap 2 = 
| Japanese Tap 3 = 
| NA Tap 3 = 
| Tap 3 = 
| Japanese Tap 4 = 
| NA Tap 4 = 
| Tap 4 = 
| Japanese Tap 5 = 
| NA Tap 5 = 
| Tap 5 = 
| Japanese Tap 6 = 
| NA Tap 6 = 
| Tap 6 = 
| Japanese Tap 7 = 
| NA Tap 7 = 
| Tap 7 = 
| Japanese Tap 8 = 
| NA Tap 8 = 
| Tap 8 = 
| Japanese Tap 9 = 
| NA Tap 9 = 
| Tap 9 = 
| Japanese Battle start = 
| NA Battle start = 
| Battle start = 
| Japanese Battle victory 1 = {6} 
| NA Battle victory 1 = 
| Battle victory 1 = 
| Japanese Battle victory 2 = {7} 
| NA Battle victory 2 = 
| Battle victory 2 = 
| Japanese Battle victory 3 = {8} 
| NA Battle victory 3 = 
| Battle victory 3 = 
| Japanese Unused 5 = {10} 
| NA Unused 5 = 
| Unused 5 = 
| Japanese Chapter select 1 = {0} 
| NA Chapter select 1 = 
| Chapter select 1 = 
| Japanese Chapter select 2 = {1} 
| NA Chapter select 2 = 
| Chapter select 2 = 
| Japanese Chapter select 3 = {2} 
| NA Chapter select 3 = 
| Chapter select 3 = 
| Japanese Chapter select 4 = {3} 
| NA Chapter select 4 = 
| Chapter select 4 = 
| Japanese Chapter select 5 = {4} 
| NA Chapter select 5 = 
| Chapter select 5 = 
| Japanese Chapter select 6 = {5} 
| NA Chapter select 6 = 
| Chapter select 6 = 
| Japanese Unused 1 = {9} 
| NA Unused 1 = 
| Unused 1 = 
| Japanese Chapter end 1 = 
| NA Chapter end 1 = 
| Chapter end 1 = 
| Japanese Chapter end 2 = 
| NA Chapter end 2 = 
| Chapter end 2 = 
| Japanese Chapter end 3 = 
| NA Chapter end 3 = 
| Chapter end 3 = 
| Japanese Disc select 1 = 
| NA Disc select 1 = 
| Disc select 1 = 
| Japanese Disc select 2 = 
| NA Disc select 2 = 
| Disc select 2 = 
| Japanese Disc select 3 = 
| NA Disc select 3 = 
| Disc select 3 = 
| Japanese Disc select 4 = 
| NA Disc select 4 = 
| Disc select 4 = 
| Japanese Connect to self from ally disc select = 
| NA Connect to self from ally disc select = 
| Connect to self from ally disc select = 
| Japanese Connect from self to ally disc select = 
| NA Connect from self to ally disc select = 
| Connect from self to ally disc select = 
| Japanese Attack 1 = 
| NA Attack 1 = 
| Attack 1 = 
| Japanese Attack 2 = 
| NA Attack 2 = 
| Attack 2 = 
| Japanese Attack 3 = 
| NA Attack 3 = 
| Attack 3 = 
| Japanese Attack 4 = 
| NA Attack 4 = 
| Attack 4 = 
| Japanese Attack 5 = 
| NA Attack 5 = 
| Attack 5 = 
| Japanese Attack 6 = 
| NA Attack 6 = 
| Attack 6 = 
| Japanese Attack 7 = 
| NA Attack 7 = 
| Attack 7 = 
| Japanese Attack 8 = 
| NA Attack 8 = 
| Attack 8 = 
| Japanese Attack 9 = 
| NA Attack 9 = 
| Attack 9 = 
| Japanese Attack 10 = 
| NA Attack 10 = 
| Attack 10 = 
| Japanese Connect to self from ally Attack = 
| NA Connect to self from ally Attack = 
| Connect to self from ally Attack = 
| Japanese Connect from self to ally = 
| NA Connect from self to ally = 
| Connect from self to ally = 
| Japanese Magia 1 = 
| NA Magia 1 = 
| Magia 1 = 
| Japanese Magia 2 = 
| NA Magia 2 = 
| Magia 2 = 
| Japanese Magia 3 = 
| NA Magia 3 = 
| Magia 3 = 
| Japanese Magia 4 = 
| NA Magia 4 = 
| Magia 4 = 
| Japanese Doppel = 
| NA Doppel = 
| Doppel = 
| Japanese Taking damage = 
| NA Taking damage = 
| Taking damage = 
| Japanese Taking damage while at critical health = 
| NA Taking damage while at critical health = 
| Taking damage while at critical health = 
| Japanese Dying = 
| NA Dying = 
| Dying = 
| Japanese Gacha introduction = 
| NA Gacha introduction = 
| Gacha introduction = 
| Japanese Random 1 = 
| NA Random 1 = 
| Random 1 = 
| Japanese Random 2 = 
| NA Random 2 = 
| Random 2 = 
| Japanese Random 3 = 
| NA Random 3 = 
| Random 3 = 
""".format(line[1], line[2], line[3], line[4], line[5], line[6], line[8], line[9], line[10],
                        line[7], line[11])
        overview[line[0]] = text + "}}"
    return overview
