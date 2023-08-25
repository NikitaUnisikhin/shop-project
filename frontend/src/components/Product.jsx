import React from 'react';
import {useNavigate} from 'react-router-dom';

const Product = ({product}) => {
    let router = useNavigate();

    return (
        <div className="product" onClick={() => router(`/products/${product.id}`)}>
            <div>
                <strong>{product.name}</strong>
                <div>Продавец: {product.seller?.username} {product.seller?.email}</div>
                <div>Цена: {product.price} руб.</div>
                <div>Описание: {product.description}</div>
            </div>
        </div>
    )
}

export default Product;