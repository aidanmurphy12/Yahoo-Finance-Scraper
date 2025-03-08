# %%
import pandas as pd

# %%
def transpose(file, output_file):
    df = pd.read_excel(file)
    df_transposed = df.set_index("Data").T
    df_transposed.to_excel(output_file, index=False)
    return df_transposed


