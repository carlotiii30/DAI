import React, { useState } from 'react';
import { Dropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap';
import '../css/dropdown.css';

const Categories = ({ onClick }) => {
    const [dropdownOpen, setDropdownOpen] = useState(false);

    const handleClickCategory = (category) => {
        onClick(category);
    };

    const toggle = () => setDropdownOpen((prevState) => !prevState);

    return (
        <Dropdown isOpen={dropdownOpen} toggle={toggle}>
            <DropdownToggle caret>Categories</DropdownToggle>
            <DropdownMenu>
                <DropdownItem>
                    <button className="drop-down" onClick={() => handleClickCategory("women's clothing")}>Women's Fashion</button>
                </DropdownItem>
                <DropdownItem>
                    <button className="drop-down" onClick={() => handleClickCategory("men's clothing")}>Men's Fashion</button>
                </DropdownItem>
                <DropdownItem>
                    <button className="drop-down" onClick={() => handleClickCategory("jewelery")}>Jewelery</button>
                </DropdownItem>
                <DropdownItem>
                    <button className="drop-down" onClick={() => handleClickCategory("electronics")}>Electronics</button>
                </DropdownItem>

            </DropdownMenu>
        </Dropdown>
    );
};

export default Categories;
