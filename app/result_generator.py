#import libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def generate(all_matchups):
    #import dataset
    pokemon=pd.read_csv('app//datasets//pokemons_data.csv',index_col=0)
    combats=pd.read_csv('app//datasets//combats.csv')

    #replace ids with pokemon names
    cols = ["First_pokemon","Second_pokemon","Winner"]
    new_combat_data=combats[cols].replace(pokemon.Name)
    new_combat_data.head()

    #Prepare actual Winner column (the actual output for training)    
    combats.Winner[combats.Winner == combats.First_pokemon] = 0
    combats.Winner[combats.Winner == combats.Second_pokemon] = 1

    #Taking diff between pokemon stats and normalizing the data
    def normalization(data_df):
        stats=["Hit Points","Attack","Defense","Sp. Atk","Sp. Def","Speed","Legendary"]
        stats_df=pokemon[stats].T.to_dict("list")
        one=data_df.First_pokemon.map(stats_df)
        two=data_df.Second_pokemon.map(stats_df)
        temp_list=[]
        for i in range(len(one)):
            temp_list.append(np.array(one[i])-np.array(two[i]))
        new_test = pd.DataFrame(temp_list, columns=stats)
        for c in stats:
            description=new_test[c].describe()
            new_test[c]=(new_test[c]-description['min'])/(description['max']-description['min'])
        return new_test

    data=normalization(combats)
    data = pd.concat([data,combats.Winner], axis=1)

    x_label=data.drop("Winner",axis=1) #inputs
    y_label=data["Winner"] #outputs

    x_train, x_test, y_train, y_test = train_test_split(x_label, y_label, test_size=0.25, random_state=42)

    clf = RandomForestClassifier(n_estimators=100)
    model = clf.fit(x_train, y_train) #training
    pred = model.predict(x_test) #predicting on validation set

    #importing test dataset 
    test_data=pd.read_csv('app//datasets//tests.csv') 

    #replace ids with name
    new_test_data=test_data[["First_pokemon","Second_pokemon"]].replace(pokemon.Name)
    new_test_data.head()

    #normalizing test data
    final_data=normalization(test_data)
    pred=model.predict(final_data)#final predictions
    test_data["Winner"]=[test_data["First_pokemon"][i] if pred[i]==0 else test_data["Second_pokemon"][i] for i in range(len(pred))]
    
    return test_data[cols].replace(pokemon.Name)
#[63:64]

