import React from 'react';

const SearchBar = ({ onSearch, onClick }) => {
  return (
    <div>
      <input
        type="text"
        id="search"
        name="search"
        placeholder="Ingresa tu búsqueda"
        onChange={onSearch}
      />
      <button className="btn btn-outline-success my-2 my-sm-0" type="button" onClick={onClick}>
        Buscar
      </button>
    </div>
  );
};

export default SearchBar;
