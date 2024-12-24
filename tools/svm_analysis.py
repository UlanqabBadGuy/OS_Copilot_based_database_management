from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import csv

def svm_analysis(csv_file_path, output_txt_path, target_column):
    """
    Perform SVM classification on a dataset from a CSV file and save results to a text file.

    Args:
        csv_file_path (str): Path to the input CSV file containing the dataset.
        output_txt_path (str): Path to save the SVM results as a text file.
        target_column (str): The name of the column containing target labels.

    Returns:
        None: Saves results to the specified text file.
    """
    try:
        # Step 1: Read data from CSV file
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        # Step 2: Separate features and target
        feature_columns = [col for col in data[0].keys() if col != target_column]
        X = [[float(row[col]) for col in feature_columns] for row in data]
        y = [row[target_column] for row in data]

        # Step 3: Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=123)

        # Step 4: Train SVM classifier
        model = SVC(kernel='linear', random_state=42)
        model.fit(X_train, y_train)

        # Step 5: Make predictions
        y_pred = model.predict(X_test)

        # Step 6: Evaluate model performance
        confusion = confusion_matrix(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        # Step 7: Save results to text file
        with open(output_txt_path, 'w') as output_file:
            output_file.write("SVM Classification Report\n")
            output_file.write("==========================\n\n")
            output_file.write("Confusion Matrix:\n")
            for row in confusion:
                output_file.write(f"{row}\n")
            output_file.write("\nClassification Report:\n")
            output_file.write(report)
        print(f"SVM results saved to {output_txt_path}")

    except Exception as e:
        raise RuntimeError(f"Error in SVM processing: {e}")