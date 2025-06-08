import pandas as pd
from sklearn import tree 
from sklearn.model_selection import train_test_split 
import graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
#https://scikit-learn.org/stable/modules/tree.html 
#Faults dataset from here: https://archive.ics.uci.edu/dataset/198/steel+plates+faults

faults = ["Pastry", "Z_Scratch", "K_Scatch", "Stains", "Dirtiness", "Bumps", "Other_Faults"]

def read_in_dataset(faults):
    df = pd.read_csv("faults.csv")
    df['fault'] = 0 
    #Lets create a categorical variable for each fault 
    #In the new "fault" column 
    for i in range(0, len(faults)):
        #index list
        true_fault_indexes = df.loc[df[faults[i]] == 1].index.tolist()
        df.loc[true_fault_indexes, "fault"] = i+1
        #Create our dataset 
    return df

df = read_in_dataset(faults)
#Create the training and test set 
drop_features = ["fault"] + faults
features = df.drop(drop_features, axis=1)
outcomes = df["fault"]
training_features, test_features, training_outcomes, test_outcomes = train_test_split(features, outcomes, test_size=0.1)

model = tree.DecisionTreeClassifier()
#model = RandomForestClassifier()
model.fit(training_features, training_outcomes)
test_accuracy_score = model.score(test_features, test_outcomes)
training_accuracy_score = model.score(training_features, training_outcomes)
print(f"Training accuracy {training_accuracy_score}")
print(f"Test accuracy {test_accuracy_score}")


print("Per Class Accuracy")
test_predictions = model.predict(test_features)
matrix = confusion_matrix(test_outcomes, test_predictions)
class_accuracies = matrix.diagonal()/matrix.sum(axis=1)
print(class_accuracies)


# #Visualize the tree 
# dot_data = tree.export_graphviz(model, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render("steel_tree")

#Predict a random value 
test_features.reset_index(inplace=True)
# test_outcomes.reset_index(inplace=True)
number = 3
random_features = pd.DataFrame([test_features.iloc[number]])
random_features = random_features.drop(["index"], axis=1)
random_outcome = test_outcomes.tolist()[number]
outcome_prediction = model.predict(random_features)
#Print
print("Features")
print(random_features)
print(random_outcome)
print(outcome_prediction[0])
print(f"Predicted Fault: {faults[outcome_prediction[0]-1]}, Actual Fault {faults[random_outcome-1]}")

predicted_probabilies = model.predict_proba(random_features)
print(f"The predicted probabilities for each class were: {predicted_probabilies}")


