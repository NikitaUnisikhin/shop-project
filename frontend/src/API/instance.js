import axios from "axios";
import AccountsService from "./AccountsService";

export const instance = axios.create({
    baseURL: "http://localhost:8000",
    withCredentials: true
});

instance.interceptors.request.use((config) => {
    config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`;
    return config;
})

instance.interceptors.response.use((config) => {
    return config;
}, async (error) => {
    const originalRequest = error.config;
    console.log(originalRequest._isRetry);
    if (
        error.response.status === 401 &&
        originalRequest &&
        !originalRequest._isRetry
    ) {
        originalRequest._isRetry = true;
        try {
            const response = await AccountsService.refresh();
            localStorage.setItem("token", response.data['access']);
            return instance.request(originalRequest);
        } catch (e) {
            // TODO перенаправление на логин
            console.log('NO AUTH');
        }
    }
    throw error;
})