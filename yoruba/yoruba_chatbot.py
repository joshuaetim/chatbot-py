import json
import re
import random_responses_yoruba


def load_json(file):
    with open(file) as bot_responses:
        print(f"loaded '{file}' successfully!")
        return json.load(bot_responses)


responses_data = load_json("bot.json")


def get_response(input_string):
    split_message = re.split(r"\s+|[,;?!.-]\s*", input_string.lower())
    score_list = []

    for response in responses_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        if input_string.lower() in response["user_input"]:
            response_score += 1
        elif required_score == len(required_words):
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1

        score_list.append(response_score)

    best_response = max(score_list)
    response_index = score_list.index(best_response)
    # print("response_index")

    if input_string == "":
        return "Jọwọ tẹ biọ́rọ̀ sílẹ̀ pẹ̀lú awọn àkọsílẹ :)"

    if best_response != 0:
        return responses_data[response_index]["bot_response"]

    return random_responses_yoruba.random_string()


while True:
    user_input = input("ìwọ: ")
    print("Àbọ̀tẹ́: ", get_response((user_input)))
