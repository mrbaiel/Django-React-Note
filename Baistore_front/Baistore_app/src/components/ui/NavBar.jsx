import React from "react";
import { Link } from "react-router-dom";
import { FaCartShopping } from "react-icons/fa"; // Импорт иконки для корзины
import styles from "./NavBar.module.css"


const NavBar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-white shadow-sm py-3">
      <div className="container">
        {/* Логотип или бренд */}
        <Link className="navbar-brand fw-bold text-uppercase" to="/">
          SHOPPIT
        </Link>

        {/* Кнопка для мобильной версии */}
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarContent"
          aria-controls="navbarContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* Контейнер для ссылок */}
        <div className="collapse navbar-collapse" id="navbarContent">
          <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
            {/* Пример дополнительных ссылок */}
            <li className="nav-item">
              <Link className="nav-link" to="/">
                Home
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/products">
                Products
              </Link>
            </li>
          </ul>

          {/* Иконка корзины */}
          <Link
            to="/cart"
            className="btn btn-dark ms-3 rounded-pill position-relative"
          >
            <FaCartShopping /> {/* Иконка */}
            <span
              className="position-absolute top-0 start-100 translate-middle badge rounded-pill"
              style={{
                fontSize: "0.85rem",
                padding: "0.5em 0.65em",
                backgroundColor: "#605DCD",
              }}
            >
              12
            </span>
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
