import React from 'react';
import '../css/product.css';

const ProductCard = ({ product }) => {
  return (
    <div className="list-group-item">
      <div className="product-card">
        <h3 className="card-title">{product.title}</h3>
        <img src={product.image} alt={product.title} className="img-thumbnail" width="150" height="150" />
        <p className="card-body"><strong>Description:</strong> {product.description}</p>
        <p className="card-body"><strong>Price:</strong> {product.price}€</p>
        <p className="card-body"><strong>Category:</strong> {product.category}</p>
      </div>
    </div>
  );
};

export default ProductCard;
