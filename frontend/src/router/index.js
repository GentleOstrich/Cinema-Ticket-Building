import {createRouter, createWebHashHistory} from 'vue-router'
import WelcomeView from '../views/WelcomeView.vue'
import LoginView from '../views/LoginView.vue'
import HomeView from '../views/HomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import AboutView from '../views/AboutView.vue'
import Userinfo from '../components/UserInformation.vue'
import TicketForm from '../components/TicketForm.vue'
import Settings from '../components/SettingInformation.vue'
import MainView from "@/views/MainView.vue";
import MovieIndex from "../components/MovieIndex.vue"
import AdminView from '../views/AdminView.vue'
import AdminReject from '../components/AdminReject.vue'
import AdminEnter from "@/components/AdminEnter.vue";

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: '/',
            name: 'welcome',
            component: WelcomeView
        },
        {
            path: '/login',
            name: 'login',
            component: LoginView
        },
        {
            path: '/movies',
            name: 'movies',
            component: MainView,
            children: [
                {
                    path: 'index',
                    name: 'index',
                    component: MovieIndex
                }
            ]
        },
        {
            path: '/home',
            name: 'home',
            component: HomeView,
            children: [
                {
                    path: 'userticket',
                    name: 'userticket',
                    component: TicketForm
                },
                {
                    path: 'userinfo',
                    name: 'userinfo',
                    component: Userinfo
                },
                {
                    path: 'settings',
                    name: 'settings',
                    component: Settings
                }
            ]
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterView
        },
        {
            path: '/about',
            name: 'about',
            component: AboutView
        },
        {
            path: '/admin',
            name: 'admin',
            component: AdminView,
            children: [
                {
                    path: '/admin/error',
                    name: 'admin/error',
                    component: AdminReject
                },
                {
                    path: '/admin/home',
                    name: 'admin/home',
                    component: AdminEnter
                }
            ]
        }

    ]
})

export default router
