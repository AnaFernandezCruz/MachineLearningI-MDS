import pandas as pd


train = pd.read_csv("./data/train.csv", delimiter=",")
test = pd.read_csv("./data/test.csv", delimiter=",")
sample = pd.read_csv("./data/sample_submission.csv", delimiter=",")

test = pd.merge(test, sample,  on='Id')

df = pd.concat([train, test])

columns_name = {
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


df.rename(columns=columns_name, inplace=True)

export_csv = df.to_csv(r'./export_dataframe.csv', index= None, header=True)
print(df)

