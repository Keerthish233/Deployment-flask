{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a327f83-0865-4ab6-9ac4-c51663450bbc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask,request,jsonify\n",
    "import joblib\n",
    "import numpy as np \n",
    "app=Flask(__name__)\n",
    "model=joblib.load(\"model.pkl\")\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return\"Welcome to the ML Model API!\"\n",
    "@app.route('/predict',method=['POST'])\n",
    "def predict():\n",
    "    data = request.get_json()\n",
    "    features = np.array(data['features']).reshape(1,-1)\n",
    "    prediction = model.predict(features)\n",
    "    return jsonify('prediction':prdiction.tolist())\n",
    "if  __name__=='__main__':\n",
    "    app.run(deburg=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
