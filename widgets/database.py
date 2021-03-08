import csv

def write(widget, lines):
    with open('widget_data/' + widget + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            writer.writerow(line)

def append(widget, lines):
    with open('widget_data/' + widget + '.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            writer.writerow(line)

def read(widget):
    lines = []
    with open('widget_data/' + widget + '.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lines.append(row)
    return lines