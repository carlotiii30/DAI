import './css/main.css';
import ProductList from './components/ProductList';
import SearchBar from './components/SearchBar';
import { useEffect, useState } from "react"
import Navbar from './components/NavBar';

export default function App() {
  const [searchTerm, setSearchTerm] = useState("");
  const [searchTermDraft, setSearchTermDraft] = useState("");

  const handleChange = (event) => {
    setSearchTermDraft(event.target.value);
  };

  const handleSearch = (event) => {
    event.preventDefault();
    setSearchTerm(searchTermDraft);
  };

  return (
    <div className="App">
      <Navbar />
      <header>
        <SearchBar onSearch={handleChange} />
        <button onClick={handleSearch}>Search</button>
      </header>
      <main>
        <ProductList searchTerm={searchTerm} />
      </main>
      <footer>
        <p> &copy; 2023 Carlota de la Vega </p>
      </footer>
    </div>
  );
}