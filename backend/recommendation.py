from rules import RULES


def get_recommendation(crop, stress):
    """
    Returns irrigation recommendation based on crop and stress level.
    """

    crop = crop.title()
    stress = stress.title()

    if crop not in RULES:
        return {
            "error": f"Crop '{crop}' not found."
        }

    if stress not in RULES[crop]:
        return {
            "error": f"Stress level '{stress}' not found."
        }

    recommendation = RULES[crop][stress]

    return {
        "crop": crop,
        "stress": stress,
        "water": recommendation["water"],
        "time": recommendation["time"],
        "priority": recommendation["priority"]
    }