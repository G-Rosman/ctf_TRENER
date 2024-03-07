<template>
  <div class="events-container">
     <h2>События на сегодня</h2>
     <ul v-if="events.length > 0" class="events-list">
       <li v-for="event in events" :key="event.id" class="event-item">
        <div class="event-info">
            <h3><a :href="event.link" target="_blank">{{ event.name }}</a></h3>
            <p>{{ event.begin_date }} - {{ event.end_date }}</p>
          </div>
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

<style>
.events-container {
 width: 80%;
 margin: 0 auto;
 padding: 20px;
 background-color: #f9f9f9;
 border-radius: 10px;
 box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.events-list {
 list-style: none;
 padding: 0;
}

.event-item {
 padding: 10px;
 margin-bottom: 10px;
 background-color: #fff;
 border-radius: 5px;
 box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.event-info h3 {
 margin: 0 0 10px;
 font-size: 18px;
}

.event-info a {
 color: #007bff;
 text-decoration: none;
}

.event-info a:hover {
 text-decoration: underline;
}

.event-info p {
 margin: 0;
 font-size: 14px;
 color: #666;
}
</style>