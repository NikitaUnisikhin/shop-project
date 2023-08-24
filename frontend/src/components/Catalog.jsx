import React, {useState} from 'react';
import Product from "./Product";
import axios from "axios";

const Catalog = () => {
    const [products, setProducts] = useState([])

    axios.get('http://127.0.0.1:8000/api/catalog/products/')
        .then(data => setProducts(data.data))

    return (
    <div>
        <h1>Товары:</h1>
        <div>
            {products.map(product =>
                <Product product={product}/>
            )}
        </div>
    </div>
    )
}

export default Catalog;