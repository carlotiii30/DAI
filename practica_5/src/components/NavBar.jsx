// Navbar.jsx
import React from 'react';
import SearchBar from './SearchBar.jsx';
import Categories from './Categories.jsx';

const Navbar = ({ handleChange, handleSearch, categoryClick }) => {

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <a className="navbar-brand" href="#">E-tienda</a>

      <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>

      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav ml-auto">
          <li className="nav-item">
            <a className="nav-link" href="/etienda/">Last offers</a>
          </li>
        </ul>

        <ul className="navbar-nav ml-auto">
          <li className="nav-item">
            <Categories onClick={categoryClick} />
          </li>
        </ul>

        <ul className="navbar-nav mr-auto">
          <li className="nav-item">
            <SearchBar onSearch={handleChange} onClick={handleSearch} />
          </li>
        </ul>

        <ul className="navbar-nav mr-auto">
          <li className="nav-item">
            <a className="nav-link" href="/etienda/">Login</a>
          </li>
        </ul>

      </div>
    </nav>
  );
};

export default Navbar;
