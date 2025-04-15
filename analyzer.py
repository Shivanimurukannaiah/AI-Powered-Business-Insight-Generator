
def summarize_data(df):
    summary = df.describe(include='all').to_dict()
    return summary
