text_colors = {
    "Black": "40",
    "Red": "41",
    "Green": "42",
    "Yellow": "43",
    "Blue": "44",
    "Purple": "45",
    "Cyan": "46",
    "White": "47"
}
bg_colors = {
    "No Effect": "0",
    "Bold": "1",
    "Underline": "2",
    "Negative1": "3",
    "Negative2": "5"
}
text_style = {
    "Black": "30",
    "Red": "31",
    "Green": "32",
    "Yellow": "33",
    "Blue": "34",
    "Purple": "35",
    "Cyan": "36",
    "White": "37"
}

for k, v in text_colors.items():
    for k1, v1 in bg_colors.items():
        for k2, v2 in text_style.items():
            print(f" \033[{v2};{v};{v1}m \\033[{k2};{k};{k1}")
