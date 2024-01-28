import csv

def process_data_big():
    INCLUDE_FIELDS = ["Male", "Female", "Median age (years)", "White", "Black or African American",
                      "American Indian and Alaska Native", "Asian", "Native Hawaiian and Other Pacific Islander",
                      "Two or more races", "Born in United States", "Foreign born", "Employed", "Unemployed",
                      "Public transportation (excluding taxicab)",
                      "Agriculture, forestry, fishing and hunting, and mining",
                      "Construction", "Manufacturing", "Wholesale trade", "Retail trade",
                      "Transportation and warehousing, and utilities",
                      "Information", "Finance and insurance, and real estate and rental and leasing",
                      "Professional, scientific, and management, and administrative and waste management",
                      "Educational services, and health care and social assistance",
                      "Arts, entertainment, and recreation, and accommodation and food services",
                      "Other services, except public administration", "Public administration", "Median (dollars)",
                      "With private health insurance", "With public coverage", "Less than 9th grade",
                      "9th to 12th grade, no diploma",
                      "High school graduate (includes equivalency)", "Some college, no degree", "Associate's degree",
                      "Bachelor's degree",
                      "Graduate or professional degree"]

    data = []
    fields = {"District": 1, "Result": -1}
    total_pop = []

    files = ["SexandGender-Data"]

    for file_name in files:
        file = open(file_name + '.csv')
        csvreader = csv.reader(file)

        i = 1
        total_pop = []

        for row in csvreader:

            if i == 1: # Skip header line
                i += 1
                continue
            if i == 2: # Field entries
                for j in range(2, len(row)):
                    if "Estimate" in row[j] and "Total population" in row[j]:  # Determines if the fields are an estimate and based on total pop
                        field = row[j][row[j].rfind('!') + 1 :] # Gets the field from the full field cell
                        if field in INCLUDE_FIELDS: # Filters out non-included fields
                            fields[field] = j
            else:
                district_name = row[1][row[1].rfind(',') + 2:]
                if "not defined" in row[1]:
                    i += 1
                    continue
                if "(at Large)" in row[1]:
                    district_name += "1"
                else:
                    district_name += row[1][row[1].rfind('District') + 9]
                district_name = district_name.replace(' ', '_')
                data.append({"District": district_name, "Result": 0.0})



                for field, index in fields.items():
                    if field == "District" or field == "Result":
                        continue
                    data[-1][field] = row[index]

            i += 1
    print(fields)
    print(data)

    with open('DistrictDataLarge.csv', 'w', newline='') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)

        # writing headers (field names)
        writer.writeheader()


        writer.writerows(data)