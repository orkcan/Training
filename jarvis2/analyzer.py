import pandas as pd


class DataAnalyzer:
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        self.data = pd.read_csv(data_file_path)

    def get_daily_summary(self, date):
        daily_data = self.data[self.data['date'] == date]
        summary = {
            'Events': daily_data['events'].tolist(),
            'Relationships': daily_data['relationships'].tolist(),
            'Learning Progress': daily_data['learning'].tolist(),
            'Daily Questions': daily_data['daily_questions'].tolist()
        }
        return summary

    def analyze_mood(self):
        mood_data = self.data[self.data['question'].str.lower().str.contains('mood')]

