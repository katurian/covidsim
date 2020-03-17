from setup import *

def generateNodes(popsUrl, coordsUrl):
    r = requests.get(popsUrl, allow_redirects=True)
    open('pops.csv', 'wb').write(r.content)

    r = requests.get(coordsUrl, allow_redirects=True)
    open('coords.zip', 'wb').write(r.content)

    with ZipFile('coords.zip', 'r') as zipObj:
       listOfFileNames = zipObj.namelist()
       for fileName in listOfFileNames:
           if fileName.endswith('.dbf'):
               zipObj.extract(fileName)
               os.rename(fileName, 'coords.dbf')

    pops = pd.read_csv(r'pops.csv')
    pops.to_excel(r'pops.xlsx', index = None, header=True)

    os.system('in2csv coords.dbf > coords.csv')
    coords = pd.read_csv(r'coords.csv')

    coords.sort_values("geoid10", axis = 0, ascending = True, 
                     inplace = True, na_position ='last') 

    coords.to_excel(r'coords.xlsx', index = None, header=True)

    pops = openpyxl.load_workbook('pops.xlsx')
    popsSheet = pops.active

    coords = openpyxl.load_workbook('coords.xlsx')
    coordsSheet = coords.active

    wb.save(r'nodes.xlsx')

    nodes = openpyxl.load_workbook('nodes.xlsx')
    nodesSheet = nodes.active

    i = 0
    for cell in coordsSheet['K:K']:
        nodesSheet.cell(row=cell.row, column=1, value=i)
        i = i + 1
    for cell in coordsSheet['K:K']:
        nodesSheet.cell(row=cell.row, column=2, value=cell.value)
    for cell in coordsSheet['L:L']:
        nodesSheet.cell(row=cell.row, column=3, value=cell.value)
    for cell in popsSheet['J:J']:
        nodesSheet.cell(row=cell.row, column=4, value=cell.value)
        
    nodesSheet['A1'] = 'NodeID'
    nodesSheet['B1'] = 'NodeAttributes_Latitude'
    nodesSheet['C1'] = 'NodeAttributes_Longitude'
    nodesSheet['D1'] = 'NodeAttributes_InitialPopulation'

    nodes.save('nodes.xlsx')
    nodes = pd.read_excel(r'nodes.xlsx')
    nodes.to_csv('nodes.csv', index=False)
    os.system('hone "nodes.csv" "nodes.json"')

    os.remove('coords.zip')
    os.remove('coords.dbf')
    os.remove('coords.csv')
    os.remove('coords.xlsx')
    os.remove('pops.csv')
    os.remove('pops.xlsx')
    os.remove('nodes.xlsx')
    os.remove('nodes.csv')


# generateNodes('http://censusdata.ire.org/15/all_140_in_15.P1.csv', 'https://www2.census.gov/geo/tiger/TIGER2010/TRACT/2010/tl_2010_15_tract10.zip')
