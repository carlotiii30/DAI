const apiUrl = 'http://localhost:8000/etienda/api';


export const fetchProducts = async (searchTerm) => {
    try {
        const response = await fetch(`${apiUrl}/productos/busqueda/${searchTerm}`);
        const data = await response.json();

        console.log('API Response:', data); // Agrega esta línea para depurar la respuesta

        // Si la respuesta es correcta, retorna los resultados
        if (response.ok) {
            return { resultados: data };
        }
    } catch (error) {
        console.error('Error al obtener productos:', error);
        throw error;
    }
};

export const fetchProductsByCategory = async (category) => {
    try {
        const response = await fetch(`${apiUrl}/productos/categoria/${category}`);
        const data = await response.json();

        console.log('API Response (Products by Category):', data);

        if (response.ok) {
            return { resultados: data };
        }
    } catch (error) {
        console.error('Error al obtener productos por categoría:', error);
        throw error;
    }
};

export const fetchCategories = async () => {
    try {
      const response = await fetch(`${apiUrl}/categorias`);

      if (!response.ok) {
        throw new Error(`Error fetching categories. Status: ${response.status}`);
      }

      const data = await response.json();

      console.log('API Response (Categories):', data);

      return { categorias: data };
    } catch (error) {
      console.error('Error al obtener categorías:', error);
      throw error;
    }
  };