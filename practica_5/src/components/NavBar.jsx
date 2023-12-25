// Navbar.jsx
import React from 'react';

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <a className="navbar-brand" href="#">E-tienda</a>
      <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav ml-2">
          <li className="nav-item">
            <a className="nav-link" href="/etienda/">Last offers</a>
          </li>
        </ul>
        <ul className="navbar-nav">
          <li className="nav-item dropdown">
            <a className="nav-link dropdown-toggle" href="#" id="navbarDropdownCategorias" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Categories
            </a>
            <div className="dropdown-menu" aria-labelledby="navbarDropdownCategorias">
              <a className="dropdown-item" href="/etienda/categoria/women's clothing">Women's Fashion</a>
              <a className="dropdown-item" href="/etienda/categoria/men's clothing">Men's Fashion</a>
              <a className="dropdown-item" href="/etienda/categoria/jewelery">Jewelery</a>
              <a className="dropdown-item" href="/etienda/categoria/electronics">Electronics</a>
            </div>
          </li>
        </ul>
        {/* ... Otros elementos de la barra de navegación ... */}
      </div>
    </nav>
  );
};

export default Navbar;
