{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b77ad818-8456-4c79-b841-9a576cb1b66c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask in c:\\users\\harsh\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (3.0.3)\n",
      "Requirement already satisfied: Werkzeug>=3.0.0 in c:\\users\\harsh\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (3.0.3)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\harsh\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (3.1.4)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\users\\harsh\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (2.2.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\users\\harsh\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (8.1.7)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\users\\harsh\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (1.8.2)\n",
      "Requirement already satisfied: colorama in c:\\users\\harsh\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from click>=8.1.3->flask) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\harsh\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from Jinja2>=3.1.2->flask) (2.1.5)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 24.1.2 -> 24.3.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install flask\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e16955fc-24f3-4206-9348-9b6b42b6db4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with stat\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\harsh\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3585: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return \"Welcome to Flask App!\"\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "334cadc3-f0f5-4640-b2ef-d2d5f6ed82f1",
   "metadata": {},
   "outputs": [
    {
     "ename": "UnpicklingError",
     "evalue": "invalid load key, '{'.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mUnpicklingError\u001b[0m                           Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 6\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpickle\u001b[39;00m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;66;03m# Load the trained model\u001b[39;00m\n\u001b[1;32m----> 6\u001b[0m model \u001b[38;5;241m=\u001b[39m \u001b[43mpickle\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mload\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mmodel.pkl\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mrb\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m      8\u001b[0m app \u001b[38;5;241m=\u001b[39m Flask(\u001b[38;5;18m__name__\u001b[39m)\n\u001b[0;32m     10\u001b[0m \u001b[38;5;66;03m# Home route that renders the front-end page (index.html)\u001b[39;00m\n",
      "\u001b[1;31mUnpicklingError\u001b[0m: invalid load key, '{'."
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template, jsonify\n",
    "import numpy as np\n",
    "import pickle\n",
    "\n",
    "# Load the trained model\n",
    "model = pickle.load(open(\"model.pkl\", \"rb\"))\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Home route that renders the front-end page (index.html)\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return render_template('index.html')  # Ensure you have the front-end page\n",
    "\n",
    "# Route to make predictions based on the input data\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    # Get data from the form (sent via POST request)\n",
    "    data = request.json\n",
    "\n",
    "    # Extract the features from the incoming request\n",
    "    features = np.array([[data['N'], \n",
    "                          data['P'], \n",
    "                          data['K'], \n",
    "                          data['temperature'], \n",
    "                          data['humidity'], \n",
    "                          data['ph'], \n",
    "                          data['rainfall']]])\n",
    "\n",
    "    # Make the prediction using the trained model\n",
    "    prediction = model.predict(features)[0]  # Get the predicted crop label\n",
    "\n",
    "    # Return the prediction as JSON\n",
    "    return jsonify({'suggested_crop': prediction})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f93b6d46-53b6-41b6-8d32-d1a7489c89d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "os.system(\"python app.py\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ecfa1500-6996-4470-a79a-af970338c24d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5001\n",
      "Press CTRL+C to quit\n",
      " * Restarting with stat\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\harsh\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3585: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, port=5001)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1c4232e-b440-4337-8bac-2a5972f4d13b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [05/Dec/2024 04:30:54] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [05/Dec/2024 04:30:54] \"GET /favicon.ico HTTP/1.1\" 404 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, use_reloader=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ab9c690-1a5f-4a46-824b-4442f38e68c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f13f6fcf-7a32-41b6-87ba-1fa6912adc68",
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install gunicorn\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8412a5b6-60df-456a-a05c-dabdcb42e97c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return \"Welcome to Flask App!\"\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, use_reloader=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4baa3dbe-e4f4-4668-9db4-d7558f771128",
   "metadata": {},
   "outputs": [],
   "source": [
    "python app.py\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ddc8c11-18f4-4373-9b66-dabc9d124bee",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
