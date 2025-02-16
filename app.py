from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask App is Running!"

@app.route('/calculate', methods=['POST'])
def calculate_fuel():
    data = request.json
    sounding = data.get('sounding', 0)
    density = data.get('density', 0)
    tcf = data.get('tcf', 1)

    # Example sounding table (replace with real data)
    sounding_table = {10: 1.2, 20: 2.5, 30: 3.8, 40: 5.2, 50: 6.5}

    volume = sounding_table.get(sounding, 0)
    corrected_volume = volume * tcf
    mass = corrected_volume * density

    return jsonify({"corrected_volume": corrected_volume, "mass": mass})

if __name__ == '__main__':
    app.run(debug=True)
