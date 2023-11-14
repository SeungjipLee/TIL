<template>
  <div>
    <h1>게시글 상세 조회 페이지</h1>
    <p>{{ post.id }}</p>
    <p>{{ post.title }}</p>
    <p>{{ post.content }}</p>
    <p>{{ post.created_at }}</p>
    <p>{{ post.updated_at }}</p>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { ref } from 'vue';
  import { useRoute } from 'vue-router';

  const route = useRoute()
  const pk = route.params.pk
  const post = ref({})
  axios({
    method:'get',
    url:`http://127.0.0.1:8000/api/v1/posts/${pk}/`
  })
    .then( res => post.value = res.data )
    .catch( err => console.log(err) )

</script>

<style scoped>

</style>