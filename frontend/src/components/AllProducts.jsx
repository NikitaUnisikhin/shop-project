import React, {useEffect, useState} from 'react';
import Product from "./Product";
import CatalogService from "../API/CatalogService";

const AllProducts = () => {
    const [products, setProducts] = useState([])

    useEffect(() => {
        async function fetchProducts() {
            const products = await CatalogService.getAllProducts();
            setProducts(products.data);
        }
        fetchProducts();
    }, []);

    return (
    <div>
        <h1 style={{textAlign:"center"}}>Товары</h1>
        <div>
            {products.map((product, index) =>
                <Product key={index} product={product}/>
            )}
        </div>
    </div>
    )
}

export default AllProducts;