
import os
import pandas as pd
from datetime import datetime

class LastfmProcessor:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.dataframes = []
        self.users = pd.DataFrame()
        self.musics = pd.DataFrame()
        self.listens = pd.DataFrame()

    def load_files(self):
        """Load all CSV files from the input folder."""
        for fichier in os.listdir(self.input_folder):
            if fichier.endswith(".csv"):
                complete_path = os.path.join(self.input_folder, fichier)
                if os.stat(complete_path).st_size == 0:
                    continue
                try:
                    df = pd.read_csv(complete_path, header=None, encoding="utf-8")
                    df["Source_File"] = os.path.splitext(fichier)[0]
                    self.dataframes.append(df)
                except Exception:
                    continue

    def process_data(self):
        """Transform data into relational tables."""
        if not self.dataframes:
            return
        combined_df = pd.concat(self.dataframes, ignore_index=True)
        combined_df.columns = ["Artist", "Album", "Music_name", "Date", "Source_File"]
        combined_df["Date"] = pd.to_datetime(combined_df["Date"], format="%d %b %Y %H:%M", errors="coerce")
        cleaned_df = combined_df.dropna(subset=["Date"])
        start_date, end_date = datetime(2006, 1, 1), datetime(2024, 12, 31)
        filtered_df = cleaned_df[(cleaned_df["Date"] >= start_date) & (cleaned_df["Date"] <= end_date)]
        self.users = pd.DataFrame(filtered_df["Source_File"].unique(), columns=["User_Name"])
        self.users["User_ID"] = range(1, len(self.users) + 1)
        music_columns = ["Artist", "Album", "Music_name"]
        self.musics = filtered_df[music_columns].drop_duplicates().reset_index(drop=True)
        self.musics["Music_ID"] = range(1, len(self.musics) + 1)
        filtered_df = filtered_df.merge(self.users, left_on="Source_File", right_on="User_Name", how="left")
        filtered_df = filtered_df.merge(self.musics, on=music_columns, how="left")
        self.listens = filtered_df[["User_ID", "Music_ID", "Date"]]

    def export_to_csv(self):
        """Export relational tables to CSV."""
        os.makedirs(self.output_folder, exist_ok=True)
        self.users.to_csv(os.path.join(self.output_folder, "users.csv"), index=False, encoding="utf-8")
        self.musics.to_csv(os.path.join(self.output_folder, "musics.csv"), index=False, encoding="utf-8")
        self.listens.to_csv(os.path.join(self.output_folder, "listens.csv"), index=False, encoding="utf-8")

    def run(self):
        """Run the full pipeline."""
        self.load_files()
        self.process_data()
        self.export_to_csv()


if __name__ == "__main__":
    input_folder = "../data/raw/Lastfm"
    output_folder = "../output"
    processor = LastfmProcessor(input_folder, output_folder)
    processor.run()
