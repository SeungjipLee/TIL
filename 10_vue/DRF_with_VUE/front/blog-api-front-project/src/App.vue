<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink :to="{name:'main'}">Main  |  </RouterLink>
        <RouterLink :to="{name:'posts'}">Posts</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
.wrapper {
  max-width: 1200px;
  margin:0 auto;
  padding: 1rem;
}

nav {
  text-align: center;
  background-color: gray;
  padding: 1rem;
}

nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}
</style>
