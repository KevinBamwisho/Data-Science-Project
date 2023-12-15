# Kevin Bamwisho
# CSCI 128 - Section A
# Final Project
# References: basketball-reference.com
# Time: 5 weeks

import csv
import matplotlib.pyplot as plt

def parse_data(filename):
    clean_nba_data =[]
    with open(filename, newline='') as csvfile:
        next(csvfile)
        nba_data = csv.reader(csvfile, delimiter =',')
        for row in nba_data:
            if row[1] == 'ABA' or row[1] == 'BAA': 
                continue
            row.remove(row[-1])
            row.remove('')
            row.remove(row[1])
            clean_nba_data.append(row)
    return clean_nba_data

def question_1(data):
    total_years = 0
    won_last_year = 0
    for i in range(len(data)-1):
        if data[i + 1][1] == data[i][1]:
            won_last_year += 1
        total_years += 1
    likelihood = (won_last_year / total_years) * 100
    return f"The likelihood of winning the next year if a team won the championship the previous year is: {likelihood:.2f}%"

def points_trend(data):
    x_values, y_value = [], []
    for row in data: x_values.append(int(row[0])), y_value.append(row[4])
    x_values.sort()
    y_value = y_value[::-1]
    
    y_values = []
    for item in y_value:
        numbers_str = ''.join(filter(str.isdigit, item))
        
        if numbers_str:
            y_values.append(int(numbers_str))
    
    return [x_values, y_values]

def calculate_likelihood(data):
    count_mvp_lead = 0
    total_series = 0
    for series in data:
        # Exclude years with missing Finals MVP data
        if series[3] != '':
            total_series += 1
            points_leader_name = series[4].split(' (')
            if series[3] == points_leader_name[0]:
                count_mvp_lead += 1

    likelihood = (count_mvp_lead / total_series) * 100
    return likelihood

def question_2(data):
    total_years = 0
    made_finals_again = 0
    for i in range(len(data)-1):
        if data[i + 1][1] == data[i][1] or data[i + 1][1] == data[i][2]:
            made_finals_again += .5
        if data[i + 1][2] == data[i][2] or data[i + 1][2] == data[i][1]:
            made_finals_again += .5
        total_years += 1
    likelihood = (made_finals_again/total_years) * 100
    return likelihood
    
if __name__ == '__main__':
    # Data structure:Year,Champion,Runner-Up,Finals MVP,Points,Rebounds,Assists
    data = (parse_data('nba_data.csv'))
    
    print(f'OUTPUT {question_1(data)}')
    x = points_trend(data)

    # Points scored over the years graph
    plt.plot(x[0], x[1])
    plt.title(f'Points Scored Over the Years')
    plt.xlabel('Years')
    plt.ylabel('Points')
    plt.savefig('points_trend.png')

    # Answered Questions
    likelihood = (calculate_likelihood(data))
    print(f"OUTPUT The likelihood of the Finals MVP leading the whole series in points is: {likelihood:.2f}%")
    likelihood_2 = question_2(data)
    print(f"OUTPUT The likelihood of a team making the Finals after making it the previous year is: {likelihood_2:.2f}%")

    points_data = [int(entry.split('(')[1].split(')')[0]) if len(entry.split('(')) > 1 else 0 for entry in [row[4] for row in data]]
    average_points = sum(points_data) / len(data)
    print(f"OUTPUT The average total points scored in the NBA finals by the leading scorer series: {average_points:.2f} pts")

    rebounds_data = [int(entry.split('(')[1].split(')')[0]) if len(entry.split('(')) > 1 else 0 for entry in [row[5] for row in data]]
    average_rebounds = sum(rebounds_data) / len(data)
    print(f"OUTPUT The average total rebounds by the leading rebounder in the NBA finals series: {average_rebounds:.2f} rebs")

    assists_data = [int(entry.split('(')[1].split(')')[0]) if len(entry.split('(')) > 1 else 0 for entry in [row[6] for row in data]]
    average_assists = sum(assists_data) / len(data)
    print(f"OUTPUT The average total assists by the leading assister in the NBA finals series: {average_assists:.2f} asts")