import json
import re

# For easy filtering just input the keys you want to ignore
keys_to_ignore = {
    "image",
    "effect_name",
    "effect_name_JP",
    "effect1",
    "Cooldown",
    "Cooldown2",
}


def remove_words_to_ignore(string):
    """Add words you want to ignore here"""
    return string \
        .replace("turn", "Turn") \
        .replace("  ", " ").strip()


def check_incorrect_memos():
    """
    A function which compares field of generated memorias with their counterpart on the wikia
    To assure this is up-to-date run template_downloader.py#load_memos first"""

    with open("memos.json", "r", encoding="utf-8") as f:
        memos = json.load(f)

    keys = {
               "image",
               "effect_name",
               "effect_name_JP",
               "effect1",
               "effect2",
               "Cooldown",
               "Cooldown2",
           } - keys_to_ignore

    x = 0
    differences = 0
    with open("txts/memoria_url_id.txt", "r", encoding="utf-8") as f:
        for line in reversed(f.readlines()):
            x += 1
            _id, memo = line.strip().split(";")
            memo = memo.replace(" ", "_").replace("?", "%3F").replace(":", "..").replace("/", "-")
            memo = ((memo + '&') if memo[-1] == '.' else memo)
            if _id in ("9002", "9001"):
                continue
            path = f"wikia_pages/memorias/{memo}/Template-{memo}.txt".replace(" ", "_")

            with open(path, "r", encoding="utf-8") as f:
                file_text = f.read()
                for key in keys:
                    text = re.findall(rf"{key} *= *(.*)", file_text)
                    generated_text = remove_words_to_ignore(text[0].strip())
                    wikia_text = remove_words_to_ignore(memos[key][_id].strip())

                    if wikia_text != generated_text:
                        differences += 1
                        diff_text = ""
                        length = min(len(wikia_text), len(generated_text))
                        for i in range(length):
                            diff_text += " " if wikia_text[i] == generated_text[i] else generated_text[i]
                        diff_text += wikia_text[length:] + generated_text[length:]
                        print(f"Incorrect for {_id} {key} for {memo}: \n\twiki: {wikia_text}\n\tgen:  {generated_text}\n\tdiff: {diff_text}")
    print(f"\n\nFound {differences} differences")


check_incorrect_memos()
