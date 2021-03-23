import csv

# Overwrite file with lines
def write(widget, lines):
    with open('widget_data/' + widget + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            writer.writerow(line)

# Append lines to file
def append(widget, lines):
    try:
        with open('widget_data/' + widget + '.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            for line in lines:
                writer.writerow(line)
    except:
        write(widget, lines)

# Read entire file as list of row lists
def read(widget):
    lines = []
    try:
        with open('widget_data/' + widget + '.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                lines.append(row)
    except:
        pass
    return lines

# Update row at index to line
def update(widget, new_line, id):
    lines = []
    with open('widget_data/' + widget + '.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lines.append(row)

    idx = -1
    for i, line in enumerate(lines):
        if len(line) > 0 and line[0] == id:
            idx = i
            break

    if idx == -1:
        # id not found
        return

    lines[idx] = new_line

    with open('widget_data/' + widget + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            writer.writerow(line)

# Delete row at index
def delete(widget, id):
    lines = []
    with open('widget_data/' + widget + '.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lines.append(row)

    idx = -1
    for i, line in enumerate(lines):
        if len(line) > 0 and line[0] == id:
            idx = i
            break

    if idx == -1:
        # id not found
        return

    del lines[idx]

    with open('widget_data/' + widget + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            writer.writerow(line)

# For testing
# import uuid
# if __name__ == '__main__':
#     ids = [str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())]
#     write("test", [[str(uuid.uuid4()), -1]])
#     write("test", [[ids[0], 0]])
#     append("test", [[ids[1], 1]])
#     append("test", [[ids[2], 2]])
#
#     lines = read("test")
#     print(lines)
#
#     line = lines[0]
#     line[1] = 3
#     print(line)
#     update("test", line, line[0])
#
#     lines = read("test")
#     print(lines)
