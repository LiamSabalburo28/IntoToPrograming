def tally_score(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    score = 0

    if a1.lower() == "mitosis":
        score += 1
    if a2 == "8":
        score += 1
    if a3.lower() == "washington":
        score += 1
    if a4.lower() == "h2o":
        score += 1
    if a5.lower() == "photosynthesis":
        score += 1
    if a6 == "1492":
        score += 1
    if a7.lower() == "sine":
        score += 1
    if a8.lower() == "gravity":
        score += 1
    if a9.lower() == "atp":
        score += 1
    if a10.lower() == "lincoln":
        score += 1

    return score

q1 = input("1. What is the process by which cells divide called? ")
q2 = input("2. What is the value of 2^3? ")
q3 = input("3. What is the last name of the first U.S. president? ")
q4 = input("4. What is the chemical formula for water? ")
q5 = input("5. What process do plants use to make food? ")
q6 = input("6. In what year did Columbus sail to the Americas? ")
q7 = input("7. In trigonometry, what function is abbreviated as 'sin'? ")
q8 = input("8. What force keeps planets in orbit around the sun? ")
q9 = input("9. What molecule stores energy in cells? ")
q10 = input("10. What is the last name of the U.S. president during the Civil War? ")

total = tally_score(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
print("Your score is:", total, "/ 10")