<template>
 <div>
    <h2>События на завтра</h2>
    <ul v-if="events.length > 0">
      <li v-for="event in events" :key="event.id">
        {{ event.name }} - {{ event.link }} - {{ event.begin_date }} - {{ event.end_date }}
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