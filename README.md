Simple flask webapp to demo framework

# Installation

1. Clone the repository
```
git clone 
```
2. Create a virtual environment
```
cd flask-test
python3 -m venv venv
source venv/bin/activate
```
3. Install requirements
```
pip install -r requirements.txt
```
4. Start server
```
flask run
```
5. Navigate to your browser `http://127.0.0.1:5000`

# Pages Accessible

http://127.0.0.1:5000/ "Hello, World!"
http://127.0.0.1:5000/stats Generates a random numpy array and calculates scipy descriptive statistics on it.
http://127.0.0.1:5000/hello/<name> where `<name>` is any string. "Hello <name>"
http://127.0.0.1:5000/sum shows a form with 2 inputs and will return the sum of two numbers.
