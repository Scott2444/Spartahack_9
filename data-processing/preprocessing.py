import csv

def string_to_int(string):
    return int(string.replace(',', ''))

def process_data():
    STATES = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado",
              "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam",
              "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana",
              "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi",
              "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico",
              "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island",
              "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont",
              "Washington", "Wisconsin", "West Virginia", "Wyoming"]

    EXCLUDE_FIELDS = ["Median age (years)", "18 years and over", "65 years and over",
                      "One race", "Different state", "State of residence", "Different state",
                      "Born in Puerto Rico, U.S. Island areas, or born abroad to American parent(s)",
                      "Civilian population 18 years and over", "Total civilian noninstitutionalized population",
                      "Under 18 years", "65 years and over", "Population 1 year and over", "Different house (in the U.S. or abroad)",
                      "Same county", "Different county", "Abroad", "Population 16 years and over", "In labor force",
                      "Civilian labor force", "Not in labor force", "Civilian labor force",
                      "Workers 16 years and over", "Civilian employed population 16 years and over",
                      "Median (dollars)", "Owner-occupied units", "Occupied units paying rent",
                      "Total households", "Median household income (dollars)", "Mean household income (dollars)",
                      "Civilian noninstitutionalized population under 19 years", "Population 25 years and over",
                      ""]

    data = []
    fields = ["District", "Result"]
    num_districts = 0
    num_districts_covered = 0

    for STATE in STATES:
        num_districts_covered += num_districts

        file = open(STATE + '_District_all.csv')
        csvreader = csv.reader(file)

        i = 1
        total_pop = []

        for row in csvreader:

            if i == 244: # End of file
                break

            if i == 1:  # Number of districts
                num_districts = (len(row) - 3) // 2
                data.extend([{"District": STATE + str(q+1), "Result": 0.0} for q in range(num_districts)])
                i += 1
                continue

            if '.' in row[3] or row[2] in EXCLUDE_FIELDS:  # Skip all float values and excluded fields
                i += 1
                continue

            if row[2] == "Total population":
                if i == 2:  # Total Population
                    for j in range(3, len(row), 2):
                        total_pop.append(string_to_int(row[j]))
                i += 1
                continue
            else:
                if row[2] in fields:
                    fields.append(row[2])
                    for district in data:
                        district[row[2]] = None

            # Calculate proportion of population
            for j in range(3, len(row), 2):
                data[num_districts_covered + (j - 3) // 2][row[2]] = string_to_int(row[j])/total_pop[(j - 3) // 2]

            i += 1  # Increment counter

    # Save data into CSV file
    print(fields)
    with open('DistrictData.csv', 'w', newline='') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)

        # writing headers (field names)
        writer.writeheader()


        writer.writerows(data)

if __name__ == '__demographics-processing__':
    process_data()