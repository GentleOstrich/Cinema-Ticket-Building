import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'MainHome',
        component: () =>
            import('../views/MainHome.vue'),
        meta: {
            needLogin: false
        }
    }
]

const router = new VueRouter({
    routes
})

export default router