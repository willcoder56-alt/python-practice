#Ehhhhh I just couldnt figure out how to download the txt file from the googly classroom

with open("scores.txt", "w") as f:
    f.write("Maya,92\n")
    f.write("Leo,67\n")
    f.write("Priya,85\n")
    f.write("Sam,58\n")
    f.write("Jordan,74\n")

total_score = 0
student_count = 0
report_lines = []

# read line by line
with open("scores.txt", "r") as f:
    for line in f:
        # strip and split
        name, score_str = line.strip().split(',')
        score = int(score_str)
        
        # YOU SHALL PASS (if you get atleast a 70)
        if score >= 70:
            status = "PASS"
        else:
            status = "FAIL"
            
        # Formating
        report_lines.append(f"{name}: {status} ({score})\n")
        
        # Track total and count 
        total_score += score
        student_count += 1

# calc (short for calculate btw) avg rounded to one dec
class_average = total_score / student_count
report_lines.append(f"Class average: {class_average:.1f}")

# write
with open("report.txt", "w") as f:
    f.writelines(report_lines)



