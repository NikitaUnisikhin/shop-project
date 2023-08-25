import axios from "axios";

export default class AccountsService {
    static async register(user) {
        await axios.post('http://127.0.0.1:8000/api/accounts/register/', user);
    }
}