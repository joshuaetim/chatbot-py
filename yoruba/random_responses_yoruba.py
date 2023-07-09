import random


def random_string():
    random_list = [
        "Ṣé ó lè tún ìbèèrè yẹn sọ?",
        "Ṣe o lè ṣe aláyé?",
        "Kò yè mí ọ́.",
        "Mí ó ní ìdáhùn sí ìbèèrè yẹn."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
