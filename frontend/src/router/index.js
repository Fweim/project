import Vue from 'vue';
import Router from 'vue-router';
import Test from '../components/Test.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Test',
      component: Test,
    }
  ],
});