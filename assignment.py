# You can remove 'pass' if you written code in the function
# Exercise 1

def save_scores(names, scores, filename):
    file = open(filename,"w")
    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
    file.close()
# Exercise 2
def average_score(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    
    total_score = 0
    count = 0
    
    for line in lines:
        cleaned_line = line.strip()
        if cleaned_line != "":
            parts = cleaned_line.split(",")
            score = int(parts[1])
            total_score += score
            count += 1
            
    if count == 0:
        return 0
        
    return round(total_score / count, 1)
# Exercise 3
def filter_passed(source, destination, pass_mark):
    src_file = open(source, "r")
    lines = src_file.readlines()
    src_file.close()
    
    passed_count = 0
    dest_file = open(destination, "w")
    
    for line in lines:
        cleaned_line = line.strip()
        if cleaned_line != "":
            parts = cleaned_line.split(",")
            score = int(parts[1])
            if score >= pass_mark:
                dest_file.write(cleaned_line + "\n")
                passed_count += 1
                
    dest_file.close()
    return passed_count
# Exercise 4
def replace_word(filename, old_word, new_word):
    file = open(filename, "r")
    content = file.read()
    file.close()
    
    count = content.count(old_word)
    new_content = content.replace(old_word, new_word)
    
    file = open(filename, "w")
    file.write(new_content)
    file.close()
    
    return count

# Exercise 5
def remove_line(filename, line_number):
    file = open(filename, "r")
        lines = file.readlines()
        file.close()
        if line_number < 1 or line_number > len(lines):
            return False        
        file = open(filename, "w")
        for index, line in enumerate(lines, start=1):
            if index != line_number:
                file.write(line)
        file.close()
    
        return True
