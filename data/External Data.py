import kagglehub
from kagglehub import KaggleDatasetAdapter



df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "adilshamim8/student-depression-dataset",
    "student_depression_dataset.csv"
)

print(df.head())





