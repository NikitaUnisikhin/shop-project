import React, {useEffect, useState} from "react";
import Product from "../components/Product";
import {useParams} from "react-router-dom";
import CatalogService from "../API/CatalogService";

const ProductCart = () => {
    let params = useParams();
    const [product, setProduct] = useState([])

    useEffect(() => {
        async function fetchProduct() {
            const product = await CatalogService.getProductById(params.id);
            console.log(product);
            setProduct(product.data);
        }
        fetchProduct();
    }, [params.id]);

    return (
        <div>
            <Product product={product}/>
        </div>
    )
}

export default ProductCart;