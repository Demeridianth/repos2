class CoffeShop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.type = {1: 'black', 2: 'white', 3: 'cappucino'}
        self.sizes = {1: 'small', 2: 'medium', 3: 'large'}
        self.extra_components = {1: 'milk', 2: 'cream', 3: 'vanilla'}

    def make_cofee(self, type_number: int, size_number: int, component_number: int) -> str:
        type = self.type.get(type_number)
        size = self.sizes.get(size_number)
        component = self.extra_components.get(component_number)

        print(f'your order is {size} {type} with {component}')
    
    
def get_user_input(prompt, convrter=str):
    return convrter(input(prompt))
    

def main():
    shop = CoffeShop('Python Coffe')
    print(f'welcome to {shop.name}')
    print(shop.type)
    type = get_user_input('choose a type name: ', int)
    print(shop.sizes)
    size = get_user_input('choose size: ', int)
    print(shop.extra_components)
    component = get_user_input('choose a type name: ', int)

    shop.make_cofee(type, size, component)


if __name__ == '__main__':
    main()
    