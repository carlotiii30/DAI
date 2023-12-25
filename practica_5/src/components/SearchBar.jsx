import React from 'react';

const SearchBar = ({ onSearch }) => {
  return (
    <div>
      <label htmlFor="search">Buscar: </label>
      <input
        type="text"
        id="search"
        name="search"
        placeholder="Ingresa tu búsqueda"
        onChange={onSearch}
      />
    </div>
  );
};

export default SearchBar;
