
from src.data_loader import load_data
from src.analyzer import summarize_data
from src.insight_generator import generate_insights

if __name__ == '__main__':
    df = load_data('data/sample_data.csv')
    summary = summarize_data(df)
    insights = generate_insights(summary)
    print(insights)
