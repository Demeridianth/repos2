from flask import Flask, render_template, request

class CoffeeShop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.types = {1: 'black', 2: 'white', 3: 'cappuccino'}
        self.sizes = {1: 'small', 2: 'medium', 3: 'large'}
        self.extra_components = {1: 'milk', 2: 'cream', 3: 'vanilla'}

    def make_coffee(self, type_number: int, size_number: int, component_number: int) -> str:
        coffee_type = self.types.get(type_number)
        size = self.sizes.get(size_number)
        component = self.extra_components.get(component_number)

        if coffee_type and size and component:
            return f"Your order is a {size} {coffee_type} with {component}."
        return "Invalid order. Please check your inputs."

# Flask App Setup
app = Flask(__name__)
shop = CoffeeShop('Python Coffee')

@app.route('/')
def home():
    return render_template('index.html', shop_name=shop.name, types=shop.types, sizes=shop.sizes, extras=shop.extra_components)

@app.route('/order', methods=['POST'])
def order():
    type_number = int(request.form.get('type_number'))
    size_number = int(request.form.get('size_number'))
    component_number = int(request.form.get('component_number'))

    result = shop.make_coffee(type_number, size_number, component_number)
    return render_template('index.html', shop_name=shop.name, types=shop.types, sizes=shop.sizes, extras=shop.extra_components, message=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


# Open your browser and go to http://127.0.0.1:5000/