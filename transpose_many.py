# %%
import pandas as pd

# %%
def transpose_many(files, output_file):
    transposed = []
    
    for file in files:
        df = pd.read_excel(file)
        df_transposed = df.set_index("Data").T
        transposed.append(df_transposed)

    final_df = pd.concat(transposed, ignore_index=True)
    final_df.to_excel(output_file, index=False)

    return final_df


