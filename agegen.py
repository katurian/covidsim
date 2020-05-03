from setup import *

def generateAgeDistr(ageUrl):
    r = requests.get(ageUrl, allow_redirects=True)
    open('age.zip', 'wb').write(r.content)

    with ZipFile('age.zip', 'r') as zipObj:
       listOfFileNames = zipObj.namelist()
       for fileName in listOfFileNames:
           if fileName == 'PEP_2018_PEPAGESEX_with_ann.csv':
               zipObj.extract(fileName)

    input_file = 'PEP_2018_PEPAGESEX_with_ann.csv'
    output_file = 'age.csv'
    cols_to_add = [66, 99, 132, 165, 198, 231, 264, 297, 330, 363, 396, 429, 462, 495, 528, 561, 594, 627]

    cols_to_add = sorted(cols_to_add, reverse=True)
    with open(input_file, "r") as source:
        reader = csv.reader(source)
        with open(output_file, "w", newline='') as result:
            writer = csv.writer(result)
            for row in reader:
                writer.writerow([row[n] for n in cols_to_add])
    
    age = pd.read_csv(r'age.csv', sep=',', error_bad_lines=False, skiprows=[0, 1], index_col=False, dtype='unicode', encoding = 'ISO-8859-1')
    age.to_excel(r'age.xlsx', index=None, header=True)
    age = openpyxl.load_workbook(r'age.xlsx')
    ageSheet = age.active

    total = []
    groups = []
    proportions = []
    distributions = []
    ages = [0, 4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 100]

    est72018sex0_age85plus = 0
    for cell in ageSheet['A:A']:
        est72018sex0_age85plus += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age85plus)

    est72018sex0_age80to84 = 0
    for cell in ageSheet['B:B']:
        est72018sex0_age80to84 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age80to84)

    est72018sex0_age75to79 = 0
    for cell in ageSheet['C:C']:
        est72018sex0_age75to79 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age75to79)

    est72018sex0_age70to74 = 0
    for cell in ageSheet['D:D']:
        est72018sex0_age70to74 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age70to74)

    est72018sex0_age65to69 = 0
    for cell in ageSheet['E:E']:
        est72018sex0_age65to69 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age65to69)
        
    est72018sex0_age60to64 = 0
    for cell in ageSheet['F:F']:
        est72018sex0_age60to64 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age60to64)
    
    est72018sex0_age55to59 = 0
    for cell in ageSheet['G:G']:
        est72018sex0_age55to59 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age55to59)

    est72018sex0_age50to54 = 0
    for cell in ageSheet['H:H']:
        est72018sex0_age50to54 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age50to54)

    est72018sex0_age45to49 = 0
    for cell in ageSheet['I:I']:
        est72018sex0_age45to49 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age45to49)

    est72018sex0_age40to44 = 0
    for cell in ageSheet['J:J']:
        est72018sex0_age40to44 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age40to44)

    est72018sex0_age35to39 = 0
    for cell in ageSheet['K:K']:
        est72018sex0_age35to39 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age35to39)

    est72018sex0_age30to34 = 0
    for cell in ageSheet['L:L']:
        est72018sex0_age30to34 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age30to34)

    est72018sex0_age25to29 = 0
    for cell in ageSheet['M:M']:
        est72018sex0_age25to29 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age25to29)

    est72018sex0_age20to24 = 0
    for cell in ageSheet['N:N']:
        est72018sex0_age20to24 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age20to24)

    est72018sex0_age15to19 = 0
    for cell in ageSheet['O:O']:
        est72018sex0_age15to19 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age15to19)

    est72018sex0_age10to14 = 0
    for cell in ageSheet['P:P']:
        est72018sex0_age10to14 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age10to14)

    est72018sex0_age5to9 = 0
    for cell in ageSheet['Q:Q']:
        est72018sex0_age5to9 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age5to9)

    est72018sex0_age0to4 = 0
    for cell in ageSheet['R:R']:
        est72018sex0_age0to4 += int(cell.value)
        total.append(int(cell.value))
    groups.append(est72018sex0_age0to4)

    total = sum(total)
    for pop in groups:
        proportions.append(pop/total)

    for i in range(0, len(proportions)):
       summary = sum(proportions[:i])
       distributions.append(summary)

    distributions.append(1)

    ageDistribution = {
        'AxisNames': ['age','year'],
        'AxisUnits': ['years'],
        'DistributionValues': distributions,
        'NumDistributionAxes': 1,
        'ResultValues': ages
    }

    print(Saving JSON file...)
    
    with open('age.json', 'w') as outfile:
        json.dump(ageDistribution, outfile)

    print('JSON written to age.json')

    os.remove('PEP_2018_PEPAGESEX_with_ann.csv')
    os.remove('age.zip')
    os.remove('age.csv')
    os.remove('age.xlsx')
    

generateAgeDistr('https://www2.census.gov/programs-surveys/popest/tables/2010-2018/counties/asrh/PEP_2018_PEPAGESEX.zip')
