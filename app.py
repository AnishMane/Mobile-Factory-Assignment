from flask import Flask, request, jsonify

app = Flask(__name__)

# Initial Data
COMPONENTS = {
    "A": {"price": 10.28, "part": "LED Screen"},
    "B": {"price": 24.07, "part": "OLED Screen"},
    "C": {"price": 33.30, "part": "AMOLED Screen"},
    "D": {"price": 25.94, "part": "Wide-Angle Camera"},
    "E": {"price": 32.39, "part": "Ultra-Wide-Angle Camera"},
    "F": {"price": 18.77, "part": "USB-C Port"},
    "G": {"price": 15.13, "part": "Micro-USB Port"},
    "H": {"price": 20.00, "part": "Lightning Port"},
    "I": {"price": 42.31, "part": "Android OS"},
    "J": {"price": 45.00, "part": "iOS OS"},
    "K": {"price": 45.00, "part": "Metallic Body"},
    "L": {"price": 30.00, "part": "Plastic Body"}
}

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    components = data.get('components', [])
    
    # Check if all required components are present
    required_components = {"Screen", "Camera", "Port", "OS", "Body"}
    component_types = set()
    for component_code in components:
        component_type = get_component_type(component_code)
        if component_type in component_types:
            return jsonify({"error": f"Duplicate component type: {component_type}"}), 400
        component_types.add(component_type)
    if component_types != required_components:
        return jsonify({"error": "Missing component types"}), 400
    
    # Calculate total price
    total_price = 0
    parts = []
    for component_code in components:
        price = COMPONENTS[component_code]['price']
        part = COMPONENTS[component_code]['part']
        total_price += price
        parts.append(part)
    
    order_id = "some-id" 
    
    return jsonify({
        "order_id": order_id,
        "total": total_price,
        "parts": parts
    }), 201

def get_component_type(component_code):
    if component_code in ["A", "B", "C"]:
        return "Screen"
    elif component_code in ["D", "E"]:
        return "Camera"
    elif component_code in ["F", "G", "H"]:
        return "Port"
    elif component_code in ["I", "J"]:
        return "OS"
    elif component_code in ["K", "L"]:
        return "Body"

if __name__ == '__main__':
    app.run(debug=True)
