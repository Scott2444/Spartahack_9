import csv
import glob
import os

def string_to_percentage(string):
    if "%" in string:
        string = string.replace('%', '')
    try:
        return float(string) / 100
    except:
        return float("NaN")

def string_to_float(string):
    if ',' in string:
        string = string.replace(',', '')
        string = string.replace('+', '')
        return float(string)
    try:
        return float(string)
    except:
        return float("NaN")

def process_data_large():

    INCLUDE_FIELDS = ["Male", "Female", "Median age (years)", "White", "Black or African American",
                      "American Indian and Alaska Native", "Asian", "Native Hawaiian and Other Pacific Islander",
                      "Two or more races", "Born in United States", "Foreign born", "Employed", "Unemployed",
                      "Public transportation (excluding taxicab)", "Agriculture, forestry, fishing and hunting, and mining",
                      "Construction", "Manufacturing", "Wholesale trade", "Retail trade", "Transportation and warehousing, and utilities",
                      "Information", "Finance and insurance, and real estate and rental and leasing",
                      "Professional, scientific, and management, and administrative and waste management",
                      "Educational services, and health care and social assistance", "Arts, entertainment, and recreation, and accommodation and food services",
                      "Other services, except public administration", "Public administration", "Median (dollars)",
                      "With private health insurance", "With public coverage", "Less than 9th grade", "9th to 12th grade, no diploma",
                      "High school graduate (includes equivalency)", "Some college, no degree", "Associate's degree", "Bachelor's degree",
                      "Graduate or professional degree"]
    NOT_PERCENTS = ["Median age (years)", "Median (dollars)"]

    folder_path = "Output Data/"


    data = []
    fields = ["District", "Result"]

    districts_made = False

    for filename in glob.glob(os.path.join(folder_path, "*.csv")):
        file = open(filename , encoding="utf-8-sig")
        csvreader = csv.reader(file)

        i = 1

        for row in csvreader:
            if i == 1 and not districts_made:
                for j in range(2, len(row), 4):
                    district_name = row[j][row[j].rfind(',') + 2 : row[j].rfind('!')-1]
                    if "not defined" in row[j]:
                        i += 1
                        continue
                    if "(at Large)" in row[j]:
                        district_name += "1"
                    else:
                        district_name += row[j][row[j].rfind('District') + 9]
                    district_name = district_name.replace(' ', '_')

                    if district_name == "Puerto_Rico1":
                        continue

                    data.append({"District": district_name, "Result": 0.0})
                districts_made = True

            field = row[0].strip()
            print(field)

            if field not in INCLUDE_FIELDS:
                i += 1
                continue

            if field in fields:
                i += 1
                continue


            percentage = True
            if field in NOT_PERCENTS:
                percentage = False

            if field not in fields:
                fields.append(field)
                for district in data:
                    district[field] = None

            for j in range(3, len(row)-4, 4):
                if (j-3) // 4 >= len(data):
                    break
                if percentage:
                    data[(j - 3) // 4][field] = string_to_percentage(row[j])
                else:
                    data[(j - 3) // 4][field] = string_to_float(row[j-2])



            i += 1  # Increment counter

    # Save data into CSV file
    print(fields)
    for row in data:
        print(row)

    fields.pop(0)
    fields.pop(0)
    fields.sort()
    fields.insert(0, "Result")
    fields.insert(0, "District")

    with open('DistrictDataLarge.csv', 'w', newline='') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)

        # writing headers (field names)
        writer.writeheader()

        writer.writerows(data)

    print("Finished")