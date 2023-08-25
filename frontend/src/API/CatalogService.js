import axios from "axios";

export default class CatalogService {
    static async getAllProducts() {
        return await axios.get('http://127.0.0.1:8000/api/catalog/products/');
    }

    static async getProductById(id) {
        return await axios.get('http://127.0.0.1:8000/api/catalog/products/' + id);
    }
}