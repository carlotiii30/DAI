import React, { useState } from 'react';
import { Dropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap';
import '../css/dropdown.css';

const Categories = ({ onCategoryClick }) => {
  const [dropdownOpen, setDropdownOpen] = useState(false);

  const handleClickCategory = (category) => {
    onCategoryClick(category);
  };

  const toggle = () => setDropdownOpen((prevState) => !prevState);

  return (
    <Dropdown isOpen={dropdownOpen} toggle={toggle}>
      <DropdownToggle caret>Categories</DropdownToggle>
      <DropdownMenu>
        <DropdownItem>
          <a className="drop-down" onClick={() => handleClickCategory("women's clothing")}>Women's Fashion</a>
        </DropdownItem>
        <DropdownItem>
          <a className="drop-down" onClick={() => handleClickCategory("men's clothing")}>Men's Fashion</a>
        </DropdownItem>
        <DropdownItem>
          <a className="drop-down" onClick={() => handleClickCategory("jewelery")}>Jewelery</a>
        </DropdownItem>
        <DropdownItem>
          <a className="drop-down" onClick={() => handleClickCategory("electronics")}>Electronics</a>
        </DropdownItem>
      </DropdownMenu>
    </Dropdown>
  );
};

export default Categories;
