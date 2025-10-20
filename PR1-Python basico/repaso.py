print('nom')
print('ap1 ap2')
print('nom', end=' ')
print('ap1', 'ap2')
print('nom','ap1', 'ap2', sep=' ')
print('nom\nap1\nap2')
print('nom\nap1\nap2\n', 680331932)    

colorTitulo= '\033[34m'
colortabla= '\033[0m' 
colorTexto= '\033[32m'

productos= [
    ('Manzana', 0.50),
    ('Plátano', 0.30),
    ('Naranja', 0.40),
    ('Pera', 0.60),
    ('Mango', 1.20)
]

print(f"{colorTitulo}{'Producto':<15}{colortabla}|{colorTitulo}{'Precio (€)':>12}{colortabla}")
print('-'*30)

for producto, precio in productos:
    print(f'{colorTexto}{producto:<15}{colortabla}|{colorTexto}{precio:>12.2f} €{colortabla}')

base = float(input('Escriba el precio antes del iva: '))
tipoIVA = input('Escriba el tipo de IVA (general 21%, reducido 10% o superreducido 4%): ').lower()
tipoPromo = input('Escriba el tipo de promoción (sinpromo, mitad, descfijo *5€* o porcentaje *5%*) ').lower()

match tipoIVA:
    case 'general':
        iva = 0.21
    case 'reducido':
        iva = 0.10
    case 'superreducido':
        iva = 0.04
    case _:
        iva = 0.21
        print('IVA introducido no válido, se usará el general por defecto')

precioConIva = base * (1*iva)

match tipoPromo:
    case 'sinpromo':
        total = precioConIva
    case 'mitad':
        total = precioConIva / 2
    case 'descfijo':
        total = precioConIva - 5
    case 'porcentaje':
        total = precioConIva * 0.95
    case _:
        print('Tipo de promoción no válido, no se asignará ningún descuento')
        total = precioConIva

print(f'Base imponible {base:<25}')
print(f'IVA {tipoIVA:<20}')
print(f'Precio con IVA {precioConIva:<25.2f}')
print(f'tipo de promo {tipoPromo:<25}')
print(f'{total<25}')