def identify_model(output):
    if "hallucinate" in output:
        return "Possibly GPT-like"
    return "Unknown"
