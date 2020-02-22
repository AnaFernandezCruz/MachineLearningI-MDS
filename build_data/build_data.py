import pandas as pd


train = pd.read_csv("./data/train.csv", delimiter=",")
test = pd.read_csv("./data/test.csv", delimiter=",")
sample = pd.read_csv("./data/sample_submission.csv", delimiter=",")

test = pd.merge(test, sample,  on='Id')

df = pd.concat([train, test])

MSSubClass_names = {
    20: '1 - STORY 1946 & NEWER ALL STYLES',
    30: '1 - STORY 1945 & OLDER',
    40: '1 - STORY W / FINISHED ATTIC ALL AGES',
    45: '1 - 1 / 2 STORY - UNFINISHED ALL AGES',
    50: '1 - 1 / 2 STORY FINISHED ALL AGES',
    60: '2 - STORY 1946 & NEWER',
    70: '2 - STORY 1945 & OLDER',
    75: '2 - 1 / 2 STORY ALL AGES',
    80: 'SPLIT OR MULTI - LEVEL',
    85: 'SPLIT FOYER',
    90: 'DUPLEX - ALL STYLES AND AGES',
    120: '1 - STORY PUD(Planned Unit Development) - 1946 & NEWER',
    150: '1 - 1 / 2 STORY PUD - ALL AGES',
    160: '2 - STORY PUD - 1946 & NEWER',
    180: 'PUD - MULTILEVEL - INCL SPLIT LEV / FOYER',
    190: '2 FAMILY CONVERSION - ALL STYLES AND AGES'
}

df['MSSubClass'] = df['MSSubClass'].replace(MSSubClass_names)

MSZoning_names = {
    'A': 'Agriculture',
    'C': 'Commercial',
    'FV': 'VillageResidential',
    'I': 'Industrial',
    'RH': 'HighDensity',
    'RL': 'LowDensity',
    'RP': 'LowDensityPark',
    'RM': 'MediumDensity'
}

df['MSZoning'] = df['MSZoning'].replace(MSZoning_names)

Street_names = {
    'Grvl': 'Gravel',
    'Pave': 'Paved'
}

df['Street'] = df['Street'].replace(Street_names)

Alley_names = {
    'Grvl': 'Gravel',
    'Pave': 'Paved',
    'NA': 'No allet access'
}

df['Alley'] = df['Alley'].replace(Alley_names)

LotShape_names = {
    'Reg': 'Regular',
    'IR1': 'Slightly irregular',
    'IR2': 'Moderately Irregular',
    'IR3': 'Irregular'
}

df['LotShape'] = df['LotShape'].replace(LotShape_names)

LandContour_names = {
    'Lvl': 'Near Flat/Level',
    'Bnk': 'Banked - Quick and significant rise from street grade to building',
    'HLS': 'Hillside - Significant slope from side to side',
    'Low': 'Depression'
}

df['LandContour'] = df['LandContour'].replace(LandContour_names)

Utilities_names = {
    'AllPub': 'All public Utilities (E,G,W,& S)',
    'NoSewr': 'Electricity, Gas, and Water (Septic Tank)',
    'NoSeWa': 'Electricity and Gas Only',
    'ELO': 'Electricity only'
}

df['Utilities'] = df['Utilities'].replace(Utilities_names)

LotConfig_names = {
    'Inside': 'Inside lot',
    'Corner': 'Corner lot',
    'CulDSac': 'Cul - de - sac',
    'FR2': 'Frontage on 2 sides of property',
    'FR3': 'Frontage on 3 sides of property'
}

df['LotConfig'] = df['LotConfig'].replace(LotConfig_names)

LandSlope_names = {
    'Gtl': 'Gentle slope',
    'Mod': 'Moderate Slope',
    'Sev': 'Severe Slope'
}

df['LandSlope'] = df['LandSlope'].replace(LandSlope_names)

Condition1_names = {
    'Artery': 'Adjacent to arterial street',
    'Feedr': 'Adjacent to feeder street',
    'Norm': 'Normal',
    'RRNn': 'Within 200 of North-South Railroad',
    'RRAn': 'Adjacent to North-South Railroad',
    'PosN': 'Near positive off-site feature--park greenbelt etc.',
    'PosA': 'Adjacent to postive off-site feature',
    'RRNe': 'Within 200 of East-West Railroad',
    'RRAe': 'Adjacent to East-West Railroad'
}

df['Condition1'] = df['Condition1'].replace(Condition1_names)

Condition2_names = {
    'Artery': 'Adjacent to arterial street',
    'Feedr': 'Adjacent to feeder street',
    'Norm':	'Normal',
    'RRNn': 'Within 200 of North-South Railroad',
    'RRAn': 'Adjacent to North-South Railroad',
    'PosN': 'Near positive off-site feature--park greenbelt etc.',
    'PosA': 'Adjacent to postive off-site feature',
    'RRNe': 'Within 200 of East-West Railroad',
    'RRAe': 'Adjacent to East-West Railroad'
}

df['Condition2'] = df['Condition2'].replace(Condition2_names)

BldgType_names = {
    '1Fam':	'Single-family Detached',
    '2FmCon': 'Two-family Conversion; originally built as one-family dwelling',
    'Duplx': 'Duplex',
    'TwnhsE': 'Townhouse End Unit',
    'TwnhsI': 'Townhouse Inside Unit'
}

df['BldgType'] = df['BldgType'].replace(BldgType_names)

HouseStyle_names = {
    '1Story': 'One story',
    '1.5Fin': 'One and one-half story: 2nd level finished',
    '1.5Unf': 'One and one-half story: 2nd level unfinished',
    '2Story': 'Two story',
    '2.5Fin': 'Two and one-half story: 2nd level finished',
    '2.5Unf': 'Two and one-half story: 2nd level unfinished',
    'SFoyer': 'Split Foyer',
    'SLvl': 'Split Level'
}

df['HouseStyle'] = df['HouseStyle'].replace(HouseStyle_names)

RoofStyle_names = {
    'Flat': 'Flat',
    'Gable': 'Gable',
    'Gambrel': 'Gabrel (Barn)',
    'Hip': 'Hip',
    'Mansard': 'Mansard',
    'Shed': 'Shed'
}

df['RoofStyle'] = df['RoofStyle'].replace(RoofStyle_names)

RoofMatl_names = {
    'ClyTile': 'Clay or Tile',
    'CompShg': 'Standard (Composite) Shingle',
    'Membran': 'Membrane',
    'Metal': 'Metal',
    'Roll': 'Roll',
    'Tar&Grv': 'Gravel & Tar',
    'WdShake': 'Wood Shakes',
    'WdShngl': 'Wood Shingles'
}

df['RoofMatl'] = df['RoofMatl'].replace(RoofMatl_names)

Exterior1st_names = {
    'AsbShng': 'Asbestos Shingles',
    'AsphShn': 'Asphalt Shingles',
    'BrkComm': 'Brick Common',
    'BrkFace': 'Brick Face',
    'CBlock': 'Cinder Block',
    'CemntBd': 'Cement Board',
    'HdBoard': 'Hard Board',
    'ImStucc': 'Imitation Stucco',
    'MetalSd': 'Metal Siding',
    'Other': 'Other',
    'Plywood': 'Plywood',
    'PreCast': 'PreCast',
    'Stone': 'Stone',
    'Stucco': 'Stucco',
    'VinylSd': 'Vinyl Siding',
    'Wd Sdng': 'Wood Siding',
    'WdShing': 'Wood Shingles'
}

df['Exterior1st'] = df['Exterior1st'].replace(Exterior1st_names)

Exterior2st_names = {
    'AsbShng': 'Asbestos Shingles',
    'AsphShn': 'Asphalt Shingles',
    'BrkComm': 'Brick Common',
    'BrkFace': 'Brick Face',
    'CBlock': 'Cinder Block',
    'CemntBd': 'Cement Board',
    'HdBoard': 'Hard Board',
    'ImStucc': 'Imitation Stucco',
    'MetalSd': 'Metal Siding',
    'Other': 'Other',
    'Plywood': 'Plywood',
    'PreCast': 'PreCast',
    'Stone': 'Stone',
    'Stucco': 'Stucco',
    'VinylSd': 'Vinyl Siding',
    'Wd Sdng': 'Wood Siding',
    'WdShing': 'Wood Shingles'
}

df['Exterior2st'] = df['Exterior2st'].replace(Exterior2st_names)

MasVnrType_names = {
    'BrkCmn': 'Brick Common',
    'BrkFace': 'Brick Face',
    'CBlock': 'Cinder Block',
    'None': 'None',
    'Stone': 'Stone'
}

df['MasVnrType'] = df['MasVnrType'].replace(MasVnrType_names)

ExterCond_names = {
    'Ex': 'Excellent',
    'Gd': 'Good',
    'TA': 'Average/Typical',
    'Fa': 'Fair',
    'Po': 'Poor'
}

df['ExterCond'] = df['ExterCond'].replace(ExterCond_names)

Foundation_names = {
    'BrkTil': 'Brick & Tile',
    'CBlock': 'Cinder Block',
    'PConc': 'Poured Contrete',
    'Slab': 'Slab',
    'Stone': 'Stone',
    'Wood': 'Wood'
}

df['Foundation'] = df['Foundation'].replace(Foundation_names)

BsmtQual_names = {
    'Ex': 'Excellent (100+ inches)',
    'Gd': 'Good (90-99 inches)',
    'TA': 'Typical (80-89 inches)',
    'Fa': 'Fair (70-79 inches)',
    'Po': 'Poor (<70 inches',
    'NA': 'No Basement'
}

df['BsmtQual'] = df['BsmtQual'].replace(BsmtQual_names)

BsmtCond_names = {
    'Ex': 'Excellent',
    'Gd': 'Good',
    'TA': 'Typical - slight dampness allowed',
    'Fa': 'Fair - dampness or some cracking or settling',
    'Po': 'Poor - Severe cracking, settling, or wetness',
    'NA': 'No Basement'
}

df['BsmtCond'] = df['BsmtCond'].replace(BsmtCond_names)

BsmtExposure_names = {
    'Gd': 'Good Exposure',
    'Av': 'Average Exposure (split levels or foyers typically score average or above)',
    'Mn': 'Mimimum Exposure',
    'No': 'No Exposure',
    'NA': 'No Basement'
}

df['BsmtExposure'] = df['BsmtExposure'].replace(BsmtExposure_names)

BsmtFinType1_names = {
    'GLQ': 'Good Living Quarters',
    'ALQ': 'Average Living Quarters',
    'BLQ': 'Below Average Living Quarters',
    'Rec': 'Average Rec Room',
    'LwQ': 'Low Quality',
    'Unf': 'Unfinshed',
    'NA': 'No Basement'
}

df['BsmtFinType1'] = df['BsmtFinType1'].replace(BsmtFinType1_names)

BsmtFinType2_names = {
    'GLQ': 'Good Living Quarters',
    'ALQ': 'Average Living Quarters',
    'BLQ': 'Below Average Living Quarters',
    'Rec': 'Average Rec Room',
    'LwQ': 'Low Quality',
    'Unf': 'Unfinshed',
    'NA': 'No Basement'
}

df['BsmtFinType2'] = df['BsmtFinType2'].replace(BsmtFinType2_names)

Heating_names = {
    'Floor': 'Floor Furnace',
    'GasA':	'Gas forced warm air furnace',
    'GasW':	'Gas hot water or steam heat',
    'Grav':	'Gravity furnace',
    'OthW':	'Hot water or steam heat other than gas',
    'Wall':	'Wall furnace'
}

df['Heating'] = df['Heating'].replace(Heating_names)

HeatingQC_names = {
    'Ex': 'Excellent',
    'Gd': 'Good',
    'TA': 'Average/Typical',
    'Fa': 'Fair',
    'Po': 'Poor'
}

df['HeatingQC'] = df['HeatingQC'].replace(HeatingQC_names)

CentralAir_names = {
    'N': 'No',
    'Y': 'Yes'
}

df['CentralAir'] = df['CentralAir'].replace(CentralAir_names)


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



export_csv = df.to_csv(r'./export_dataframe.csv', index= None, header=True)
print(df)

