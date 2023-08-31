import Home from "../pages/Home";
import ProductCart from "../pages/ProductCart";
import Register from "../pages/Register";
import Login from "../pages/Login";
import ProfileCart from "../pages/ProfileCart";

export const privateRoutes = [
    {path: '/profile', element: ProfileCart}
]

export const publicRoutes = [
    {path: '/home', element: Home},
    {path: '/products/:id', element: ProductCart},
    {path: '/register', element: Register},
    {path: '/login', element: Login},
]
