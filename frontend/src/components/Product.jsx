import React from 'react';

const Product = ({product}) => {
    return (
        <div>
            <div>
                <strong>{product.name}</strong>
                <ul>
                    <li>{product.price}</li>
                    <li>{product.description}</li>
                </ul>
            </div>
        </div>
    )
}

export default Product;