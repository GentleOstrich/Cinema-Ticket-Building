import {createRouter, createWebHashHistory} from 'vue-router'
import WelcomeView from '../views/WelcomeView.vue'
import LoginView from '../views/LoginView.vue'
import HomeView from '../views/HomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import AboutView from '../views/AboutView.vue'
import Userinfo from '../components/UserInformation.vue'
import TicketForm from '../components/TicketForm.vue'
import MainView from "@/views/MainView.vue";
import AdminView from '../views/AdminView.vue'
import AdminReject from '../components/AdminReject.vue'
import AdminEnter from "@/components/AdminEnter.vue";
import AdminMovieForm from "@/components/AdminMovieForm.vue";
import AdminUserForm from "@/components/AdminUserForm.vue";
import MovieInfoView from "@/views/MovieInfoView.vue";
import AdminBroadcastForm from "@/components/AdminBroadcastForm.vue";

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
            path: '/movies/index',
            name: 'movies',
            component: MainView,
        },
        {
            path: '/movies/index/movie_info',
            name: 'movies_info',
            component: MovieInfoView,
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
                },
                {
                    path: '/admin/movies',
                    name: 'admin/movies',
                    component: AdminMovieForm
                },
                {
                    path: '/admin/users',
                    name: 'admin/users',
                    component: AdminUserForm
                },
                {
                    path: '/admin/broadcast',
                    name: 'admin/users',
                    component: AdminBroadcastForm
                }
            ]
        }

    ]
})

export default router
