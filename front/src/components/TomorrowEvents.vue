<template>
    <div>
       <h2>События на завтра</h2>
       <ul v-if="events.length > 0">
         <li v-for="event in events" :key="event.id">
           {{ event.name }} - {{ event.time }}
         </li>
       </ul>
       <p v-else>Данных пока нет, но ответ от сервера получен.</p>
    </div>
   </template>
   
   <script>
   export default {
    props: {
       events: Array
    }
   }
   </script>
   