import pandas as pd
import argparse
import logging

logging.basicConfig(level=logging.INFO,filename="test.log", filemode="w", format="%(message)s")


class TitanicCleaner:
  def __init__(self, file_name):
    self.file_name = file_name
    self.data = None

  def load_data(self):
    logging.info("Loading csv file.....")
    self.data = pd.read_csv(self.file_name)
    data = self.data
    logging.info(f"Data loaded successfully from {self.file_name}")
    logging.info(data.head())

  def fill_missing_value(self):
    data = self.data
    # data = self.load_data()
    missing_values = data.isnull().sum()
    missing_values_count = data.isnull().sum().sum()
    logging.info("Checking for missing values...")
    logging.info(missing_values)
    if missing_values_count > 0:
      data.fillna(value={'Age': data.Age.mean()}, inplace=True)
      data.fillna(value={'Fare': 1}, inplace=True)
      data.fillna(value={'Cabin': 0}, inplace=True)
    logging.info("Filling missing values....")
    logging.info(data.isnull().sum())

  def remove_duplicate(self):
    data = self.data
    # data = self.load_data()
    duplicates = data.duplicated().value_counts()
    if duplicates is True:
      data.drop_duplicates()
    logging.info("Checking for duplicates....")
    logging.info(duplicates)

  def grouped_age(self):
    data = self.data
    # data = self.load_data()
    bin = [0,18, 40, 60, 66]
    labels = ['<18', '18-40', '41-60', '60+']
    data['grouped_age'] = pd.cut(data['Age'], bins=bin, labels=labels, right=False)
    survival_rate_by_age_group = data.groupby(['grouped_age'], observed=False)['Survived'].mean() * 100
    logging.info("Adding transformation.....")
    logging.info(survival_rate_by_age_group)
  
  def family_size(self):
    data = self.data
    # data = self.load_data()
    data['FamilySize'] = data['SibSp'] + data['Parch']
    logging.info("Calculating Family Size...")
    logging.info("Checking for Family Size on the table...")
    logging.info(data)

  def map_embarked_column(self):
    # data = self.load_data()
    data = self.data
    mapped_embarked = {
      'S': 'Southampton',
      'C': 'Cherbough',
      'Q': 'Queenstown'
    }
    data['Embarked'] = data['Embarked'].map(mapped_embarked)
    logging.info("Mapping Embarked Column....")
    logging.info(data.head())


def main():
  parser = argparse.ArgumentParser(description="Titanic Data Analysis")
  parser.add_argument('--file', type=str, required=True, help="Path to the Titanic Data Analysis csv file.")
  args = parser.parse_args()

  titanic = TitanicCleaner(args.file)
  # logging.INFO("Load Titanic data and analyze missing values for the specified column")
  titanic.load_data()
  titanic.fill_missing_value()
  titanic.remove_duplicate()
  titanic.grouped_age()
  titanic.family_size()
  titanic.map_embarked_column()

if __name__ == "__main__":
  main()

  # my_file = "tested.csv"
  # load = TitanicCleaner(my_file)
  

  