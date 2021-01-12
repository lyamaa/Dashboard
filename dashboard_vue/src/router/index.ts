import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

import Register from "../views/Register.vue"
import Login from "../views/Login.vue"
import Users from "@/views/users/Users.vue"
import Roles from "@/views/roles/Roles.vue"
import UserCreate from "@/views/users/UserCreate.vue"
import UserEdit from "@/views/users/UserEdit.vue"
import Home from "@/views/Layout/Home.vue"
import Dashboard from "@/components/Dashboard.vue"
import RolesCreate from "@/views/roles/RolesCreate.vue"
import RolesEdit from "@/views/roles/RolesEdit.vue"
import Products from "@/views/products/Products.vue"
import ProductCreate from "@/views/products/ProductCreate.vue"
import ProductEdit from "@/views/products/ProductEdit.vue"
import Orders from "@/views/orders/Orders.vue"
import OrderItem from "@/views/orders/OrderItems.vue"
import Profile from "@/views/profile/Profile.vue"


const routes: Array<RouteRecordRaw> = [
  {
    path: '',
    name: 'Home',
    component: Home,
    children: [
      {path: '', redirect: '/dashboard'},
      {path: '/dashboard', component: Dashboard},
      {path: '/users', component: Users},
      {path: '/roles', component: Roles},
      {path: '/user/create', component: UserCreate},
      {path: '/users/:id/edit', component: UserEdit},
      {path: '/roles/create', component: RolesCreate},
      {path: '/roles/:id/edit', component: RolesEdit},
      {path: '/products', component: Products},
      {path: '/product/create', component: ProductCreate},
      {path: '/product/:id/edit', component: ProductEdit},
      {path: '/orders', component: Orders},
      {path: '/orders/:id', component: OrderItem},
      {path: '/profile', component: Profile},
    ]
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/users',
    name: 'Users',
    component: Users
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
 
    
]

const router = createRouter({
  history: createWebHistory(),
 
  routes
})


export default router
