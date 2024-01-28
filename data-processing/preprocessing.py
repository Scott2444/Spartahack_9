import csv

def string_to_int(string):
    return int(string.replace(',', ''))

def process_data():
    EXCLUDE_FIELDS = ["Median age (years)", "18 years and over"]

    file = open('Michigan_District_all.csv')
    csvreader = csv.reader(file)

    i = 1
    total_pop = []
    num_districts = 0
    fields = []

    data = []
    for row in csvreader:

        if i == 244: # End of file
            break

        if i == 1:  # Number of districts
            num_districts = (len(row) - 3) // 2
            data = [{} for q in range(num_districts)]
            i += 1
            continue

        if '.' in row[3]: # or row[2] in EXCLUDE_FIELDS:  # Skip all float values and excluded fields
            i += 1
            continue

        if row[2] == "Total population":
            if i == 2:  # Total Population
                for j in range(3, len(row), 2):
                    total_pop.append(string_to_int(row[j]))
            i += 1
            continue
        else:
            fields.append(row[2])
            for district in data:
                district[row[2]] = None

        # Calculate proportion of population
        print(len(fields))
        print(len(data[0]))
        for j in range(3, len(row), 2):
            data[(j - 3) // 2][row[2]] = string_to_int(row[j])/total_pop[(j - 3) // 2]

        i += 1  # Increment counter

    # Remove unused fields from data
    for row in data:
        print(row)


    # Save data into CSV file
    print(fields)
    # print(data)
    with open('DistrictData.csv', 'w', newline='') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)

        # writing headers (field names)
        writer.writeheader()


        writer.writerows(data)

if __name__ == '__demographics-processing__':
    process_data()