from transform_trg.transform_trg import mer
import pandas as pd
def load_trg(ds_nodash):

    df = mer(ds_nodash)
    
    korea_movie = df[df['repNationCd']=='K']
    korea_movie['salesAmt'] = pd.to_numeric(korea_movie['salesAmt'])
    korea_movie.sort_values('salesAmt', ascending=False, inplace=True)
    korea_movie.reset_index(inplace=True, drop=True)
    
    print(korea_movie.head())
