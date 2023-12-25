import React, { useEffect, useState } from 'react';
import ProductCard from './ProductCard';
import { fetchProducts } from '../utils/api';

const ProductList = ({ searchTerm }) => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProductsData = async () => {
      try {
        const data = await fetchProducts(searchTerm);
        console.log('Data:', data);

        // Verifica si hay productos en la respuesta
        if (data.resultados && data.resultados.length > 0) {
          setProducts(data.resultados);
        } else {
          // Si no hay productos, puedes manejar esto de alguna manera, por ejemplo, mostrando un mensaje o realizando otra acción
          console.log('No se encontraron productos.');
        }
      } catch (error) {
        console.error('Error al obtener productos:', error);
      }
    };

    fetchProductsData();
  }, [searchTerm]);

  return (
    <div>
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};

export default ProductList;
