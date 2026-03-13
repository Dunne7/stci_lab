import csv, json

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert a temperature from Fahrenheit to Celsius.

    Formula:
        Celsius = (Fahrenheit - 32) × 5/9

    Args:
        fahrenheit (float): Temperature in degrees Fahrenheit.

    Returns:
        float: Temperature converted to Celsius.
    """
    return (fahrenheit - 32) * 5/9


def reverse_string(s: str) -> str:
    return s[::-1]



def add(a: int, b: int) -> int:
    return a + b



# need read FileExistsError

def classify_student_record(line: str) -> str:
    parts = line.strip().split(",")

    if len(parts) != 2:
        raise ValueError("Invalid record format")

    name, score_str = parts
    if not score_str.isdigit():
        raise ValueError("Score must be a number")

    score = int(score_str)

    if score < 0 or score > 100:
        raise ValueError("Score out of range")

    if score >= 70:
        return f"{name}: First Class"
    if score >= 60:
        return f"{name}: 2.1"
    if score >= 50:
        return f"{name}: 2.2"
    if score >= 40:
        return f"{name}: Pass"
    return f"{name}: Fail"




def calculate_team_points(results, team):
    # calculate the number of points a team has from a results array containing
    # team_name, win, draw, lost
    # 3 points for win
    # 1 point for draw
    # 0 point for lost

    noTeams = len(results)
    points = -1
    for result in results:
        if result[0] == team:
            points = int(result[1]) * 3 + int(result[2]) * 1 
   
    return points
    

def load_results(file_path):
    array = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            array.append(row)
    return array
  