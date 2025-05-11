import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css"; // We'll create this CSS file next

function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">Krishna Jewellers</div>
      <ul className="nav-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/products">Products</Link></li>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/contact">Contact</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
