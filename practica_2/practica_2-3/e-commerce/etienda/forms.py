from django import forms
from django.core.validators import RegexValidator

# Validador para asegurarse de que la primera letra sea mayúscula
validator_mayus = RegexValidator(
    regex=r"^[A-Z].*", message="El nombre debe comenzar con mayúscula."
)

# Opciones de categoría
CATEGORIAS = [
    ("women's clothing", "Women's clothing"),
    ("men's clothing", "Men's clothing"),
    ("jewelery", "Jewelery"),
    ("electronics", "Electronics"),
]


# Formulario para crear un producto
class ProductoForm(forms.Form):
    title = forms.CharField(
        label="Nombre", max_length=100, validators=[validator_mayus]
    )
    price = forms.DecimalField(label="Precio")
    description = forms.CharField(label="Descripción", max_length=1000)
    image = forms.ImageField(label='Imagen', required=False)
    category = forms.ChoiceField(label="Categoría", choices=CATEGORIAS)
