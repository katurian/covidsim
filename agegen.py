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
    cols_to_add = [36, 3]

    cols_to_add = sorted(cols_to_add, reverse=True)
    with open(input_file, "r") as source:
        reader = csv.reader(source)
        with open(output_file, "w", newline='') as result:
            writer = csv.writer(result)
            for row in reader:
                writer.writerow([row[n] for n in cols_to_add])

    #age = pd.read_csv(r'PEP_2018_PEPAGESEX_with_ann.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode', encoding = 'ISO-8859-1')
    #age.to_excel(r'age.xlsx', index = None, header=True)
    #age = openpyxl.load_workbook(r'age.xlsx')
    #ageSheet = age.active

    #os.remove('PEP_2018_PEPAGESEX_with_ann.csv')
    #os.remove('age.zip')

    default = pd.DataFrame()
    default.to_excel(r'default.xlsx')
    default = openpyxl.load_workbook(r'default.xlsx')
    defaultSheet = default.active
               
    defaultSheet['A1'] = 'IndividualAttributes_AgeDistribution_AxisNames'
    defaultSheet['B1'] = 'IndividualAttributes_AgeDistribution_AxisUnits'
    defaultSheet['C1'] = 'IndividualAttributes_AgeDistribution_DistributionValues'
    defaultSheet['D1'] = 'IndividualAttributes_AgeDistribution_NumDistributionAxes'
    defaultSheet['E1'] = 'IndividualAttributes_AgeDistribution_ResultValues'
    defaultSheet['F1'] = 'IndividualAttributes_AgeDistribution1'
    defaultSheet['G1'] = 'IndividualAttributes_AgeDistribution2'
    defaultSheet['H1'] = 'IndividualAttributes_AgeDistributionFlag'
    defaultSheet['I1'] = 'IndividualAttributes_FertilityDistribution_AxisNames'
    defaultSheet['J1'] = 'IndividualAttributes_FertilityDistribution_AxisScaleFactors'
    defaultSheet['K1'] = 'IndividualAttributes_FertilityDistribution_AxisUnits'
    defaultSheet['L1'] = 'IndividualAttributes_FertilityDistribution_NumDistributionAxes'
    defaultSheet['M1'] = 'IndividualAttributes_FertilityDistribution_NumPopulationGroups'
    defaultSheet['N1'] = 'IndividualAttributes_FertilityDistribution_PopulationGroups'
    defaultSheet['O1'] = 'IndividualAttributes_FertilityDistribution_ResultScaleFactor'
    defaultSheet['P1'] = 'IndividualAttributes_FertilityDistribution_ResultUnits'
    defaultSheet['Q1'] = 'IndividualAttributes_FertilityDistribution_ResultValues'
    defaultSheet['R1'] = 'IndividualAttributes_ImmunityDistribution1'
    defaultSheet['S1'] = 'IndividualAttributes_ImmunityDistribution2'
    defaultSheet['T1'] = 'IndividualAttributes_ImmunityDistributionFlag'
    defaultSheet['U1'] = 'IndividualAttributes_MigrationHeterogeneityDistribution1'
    defaultSheet['V1'] = 'IndividualAttributes_MigrationHeterogeneityDistribution2'
    defaultSheet['W1'] = 'IndividualAttributes_MigrationHeterogeneityDistributionFlag'
    defaultSheet['X1'] = 'IndividualAttributes_MortalityDistribution_AxisScaleFactors'
    defaultSheet['Y1'] = 'IndividualAttributes_MortalityDistribution_AxisUnits'
    defaultSheet['Z1'] = 'IndividualAttributes_MortalityDistribution_NumDistributionAxes'
    defaultSheet['AA1'] = 'IndividualAttributes_MortalityDistribution_NumPopulationGroups'
    defaultSheet['AB1'] = 'IndividualAttributes_MortalityDistribution_PopulationGroups'
    defaultSheet['AC1'] = 'IndividualAttributes_MortalityDistribution_ResultScaleFactor'
    defaultSheet['AD1'] = 'IndividualAttributes_MortalityDistribution_ResultUnits'
    defaultSheet['AE1'] = 'IndividualAttributes_MortalityDistribution_ResultValues'
    defaultSheet['AF1'] = 'IndividualAttributes_PrevalenceDistribution1'
    defaultSheet['AG1'] = 'IndividualAttributes_PrevalenceDistribution2'
    defaultSheet['AH1'] = 'IndividualAttributes_PrevalenceDistributionFlag'
    defaultSheet['AI1'] = 'IndividualAttributes_RiskDistribution1'
    defaultSheet['AJ1'] = 'IndividualAttributes_RiskDistribution2'
    defaultSheet['AK1'] = 'IndividualAttributes_RiskDistributionFlag'
    defaultSheet['AL1'] = 'IndividualAttributes_NodeAttributes_Airport'
    defaultSheet['AM1'] = 'IndividualAttributes_NodeAttributes_Altitude'
    defaultSheet['AN1'] = 'IndividualAttributes_NodeAttributes_BirthRate'
    defaultSheet['AO1'] = 'IndividualAttributes_NodeAttributes_InitialPopulation'
    defaultSheet['AP1'] = 'IndividualAttributes_NodeAttributes_Latitude'
    defaultSheet['AQ1'] = 'IndividualAttributes_NodeAttributes_Longitude'
    defaultSheet['AR1'] = 'IndividualAttributes_NodeAttributes_Region'
    defaultSheet['AS1'] = 'IndividualAttributes_NodeAttributes_Seaport'

    #for cell in ageSheet['AK:AK']:
        #print(type(cell.value))
        #nodesSheet.cell(row=cell.row, column=2, value=cell.value)
    
    #default.save(r'default.xlsx')
    #default = pd.read_excel(r'default.xlsx')
    #default.to_csv('default.csv', index=False)
    #os.system('hone "default.csv" "default.json"')
    

generateAgeDistr('https://www2.census.gov/programs-surveys/popest/tables/2010-2018/counties/asrh/PEP_2018_PEPAGESEX.zip')
