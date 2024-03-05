<template>
  <div id="app">
     <TodayEvents :events="todayEvents" />
     <TomorrowEvents :events="tomorrowEvents" />
  </div>
 </template>
 
 <script>
 import TodayEvents from './components/TodayEvents.vue';
 import TomorrowEvents from './components/TomorrowEvents.vue';
 
 export default {
  name: 'App',
  components: {
     TodayEvents,
     TomorrowEvents
  },
  data() {
     return {
       todayEvents: [],
       tomorrowEvents: []
     };
  },
  created() {
     this.fetchEvents();
  },
  methods: {
     async fetchEvents() {
       try {
         const Response = await fetch('http://localhost:8000/events');
         const Events = await Response.json();
         this.Events = Events;

       } catch (error) {
         console.error('Ошибка при получении данных:', error);
       }
     }
  }
 }
 </script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
