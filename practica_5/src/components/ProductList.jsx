import React, { useEffect, useState } from 'react';
import ProductCard from './ProductCard';
import { fetchProducts, fetchProductsByCategory } from '../utils/api';

const ProductList = ({ searchTerm, selectedCategory }) => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProductsData = async () => {
      try {
        console.log('Search term:', searchTerm);
        console.log('Selected category:', selectedCategory);

        if (selectedCategory) {
          // Si se seleccionó una categoría, obtén los productos de esa categoría
          const data = await fetchProductsByCategory(selectedCategory);
          console.log('Data:', data);

          console.log('Resultados Length:', data.resultados.length);

          // Verifica si hay productos en la respuesta
          if (data && data.resultados?.length) {
            setProducts(data.resultados);
          } else {
            console.log('No se encontraron productos.');
          }

          return;
        }
        else if (searchTerm) {
          // Si se ingresó un término de búsqueda, obtén los productos de esa búsqueda
          const data = await fetchProducts(searchTerm);
          console.log('Data:', data);

          console.log('Resultados Length:', data.resultados.length);

          // Verifica si hay productos en la respuesta
          if (data && data.resultados?.length) {
            setProducts(data.resultados);
          } else {
            // Si no hay productos
            console.log('No se encontraron productos.');
          }
        }

      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    fetchProductsData();
  }, [searchTerm], [selectedCategory]);

  return (
    <div>
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};

export default ProductList;
