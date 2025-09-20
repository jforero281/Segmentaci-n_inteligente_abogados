from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer


class Train:
    def __init__(self, df,numeric_features, categorical_features, categorical_high, target_column, model, test_size=0.2):
        self.df=df
        self.numeric_features=numeric_features
        self.categorical_features=categorical_features
        self.categorical_high=categorical_high
        self.target_columns=target_column
        self.test_size=test_size
        self.model=model

    def train_test_split(self):
        X_train, X_test, y_train, y_test = train_test_split(self.df.drop(columns=["DECISION"]), self.df["DECISION"], test_size=self.test_size, random_state=42)
        return X_train, X_test, y_train, y_test
    


    def create_pipeline_numeric(self):
        numeric_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())])
        return numeric_transformer
    
    def create_pipeline_categorical(self):
        categorical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='constant', fill_value='other')),('onehot', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'))])
        return categorical_transformer


    def create_pipelilne_categorical_high(self):
        categorical_high_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='constant', fill_value='Other')),('ordinal', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1))])
        return categorical_high_transformer
    
    def create_preprocessor(self):
        preprocessor = ColumnTransformer(transformers=[('num', self.create_pipeline_numeric, self.numeric_features),('cat', self.create_pipeline_categorical, self.categorical_features),('cat2', self.create_pipelilne_categorical_high, self.categorical_high)],remainder='drop')
        return preprocessor
    

    def create_pipeline_train(self):
        pipeline_train_cont = Pipeline(steps=[('preprocessor', self.create_preprocessor()),('classifier', self.model)])
        return pipeline_train_cont
    
    def train(self):
        X_train, X_test, y_train, y_test = train_test_split()
        pipeline=self.create_pipeline_train()
        pipeline.fit(X_train, y_train)
        return pipeline
    


    


    
