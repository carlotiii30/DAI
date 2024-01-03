import React from 'react';
import '../css/product.css';

const ProductCard = ({ product }) => {
  return (
    <li className="list-group-item">
      <h3 className="card-title">{product.title}</h3>
      <img src={product.image} alt={product.title} className="img-thumbnail" width="150" height="150" />
      <p><strong>Description:</strong> {product.description}</p>
      <p><strong>Price:</strong> {product.price}€</p>
      <p><strong>Category:</strong> {product.category}</p>
    </li>
  );
};

export default ProductCard;
