<template>
  <div id="app">
     <TodayEvents class="events-component" :events="todayEvents" />
     <TomorrowEvents class="events-component" :events="tomorrowEvents" />
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
        const todayResponse = await fetch('http://localhost:8000/today');
        const todayEvents = await todayResponse.json();
        this.todayEvents = todayEvents;

        const tomorrowResponse = await fetch('http://localhost:8000/tomorrow');
        const tomorrowEvents = await tomorrowResponse.json();
        this.tomorrowEvents = tomorrowEvents;
      } catch (error) {
        console.error('Ошибка при получении данных:', error);
      }
  }
  }}

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
body::before {
 content: "";
 position: fixed;
 top: 0;
 left: 0;
 width: 100%;
 height: 100%;
 background-image: url('@/assets/background.jpg');
 background-size: cover;
 background-position: center;
 opacity: 0.5;
 z-index: -1;
}
.events-component {
  transition: opacity 0.3s ease;
  opacity: 0.5;
}

.events-component:hover {
 opacity: 0.9; 
}
</style>
