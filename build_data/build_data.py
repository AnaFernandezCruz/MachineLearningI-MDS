import pandas as pd

train = pd.read_csv("./data/train.csv", delimiter=",")
test = pd.read_csv("./data/test.csv", delimiter=",")
sample = pd.read_csv("./data/sample_submission.csv", delimiter=",")

test = pd.merge(test, sample,  on='Id')

df = pd.concat([train, test])

MSSubClass_names = {
    20: 'NEWERSTYLES', #1 - STORY 1946 & NEWER ALL STYLES
    30: 'OLDER', #1 - STORY 1945 & OLDER
    40: 'ATTICAGES', #1 - STORY W / FINISHED ATTIC ALL AGES
    45: 'UNFINISHEDAGES', #1 - 1 / 2 STORY - UNFINISHED ALL AGES
    50: 'FINISHEDAGES', #1 - 1 / 2 STORY FINISHED ALL AGES
    60: 'NEWER', #2 - STORY 1946 & NEWER
    70: 'OLDER', #2 - STORY 1945 & OLDER
    75: 'STORYAGES', #2 - 1 / 2 STORY ALL AGES
    80: 'MULTILEVEL', #SPLIT OR MULTI - LEVEL
    85: 'FOYER', #SPLIT FOYER
    90: 'DUPLEX', #DUPLEX - ALL STYLES AND AGES
    120: 'PUD', #1 - STORY PUD(Planned Unit Development) - 1946 & NEWER
    150: 'PUDAGES', #1 - 1 / 2 STORY PUD - ALL AGES
    160: 'PUDNEWER', #2 - STORY PUD - 1946 & NEWER
    180: 'MULTIINCL', #PUD - MULTILEVEL - INCL SPLIT LEV / FOYER
    190: 'CONVERSION' #2 FAMILY CONVERSION - ALL STYLES AND AGES
}

print('MSSubClass: ', df['MSSubClass'].unique())
df['MSSubClass'] = df['MSSubClass'].replace(MSSubClass_names)

MSZoning_names = {
    'A': 'A', #Agriculture
    'C': 'C', #Commercial
    'FV': 'VR', #VillageResidential
    'I': 'I', #Industrial
    'RH': 'HD', #HighDensity
    'RL': 'LD', #LowDensity
    'RP': 'LDP', #LowDensityPark
    'RM': 'MD', #MediumDensity
    'C (all)': 'C' #C (all)
}

print('MSZoning: ', df['MSZoning'].unique())
df['MSZoning'] = df['MSZoning'].replace(MSZoning_names)

Street_names = {
    'Grvl': 'G', #Gravel
    'Pave': 'P' #Paved
}

print('Street: ', df['Street'].unique())
df['Street'] = df['Street'].replace(Street_names)

Alley_names = {
    'Grvl': 'G', #Gravel
    'Pave': 'P', #Paved
    'NA': 'NAA' #No allet access
}

print('Alley: ', df['Street'].unique())
df['Alley'] = df['Alley'].replace(Alley_names)
#NIVELES
LotShape_names = {
    'Reg': 0, #Regular
    'IR1': 1, #Slightly irregular
    'IR2': 2, #Moderately Irregular
    'IR3': 3  #Irregular
}

print('LotShape: ', df['LotShape'].unique())
df['LotShape'] = df['LotShape'].replace(LotShape_names)

LandContour_names = {
    'Lvl': 'LVL', #Near Flat/Level
    'Bnk': 'BNK', #Banked - Quick and significant rise from street grade to building
    'HLS': 'HLS', #Hillside - Significant slope from side to side
    'Low': 'LOW' #Depression
}

print('LandContour: ', df['LandContour'].unique())
df['LandContour'] = df['LandContour'].replace(LandContour_names)

Utilities_names = {
    'AllPub': 'ALLPUB', #All public Utilities (E,G,W,& S)
    'NoSewr': 'NOSEWR', #Electricity, Gas, and Water (Septic Tank)
    'NoSeWa': 'NOSEWA', #Electricity and Gas Only
    'ELO': 'ELO' #Electricity only
}

print('Utilities: ', df['Utilities'].unique())
df['Utilities'] = df['Utilities'].replace(Utilities_names)

LotConfig_names = {
    'Inside': 'INSIDE', #Inside lot
    'Corner': 'CORNER', #Corner lot
    'CulDSac': 'CULDSAC', #Cul - de - sac
    'FR2': 'FR', #Frontage on 2 sides of property
    'FR3': 'FRR' #Frontage on 3 sides of property
}

print('LotConfig: ', df['LotConfig'].unique())
df['LotConfig'] = df['LotConfig'].replace(LotConfig_names)
#NIVELES
LandSlope_names = {
    'Gtl': 0, #Gentle slope
    'Mod': 1, #Moderate Slope
    'Sev': 2 #Severe Slope
}

print('LandSlope: ', df['LandSlope'].unique())
df['LandSlope'] = df['LandSlope'].replace(LandSlope_names)

Condition1_names = {
    'Artery': 'ARTERY', #Adjacent to arterial street
    'Feedr': 'FEEDR', #Adjacent to feeder street
    'Norm': 'NORNAM', #Normal
    'RRNn': 'RRNN', #Within 200 of North-South Railroad
    'RRAn': 'RRAN', #Adjacent to North-South Railroad
    'PosN': 'POSN', #Near positive off-site feature--park greenbelt etc.
    'PosA': 'POSA', #Adjacent to postive off-site feature
    'RRNe': 'RRNE', #Within 200 of East-West Railroad
    'RRAe': 'RRAE' #Adjacent to East-West Railroad
}

print('Condition1: ', df['Condition1'].unique())
df['Condition1'] = df['Condition1'].replace(Condition1_names)

Condition2_names = {
    'Artery': 'ARTERY', #Adjacent to arterial street
    'Feedr': 'FEEDR', #Adjacent to feeder street
    'Norm':	'NORMAL', #Normal
    'RRNn': 'RRNN', #Within 200 of North-South Railroad
    'RRAn': 'RRAN', #Adjacent to North-South Railroad
    'PosN': 'POSN', #Near positive off-site feature--park greenbelt etc.
    'PosA': 'POSA', #Adjacent to postive off-site feature
    'RRNe': 'RRNE', #Within 200 of East-West Railroad
    'RRAe': 'RRAE' #Adjacent to East-West Railroad
}

print('Condition2: ', df['Condition2'].unique())
df['Condition2'] = df['Condition2'].replace(Condition2_names)

BldgType_names = {
    '1Fam':	'SD', #Single-family Detached
    '2fmCon': 'TC', #Two-family Conversion; originally built as one-family dwelling
    'Duplex': 'D', #Duplex
    'TwnhsE': 'TEU', #Townhouse End Unit
    'Twnhs': 'TIU' #Townhouse Inside Unit
}

print('BldgType: ', df['BldgType'].unique())
df['BldgType'] = df['BldgType'].replace(BldgType_names)

HouseStyle_names = {
    '1Story': 'OS', #One story
    '1.5Fin': 'OHF', #One and one-half story: 2nd level finished
    '1.5Unf': 'OHU', #One and one-half story: 2nd level unfinished
    '2Story': 'TS', #Two story
    '2.5Fin': 'THF', #Two and one-half story: 2nd level finished
    '2.5Unf': 'THU', #Two and one-half story: 2nd level unfinished
    'SFoyer': 'SF', #Split Foyer
    'SLvl': 'SL' #Split Level
}

print('HouseStyle: ', df['HouseStyle'].unique())
df['HouseStyle'] = df['HouseStyle'].replace(HouseStyle_names)

RoofStyle_names = {
    'Flat': 'F', #Flat
    'Gable': 'G', #Gable
    'Gambrel': 'GB', #Gabrel (Barn)
    'Hip': 'H', #Hip
    'Mansard': 'M', #Mansard
    'Shed': 'S' #Shed
}

print('RoofStyle: ', df['RoofStyle'].unique())
df['RoofStyle'] = df['RoofStyle'].replace(RoofStyle_names)

RoofMatl_names = {
    'ClyTile': 'CT', #Clay or Tile
    'CompShg': 'SS', #Standard (Composite) Shingle
    'Membran': 'M', #Membrane
    'Metal': 'MT', #Metal
    'Roll': 'RLL', #Roll
    'Tar&Grv': 'GT', #Gravel & Tar
    'WdShake': 'WSH', #Wood Shakes
    'WdShngl': 'WS' #Wood Shingles
}

print('RoofMatl: ', df['RoofMatl'].unique())
df['RoofMatl'] = df['RoofMatl'].replace(RoofMatl_names)

Exterior1st_names = {
    'AsbShng': 'AS', #Asbestos Shingles
    'AsphShn': 'ASH', #Asphalt Shingles
    'BrkComm': 'BC', #Brick Common
    'BrkFace': 'BF', #Brick Face
    'CBlock': 'CIB', #Cinder Block
    'CemntBd': 'CB', #Cement Board
    'HdBoard': 'HB', #Hard Board
    'ImStucc': 'IS', #Imitation Stucco
    'MetalSd': 'MS', #Metal Siding
    'Other': 'O', #Other
    'Plywood': 'PW', #Plywood
    'PreCast': 'PR', #PreCast
    'Stone': 'ST', #Stone
    'Stucco': 'STC', #Stucco
    'VinylSd': 'VS', #Vinyl Siding
    'Wd Sdng': 'WS', #Wood Siding
    'WdShing': 'WSH' #Wood Shingles
}

print('Exterior1st: ', df['Exterior1st'].unique())
df['Exterior1st'] = df['Exterior1st'].replace(Exterior1st_names)

Exterior2st_names = {
    'AsbShng': 'ASBSHNG', #Asbestos Shingles
    'AsphShn': 'ASPHSHN', #Asphalt Shingles
    'BrkComm': 'BRKCOMM', #Brick Common
    'BrkFace': 'BRKFACE', #Brick Face
    'CBlock': 'CBLOCK', #Cinder Block
    'CmentBd': 'CEMNTBD', #Cement Board
    'HdBoard': 'HDBOARD', #Hard Board
    'ImStucc': 'IMSTUCC', #Imitation Stucco
    'MetalSd': 'METALSD', #Metal Siding
    'Other': 'OTHER', #Other
    'Plywood': 'PLYWOOD', #Plywood
    'PreCast': 'PRECAST', #PreCast
    'Stone': 'STONE', #Stone
    'Stucco': 'STUCCO', #Stucco
    'VinylSd': 'VINYLSD', #Vinyl Siding
    'Wd Sdng': 'WDSDNG', #Wood Siding
    'Wd Shng': 'WDSHING' #Wood Shingles
}
print('Exterior2nd: ', df['Exterior2nd'].unique())
df['Exterior2nd'] = df['Exterior2nd'].replace(Exterior2st_names)

MasVnrType_names = {
    'BrkCmn': 'BC', #Brick Common
    'BrkFace': 'BF', #Brick Face
    'CBlock': 'CB', #Cinder Block
    'None': 'N', #None
    'Stone': 'S' #Stone
}
print('MasVnrType: ', df['MasVnrType'].unique())
df['MasVnrType'] = df['MasVnrType'].replace(MasVnrType_names)

#NIVELES
ExterCond_names = {
    'Ex': 4, #Excellent
    'Gd': 3, #Good
    'TA': 2, #Average/Typical
    'Fa': 1, #Fair
    'Po': 0 #Poor
}

print('ExterCond: ', df['ExterCond'].unique())
df['ExterCond'] = df['ExterCond'].replace(ExterCond_names)

Foundation_names = {
    'BrkTil': 'BT', #Brick & Tile
    'CBlock': 'CB', #Cinder Block
    'PConc': 'PC', #Poured Contrete
    'Slab': 'S', #Slab
    'Stone': 'ST', #Stone
    'Wood': 'W' #Wood
}

print('Foundation: ', df['Foundation'].unique())
df['Foundation'] = df['Foundation'].replace(Foundation_names)
#NIVELES
BsmtQual_names = {
    'Ex': 5, #Excellent (100+ inches)
    'Gd': 4, #Good (90-99 inches)
    'TA': 3, #Typical (80-89 inches)
    'Fa': 2, #Fair (70-79 inches)
    'Po': 1, #Poor (<70 inches)
    'NA': 0 #No Basement
}

print('BsmtQual: ', df['BsmtQual'].unique())
df['BsmtQual'] = df['BsmtQual'].replace(BsmtQual_names)

#NIVELES
BsmtCond_names = {
    'Ex': 5, #Excellent
    'Gd': 4, #Good
    'TA': 3, #Typical - slight dampness allowed
    'Fa': 2, #Fair - dampness or some cracking or settling
    'Po': 1, #Poor - Severe cracking, settling, or wetness
    'NA': 0 #No Basement
}

print('BsmtCond: ', df['BsmtCond'].unique())
df['BsmtCond'] = df['BsmtCond'].replace(BsmtCond_names)

#NIVELES
BsmtExposure_names = {
    'Gd': 4, #Good Exposure
    'Av': 3, #Average Exposure (split levels or foyers typically score average or above)
    'Mn': 2, #Mimimum Exposure
    'No': 1, #No Exposure
    'NA': 0 #No Basement
}

print('BsmtExposure: ', df['BsmtExposure'].unique())
df['BsmtExposure'] = df['BsmtExposure'].replace(BsmtExposure_names)

#NIVELES
BsmtFinType1_names = {
    'GLQ': 6, #Good Living Quarters
    'ALQ': 5, #Average Living Quarters
    'BLQ': 4, #Below Average Living Quarters
    'Rec': 3, #Average Rec Room
    'LwQ': 2, #Low Quality
    'Unf': 1, #Unfinshed
    'NA': 0 #No Basement
}

print('BsmtFinType1: ', df['BsmtFinType1'].unique())
df['BsmtFinType1'] = df['BsmtFinType1'].replace(BsmtFinType1_names)

#NIVELES
BsmtFinType2_names = {
    'GLQ': 6, #Good Living Quarters
    'ALQ': 5, #Average Living Quarters
    'BLQ': 4, #Below Average Living Quarters
    'Rec': 3, #Average Rec Room
    'LwQ': 2, #Low Quality
    'Unf': 1, #Unfinshed
    'NA': 0 #No Basement
}

print('BsmtFinType2: ', df['BsmtFinType2'].unique())
df['BsmtFinType2'] = df['BsmtFinType2'].replace(BsmtFinType2_names)

#NIVELES
Heating_names = {
    'Floor': 'FLOOR', #Floor Furnace
    'GasA':	'GASA', #Gas forced warm air furnace
    'GasW':	'GASW', #Gas hot water or steam heat
    'Grav':	'GRAV', #Gravity furnace
    'OthW':	'OTHW', #Hot water or steam heat other than gas
    'Wall':	'WALL' #Wall furnace
}

print('Heating: ', df['Heating'].unique())
df['Heating'] = df['Heating'].replace(Heating_names)

#NIVELES
HeatingQC_names = {
    'Ex': 4, #Excellent
    'Gd': 3, #Good
    'TA': 2, #Average/Typical
    'Fa': 1, #Fair
    'Po': 0 #Poor
}

print('HeatingQC: ', df['HeatingQC'].unique())
df['HeatingQC'] = df['HeatingQC'].replace(HeatingQC_names)

CentralAir_names = {
    'N': 0, #No
    'Y': 1 #Yes
}

print('CentralAir: ', df['CentralAir'].unique())
df['CentralAir'] = df['CentralAir'].replace(CentralAir_names)

ExterQual_names = {
    'Gd': 'GD',
    'TA': 'TA',
    'Ex': 'EX',
    'Fa': 'FA'
}

print('ExterQual: ', df['ExterQual'].unique())
df['ExterQual'] = df['ExterQual'].replace(ExterQual_names)

Electrical_names = {
    'SBrkr': 'SBRKR',
    'FuseF': 'FUSEF',
    'FuseA': 'FUSEA',
    'FuseP': 'FUSEP',
    'Mix': 'MIX'
}

print('Electrical: ', df['Electrical'].unique())
df['Electrical'] = df['Electrical'].replace(Electrical_names)


KitchenQual_names = {
    'Gd': 'GD',
    'TA': 'TA',
    'Ex': 'EX',
    'Fa': 'FA'
}

print('KitchenQual: ', df['KitchenQual'].unique())
df['KitchenQual'] = df['KitchenQual'].replace(KitchenQual_names)

Functional_names = {
    'Typ': 'TYP',
    'Min1': 'MIN',
    'Maj1': 'MAJ',
    'Min2': 'MINN',
    'Mod': 'MOD',
    'Maj2': 'MAJJ',
    'Sev': 'SEV'
}

print('Functional: ', df['Functional'].unique())
df['Functional'] = df['Functional'].replace(Functional_names)

FireplaceQu_names = {
    'TA': 'TA',
    'Gd': 'GD',
    'Fa': 'FA',
    'Ex': 'EX',
    'Po': 'PO'
}

print('FireplaceQu: ', df['FireplaceQu'].unique())
df['FireplaceQu'] = df['FireplaceQu'].replace(FireplaceQu_names)

GarageType_names = {
    'Attchd': 'ATTCH',
    'Detchd': 'DETCH',
    'BuiltIn': 'BUIN',
    'CarPort': 'CARP',
    'Basment': 'BS',
    '2Types': 'TYPES'
}

print('GarageType: ', df['GarageType'].unique())
df['GarageType'] = df['GarageType'].replace(GarageType_names)

GarageFinish_names = {
    'RFn': 'RFN',
    'Unf': 'UNF',
    'Fin': 'FIN'
}

print('GarageFinish: ', df['GarageFinish'].unique())
df['GarageFinish'] = df['GarageFinish'].replace(GarageFinish_names)


GarageQual_names = {
    'TA': 'TA',
    'Fa': 'FA',
    'Gd': 'GD',
    'Ex': 'EX',
    'Po': 'PO'
}

print('GarageQual: ', df['GarageQual'].unique())
df['GarageQual'] = df['GarageQual'].replace(GarageQual_names)

GarageCond_names = {
    'TA': 'TA',
    'Fa': 'FA',
    'Gd': 'GD',
    'Ex': 'EX',
    'Po': 'PO'
}

print('GarageCond: ', df['GarageCond'].unique())
df['GarageCond'] = df['GarageCond'].replace(GarageCond_names)

Fence_names = {
    'MnPrv': 'MNPRV',
    'GdWo': 'GDWO',
    'GdPrv': 'GDPRV',
    'MnWw': 'MNWW'
}

print('Fence: ', df['Fence'].unique())
df['Fence'] = df['Fence'].replace(Fence_names)

MiscFeature_names = {
    'Shed': 'SHED',
    'Gar2': 'GAR',
    'Othr': 'OTHR',
    'TenC': 'TENC'
}

print('MiscFeature: ', df['MiscFeature'].unique())
df['MiscFeature'] = df['MiscFeature'].replace(MiscFeature_names)

SaleType_names = {
    'WD': 'WD',
    'New': 'NEW',
    'COD': 'COD',
    'ConLD': 'CONLD',
    'ConLI': 'CONLI',
    'CWD': 'CWD',
    'ConLw': 'CONLW',
    'Con': 'CON',
    'Oth': 'OTH'
}

print('SaleType: ', df['SaleType'].unique())
df['SaleType'] = df['SaleType'].replace(SaleType_names)

SaleCondition_names = {
    'Normal': 'NORMAL',
    'Abnorml': 'ABNORMAL',
    'Partial': 'PARTIAL',
    'AdjLand': 'ADJLAND',
    'Alloca': 'ALLOCA',
    'Family': 'FAMILY'
}

print('SaleCondition: ', df['SaleCondition'].unique())
df['SaleCondition'] = df['SaleCondition'].replace(SaleCondition_names)

column_names = {
    'Id': 'id',
    'MSSubClass': 'clase_construcion',
    'MSZoning': 'clase_zonificacion',
    'LotFrontage': 'proximidad_calle',
    'Street': 'acceso_carretera',
    'Alley': 'acceso_callejon',
    'LotShape': 'forma_propiedad',
    'LotArea': 'area_propiedad',
    'LandContour': 'nivelado_propiedad',
    'Utilities': 'tipo_servicios',
    'LotConfig': 'tipo_solar',
    'LandSlope': 'nivelado_solar',
    'Neighborhood': 'vecindarion',
    'Condition1': 'proximidad_ferrocarril',
    'Condition2': 'proximidad_ferrocarril2',
    'BldgType': 'tipo_propiedad',
    'HouseStyle': 'estilo_propiedad',
    'OverallQual': 'calidad_material',
    'OverallCond': 'condicion_general',
    'YearBuilt': 'anio_construcion',
    'YearRemodAdd': 'anio_remodelacion',
    'RoofStyle': 'tipo_techo',
    'RoofMatl': 'material_techo',
    'Exterior1st': 'cubierta_exterior',
    'Exterior2nd': 'revestimiento_exterior',
    'MasVnrType': 'tipo_chapa',
    'MasVnrArea': 'area_revestimiento',
    'ExterQual': 'calidad_exterior',
    'ExterCond': 'condicion_exterior',
    'Foundation': 'tipo_cimiento',
    'BsmtQual': 'calidad_sotano',
    'BsmtCond': 'condicion_sotano',
    'BsmtExposure': 'exposicion_sotano',
    'BsmtFinType1': 'tipo_sotano1',
    'BsmtFinSF1': 'area_asotano1',
    'BsmtFinType2': 'tipo_sotano2',
    'BsmtFinSF2': 'area_sotano2',
    'BsmtUnfSF': 'area_nosotano',
    'TotalBsmtSF': 'area_sotano',
    'Heating': 'tipo_calefacion',
    'HeatingQC': 'calidad_calefacion',
    'CentralAir': 'tipo_aireAcond',
    'Electrical': 'tipo_electricidad',
    '1stFlrSF': 'area_piso1',
    '2ndFlrSF': 'area_piso2',
    'LowQualFinSF': 'area_bajacalidad',
    'GrLivArea': 'area_habitableUp',
    'BsmtFullBath': 'n_baniosSotano',
    'BsmtHalfBath': 'n_mitadBanioSotano',
    'FullBath': 'n_banios',
    'HalfBath': 'n_medioBanio',
    'Bedroom': 'n_dormitorios',
    'Kitchen': 'n_cocinas',
    'KitchenQual': 'calidad_cocina',
    'TotRmsAbvGrd': 'n_habitacionesNoBanios',
    'Functional': 'calificacion_domestica',
    'Fireplaces': 'n_chimeneas',
    'FireplaceQu': 'calidad_chimeneas',
    'GarageType': 'tipo_garage',
    'GarageYrBlt': 'anio_garage',
    'GarageFinish': 'acabado_garage',
    'GarageCars': 'area_garageCoches',
    'GarageArea': 'area_garage',
    'GarageQual': 'calidad_garage',
    'GarageCond': 'condicion_garage',
    'PavedDrive': 'tipo_entrada',
    'WoodDeckSF': 'area_madera',
    'OpenPorchSF': 'area_porcheAbierto',
    'EnclosedPorch': 'area_porcheCerrado',
    '3SsnPorch': 'area_tresEstaPorche',
    'ScreenPorch': 'area_pantalla_porche',
    'PoolArea': 'area_pisicina',
    'PoolQC': 'calidad_piscina',
    'Fence': 'calidad_cerca',
    'MiscFeature': 'caracteristicas_noCubiertas',
    'MiscVal': 'valor_miscelanea',
    'MoSold': 'mes_vendido',
    'YrSold': 'anio_vendido',
    'SaleType': 'tipo_venta',
    'SaleCondition': 'condicion_venta',
    'SalePrice': 'precio'
}


df.rename(columns= column_names, inplace=True)

export_csv = df.to_csv(r'../export_dataframe.csv', index= None, header=True)
#print(df)

