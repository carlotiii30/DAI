import ProductList from './components/ProductList';
import { useState } from "react"
import Navbar from './components/NavBar';

export default function App() {
  const [searchTerm, setSearchTerm] = useState("");
  const [searchTermDraft, setSearchTermDraft] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("");

  const handleChange = (event) => {
    setSearchTermDraft(event.target.value);
  };

  const handleSearch = () => {
    setSearchTerm(searchTermDraft);
    setSelectedCategory(null);
  }

  const handleCategoryClick = (category) => {
    setSelectedCategory(category);
    setSearchTerm(null);
  }

  return (
    <div>
      <header>
      <Navbar
        handleChange={handleChange}
        handleSearch={handleSearch}
        categoryClick={handleCategoryClick}
      />
      </header>

      <main>
        <ProductList searchTerm={searchTerm} selectedCategory={selectedCategory} />
      </main>

      <footer>
        <p> &copy; 2023 Carlota de la Vega </p>
      </footer>
    </div>
  );
}