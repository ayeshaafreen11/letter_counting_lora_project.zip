import re

def numbering_reward(text):
    return 1 if re.search(r"\d", text) else -1

def spelling_reward(text):
    return 1 if ":" in text else -1

def formatting_reward(text):
    return 1 if "," in text else -1

def counting_reward(pred, truth):
    return 5 if pred == truth else -5

def correctness_reward(pred, truth):
    return 10 if pred.strip() == truth.strip() else -10
