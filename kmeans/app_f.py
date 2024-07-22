from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)


model = joblib.load('kmeans_pipeline.pkl')


cluster_labels = {0: 'ouro', 1: 'prata', 2: 'bronze'}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  
    df = pd.DataFrame(data)
    
   
    df['cluster'] = model.predict(df)
    df['cluster_label'] = df['cluster'].map(cluster_labels)
    
 
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and file.filename.endswith('.csv'):
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)
        df = pd.read_csv(filepath)
        
        
        df['cluster'] = model.predict(df)
        df['cluster_label'] = df['cluster'].map(cluster_labels)
        
        
        result_filepath = os.path.join('uploads', 'result_' + file.filename)
        df.to_csv(result_filepath, index=False)
        
        return jsonify({"message": "File processed", "result_file": result_filepath}), 200

    return jsonify({"error": "Invalid file type"}), 400

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
