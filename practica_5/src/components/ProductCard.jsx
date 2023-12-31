import React from 'react';
import '../css/product.css';

const ProductCard = ({ product }) => {
  return (
    <div className="product-card">
      <h3>{product.title}</h3>
      <img src={product.image} alt={product.title} className="product-image" />
      <p><strong>Description:</strong> {product.description}</p>
      <p><strong>Price:</strong> {product.price}€</p>
      <p><strong>Category:</strong> {product.category}</p>
    </div>
  );
};

export default ProductCard;
