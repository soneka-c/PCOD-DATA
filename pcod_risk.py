def calculate_pcod_risk(bmi, irregular_cycles, acne, hair_growth):
    score = 0

    if bmi >= 25:
        score += 2
    if irregular_cycles:
        score += 3
    if acne:
        score += 2
    if hair_growth:
        score += 3

    return score


print("PCOD Risk Score Calculator")

bmi = float(input("Enter BMI: "))
irregular = input("Irregular cycles? (y/n): ").lower() == "y"
acne = input("Acne present? (y/n): ").lower() == "y"
hair = input("Excess hair growth? (y/n): ").lower() == "y"

risk = calculate_pcod_risk(bmi, irregular, acne, hair)

print("\nRisk Score:", risk)

if risk >= 7:
    print("High PCOD risk — clinical evaluation recommended")
elif risk >= 4:
    print("Moderate risk — monitor symptoms")
else:
    print("Low risk")
