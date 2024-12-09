import pandas as pd
import os
import sys
from bs4 import BeautifulSoup

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.db import get_db
from models.models import Fifa

def get_fifa_data() -> pd.DataFrame:
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file_path = os.path.join(dir, "data", "FIFA17_official_data.csv")

    if os.path.exists(csv_file_path):
        df = pd.read_csv(csv_file_path)
        return df 
    else:
        print(f"csv file not found at: {csv_file_path}")
    
def clean_fifa_data(df: pd.DataFrame) -> pd.DataFrame:

    # Define a helper function to clean HTML from a single value
    def clean_html(value):
        if isinstance(value, str):  # Only clean if the value is a string
            return BeautifulSoup(value, "html.parser").get_text()
        return value  # Return the value unchanged if it's not a string

    # Apply the cleaning function to all columns within the function
    for column in df.columns:
        df[column] = df[column].apply(clean_html)

    print("HTML content removed from the DataFrame.")
    return df


def update_db(df: pd.DataFrame):
    fifa17_db = get_db()

    db_data = [
        Fifa(
            ID = row["ID"],
            Name = row['Name'],
            Age = row["Age"],
            Photo = row["Photo"],
            Nationality = row["Nationality"],
            Flag = row["Flag"],
            Overall = row["Overall"],
            Potential = row["Potential"],
            Club = row["Club"],
            ClubLogo = row["ClubLogo"],
            Value = row["Value"],
            Wage = row["Wage"],
            Special = row["Special"],
            PreferredFoot = row["PreferredFoot"],
            InternationalReputation = row["InternationalReputation"],
            WeakFoot = row["WeakFoot"],
            SkillMoves = row["SkillMoves"],
            WorkRate = row["WorkRate"],
            BodyType = row["BodyType"],
            RealFace = row["RealFace"],
            Position = row["Position"],
            JerseyNumber = row["JerseyNumber"],
            Joined = row["Joined"],
            LoanedFrom = row["LoanedFrom"],
            ContractValidUntil = row["ContractValidUntil"],
            Height = row["Height"],
            Weight = row["Weight"],
            Crossing = row["Crossing"],
            Finishing = row["Finishing"],
            HeadingAccuracy = row["HeadingAccuracy"],
            ShortPassing = row["ShortPassing"],
            Volleys = row["Volleys"],
            Dribbling = row["Dribbling"],
            Curve = row["Curve"],
            FKAccuracy = row["FKAccuracy"],
            LongPassing = row["LongPassing"],
            BallControl = row["BallControl"],
            Acceleration = row["Acceleration"],
            SprintSpeed = row["SprintSpeed"],
            Agility = row["Agility"],
            Reactions = row["Reactions"],
            Balance = row["Balance"],
            ShotPower = row["ShotPower"],
            Jumping = row["Jumping"],
            Stamina = row["Stamina"],
            Strength = row["Strength"],
            LongShots = row["LongShots"],
            Aggression = row["Aggression"],
            Interceptions = row["Interceptions"],
            Positioning = row["Positioning"],
            Vision = row["Vision"],
            Penalties = row["Penalties"],
            Composure = row["Composure"],
            Marking = row["Marking"],
            StandingTackle = row["StandingTackle"],
            SlidingTackle = row["SlidingTackle"],
            GKDiving = row["GKDiving"],
            GKHandling = row["GKHandling"],
            GKKicking = row["GKKicking"],
            GKPositioning = row["GKPositioning"],
            GKReflexes = row["GKReflexes"],
            BestPosition = row["BestPosition"],
            BestOverallRating = row["BestOverallRating"],
        )
        for row in df.to_dict(orient='records')
    ]
    
    fifa17_db.add_all(db_data)
    fifa17_db.commit()
    print("Database updated successfully.") 


if __name__ == "__main__":
    fifa_df = get_fifa_data()
    cleaned_df = clean_fifa_data(fifa_df)
    update_db(cleaned_df)
